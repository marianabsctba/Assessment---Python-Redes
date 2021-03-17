#Questão 04)
#Escreva um programa em Python que leia um arquivo texto e apresente na tela o seu conteúdo reverso.

import os


file_name = "questao4.txt"


def reversed_file(file_name):
    with open(file_name) as file:
        file.seek(0, os.SEEK_END)
        pos = file.tell()
        line = ''
        while pos >= 0:
            file.seek(pos)
            next_line = file.read(1)
            if next_line == "\n":
                yield line[::-1]
                line = ''
            else:
                line += next_line
            pos -= 1
        yield line[::-1]


if __name__ == '__main__':
    for line in reversed_file(file_name):
        print(line[::-1])
