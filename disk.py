def parse_inventory(keys):
    number, item_name, stock, type_of_item, director, genre, initial_price, replacement_price = keys.split(
        ',')
    return [
        number, item_name,
        int(stock), type_of_item, director, genre,
        int(initial_price),
        float(replacement_price)
    ]


def open_file(file_name):
    with open(file_name) as file:
        keys = file.read()
        inventory = {}
        lines = keys.split('\n')[1:]
        for line in lines:
            if line:
                d = parse_inventory(line)
                inventory[d[0]] = {
                    'Name': d[1],
                    'Stock': d[2],
                    'Type_of_item': d[3],
                    'Director': d[4],
                    'Genre': d[5],
                    'Initial_price': d[6],
                    'Replacement_price': d[7]
                }
        return inventory


def open_file_history():
    with open('history.txt') as file:
        keys = file.read()
        lines = keys.split('\n')[1:]
        st = ''
        for line in lines:
            st += '{}\n'.format(line)
            return st.lstrip()


#number,item_name,stock,type_of_item,director,genre,initial_price,replacement_price
def inventory_into_string(inventory):
    st = ''
    for key in inventory:
        item = inventory[key]
        st += '\n{},{},{},{},{},{},{},{}\n'.format(
            key, item["Name"], item["Stock"], item["Type_of_item"],
            item["Director"], item["Genre"], item["Initial_price"],
            item["Replacement_price"])

    return st.rstrip()


def history_into_string(history):
    return '\n{},{},{},{},{}'.format(history['time'], history['Name'],
                                     history['days_rental'], history['profit'],
                                     history['deposit'])


def write_to_file_inven(inventory):
    with open('inventory.txt', 'w') as file:
        file.write(
            f'number,item_name,stock,type_of_item,director,genre,initial_price,replacement_price{inventory_into_string(inventory)}'
        )


def write_to_file_history(history):
    with open('history.txt', 'a') as file:
        file.write(f'{history_into_string(history)}')


def revenue():
    total = []
    with open('history.txt', 'r') as file:
        file.readline()
        for line in file:
            line = line.split(',')
            total.append(float(line[3]))
    return sum(total)
