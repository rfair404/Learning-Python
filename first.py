print("hello world")
#print('hello world 2')
'''
a=1
b=3
print(a+b)
'''
# a="4"
# b="15"
# # print(int(a)+int(b))
# print(float(int(b) ** int(a)))
#print()
'''
a=9
if a == 0:
	print("zero")
elif a <= 5:
    print(a)
else:
    print("a mroe than 5")
'''

def oddOrEven(number):
	if(number % 2 == 0):
		return("that number is even")

	else:
		return("that number is odd")



# for a in range(5,25):
#     print(a)

a = 1
while a<10:
	print(a)
	b=oddOrEven(a)
	print(b.replace('even', 'odd'))
	a+=3

while a<20:
	print(a)
	b=oddOrEven(a)
	print(b.replace('odd', 'even'))
	a+=5