import json
import javalang
from javalang.tree import StatementExpression
from collections.abc import Iterable


from Parser.codeToGraph.components.classComponent import ClassComponent
from Parser.codeToGraph.components.fieldComponent import FieldComponent
from Parser.codeToGraph.components.methodComponent import MethodComponent
from Parser.codeToGraph.types import typeof

primitive_variables = set(['String','boolean', 'byte', 'char', 'double','float', 'int', 'long', 'short'])
generic_types = set(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
unwanted_types = primitive_variables.union(generic_types)


def component_handler(graph, x):
    class_component = class_handler(x)
    name = class_component.name
    if name.lower() == 'main':
        return

    type = class_component.type
    modifiers = class_component.modifiers
    class_vertex = graph.add_class(name, modifiers)

    for attr in class_component.fields:
        if attr.type not in unwanted_types:
            class_vertex.add_attribute(attr.type)
            field_type_vertex = graph.add_class(attr.type, 'class')
            graph.add_edge('field', class_vertex, field_type_vertex)

    for method in class_component.methods:
        name = method.name
        if name.lower == 'main':
            continue
        arguments = []
        for arg in method.arguments:
            if arg not in unwanted_types:
                arguments.append(arg)
        return_type = method.return_type
        method_vertex = graph.add_method(name, arguments, modifiers, return_type)
        graph.add_edge('method', class_vertex, method_vertex)

        for arg in arguments:
            arg_vertex = graph.add_class(arg)
            graph.add_edge('argument', method_vertex, arg_vertex)

    for inner_class in class_component.inner_classes:
        inner_class_vertex = component_handler(graph, inner_class)
        graph.add_edge('inner class', class_vertex, inner_class_vertex)


    if class_component.extends:
        name = class_component.extends
        extended_class_vertex = graph.add_class(name, 'class')
        graph.add_edge('extends', class_vertex, extended_class_vertex)

    for interface_name in class_component.implements:
        interface_vertex = graph.add_interface(interface_name)
        graph.add_edge('implements', class_vertex, interface_vertex)

    return class_vertex


def class_handler(component)->ClassComponent:
    name = component.name
    modifier = component.modifiers
    extends = ''
    implements_list = []
    inner_classes = []
    interface = typeof(component)=='interface'

    if component.extends:
        if isinstance(component.extends, str):
            extends = component.extends
        elif isinstance(component.extends, list):
            extends = component.extends[0].name
        else:
            extends = component.extends.name

    if not interface and component.implements:
        implements = component.implements
        for class_name in implements:
            if isinstance(class_name,str):
                implements_list.append(class_name)
            else:
                implements_list.append(class_name.name)

    if interface:
        modifier.add('interface')

    class_comp = ClassComponent(name, modifier, extends, implements_list,inner_classes, interface)
    try:
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
    except: None
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


def method_handler(component)-> MethodComponent:
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

