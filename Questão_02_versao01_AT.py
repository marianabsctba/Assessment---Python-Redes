#Questão 2)
#Escreva um programa que obtenha um nome de um arquivo texto do usuário e crie um processo para
#executar o programa do sistema Windows bloco de notas (notepad) para abrir o arquivo.

import os, platform

platformer = platform.system()


def main():
    user_file = (input("Qual arquivo de texto você deseja abrir? ") + ".txt")
    if platformer  == 'Windows':    #windows notepad
        os.system(f"notepad {user_file}") 
    else:
        print("O sistema op. não é Windows. Programa reiniciado.")
        exit(1)


if __name__ == "__main__":
    main()
