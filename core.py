def deposit_fee(item):
    fee = item['Replacement_price'] / 10
    return fee

def total_rental_fee(item, days):
    days = int(days)
    fee = item['Daily fee'] * days
    tax = 1.07
    fee *= tax
    return round(fee, 2)

def can_return(item):
    if item['Stock'] < 15:
        return True 
    else:
        return False

def is_in_stock(item):
    if item['Stock'] == 0:
        return False
    else: 
        return True

def make_inv_options(inventory):
    return '\n'.join([
        '{}--{}'.format(str(i + 1), item['Name'])
        for i, item in enumerate(inventory.values())
    ])

def employee_inven(inven):
    return '\n'.join([
        '{}--{}, Stock: {}, Replacement Price: {}, Daily Fee: {}'.format(
            str(i + 1), item['Name'], item['Stock'], item['Replacement fee'],
            item['Daily fee']) for i, item in enumerate(inv.values())
    ])

    def make_history(time, days, fee_1, fee_2):
        history = {
            'time': time,
            'days_rented': days,
            'deposit': fee_1
            'profit': fee_2
        }
        return history 
