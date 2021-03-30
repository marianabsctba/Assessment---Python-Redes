#Questão 2)
#Escreva um programa que obtenha um nome de um arquivo texto do usuário e crie um processo para
#executar o programa do sistema Windows bloco de notas (notepad) para abrir o arquivo.

import os, platform, subprocess

user_file = (input("Qual arquivo de texto você deseja abrir? ") + ".txt")  #observação: não tenho linux nem mac para testar, infelizmente.

platformer = platform.system()
    
def open_file_notepad(): 
    try:    
        if platformer == 'Darwin':       #MACOS
            subprocess.call(('open', user_file))
        elif platformer == 'Windows':    #windows notepad
            os.system(f"notepad {user_file}") 
        else:                                   
            subprocess.call(('xdg-open', user_file)) #Linux
    except:
        print('Erro. Tente novamente ou escolha novo arquivo.")
        
        
open_file_notepad()
