import os, platform, subprocess


user_file = (input("Qual arquivo de texto você deseja abrir? ") + ".txt") 
    
def open_file_notepad(): 
    try:    
        if platform.system() == 'Darwin':       #MACOS (vi outra forma de usar um executável chamado paralell, mas não baixei)
            subprocess.call(('open', user_file))
        elif platform.system() == 'Windows':    #windows, mas abrindo o arquivo de texto automaticamente, eis que bloco de notas seria automático
            os.startfile(user_file)
        else:                                   
            os.system('gedit', user_file) #Linux #não consegui testar windows nem MAC, pois não possuo
        
        print(f"Sistema Operacional: {os.name} {platform.system()} {platform.release()}")
    except:
        print("Erro. Escolha novo arquivo e/ou verifique seu SO ou tente novamente.")
        print(f"Sistema operacional: {os.name} {platform.system()} {platform.release()}")        
        pass
        
        
open_file_notepad()
