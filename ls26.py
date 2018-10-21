class TreeNode:
    def __init__(self, parent, value):
        self.parent = parent
        self.child = []
        self.value = value
        self.syntax = None


class SimpleTree:
    def __init__(self, root):
        self.root = TreeNode(None, root)
        self.current = self.root
        self.node_stack = []
        self.node_stack.append(self.root)

    def reload(self):
        """ Метод для перезапуска итератора"""
        while self.node_stack.size() != 0:
            self.node_stack.pop()
        self.node_stack.push(self.root)
        return

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.node_stack) == 0:
            raise StopIteration
        else:
            node = self.node_stack.pop()
            for element in node.child:
                self.node_stack.append(element)
        return node

    def add_tree_node(self, value):
        """Добавление дочернего узла к текущему узлу"""
        new_node = TreeNode(self.current, value)
        self.current.child.append(new_node)
        self.current = new_node
        return


class ANode:
    def __init__(self):
        self.token_type = None
        self.token_value = None


OPERATORS = {'+': (1, 'операция', lambda x, y: x + y), '-': (2, 'операция', lambda x, y: x - y),
             '*': (3, 'операция', lambda x, y: x * y), '/': (4, 'операция', lambda x, y: x / y),
            }

def pars(string):
    number = ''
    parsed_formula = []
    """Эта часть функции разбивает строку на элементы списка"""
    for s in string:
        if s in '1234567890':
            number += s
        elif number:
            parsed_formula.append(number)
            number = ''
        if s in OPERATORS or s in '()':
            parsed_formula.append(s)
    if number:
        parsed_formula.append(number)
    return parsed_formula

def put_parentheses(parsed_formula):
    stack = []
    postfix = []
    """Эта часть функции собирает из списка выражение в постфиксной записи"""
    for token in parsed_formula:
        if token in OPERATORS:
            while stack and stack[-1] != "(" and OPERATORS[token][0] <= OPERATORS[stack[-1]][0]:
                postfix.append(stack.pop())
            stack.append(token)
        elif token == ")":
            while stack:
                x = stack.pop()
                if x == "(":
                    break
                postfix.append(x)
        elif token == "(":
            stack.append(token)
        else:
            postfix.append(token)
    while stack:
        postfix.append(stack.pop())
    """Наконец, пересобираем из постфиксного выражения обычное с правильно расставленными скобками"""
    for ch in postfix:
        if ch not in OPERATORS:
            stack.append(ch)
        else:
            b = stack.pop()
            a = stack.pop()
            expr = '(' + a + ch + b + ')'
            stack.append(expr)
    print(stack[0])
    return stack[0]

def token(arr):
    tokens = []
    for el in arr:
        tok = ANode()
        if el in '()':
            tok.token_type = 'Скобка'
            tok.token_value = el
            tokens.append(tok)
        elif el in OPERATORS:
            tok.token_type = 'операция'
            tok.token_value = el
            tokens.append(tok)
        else:
            tok.token_type = 'число'
            tok.token_value = el
            tokens.append(tok)
    return tokens

tokens = token(put_parentheses(pars('(7+((3*5)-2)))')))

for i in tokens:
    print(i.token_value, i.token_type, end=' ')
print()

def build_ast(tokens):
    abstract_syntax_tree = SimpleTree(None)
    while len(tokens) > 0:
        current_token = tokens.pop(0)
        if current_token.token_value == '(':
            abstract_syntax_tree.add_tree_node(None)
            continue
        elif current_token.token_value == ')':
            abstract_syntax_tree.current = abstract_syntax_tree.current.parent
            continue
        elif current_token.token_type == 'число':
            abstract_syntax_tree.current.value = current_token.token_value
            abstract_syntax_tree.current = abstract_syntax_tree.current.parent
            continue
        elif current_token.token_type == 'операция':
            abstract_syntax_tree.current.value = current_token.token_value
            abstract_syntax_tree.add_tree_node(None)
            continue
    abstract_syntax_tree.current = abstract_syntax_tree.root
    return abstract_syntax_tree

abstract_syntax_tree = build_ast(tokens)


def calculate_ast(abstract_syntax_tree):
    while True:
        if abstract_syntax_tree.current.value in OPERATORS:
            stop = False
            for child in abstract_syntax_tree.current.child:
                if child.value in OPERATORS:
                    abstract_syntax_tree.current = child
                    stop = True
            if stop:
                continue
            x, y = int(abstract_syntax_tree.current.child[0].value), int(abstract_syntax_tree.current.child[1].value)
            abstract_syntax_tree.current.syntax = '(' + str(x) + str(abstract_syntax_tree.current.value) + str(y) + ')'
            abstract_syntax_tree.current.value = OPERATORS[abstract_syntax_tree.current.value][2](x, y)
            abstract_syntax_tree.current.child.clear()
            if abstract_syntax_tree.current.parent:
                abstract_syntax_tree.current = abstract_syntax_tree.current.parent
            continue
        if abstract_syntax_tree.current == abstract_syntax_tree.root:
            return abstract_syntax_tree.root

result = calculate_ast(abstract_syntax_tree)
print(result.value, result.syntax, eval(result.syntax))