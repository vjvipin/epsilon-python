l = [10,20,30,40,50]
l2 = [value * value for value in l]
print(l2)

# map 
def sqr(num1):
#     print(num1)
    return num1 * num1 
    

l = [10,20,30,40,50,60]
m = list(map(sqr,l))
print(m)

# ex 2
def add(num1,num2,num3):
    print(num1,num2,num3)
    return num1 + num2 + num3

l1 = [1,2,3,4,5]
l2 = [10,20,30,40,50]
l3 = [100,200,300,400,500]

l = list(map(add,l1,l2,l3))
print(l)

# filter 

def even(num1):
    if num1 % 2 == 0:
        return True
    else:
        return False
l = [10,20,30,45,15,35,45,80]
f = list(filter(even,l))
print(f)


# lambda and map
l = [10,20,30,40,50]
m = list(map(lambda num1: num1 * num1,l))
print(m)

l1 = [10,20,30,40,50]
l2 = [1,2,3,4,5]
l3 = [100,200,300,400,500]

l4 = list(map(lambda num1,num2,num3:num1 + num2 + num3,l1,l2,l3))
print(l4)


# lambda and filter

l = [10,20,30,45,25,45,30,47,80]
l2 = list(filter(lambda num1: num1 %2 == 0,l))
print(l2)

# lambda
char = 'a'
f = lambda char: 'vowel' if char in 'aeiou' else 'consonent'
print(f(char))


