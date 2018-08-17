#!/bin/python3

def matrixRotation(m, n, r, matrix, x, y):
    if min(m, n) < 2:
        return matrix
    else:
        layer = []
        for i in range(n):
            layer.append(matrix[x][y + i])
            
        for i in range (1, m):
            layer.append(matrix[x + i][y + n - 1])
            
        for i in range (1, n):
            layer.append(matrix[x + m - 1][y + n - 1 - i])  
            
        for i in range (1, m - 1):
            layer.append(matrix[x + m - 1 - i][y])
               
        mxx = x
        myy = y
        i = 0
        while i < n:           
            matrix[mxx][myy] = layer[(i + r) % len(layer)]
            myy = myy + 1
            i = i + 1         
        mxx = mxx + 1
        myy = myy - 1
        
        while i < n + m - 1:
            matrix[mxx][myy] = layer[(i + r) % len(layer)]
            mxx = mxx + 1
            i = i + 1      
        mxx = mxx - 1
        myy = myy - 1    
        
        while i < (2 * n) + m - 2:
            matrix[mxx][myy] = layer[(i + r) % len(layer)]      
            myy = myy - 1
            i = i + 1
        myy = myy + 1
        mxx = mxx - 1
        
        while i < (2 * n) + (2 * m) - 3:
            matrix[mxx][myy] = layer[(i + r) % len(layer)]
            mxx = mxx - 1
            i = i + 1
    
        return matrixRotation(m - 2, n - 2, r, matrix, x + 1, y + 1)
        
    
if __name__ == '__main__':
    mnr = input().split()

    m = int(mnr[0])

    n = int(mnr[1])

    r = int(mnr[2])

    matrix = []

    for _ in range(m):
        matrix.append(list(map(int, input().rstrip().split())))

    ret = matrixRotation(m, n ,r, matrix, 0, 0)
    
    for i in range(len(matrix)):
        s = ""
        for j in range(len(matrix[0])):
            s += str(matrix[i][j]) + " "
        print(s)
