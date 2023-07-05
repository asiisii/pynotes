li = ["a", "b", "c", "d"] #add and remove from the list, will keep order
tup = ("a", "b", "c", "d") #CANNOT modify tuplem will keep order
sets = {"a", "b", "c", "d"} #can add and remove from the set, can't have duplicates, won't keep order

print(li[0]) #a
print(tup[0]) #a
#print(sets[0]) #TypeError: 'set' object is not subscriptable

li[0] = "Habibi"
print(li) #['Habibi', 'b', 'c', 'd']
# tup[0] = "Habibi"
#print(tup) #TypeError: 'tuple' object does not support item assignment

li.append("Puku")
print(li) #['Habibi', 'b', 'c', 'd', 'Puku']

li.remove("b")
print(li) #['Habibi', 'c', 'd', 'Puku']

sets.add("Puku")
print(sets) #{'Puku', 'b', 'a', 'd', 'c'}
sets.add("Puku")
#because sets can't have duplicates
print(sets) #{'Puku', 'b', 'a', 'd', 'c'}

