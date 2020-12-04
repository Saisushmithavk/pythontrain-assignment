rows = int(input("Enter the number of rows:")) 
columns= int(input("Enter the number of columns:")) 
 
matrix = [] 
print("Enter the entries row wise:") 
  
for i in range(rows):           
    a =[] 
    for j in range(columns):       
         a.append(int(input())) 
    matrix.append(a) 
 
for i in range(rows): 
    for j in range(columns): 
        print(matrix[i][j], end = " ") 
    print() 