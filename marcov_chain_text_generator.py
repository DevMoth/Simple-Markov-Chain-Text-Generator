# Given a list of words generates a graph of all connections between words in the list
def gen_graph_from_list(gen_list):
    Dict = []
    for elem in gen_list:
        if elem not in Dict:
            Dict.append(elem)
    Matr = [[0 for j in range(len(Dict))] for i in range(len(Dict))]
    for i in range(0, len(gen_list)-1):
        ind_st = Dict.index(gen_list[i])
        ind_fn = Dict.index(gen_list[i+1])
        Matr[ind_st][ind_fn] += 1
    return [Matr, Dict]
# Given a plain text and a list of characters to remove, generates a graph of all connections between the words in the text with excluded characters
def gen_graph_from_text(text, *, ignore_list = []):
    for elem in ignore_list:
        text = text.replace(elem, "")
    gen_list = text.split()
    return gen_graph_from_list(gen_list)
    
import random as r
#Given a graph of connections, previous state and a chance to randomly "hop" to a different node, returns a new state (the index of a chosen element)
def marc_chain_step(matr, state_ind, *, rand_hop_chance = 0):
    summ = sum(matr[state_ind])
    if r.random() <= rand_hop_chance or summ == 0:
        return r.randint(0, len(matr)-1)
    choice = r.randint(1, summ)
    new_state = -1
    while choice > 0:
        new_state += 1
        choice -= matr[state_ind][new_state]
    return new_state

#Given a list of words to print, asks the user if the words should be output as a list or as text and outputs accordingly
def print_routine(print_list):
    sep_mode = input("Вывести текст списком? (да/Нет)\n")
    if sep_mode == "Да":
        sep = "\n"
    else:
        sep = " "
    for word in print_list:
        print(word, end = sep)
    if sep != "\n":
        print()
# Main program loop
while 1:
    #Asks the user for the mode of input (1- showcase, 2- direct input, 3- input from a text file)
    mode = input("Выберите режим(введите число):\n 1. Огурец\n 2. Ввод\n 3. Ввод из файла\n")
    if mode == "1":
        f = open("дикий_огурец.txt", encoding = "utf-8")
        fruit_lines = [a.replace("\n", "") for a in f.readlines()]
        Matr, Dict = gen_graph_from_list(fruit_lines)
    elif mode == "2":
        Matr, Dict = gen_graph_from_text(input("Текст: "))
    elif mode == "3":
        text = open(input("Имя файла: "), encoding = "utf-8").read().replace("\n", "")
        Matr, Dict = gen_graph_from_text(text)
    else:
        Matr = [[1]]
        Dict = ["гойда"]
        print("Неверный режим, используется шуточный режим")

    # Asks the user for the count of words to be output
    iterations = int(input("Количество слов: "))
    result = []
    state = 0
    for i in range(iterations):
        result.append(Dict[state])
        state = marc_chain_step(Matr, state, rand_hop_chance = 0.1)
    print_routine(result)
    print()
        
