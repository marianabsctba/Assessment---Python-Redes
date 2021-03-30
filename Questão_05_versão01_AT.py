#Questão 05)
#Escreva um programa em Python que leia dois arquivos, a.txt e b.txt, como a seguir (...)

#Seu programa deve somar elemento por elemento de cada arquivo e imprimir o resultado na tela.
#Isto é, o primeiro elemento de a.txt deve ser somado ao primeiro elemento de b.txt, segundo elemento de a.txt deve ser somado ao segundo elemento de b.txt,
#e assim sucessivamente. Caso um arquivo tenha mais elementos que o outro, os elementos que sobrarem do maior devem ser somados a zero.

import numpy as np

def files(file_name):
    try:
        with open(file_name, 'r') as file:
            data = file.read().split()
        return data
    except FileNotFoundError as error:
        return (str(error))


def lis(first_list):
    second_list = []
    for v in first_list:
        try:
            second_list.append(int(v))
        except:
            pass
            second_list.append(0)
    return second_list


def sum_files():
    count_a = len(a)
    count_b = len(b)

    if count_a < count_b:
        a[count_a:count_b] = (count_b - count_a) * [0]
    else:
        b[count_b:count_a] = (count_a - count_b) * [0]

    print("Soma: ", np.array(a) + np.array(b))



a = files('a.txt')
b = files('b.txt')

print('A:', a)
print('B:', b)

a = lis(a)
b = lis(b)

sum_files()
