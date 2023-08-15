x = int(input("Enter The Number:"))
a = "It Is Prime Number"
for i in range(2, x):
	if x % i == 0:
		a = "It Is Not Prime Number"
print(a)
