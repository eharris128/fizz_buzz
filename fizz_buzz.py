import sys

counter = 1

if len(sys.argv) == 1:
    index = int(input('Pick any positive number: '))
else:
    index = int(sys.argv[1])

while counter <= index:
    if counter % 15 == 0:
        print('Fizz buzz counting up to fizzbuzz')
    elif counter % 5 == 0:
        print('Fizz buzz counting up to buzz')
    elif counter % 3 == 0:
        print('Fizz buzz counting up to fizz')
    else:
        print('Fizz buzz counting up to {}'.format(counter))
    counter += 1