import os


def catalog_reader(file_name_1, file_name_2, file_name_3, new_file_name):
    catalog_name = 'sorted'
    base_path = os.getcwd()
    file_name = [file_name_1, file_name_2, file_name_3]
    files_dict = {}
    for file_index in file_name:
        file_path = file_index
        full_path = os.path.join(base_path, catalog_name, file_path)
        with open(full_path, 'r', encoding='utf-8') as file:
            data = file.readlines()
            string_counter = len(data)
            files_dict[string_counter] = file_path

    sorted_files_dict = sorted(files_dict.items())

    for str_counter, doc_name in sorted_files_dict:
        file_path = doc_name
        full_path = os.path.join(base_path, catalog_name, file_path)
        with open(full_path, 'r', encoding='utf-8') as file:
            data = file.read()
        full_path = os.path.join(base_path, catalog_name, new_file_name)
        with open(full_path, 'a', encoding='utf-8') as new_file:
            new_file.write(f'{doc_name}\n')
            new_file.write(str(f'{str_counter}\n'))
            new_file.write(f'{data}\n')
    return


catalog_reader('1.txt', '2.txt', '3.txt', 'new_text.txt')