"""
Let's learn about list comprehensions! You are given three integers X,Y and Z representing the dimensions of a cuboid
along with an integer . You have to print a list of all possible coordinates given by (i,j,k) on a 3D grid where
the sum of  is not equal to N .
"""

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    lista = [[i, j, k] for i in range(0, x + 1) for j in range(0, y + 1) for k in range(0, z + 1) if i + j + k != n]
    print(lista)