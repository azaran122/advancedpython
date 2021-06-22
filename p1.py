numbers=[10,11,8,6,100,7,9,2]
a=list(map(lambda x: 'big' if x>10 else 'small', numbers))
print (a)
mylist=[1,5,3,7,9,10,3]
a=list(filter(lambda x: x%2 == 0, mylist))
print(a)

#generator
def firstn():
 return(1,2,3)
# yield
def firstn1():
 yield 1
 yield 2
 yield 3

a=firstn()
print('function returns:',a)


b=firstn1()
print('yieldcall:', b)
print('yieldcall:', b)



