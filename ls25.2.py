class ANode:
    def __init__(self):
        self.token_type = None
        self.token_value = None

OPERATORS = {'+': (1, 'операция'), '-': (2, 'операция'),
             '*': (3, 'операция'), '/': (4, 'операция'),
            }

def pars_with_parentheses(formula_string):
    number = ''
    parentheses = ''
    parsed_formula = []
    """разбиваем строку на элементы. Выражения в скобках идут как один элемент, чтобы сохранить приоритетность"""
    i = 0
    while i <= len(formula_string) - 1:
        if formula_string[i] in '1234567890':
            number += formula_string[i]
            i += 1
            continue
        elif number:
            parsed_formula.append(number)
            number = ''
        if formula_string[i] == '(':
            while formula_string[i] != ')' and i <= len(formula_string) - 1:
                parentheses += formula_string[i]
                i += 1
            parentheses += ')'
            parsed_formula.append(parentheses)
            parentheses = ''
            continue
        if formula_string[i] in OPERATORS:
            parsed_formula.append(formula_string[i])
            i += 1
            continue
        i += 1
    if number:
        parsed_formula.append(number)
    return parsed_formula

def put_parentheses(formula):
    """расставляем скобки"""
    prior = 4
    stack = []
    while prior != 0:
        while formula:
            element = formula.pop(0)
            if element in OPERATORS and OPERATORS[element][0] == prior:
                exp = '(' + stack.pop() + element + formula.pop(0) + ')'
                stack.append(exp)
                continue
            stack.append(element)
        prior -= 1
        formula = stack
        stack = []
    return formula[0]

def pars_before_tok(formula):
    number = ''
    parsed_formula = []
    """Эта часть функции разбивает строку на элементы списка"""
    for s in formula:
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

tok_list = token(pars_before_tok(put_parentheses(pars_with_parentheses('7+3/25*(5-2)'))))

for i in tok_list:
    print(i.token_value, i.token_type, end=' ')
