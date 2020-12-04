a = int(input("Enter the start no: "))

for num in range (a, a + 100):
    count = 0
    for i in range(2, (num//2 + 1)):
        if(num % i == 0):
            count = count + 1
            break

    if (count == 0 and num != 1):
        print(" %d" %num, end = '  ')