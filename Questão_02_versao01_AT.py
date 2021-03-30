#Questão 2)
#Escreva um programa que obtenha um nome de um arquivo texto do usuário e crie um processo para
#executar o programa do sistema Windows bloco de notas (notepad) para abrir o arquivo.

import os, platform, subprocess


user_file = (input("Qual arquivo de texto você deseja abrir? ") + ".txt")

    
def open_file_notepad(user_file):
    if os.path.exists(user_file):         
        platformer = platform.system()
        
        if platformer == "Windows":
            print("Sistema Operacional: ", platformer)
            os.system(f"notepad {user_file}")            
        else:
            print("Sistema Operacional: ", platformer)
            subprocess.Popen(['APP_COMMAND', f'~/{user_file}'])    
    else:
        print(f'O arquivo {user_file} não existe ou não é um arquivo. Tente novamente.')
        exit(1)
            
        
open_file_notepad(user_file)
