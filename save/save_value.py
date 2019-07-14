from telephone_book import tel_dictionary


def save_value():
    tel_dictionary[input('Insert Name: ')] = input('Insert Phone number:')
