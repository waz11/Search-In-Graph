import javalang

types = {
    javalang.tree.ClassDeclaration: 'class',
    javalang.tree.FieldDeclaration: 'field',
    javalang.tree.ConstructorDeclaration: 'constructor',
    javalang.tree.MethodDeclaration: 'method',
    javalang.tree.InterfaceDeclaration: 'interface'
}

def typeof(component):
    return types.get(type(component))