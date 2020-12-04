r = int(input("Enter the no of rows:")) 
c = int(input("Enter the no of columns:")) 
 
m = [] 
print("Enter the numbers:")   
for i in range(r):          
    a =[] 
    for j in range(c):      
         a.append(int(input())) 
    m.append(a)  
for i in range(r): 
    for j in range(c): 
        print(m[i][j], end = " ") 
    print()