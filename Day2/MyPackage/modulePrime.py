def getPrime():
    __name__
prime=[]
a =int(input("enter the number:"))
for n in range(a,a+100):
	isPrime =True
	for i in range(2,n):
		if(n % i) == 0:
			isPrime =False
	if isPrime:
		prime.append(n)
print(prime)

if __name__ == "__main__":
    getPrime()