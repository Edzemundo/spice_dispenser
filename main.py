import pyfirmata

def update_values():
        global data
        global ingredients
        global mass
        with open("data") as datafile:
                data = datafile.readlines()
                ingredients = [i.replace("\n","") for i in data if " " in i]
                mass = [float(m.replace("\n","")) for m in data if " " not in m]
                print(data)

def dispense(ingredient, amount):
    if ingredient == ingredients[0]:
        mass[ingredients.index(ingredient)] -= amount
        
    elif ingredient == ingredients[1]:
        mass[ingredients.index(ingredient)] -= amount
        
    elif ingredient == ingredients[2]:
        mass[ingredients.index(ingredient)] -= amount
        
    elif ingredient == ingredients[3]:
        mass[ingredients.index(ingredient)] -= amount
    
    data[len(ingredients) + ingredients.index(ingredient)] = f"{mass[ingredients.index(ingredient)]}\n"
    with open("data", "w") as datafile:
        datafile.writelines(data)
    
#     print(data)
            
            


if __name__ == "__main__":
    # dispense(ingredients[2],0.5)
    print(data)
    print(ingredients)
    print(mass)