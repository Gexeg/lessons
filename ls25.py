class ANode:
    def __init__(self):
        self.token_type = None
        self.token_value = None

OPERATORS = {'+': (1, 'операция'), '-': (2, 'операция'),
             '*': (3, 'операция'), '/': (4, 'операция'),
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
    """Эта часть функции собирает из списка пост"""
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

tok_list = token(put_parentheses(pars('7+3/25*(5-2)')))

for i in tok_list:
    print(i.token_value, i.token_type, end=' ')
