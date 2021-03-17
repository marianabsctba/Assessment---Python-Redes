import os


def see_files():
    pairs = []
    
    directory = os.getcwd()
    lists = os.listdir(directory)
    
    for file in lists:
        location = os.path.join(directory, file)        
        if os.path.isfile(location):
            
            size = os.path.getsize(location)
            size = round((size/1024), 2)
            pairs.append((location, size))

    pairs.sort(key=lambda s: s[1], reverse=True) #do maior tamanho para o menor
    return pairs


def print_files():    
    text = ''
    
    p = see_files()
    
    for l, pair in p:
        text += "Arquivo: {:>20}, tamanho(kB): {:<10}\n".format(l, pair)
        #print(text)

    new_file = open("questao3_AT.txt", "w")
    new_file.write(text)
    new_file.close()
    os.startfile('questao3_AT.txt')

print_files()


