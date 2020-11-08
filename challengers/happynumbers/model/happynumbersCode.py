
def happy_numbers(numbers):

    number = str(numbers)

    while True:
        soma = 0

        for y in number:
            soma += int(y) ** 2
            number = str(soma)

        if soma == 4:
            return 'sad'.title()

        if soma == 1:
            return 'happy'.title()
