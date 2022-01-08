import javalang
from Parser.codeToGraph.components.classComponent import ClassComponent
from Parser.codeToGraph.components.fieldComponent import FieldComponent
from Parser.codeToGraph.components.methodComponent import MethodComponent

def typeof(component):

    types = {
        javalang.tree.ClassDeclaration: 'class',
        javalang.tree.FieldDeclaration:'field',
        javalang.tree.ConstructorDeclaration: 'constructor',
        javalang.tree.MethodDeclaration: 'method',
        javalang.tree.InterfaceDeclaration: 'interface'
    }
    return types.get(type(component))

def handle_class(component):
    name = component.name
    modifier = component.modifiers
    extends = ''
    implements_list = []
    interface = typeof(component)=='interface'

    if component.extends:
        extends = component.extends.name

    if not interface and component.implements:
        implements = component.implements
        for class_name in implements:
            implements_list.append(class_name.name)

    if interface:
        modifier.add('interface')

    class_comp = ClassComponent(name, modifier, extends, implements_list, interface)
    for comp in component.body:
        if (typeof(comp) == 'field'):
            field = handle_field(comp)
            class_comp.fields.append(field)

        if (typeof(comp) == 'method'):
            method = handle_method(comp)
            class_comp.methods.append(method)
    return class_comp

def handle_field(component):
    type = component.type.name
    name = component.declarators[0].name
    field_comp = FieldComponent(type, name)
    return field_comp

def handle_method(component):
    arguments = set()
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
