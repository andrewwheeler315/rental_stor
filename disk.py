def open_file(file_name):
    with open(file_name) as file:
        items = file.readlines()
        return items
