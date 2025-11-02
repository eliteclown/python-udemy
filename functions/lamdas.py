add = lambda x,y : x+y
add(2,3)

print(add(2,3))

#map use with lamda
numbers = [1,2,3,4,5]
squared = map(lambda x:x**2,numbers)
print(list(squared))


#filter use with lamda
even=filter(lambda x:x%2==0,numbers)
print(list(even))

#sort use with lamda
points = [(1,2),(3,1),(5,4),(2,0)]
points.sort(key=lambda x:x[0])
print(points)

maxi = lambda x,y:x if x>y  else y
print(maxi(10,20))