import os, platform, subprocess


user_file = (input("Qual arquivo de texto você deseja abrir? ") + ".txt") #aqui eu limitei a abertura de arquivos txt de modo genérico, só para testar
    
def open_file_notepad(): 
    try:    
        if platform.system() == 'Darwin':       #MACOS
            subprocess.call(('open', user_file))
        elif platform.system() == 'Windows':    #windows, mas abrindo o arquivo de texto automaticamente
            os.startfile(user_file)
        else:                                   
            subprocess.call(('xdg-open', user_file)) #Linux
    except FileNotFoundError as e:
        print(e)
        
        
open_file_notepad()
