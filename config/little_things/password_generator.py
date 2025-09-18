import random

def get_random_password(len_pass, type_pass):
    symbols_1 = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    symbols_2 = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+[]{}|;:\'\",.<>?/'

    result = ''
    if type_pass:
        for i in range(len_pass):
            result += random.choice(symbols_2)
    else:
        for i in range(len_pass):
            result += random.choice(symbols_1)

    print(result)

    return result