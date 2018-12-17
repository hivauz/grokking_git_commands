import time
n = 6
result_matrix = [[0 for x in range(n)] for y in range(n)]

def print_matrix( r):
  for i in range(n):
    for j in range(n):
      print(r[i][j], end = '\t')
    print()

counter = 1
k = n
# row left to right
print("the middle is" + str((n//2+1)))
for i in range(n//2+1):
    time.sleep(2)
    print("********************************************")
    
    print("i: " + str(i) + " k: " + str(k))
    for di in range(i,k):
      print("[" + str(i) + "]" + "[" + str(di) + "]", end=' ')
      result_matrix[i][di] = counter
      counter+=1
    
    print()
    #print_matrix(result_matrix)

    for di in range(i+1,k):
      print("[" + str(di) + "]" + "[" + str(k-1) + "]", end=' ')
      result_matrix[di][k-1] = counter
      counter+=1
    
    print()
    #print_matrix(result_matrix)
    for di in range(-(i+2), -(k+1),-1):
      print("[" + str(k-1) + "]" + "[" + str(di) + "]", end=' ')
      result_matrix[k-1][di] = counter
      counter+=1
    
    print()
    #print_matrix(result_matrix)
    for di in range(-(i+2),-k,-1):
      print("[" + str(di) + "]" + "[" + str(i) + "]", end=' ')
      result_matrix[di][i] = counter
      counter+=1
    print()
    
    #print()
    #print_matrix(result_matrix)
    k = k-1


print("\n\n\n--------------------")
#print_matrix(result_matrix)


print(result_matrix[5][-2])
