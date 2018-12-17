matrix = []
counter = 0
width = height =0

while True:
    b = input().split()
    if b[0] == "end":        
        break
    else:
        b = list(map(int, b))
        height = len(b)
        matrix.append(b)
        counter+=1
    width = counter

def print_m(m):    
    if width == height == 1:
        print(m[0])
                        
    else:                
        for i in m:
            for column in i:
                print(column, end = '  ')
            print()

def print_one_liner(m):    
    for i in range(height):
        print(m[0][i],end = ' ')

    
def print_one_column(m):
    for i in range(width):
        print(m[i][0])
        
def gen_one_liner_matrix(old_matrix):
    new_m = [[0 for i in range(height)]]    
    for i in range(height):                     
        left_j = i-1
        right_j = i+1        
        if i == 0: #leftmost element           
            left_j = -1
        if i == height-1:#rightmost element            
            right_j = 0
            
        left_element = old_matrix[0][left_j]
        right_element = old_matrix[0][right_j]
        sum_s = old_matrix[0][i] *2 + left_element + right_element
        new_m[0][i] = (old_matrix[0][i] *2 + left_element + right_element)
    print_one_liner(new_m)
   
def gen_one_column(old_matrix):
    new_matrix = [ [ 0 for i in range(1)] for j in range(width)]
    for i in range(width):
        top_i = i-1
        bottom_i = i+1
        if i == 0:
            top_i = -1
        if i == width-1:            
            bottom_i = 0           
        top_element = old_matrix[top_i][0]
        bottom_element = old_matrix[bottom_i][0]
        
        sum_s = old_matrix[i][0]*2 + top_element+bottom_element
        
        new_matrix[i][0] = sum_s
    print_one_column(new_matrix)
 
def gen_matrix(old_matrix):    
    if width == 1 and height == 1:
        print(old_matrix[0][0]*4)
    elif width == 1 and height >1:
        gen_one_liner_matrix(old_matrix)
        
    elif height == 1 and width != 1:
        gen_one_column(old_matrix)
    else:
        new_matrix = [[0 for i in range(height)] for j in range(width)]
        for row in range(width):            
            for column in range(height):

                top_i = row-1
                top_j = column
                
                bottom_i = row+1
                bottom_j = column

                left_i = row
                left_j = column-1
                
                right_i = row
                right_j = column+1
                if top_i < 0:
                    top_i == -1                
                if bottom_i > width-1:
                    bottom_i = 0
                if left_j < 0:
                    left_j == -1
                if right_j > height-1:
                    right_j = 0
                
                top_el = old_matrix[top_i][top_j]
                bottom_el = old_matrix[bottom_i][bottom_j]                
                left_el = old_matrix[left_i][left_j]
                right_el = old_matrix[right_i][right_j]
                sum_s = top_el+bottom_el+left_el+right_el                            
                new_matrix[row][column] = (sum_s)
                
        print_m(new_matrix)

new_2 =gen_matrix(matrix)
