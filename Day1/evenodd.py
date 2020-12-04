start=int(input('enter an start number'))

print('even number')
for n in range(start, start+10):
    if(n % 2 == 0):
        print("{0}".format(n),end=' ')
        
print('odd number')
for n in range(start, start+10):
    if(n % 2 != 0):
        print("{0}".format(n),end=' ')