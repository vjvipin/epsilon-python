#itertools:
import itertools

#for i in itertools.chain([1,2,3], 'abc', (3,4)):
#	print (i)

#a=0
#for i in itertools.cycle('abcd'):
#	print (i)
#	a=a+1
#	if a==10:
# 		break
a=0
for i in itertools.count(5,5):
 	print (i)
 	a=a+1
 	if a==5:
 		break

for i in itertools.repeat('abcd', 8):
	print (i)
a=[2,4,-6,-4,2]
# for i in itertools.ifilter(lambda x:x>0, a):
# 	print (i)

# a=lambda x: 2 if x%2==0 else 1
# print (a(7))

# for i in itertools.ifilterfalse(lambda x:x>0, a):
# 	print (i)

# for i in itertools.imap(lambda x:x*2, a):
# 	print (i)

# for i in itertools.permutations('abcd', 3):
# 	print (i)

# for i in itertools.combinations('abcd', 3):
# 	print (i)

# for i in itertools.combinations_with_replacement('abcd', 5):
# 	print (i)

# for i in itertools.product("abcd", repeat=3):
# 	print (i)

# for i in itertools.izip([1,2,3], 'abc', (34,56,78)):
# 	print (i)

#generators

# def myGenerator():
# 	i=0
# 	while i<5:
# 		yield i
# 		i+=1
# f=myGenerator()
# # print (type(f))
# # print (f)
# print (f.next())
# print (f.next())
# print (f.next())

# def myGenerator():
# 	i=0
# 	while i<5:
# 		return 'hello'
# 		i+=1
# f=myGenerator()
# print (type(f))

#decorators:
# name='habc'
# def myDecorator(a):
# 	def internalFunc():
# 		print ("before function call")
# 		if name.startswith('a'):
# 			a()
# 		print ('after function call')
# 	return internalFunc

# @myDecorator
# def func():
# 	print ('hello')

# func()

