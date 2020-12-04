def recursion(n):
    if(n<=10):
        print(n, end=' ')
        recursion(n+1)

recursion(1)