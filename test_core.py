import core

games = {
    'Name': 'Final Fantasy VII',
    'Stock': 15,
    'Type_of_item': "Game",
    'Director': "Yoshinori Kitase",
    'Genre': "ATB Turn Based RPG",
    'Initial_price': 2,
    'Replacement_price': 2.0
}

games2 = {
    'Name': 'Final Fantasy VII',
    'Stock': 1,
    'Type_of_item': "Game",
    'Director': "Yoshinori Kitase",
    'Genre': "ATB Turn Based RPG",
    'Initial_price': 2,
    'Replacement_price': 2.0
}
games3 = {
    'Name': 'Final Fantasy VII',
    'Stock': 0,
    'Type_of_item': "Game",
    'Director': "Yoshinori Kitase",
    'Genre': "ATB Turn Based RPG",
    'Initial_price': 2,
    'Replacement_price': 2.0
}
inventory = {
    '1': {
        'Name': 'Billy'
    },
    '2': {
        'Name': 'Dansen'
    },
    '3': {
        'Name': 'Amy'
    },
    '4': {
        'Name': 'Preston Garvey'
    }
}

inv = {
    '1': {
        'Name': 'CS: GO',
        'Stock': 5,
        'Replacement_price': 10,
        'Initial_price': 2
    }
}


def test_deposit_fee_games():
    assert core.deposit_fee(games) == 0.2


def test_total_rental_fee_games():
    days = '3'
    assert core.total_rental_fee(games, days) == 6.42


def test_can_not_return_games():
    assert core.can_return(games) == False


def test_can_return_games():
    assert core.can_return(games2) == True


def test_is_in_stock():
    assert core.is_in_stock(games) == True


def test_not_in_stock():
    assert core.is_in_stock(games3) == False


def test_make_inven_options():
    assert core.make_inven_options(
        inventory) == """1--Billy\n2--Dansen\n3--Amy\n4--Preston Garvey"""


def test_make_employee_inven():
    assert core.employee_inven(
        inv
    ) == '''1--CS: GO, Stock: 5, Replacement Price: 10, Initial Price: 2'''


def test_make_history():
    time = "12:00"
    name = "Raid"
    days = 3
    fee_1 = 5
    fee_2 = 10
    assert core.make_history(time, name, days, fee_1, fee_2) == {
        'time': '12:00',
        'Name': "Raid",
        'days_rental': 3,
        'deposit': 5,
        'profit': 10
    }
