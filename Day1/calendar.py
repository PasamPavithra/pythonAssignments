w = 3 
start=w-1
print('sun mon tue wed thu fri sat')
print(' ' * (start * 4), end='')
for var in range(1,31):
	print(f'{var:<3}',end=' ')
	start+=1
	if start%7==0:
		start=0
		print()