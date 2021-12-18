from CodeMapping.Parser.utils import primitive_types


class Task:

    def __init__(self):
        self.task = None
        self.key = 0
        self.documentation = ""
        self.code = None
        self.code_changed = False

    def changed_code(self):
        self.code_changed = True

    def get_key(self):
        return self.key

    def set_documentation(self, documentation):
        documentation = documentation.replace("/**", '')
        documentation = documentation.replace("*/", '')
        self.documentation += documentation

    def set_key(self, key):
        self.key = key

    def set_code(self, code):
        if self.code is not None:
            self.code_changed = True
        self.code = code


# ------------------------------------------------------------------------------
class CodeWrapper(Task):
    def __init__(self, query, text):
        super().__init__()
        self.query = query
        self.text = text
        self.answer_text = None
        self.sub_classes = []
        self.url = None
        self.methods = []
        self.imports = []
        self.imports_codes = []
        self.tags = []
        self.score = None
        self.post_id = None

    def __eq__(self, other):
        """
        equality of two queries
        :param other:
        :return True is 2 queries are equal, otherwise False
        """
        if self.query == other.query:
            return True
        return False

    def set_id(self, post_id):
        self.post_id = post_id

    def set_tags(self, tags):
        self.tags = tags

    def set_score(self, score):
        self.score = score

    def set_url(self, url):
        # TODO: to fix function
        self.url = url

    def get_queries_class(self):
        return self.sub_classes

    def get_class(self, class_to_return):
        for curr_class in self.sub_classes:
            if curr_class.get_class_name() in primitive_types:
                continue
            else:
                if curr_class.get_class_name() == class_to_return:
                    return curr_class
        return None

    def get_methods(self, method_name):
        # TODO: handle two functions from same name
        return next((x for x in self.methods if x.get_method_name() == method_name), None)

    def add_imports(self, _import):
        self.imports.append(_import)

    def add_answer_text(self, answer_text):
        self.text += answer_text

    def add_methods(self, method):
        self.methods.append(method)

    def add_class(self, task):
        self.sub_classes.append(task)

    def add_imports_code(self, _import):
        self.imports_codes.append(_import)


# ------------------------------------------------------------------------------

class ClassTask(Task):

    def __init__(self, class_name):
        super().__init__()
        self.class_name = class_name
        self.Attributes = []
        self.Methods = []
        self.Implements = []
        self.Extends = None
        self.Constructors = []
        self.sub_classes = []
        self.Enums = []

    def get_class_atts_names(self):
        att_names = []
        for att in self.Attributes:
            curr_att_dec = att.name
            if att.att_type is not None and att.att_type.class_name is not None:
                curr_att_dec = att.att_type.class_name + " " + curr_att_dec
            att_names.append(curr_att_dec)
        return att_names

    def add_sub_class(self, sub_class):
        self.sub_classes.append(sub_class)

    def add_class_enums(self, enum):
        self.Enums.append(enum)

    def add_implement_class(self, implement_class):
        self.Implements.append(implement_class)

    def add_extended_class(self, extended_class):
        self.Extends = extended_class

    def add_constructors(self, constructor):
        self.Constructors.append(constructor)

    def add_class_methods(self, method):
        self.Methods.append(method)

    def add_class_attributes(self, attribute):
        self.Attributes.append(attribute)

    def get_class_object(self):
        return self.task

    def get_class_name(self):
        return self.class_name

    def get_class_attributes(self):
        return self.Attributes

    def get_class_method(self, method):
        return next((x for x in self.Methods if x.get_method_name() == method), None)

    def get_specific_attribute(self, attribute):
        return next((x for x in self.Attributes if x.get_attribute_name() == attribute), None)

    def get_all_method(self):
        return self.Methods

    def get_constructor(self):
        if self.Constructors:
            return self.Constructors[0]
        return None

    def __eq__(self, other):
        return self.class_name == other.get_class_name()


# ------------------------------------------------------------------------------
class ClassAttribute(Task):

    def __init__(self, class_task, attribute_name, att_type=None, object_type=None):
        super().__init__()
        self.class_name = class_task
        self.name = attribute_name
        self.att_type = att_type
        self.object_type = object_type

    def get_att_obj_type(self):
        return self.object_type

    def get_attribute_name(self):
        return self.name

    def get_attribute_class(self):
        return self.class_name

    def get_attribute_type(self):
        return self.att_type


# ------------------------------------------------------------------------------

class MultiTypeClassAttribute(ClassAttribute):

    def __init__(self, class_task, attribute_name, att_types, object_type):
        super().__init__(class_task, attribute_name, object_type=object_type)
        self.types = att_types


# ------------------------------------------------------------------------------

class MethodTask(Task):

    def __init__(self, method_name, class_task):
        super().__init__()
        self.task = class_task
        self.Attributes = []
        self.method_name = method_name
        self.calling_methods = []
        self.method_token = None
        self.params = []

    def add_method_calls(self, method):
        self.calling_methods.append(method)

    def add_method_attributes(self, attribute):
        self.Attributes.append(attribute)

    def get_method_name(self):
        return self.method_name

    def get_method_super_class(self):
        return self.task

    def get_calling_method(self):
        return self.calling_methods

    def get_attribute(self, attribute):
        return next((x for x in self.Attributes if x.get_attribute_name() == attribute), None)

    def find_method_call(self, method_called):
        for calling in self.calling_methods:
            if calling.get_method_name() == method_called:
                return calling
        return None


# ------------------------------------------------------------------------------

class EnumTask(Task):

    def __init__(self, enum_name, task):
        super().__init__()
        self.enum_name = enum_name
        self.super_task = task
        self.enum_consts = []

    def add_enum_const(self, const):
        self.enum_consts.append(const)