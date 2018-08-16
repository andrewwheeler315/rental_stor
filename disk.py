def parse_inventory(keys):
number, item_name, stock, type_of_item, director, genre, initial_price, replacement_price
return[number, item_name, int(stock), type_of_item, director, genre, int(initial_price), int(replacement_price)]

def open_file(file_name):
    with open(file_name) as file:
        keys = file.read()
        inventory = {}
        lines = keys.split('\n')[1:]
        for line in lines:
            if line:
                d = parse_inventory_item(line)
                inventory[d[0]] = {
                    'Name': d[1],
                    'Stock': d[2],
                    'Replacement_fee': d[3],
                    'Daily_fee': d[4]
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

def inventory_into_string(inventory):
    st = ''
    for key in inventory:
        item = inventory[key]
        st += '\n{},{},{},{},{},{},{}\n'.format(key, item["Name"], item["Stock"],
                                                item['Replacement'],
                                                item["Daily"])

    return st.rstrip()

def history_into_string(history):
    return '\n{},{},{},{}'.format(history['time'], history['days_rental'],
                                  history['deposit'], history['profit'])

def write_to_file_inven(inventory):
    with open ('inventory.txt', 'w') as file:
        file.write(
            f'number,item_name,stock,type_of_item,director,genre,initial_price,replacement_price{inventory_to_string(inventory)}'
        )    

        def write_to_file_history(history):
            with open('history.txt', 'a') as file:
                file.write(f'{history_to_string(history)}')
