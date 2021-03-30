#Questão 05)
#Escreva um programa em Python que leia dois arquivos, a.txt e b.txt, como a seguir (...)

#Seu programa deve somar elemento por elemento de cada arquivo e imprimir o resultado na tela.
#Isto é, o primeiro elemento de a.txt deve ser somado ao primeiro elemento de b.txt, segundo elemento de a.txt deve ser somado ao segundo elemento de b.txt,
#e assim sucessivamente. Caso um arquivo tenha mais elementos que o outro, os elementos que sobrarem do maior devem ser somados a zero.


def lining():
    print("==" * 40)

def sum_data_files(): 

    lines, cols = 1, 10      # partindo do pressuposto em se sabendo número de linhas e colunas
    sums = [[0] * cols for _ in range(lines)]

    files_names = ["a.txt", "b.txt"]
    
    for file in files_names:
        with open(file) as f:
            for i, lin in enumerate(f):
                for j, col in enumerate(lin.split()):
                    sums[i][j] += int(col)                    
                    
    lining()    
    print("O resultado da soma dos números dos arquivos", files_names[0], "e", files_names[1], "é: ")
    
    for lin in sums:
        print(*lin)
    lining()


sum_data_files()
