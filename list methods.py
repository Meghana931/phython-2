#Implementing list methods.
#1)append()
l1 = [4,8,16,32]
l1.append(64)
#2)clear()
l2 = [9,18,27,36]
l2.clear()
#3) count()
l3 = [10,20,30,40]
l3.copy()
#4) count() list.count takes exactly one argument
l4 = [20,30,40,50]
x = l4.count(40)
print(x)
#5) extend()
l3.extend(l4)
print("list after extend(): ",l3)
#6)index()
l5 = [44,55,66,77]
index = l5.index(66)
print(index)
#7)insert() (index,element)
quad = ['USA','JAPAN','AUSTRALIA']
quad.insert(3,'INDIA')
print(quad)
#8)pop()
fun = ['netflix','anime','movies','serials']
fun.pop(3)
print(fun)
#9) remove()
fun.remove('movies')
print(fun)
#10) reverse()
places = ['leh','sikkim','coorg']
places.reverse()
print(places)
#11) sort()
l6 = [1000,10000,10,100000]
l6.sort()
print(l6)