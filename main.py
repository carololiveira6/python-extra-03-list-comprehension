import re

def list_comprehension_exercise_1():

    number_list = [ x for x in range(11) ]
    print(number_list)

def list_comprehension_exercise_2():

    number_list = [ x for x in range(22) if x % 2 == 0 or x % 3 == 0]
    print(number_list)

def list_comprehension_exercise_3():

    number_list = [ x for x in range(-5, 32) if x % 2 != 0 and x % 5 != 0]
    print(number_list)

def list_comprehension_exercise_4():

    number_list = [ x * x for x in range(11) ]
    print(number_list)

sentence = 'O Rato Rui Gosta De QueiJo FresQuiNho'

def list_comprehension_exercise_5(sentence: str):

    result = [ x for x in sentence if x.isupper() == True]
    print(result)

another_sentence = 'o rato rui roeu a roupa do rei de roma'

def list_comprehension_exercise_6(another_sentence: str):
    
    result = [ x for x in re.split(r'\W', another_sentence) if len(x) >= 4 and x.startswith('r')]
    print(result)

if __name__ == '__main__':

    first_function = list_comprehension_exercise_1()

    second_function = list_comprehension_exercise_2()

    third_function = list_comprehension_exercise_3()

    fourth_function = list_comprehension_exercise_4()

    fifth_function = list_comprehension_exercise_5(sentence)

    sixth_function = list_comprehension_exercise_6(another_sentence)