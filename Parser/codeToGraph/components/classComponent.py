class ClassComponent:
    def __init__(self,name, modifiers=[], extends='', implements=[], inner_classes=[], interface=False):
        self.type = 'class'
        self.name = name
        self.modifiers = modifiers
        self.extends = extends
        self.implements = implements
        self.inner_classes = inner_classes
        self.fields = []
        self.methods = []
        if interface:
            self.modifiers.add('interface')


    def __str__(self):
        fields = ''
        for field in self.fields:
            fields += '('+field.type +' '+ field.name+')'
        methods = ''
        for method in self.methods:
            methods += '('+ method.name +')'
        return "[type:{}, name:{}, modifiers:{}, extends:{}, implements:{}, fields:{}, methods:{}]".format(self.type, self.name, self.modifiers, self.extends,self.implements, fields, methods)
