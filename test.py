with open("data") as datafile:
        dataraw = datafile.readlines()
        data = [d.replace("\n","") for d in dataraw]
#         keys = [data.index(k) for k in data if " " in k]
        

# # global ingredients
# ingredients = {k:v for (k,v) in zip(keys,data)}
# mass = [float(m) for m in data if " " not in m]

# state = ["",""]

# def dispense(ingredient, amount):
#         match ingredient:
#                 case ingredients.get(0):
#                         mass[0] -= amount 

print(dataraw)
print(data)