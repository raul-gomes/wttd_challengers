
def tira_modulo(base, num):
    return num % base == 0


def sayFizzBuzz(num):

    say = int(num)

    if tira_modulo(3, num):
        say = 'fizz'

    if tira_modulo(5, num):
        say = 'buzz'

    if tira_modulo(3, num) and tira_modulo(5, num):
        say = 'fizzbuzz'

    return say