
num = int(input())


for i in range(num):
    for j in range(num -i - 1,0, -1):
        print(' ',end='')

    for k in range(i + 1):
	    print('*',end='')

    print()

for i in range(1, num+1):
    for j in range(num-i):
        print(' ', end='')

    for k in range(i):
        print('*', end='')

    print()

for i in range(num):
	print(" " * (num - i - 1), end = "")
	print("*" * (i + 1))
