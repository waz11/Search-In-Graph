
class FieldComponent:
    def __init__(self, type,name):
        self.type = type
        self.name = name
    def __str__(self):
        return "[type:{}, name:{}]".format(self.type, self.name)
