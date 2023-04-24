'''
The Exam Results
v.1.0
Gerasimchik D.Y.
QA2022
24.04.2023
'''
from random import randrange


def count_marks(ls):
    five = 0
    four = 0
    three = 0
    deuce = 0
    unit = 0
    zero = 0
    for item in ls:
        if item == 5:
            five += 1
        elif item == 4:
            four += 1
        elif item == 3:
            three += 1
        elif item == 2:
            deuce += 1
        elif item == 1:
            unit += 1
        elif item == 0:
            zero += 1

    return five, four, three, deuce, unit, zero


def count_percent(five, four, three, deuce, unit, zero, size):
    five_prcnt = round(five / size * 100, 1)
    four_prcnt = round(four / size * 100, 1)
    three_prcnt = round(three / size * 100, 1)
    deuce_prcnt = round(deuce / size * 100, 1)
    unit_prcnt = round(unit / size * 100, 1)
    zero_prcnt = round(zero / size * 100, 1)

    return (five_prcnt, four_prcnt, three_prcnt,
            deuce_prcnt, unit_prcnt, zero_prcnt)


def automatic_or_manual():
    answer = input("Would you like to use manual or automatic random data entry?"
                   "\nЖелаете воспользоваться ручным или автоматическим рандомным вводом данных?"
                   "\nManual (M or 1) / (A or 2) Automatic: ")
    if answer == "1" or answer.casefold() == "m" or answer.casefold() == "м":
        return True
    else:
        return False


def auto_create_list(size, def_mark=3):
    ls = []
    for _ in range(size):
        ls.append(def_mark)
    return ls


def rand_marks(ls):
    for i in range(len(ls)):
        ls[i] = randrange(6)


def manual_create_list(size):
    ls = []

    for item in range(size):
        num = input(f"Input a grade for student №{item + 1}: ")

        while (not 0 <= int(num) <= 5):
            num = input(f"Oops! Invalid data. Try again..\n"
                        f"Input a grade for student №{item + 1}: ")
        else:
            ls.append(int(num))

    return ls


def covert(ls):
    msg = ""
    for item in ls:
        msg += str(item) + " "
    return msg


def main():
    # size = abs(int(input("Input the number of students: ")))
    if automatic_or_manual():
        size = abs(int(input("Input the number of students: ")))
        ls = manual_create_list(size)
    else:
        size = abs(int(input("Input the number of students: ")))
        ls = auto_create_list(size)
        rand_marks(ls)

    five, four, three, deuce, unit, zero = count_marks(ls)
    (five_prcnt, four_prcnt, three_prcnt,
     deuce_prcnt, unit_prcnt, zero_prcnt) = count_percent(five, four, three,
                                                          deuce, unit, zero, size)

    output_eng(five, four, three, deuce, unit, zero,
               five_prcnt, four_prcnt, three_prcnt,
               deuce_prcnt, unit_prcnt, zero_prcnt, ls)

    output_rus(five, four, three, deuce, unit, zero,
               five_prcnt, four_prcnt, three_prcnt,
               deuce_prcnt, unit_prcnt, zero_prcnt, ls)


def output_rus(five, four, three, deuce, unit, zero,
               five_prcnt, four_prcnt, three_prcnt,
               deuce_prcnt, unit_prcnt, zero_prcnt, ls):
    msg = f"""Обработка результатов экзамена
Исходные оценки: {covert(ls)}

Результаты экзамена:
пятерок - {five_prcnt} % ({five})
четверок - {four_prcnt} % ({four})
троек - {three_prcnt} % ({three})
двоек - {deuce_prcnt} % ({deuce})
единиц - {unit_prcnt}% ({unit})
нулей - {zero_prcnt}% ({zero})"""

    print(msg)


def output_eng(five, four, three, deuce, unit, zero,
               five_prcnt, four_prcnt, three_prcnt,
               deuce_prcnt, unit_prcnt, zero_prcnt, ls):
    msg = f"""\nThe Exam Result Handling
Marks: {covert(ls)}
Exam Result:
fives - {five_prcnt} % ({five})
fours - {four_prcnt} % ({four})
triplets - {three_prcnt} % ({three})
deuces - {deuce_prcnt} % ({deuce})
units - {unit_prcnt}% ({unit})
zeros - {zero_prcnt}% ({zero})\n"""

    print(msg)


def test():
    marks = str(count_marks([0, 1, 2, 3, 4, 5]) == (1, 1, 1, 1, 1, 1)) + "\n"
    marks += str(count_marks([5, 5, 5]) == (3, 0, 0, 0, 0, 0)) + "\n"
    marks += str(count_marks([4, 4]) == (0, 2, 0, 0, 0, 0)) + "\n"
    marks += str(count_marks([3, 3, 3]) == (0, 0, 3, 0, 0, 0)) + "\n"
    marks += str(count_marks([2]) == (0, 0, 0, 1, 0, 0)) + "\n"
    marks += str(count_marks([1, 1, 1, 1]) == (0, 0, 0, 0, 4, 0)) + "\n"
    marks += str(count_marks([0, 0]) == (0, 0, 0, 0, 0, 2)) + "\n"
    marks += str(count_marks([]) == (0, 0, 0, 0, 0, 0)) + "\n"
    marks += str(count_marks([16, 8, -10]) == (0, 0, 0, 0, 0, 0))

    percent = "\n\n" + str(count_percent(1, 1, 1, 1, 1, 1, 5)
                           == (20, 20, 20, 20, 20, 20)) + "\n"
    percent += str(count_percent(0, 0, 0, 0, 0, 0, 5) == (0, 0, 0, 0, 0, 0))

    print(marks, percent)


if __name__ == '__main__':
    main()
    test()
