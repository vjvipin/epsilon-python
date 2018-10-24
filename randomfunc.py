import random

#print(dir(random))
#print(help(random.uniform))
#a = random.random()
#a = random.randrange(5,30)
#print(help(random.randrange))
#random.seed(5)
#a = random.randint(5,30)
l = [2,3,1,34,56]

mylist = list(range(100))
random.shuffle(mylist)
print(mylist)

#print(random.choice(l))
random.shuffle(l)
print(l)

#print(a)
'''
a = random.randint(5,30)
print(a)
print(l)
#print(random.uniform(3,90))
l = list(range(1,1000))
print(l)
random.shuffle(l)
print(l)
#l = random.randrange(1,1000)
'''
