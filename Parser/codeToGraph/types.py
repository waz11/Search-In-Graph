import re

import javalang

types = {
    javalang.tree.ClassDeclaration: 'class',
    javalang.tree.FieldDeclaration: 'field',
    javalang.tree.ConstructorDeclaration: 'constructor',
    javalang.tree.MethodDeclaration: 'method',
    javalang.tree.InterfaceDeclaration: 'interface',


    # javalang.tree.StatementExpression: 'statement',
    javalang.tree.WhileStatement: 'statement',
    javalang.tree.IfStatement: 'if',
    javalang.tree.ForStatement: 'for',
    javalang.tree.StatementExpression: 'expression',
    javalang.tree.MethodInvocation: 'calling',
    javalang.tree.BinaryOperation: 'operation',
    javalang.tree.Assignment: 'assignment'
}

def typeof(component):
    return types.get(type(component))
