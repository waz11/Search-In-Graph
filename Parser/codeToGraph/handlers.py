import json
import javalang
from javalang.tree import StatementExpression
from collections.abc import Iterable


from Parser.codeToGraph.components.classComponent import ClassComponent
from Parser.codeToGraph.components.fieldComponent import FieldComponent
from Parser.codeToGraph.components.methodComponent import MethodComponent
from Parser.codeToGraph.types import typeof


def class_handler(component)->ClassComponent:
    name = component.name
    modifier = component.modifiers
    extends = ''
    implements_list = []
    inner_classes = []
    interface = typeof(component)=='interface'

    if component.extends:
        if isinstance(component.extends, list):
            extends = component.extends[0].name
        else:
            extends = component.extends.name

    if not interface and component.implements:
        implements = component.implements
        for class_name in implements:
            implements_list.append(class_name.name)

    if interface:
        modifier.add('interface')

    class_comp = ClassComponent(name, modifier, extends, implements_list,inner_classes, interface)
    for comp in component.body:
        if typeof(comp) == 'class':
            inner_class_comp = class_handler(comp)
            inner_classes.append(inner_class_comp)

        elif (typeof(comp) == 'field'):
            field = field_handler(comp)
            class_comp.fields.append(field)

        elif (typeof(comp) == 'method' and comp.name.lower() != 'main'):
            method = method_handler(comp)
            class_comp.methods.append(method)
    return class_comp

def field_handler(component)->FieldComponent:
    type = component.type.name
    name = component.declarators[0].name
    field_comp = FieldComponent(type, name)
    return field_comp

calls = []

def handler(x):
    if typeof(x) == 'calling':
        # print(x.member)
        calls.append(x.member)
        return x.member
    elif typeof(x) == 'expression':
        handler(x.expression)
    elif typeof(x) == 'statement':
        if hasattr(x, 'body'):
            handler(x.body)
    elif typeof(x) == 'if':
        # print(x)
        handler(x.condition)
        if x.else_statement != None:
            handler(x.else_statement)
        if x.then_statement != None:
            handler(x.then_statement)
    elif typeof(x) == 'operation':
        handler(x.operandl)
    elif typeof(x) == 'assignment':
        handler(x.value)
    else:
        if hasattr(x, 'statements'):
            for st in x.statements:
                handler(st)
        # else:
        #     print(x)
        #     print(type(x))



def method_body_handler(component):
    calls.clear()
    for x in component:
        handler(x)
    # print(calls)
    return calls.copy()


def method_handler(component)->MethodComponent:
    arguments = set()
    if component.body:
        method_calls = method_body_handler(component.body)
        # if len(method_calls)>0:
        #     print(method_calls)
    if component.parameters:
        for x in component.parameters:
            type = x.type.name
            arguments.add(type)
    name = component.name
    modifiers = component.modifiers
    if component.return_type:
        return_type = component.return_type.name
    else:
        return_type = 'void'
    method_comp = MethodComponent(name, modifiers,arguments, return_type)
    return method_comp

