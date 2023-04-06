import PySimpleGUI as sg
import main


def refresh():
        main.update_values()
        global ingredients
        global mass
        ingredients = main.ingredients
        mass = main.mass
        
# ---------------------------------------------------------------------------------------------------------------------------------

def gui():
              
        layout = [[sg.Text("Enter desired mass (in grams): "), sg.Input(key = "desired_mass")],
                [sg.Push(), sg.Text(key = "status1"), sg.Push()],
                [sg.Push(), sg.Text(key = "status2"), sg.Push()],
                [sg.Push(), sg.Text(key = "status3"), sg.Push()],
                [sg.VPush()],
                [sg.Button(ingredients[0], size=(15), key = "ing1"), sg.Push(), sg.Button(ingredients[1], size=(15), key = "ing2")],
                [sg.Button(ingredients[2], size=(15), key = "ing3"), sg.Push(), sg.Button(ingredients[3], size=(15), key = "ing4")],
                [sg.Push(), sg.Button("Dispense", size=(15), key = "dispense", pad=(10,10)), sg.Push()]]

        window = sg.Window("Spice Dispenser", layout, size=(290,230))

        state = [-1,0]

        while True:
                event, values = window.read()
                refresh()
                print(state)
                        
                if len(values["desired_mass"]) != 0:
                        try:
                                desired_mass = float(values["desired_mass"])
                        except ValueError:
                                sg.popup("Input is not a valid number!")
                else:
                        desired_mass = ""
                        
                
                if event == sg.WIN_CLOSED:
                        break
                
                
                if event == "ing1":
                        if desired_mass != "":
                                remaining_mass = mass[0] - desired_mass
                                if  remaining_mass < 0:
                                        sg.popup(f"You dont have enough!")
                                        
                                else:        
                                        window["status1"].update(f"{ingredients[0]} selected")
                                        window["status2"].update(f"{desired_mass}g will be dispensed")
                                        window["status3"].update(f"{mass[0] - desired_mass}g will be remaining")
                                        state = [0,1]    
                        
                        else:
                                window["status1"].update(f"{ingredients[0]} selected")
                                window["status2"].update(f"{mass[0]}g remaining")
                                window["status3"].update("")
                
                
                if event == "ing2":                        
                        if desired_mass != "":
                                remaining_mass = mass[1] - desired_mass
                                if  remaining_mass < 0:
                                        sg.popup(f"You dont have enough!")
                                else:        
                                        window["status1"].update(f"{ingredients[1]} selected")
                                        window["status2"].update(f"{desired_mass}g will be dispensed")
                                        window["status3"].update(f"{mass[1] - desired_mass}g will be remaining")
                                        state = [1,1]    
                        
                        else:
                                window["status1"].update(f"{ingredients[1]} selected")
                                window["status2"].update(f"{mass[1]}g remaining")
                                window["status3"].update("")
                
                
                if event == "ing3":                        
                        if desired_mass != "":
                                remaining_mass = mass[2] - desired_mass
                                if  remaining_mass < 0:
                                        sg.popup(f"You dont have enough!")
                                else:        
                                        window["status1"].update(f"{ingredients[2]} selected")
                                        window["status2"].update(f"{desired_mass}g will be dispensed")
                                        window["status3"].update(f"{mass[2] - desired_mass}g will be remaining")
                                        state = [2,1]    
                        
                        else:
                                window["status1"].update(f"{ingredients[2]} selected")
                                window["status2"].update(f"{mass[2]}g remaining")
                                window["status3"].update("")
                                
                if event == "ing4":                        
                        if desired_mass != "":
                                remaining_mass = mass[3] - desired_mass
                                if  remaining_mass < 0:
                                        sg.popup(f"You dont have enough!")
                                else:        
                                        window["status1"].update(f"{ingredients[3]} selected")
                                        window["status2"].update(f"{desired_mass}g will be dispensed")
                                        window["status3"].update(f"{mass[3] - desired_mass}g will be remaining")
                                        state = [3,1]    
                        
                        else:
                                window["status1"].update(f"{ingredients[3]} selected")
                                window["status2"].update(f"{mass[3]}g remaining")
                                window["status3"].update("")
                
                if event == "dispense":
                        if state[1] == 1 and desired_mass != 0:
                                main.dispense(ingredients[state[0]],desired_mass)
                        elif state[1] == 1 and desired_mass == 0:
                                sg.popup("0g has been entered")
                        elif state[1] == 0:
                                sg.popup("Ingredient not selected or mass not entered")
                                
                        window["status1"].update("")
                        window["status2"].update("")
                        window["status3"].update("")
                        
if __name__ == "__main__":
        refresh()
        gui()
                        