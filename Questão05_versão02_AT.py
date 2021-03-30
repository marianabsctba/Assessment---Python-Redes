def lining():
    print("==" * 20)
    

def sum_data_files():
    lines, cols = 1, 10      
    sums = [[0] * cols for _ in range(lines)]  
    try:
        for file in files_names:
            with open(file) as f:
                for i, lin in enumerate(f):
                    for j, col in enumerate(lin.split()):
                        sums[i][j] += int(col)
        for lin in sums:
            print(*lin)
            
    except FileNotFoundError as error:
        print(str(error))
  
    
   
files_names = ["a.txt", "b.txt"]

lining()
sum_data_files()
lining()
