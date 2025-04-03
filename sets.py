#create empty set
set = set()

# add elements
set.add(1)
set.add(2)
set.add(3)
set.add(4)
set.add(3) # no duplicates will appear on set
set.remove(1)# to remove
print(set)
print(f"The elements has {len(set)} parts")
set.update({4,2,3,6}) # add multiple elements
set.add(89) # add set inside set
print(set)
print(f"The elements has {len(set)} parts")