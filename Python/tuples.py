"""
Given an integer, n , and n space-separated integers as input, create a tuple, t ,
of those n integers. Then compute and print the result of .
"""
if __name__ == '__main__':
    n = int(input())
    integer_list = input().split()
    integer_list = [int(x) for x in integer_list]
    t = tuple(integer_list)
    result = hash(t)
    print(result)
