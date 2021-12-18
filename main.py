from CodeMapping.CodeFromFile import CodeFromFile


def main():
    file_path = './files/src'
    name = 'ron'
    output_path = './files/out'

    code_from_file = CodeFromFile(file_path, name, output_path)
    # code_from_file.concat_files()
    # code_from_file.test_new_file()

if __name__ == '__main__':
    main()
