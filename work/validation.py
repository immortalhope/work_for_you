import re
# функція повертає ціле число більше нуля до трьох знаків
def get_number(text):

    while True:
        number_str = input(text)

        # if bool(re.match(r"\d{1,3}", number) ):
        #     correct = True
        # else:
        #     correct = False
        # correct = bool(re.match(r"\d{1,3}", number_str) )
        #

        if bool(re.match(r"\d{1,3}", number_str) ):
            number = int(number_str)
            if number > 0:
                return number

#\d визначає всі цифри
# {1,3} від одного знака до трьох