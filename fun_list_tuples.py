#using list.sort()
list=[(2,-1),(1,3),(4,4),(2,2),(2,1)]
list.sort(key=lambda y:y[1])
print(list)