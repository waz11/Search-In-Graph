import os


def handle_task(mapped_dict, name, key, **kwargs):
    mapped_dict["name"] = name
    mapped_dict["key"] = key
    if "type" in kwargs and kwargs["type"]:
        mapped_dict["type"] = kwargs["type"]
    if "att_names" in kwargs and kwargs["att_names"]:
        mapped_dict["attributes"] = kwargs["att_names"]


def handle_arrows(mapped_arrows_dict, first_key, second_key, type, text=None, index_call=None):
    mapped_arrows_dict["type"] = type
    if text:
        mapped_arrows_dict["name"] = text
    mapped_arrows_dict["from"] = first_key
    mapped_arrows_dict["to"] = second_key

    if index_call:
        mapped_arrows_dict["number_call"] = index_call


class MapCreator:

    def __init__(self, mapped_code):
        self.mapped_code = mapped_code
        self.map_list = []
        self.current_mapped_classes = []
        self.current_mapped_methods = []

    def create_dictionary(self, task):
        full_task_dict = {"vertices": [], "edges": []}
        key = 0

        """ add the query task"""
        key, full_task_dict, query_key = self.create_query_task(task, full_task_dict, key)

        """ extract the class  """
        key, full_task_dict = self.create_class_task(task, full_task_dict, key, query_key)

        return self.task_dict(task, key, full_task_dict, flag=False)

    def task_dict(self, task, key, full_task_dict, **kwargs):
        if kwargs.get("flag"):
            flag = kwargs.get("flag")
        else:
            flag = False
        """ extract the implemented class  """
        if not flag:
            for sub_class in task.sub_classes:
                key, full_task_dict = self.add_implemented_task(sub_class, full_task_dict, key)
        else:
            key, full_task_dict = self.add_implemented_task(task, full_task_dict, key)

        """extract the extended class """
        if not flag:
            for sub_class in task.sub_classes:
                key, full_task_dict = self.add_extended_task(sub_class, full_task_dict, key)
        else:
            key, full_task_dict = self.add_extended_task(task, full_task_dict, key)

        """ extract the class's methods  """
        if not flag:
            for sub_class in task.sub_classes:
                if sub_class.class_name == "Workbook":
                    print("a")
                key, full_task_dict = self.create_method_tasks(sub_class, full_task_dict, key)
        else:
            key, full_task_dict = self.create_method_tasks(task, full_task_dict, key)

        """extract the class's attributes"""
        # key, full_task_dict = self.create_attribute_tasks(code, full_task_dict, key)

        """extract the calling methods"""
        if not flag:
            for sub_class in task.sub_classes:
                key, full_task_dict = self.add_calling_methods(sub_class, full_task_dict, key)
        else:
            key, full_task_dict = self.add_calling_methods(task, full_task_dict, key)

        """extract the sub classes"""
        if not flag:
            for sub_class in task.sub_classes:
                key, full_task_dict = self.add_sub_clases_task(sub_class, full_task_dict, key)
        else:
            key, full_task_dict = self.add_sub_clases_task(task, full_task_dict, key)
        return full_task_dict

    def add_sub_clases_task(self, code, full_task_dict, key):
        for sub_class in code.sub_classes:
            mapped_arrows_dict = {}
            mapped_task_dict = {}
            "avoid system calls"
            """checks if the called sub_class is already mapped"""
            if sub_class.get_key() == 0:

                handle_task(mapped_task_dict, sub_class.class_name, key, comments=sub_class.documentation,
                            type="class", att_names=sub_class.get_class_atts_names())

                full_task_dict["vertices"].append(mapped_task_dict)
                sub_class.set_key(key)
                current_key = key
                key += 1
            else:
                current_key = sub_class.get_key()
            """connect the arrows from a specific method to its called methods"""
            handle_arrows(mapped_arrows_dict, code.get_key(), current_key, "method")
            full_task_dict["edges"].append(mapped_arrows_dict)
            self.task_dict(sub_class, key, full_task_dict, flag=True)

        return key, full_task_dict

    def create_query_task(self, code, full_task_dict, key):
        mapped_task_dict = {}
        code.set_key(key)
        query_key = key

        handle_task(mapped_task_dict, code.query, key, comments=None, tags=code.tags,
                    score=code.score, url=code.url, type="project", post=code.text)
        key += 1
        """append the task to the map"""
        full_task_dict["vertices"].append(mapped_task_dict)
        return key, full_task_dict, query_key

    def create_class_task(self, code, full_task_dict, key, query_key):
        for sub_class in code.sub_classes:
            mapped_task_dict = {}
            mapped_arrows_dict = {}
            sub_class.set_key(key)
            handle_task(mapped_task_dict, sub_class.class_name, key, comments=sub_class.documentation,
                        type="class", att_names=sub_class.get_class_atts_names())

            key += 1
            """append the class to the map"""
            full_task_dict["vertices"].append(mapped_task_dict)
            """append connections to the map"""
            handle_arrows(mapped_arrows_dict, query_key, sub_class.get_key(), "class")
            full_task_dict["edges"].append(mapped_arrows_dict)
            self.current_mapped_classes.append(sub_class)
        return key, full_task_dict

    def add_implemented_task(self, code, full_task_dict, key):
        for implement_class in code.Implements:
            mapped_arrows_dict = {}
            """connect the tasks of the implemented class and the main class"""
            handle_arrows(mapped_arrows_dict, code.get_key(), implement_class.get_key(),"implements")
            full_task_dict["edges"].append(mapped_arrows_dict)
            key += 1
            self.current_mapped_classes.append(implement_class)

        return key, full_task_dict

    def add_extended_task(self, code, full_task_dict, key):
        if code.Extends is not None:
            mapped_arrows_dict = {}
            handle_arrows(mapped_arrows_dict, code.get_key(), code.Extends.get_key(), "extends")
            full_task_dict["edges"].append(mapped_arrows_dict)
            key += 1
            self.current_mapped_classes.append(code.Extends)

        return key, full_task_dict

    def create_method_tasks(self, code, full_task_dict, key):
        for method in code.Methods:
            mapped_arrows_dict = {}
            mapped_task_dict = {}
            handle_task(mapped_task_dict, method.method_name, key, comments=method.documentation,
                        type="method", att_names=method.params)

            method.set_key(key)
            """adds the method to the map"""
            full_task_dict["vertices"].append(mapped_task_dict)
            handle_arrows(mapped_arrows_dict, code.get_key(), key, "method")
            """connects the arrows from method to super class"""
            full_task_dict["edges"].append(mapped_arrows_dict)
            key += 1
            self.current_mapped_methods.append(method)

        return key, full_task_dict

    def create_attribute_tasks(self, code, full_task_dict, key):
        for sub_class in code.sub_classes:
            for attribute in sub_class.Attributes:
                mapped_arrows_dict = {}
                mapped_task_dict = {}
                handle_task(mapped_task_dict, attribute.name, key, type="attribute")
                attribute.set_key(key)
                full_task_dict["vertices"].append(mapped_task_dict)
                handle_arrows(mapped_arrows_dict, sub_class.get_key(), key, "AchievedBy", "achieved by")
                full_task_dict["edges"].append(mapped_arrows_dict)
                key += 1
        return key, full_task_dict

    def get_method_task(self, method_name):
        for method in self.current_mapped_methods:
            if method.get_method_name() == method_name:
                return method
        return None

    def get_sub_class_task(self, class_name):
        for sub_class in self.current_mapped_classes:
            if sub_class.get_class_name() == class_name:
                return sub_class
        return None

    def add_calling_methods(self, code, full_task_dict, key):
        index_call = 1
        for method in code.Methods:
            for calling_method in method.calling_methods:
                mapped_arrows_dict = {}
                mapped_task_dict = {}
                "avoid system calls"
                linked_method = self.get_method_task(calling_method.method_name)
                if linked_method is None:
                    continue
                """checks if the called method is already mapped"""
                if linked_method.get_key() == 0:
                    handle_task(mapped_task_dict, method.method_name, key, type="method",
                                att_names=method.params)
                    full_task_dict["vertices"].append(mapped_task_dict)
                    handle_arrows(mapped_arrows_dict, method.get_key(), key, "method", index_call=index_call)
                    full_task_dict["edges"].append(mapped_arrows_dict, index_call=index_call)
                    index_call += 1
                    current_key = key
                    key += 1
                else:
                    current_key = linked_method.get_key()
                """connect the arrows from a specific method to its called methods"""
                handle_arrows(mapped_arrows_dict, method.get_key(), current_key, "method",index_call=index_call)
                full_task_dict["edges"].append(mapped_arrows_dict)
                index_call += 1

        return key, full_task_dict
