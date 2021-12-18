from Parser.CodeFromFile import CodeFromFile


def main():
    file_path = 'Files/src'
    output_path = 'Files/out.json'

    code_from_file = CodeFromFile(file_path,'', output_path)
    code_from_file.concat_files()
    code_from_file.test_new_file()


if __name__ == '__main__':
    main()
