houses = {"harry":"gryffindor","ron":"gryffindor","hermione":"gryffindor","draco":"slytherin","snape":"slytherin"}

print(houses["harry"])
print(houses["ron"])
print(houses)
houses["pars"] = "slytherin"
print(houses)
name = input("Enter name: ")
print(houses[name])
dname = input("Enter dname: ")
dhouses = input("Enter dhouses: ")
houses.update({dname: dhouses})
print(houses)