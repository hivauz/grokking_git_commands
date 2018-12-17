n = 6
a = [] ; b = [] ; i = 0 ; j = -1 ;
z = 0

a = [ [0 for i in range(n)] for j in range(n)]
    
while z != n**2:
    
    for right in range(n):        
        z += 1
        j += 1
        a[i][j] = z
    n -= 1
    for bottom in range (n):
        z += 1
        i += 1
        a[i][j] = z
    for left in range (n):
        z += 1
        j -= 1
        a[i][j] = z
    n -= 1
    for up in range (n):
        z += 1
        i -= 1
        a[i][j] = z


for row in a:
    for element in row:
        print (element, end = " ")
    print ()
