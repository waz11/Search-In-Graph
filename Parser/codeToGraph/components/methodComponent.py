class MethodComponent:
    def __init__(self, name, modifiers=[],arguments=[], return_type=''):
        self.name = name
        self.modifiers=modifiers
        self.arguments=arguments
        self.return_type=return_type
    def __str__(self):
        return "[name:{}, modifiers:{}, type_parameters:{}, return_type:{}]".format(self.name, self.modifiers, self.type_parameters, self.return_type)
