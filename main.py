def list_comprehension_exercise_1():
    list_comprehension = [ x for x in range(0, 11)]
    return list_comprehension
def list_comprehension_exercise_2():
    list_comprehension = [ x for x in range(0, 22) if x%2 == 0 or x%3 == 0]
    return list_comprehension
def list_comprehension_exercise_3():
    list_comprehension = [ x for x in range(-5, 32) if x%2 != 0 and x%5 != 0]
    return list_comprehension
def list_comprehension_exercise_4():
    list_comprehension = [ x**2 for x in range(0, 11)]
    return list_comprehension
def list_comprehension_exercise_5(sentence):
    list_comprehension = [ x for x in sentence if x.isupper()]
    return list_comprehension
def list_comprehension_exercise_6(sentence):
    list_sentence = sentence.split(" ")
    list_comprehension = [ list_sentence for list_sentence in list_sentence if len(list_sentence) > 3 and list_sentence[0].lower() == "r"]
    return list_comprehension

list_comprehension_exercise_6('O Rato Rui Gosta De QueiJo FresQuiNho')