index = 0

while index != 16:
    if index % 15 == 0:
        print('Fizz buzz counting up to fizzbuzz')
    elif index % 5 == 0:
        print('Fizz buzz counting up to buzz')
    elif index % 3 == 0:
        print('Fizz buzz counting up to fizz')
    else:
        print('Fizz buzz counting up to {}'.format(index))
    index += 1

