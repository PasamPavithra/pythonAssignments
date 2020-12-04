l=[]
n=int(input('enter no:'))
for x in range(100):
	l.append(n + x)
print(l)
	
for x in range(100):
	for n in range(2,l[x]):
		if l[x]%n==0:
			l[x]=0
			break
print(l)

zero,max=0,0
for x in range(100):
	if l[x]==0:
		zero+=1
	else:
		if max<zero:
			max=zero
		zero=0
			
print(f'zeros count-->{max}')