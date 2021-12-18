from itertools import takewhile

import javalang

primitive_types = ['Boolean', 'boolean', 'char', 'byte', 'short', 'int', 'long', 'float', 'double', 'String', 'string',
                   'System', 'System.out', 'Scanner', 'Log']

def extract_specific_code(position, parser_token_list, obj, current_query, modifiers=None):
    current_query.changed_code()  # notify that code has been changed
    start_index = 0

    """find the start index in the token list"""
    for token in parser_token_list:
        if token.position == position:
            break
        start_index += 1

    """fix start index in the token list before the modifiers"""
    if modifiers is not None:
        while start_index > 0 and position[0] == parser_token_list[start_index].position[0]:
            start_index -= 1
        if start_index != 0:
            start_index += 1
        col_position = parser_token_list[start_index].position[1]
    else:
        col_position = position[1]

    """find the end index in the token list"""
    end_index = start_index + 1
    for index in range(start_index + 1, len(parser_token_list)):
        if parser_token_list[index].position[1] == col_position and parser_token_list[index].value == '}':
            if isinstance(parser_token_list[index], javalang.tokenizer.Separator):
                break
        end_index += 1

    code = javalang.tokenizer.reformat_tokens(parser_token_list[start_index:end_index + 1])  # get the code

    return code


def create_collected_code(query):
    """
    create_collected_code Function - creates a code out of all new changed sub codes
    :param query:
    """

    new_code = ""
    non_changed_classes = []

    if query.imports_codes is not []:
        for _import in query.imports_codes:
            new_code += "import " + _import + ';\n'
    """find which classes have been changed"""
    for sub_class in query.sub_classes:
        if not sub_class.code_changed:
            if sub_class.code is not None:
                new_code += sub_class.code
        else:
            # class_name = sub_class.get_class_name()
            non_changed_classes.append(sub_class)

    """handle the changed classes"""
    for modified_class in non_changed_classes:
        if modified_class.code is None:
            continue
        new_class_code = ""
        new_class_code += modified_class.code.split('{')[0] + "{\n"
        whitespace = list(takewhile(str.isspace, new_class_code))
        "".join(whitespace)
        indent = len(whitespace) + 4
        for class_enum in modified_class.Enums:
            new_class_code += (' ' * indent) + class_enum.code
        for class_attributes in modified_class.Attributes:
            if class_attributes.code not in new_class_code:
                new_class_code += (' ' * indent) + class_attributes.code
        for class_method in modified_class.Methods:
            if class_method.code is not None:
                new_indent = '\n ' + ' ' * indent
                method_code = class_method.code.replace('\n', new_indent)
                new_class_code += (' ' * indent) + method_code + '\n '
        new_class_code += (' ' * (indent - 4)) + '}' + '\n'

        modified_class.code = new_class_code
        new_code += modified_class.code
    query.code = new_code


def extract_att_code(position, parser_token_list, current_query, modifiers=None):
    """
    extract_att_code Function - extract the attribute codes
    :param position:
    :param parser_token_list:
    :param current_query:
    :param modifiers:
    :return: code - txt represents the code of the specific attribute
    """
    current_query.changed_code()  # change the attribute code to be changed

    """find the start index"""
    start_index = 0
    for token in parser_token_list:
        if token.position == position:
            break
        start_index += 1

    """fix start index in the token list before the modifiers"""
    if modifiers is not None:
        while start_index > 0 and position[0] == parser_token_list[start_index].position[0]:
            start_index -= 1
        start_index += 1
    # TODO: check if relevant
    #     col_position = parser_token_list[start_index].position[1]
    # else:
    #     col_position = position[1]

    """find the end index in the token list"""
    end_index = start_index + 1
    for index in range(start_index + 1, len(parser_token_list)):
        if parser_token_list[index].position[0] != position[0]:
            break
        end_index += 1

    code = javalang.tokenizer.reformat_tokens(parser_token_list[start_index:end_index])  # get the code

    return code

