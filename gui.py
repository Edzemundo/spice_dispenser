import PySimpleGUI as sg

ingredients = {0:"1. Candy Corn", 1:"2. Sugar", 3:"3. Paprika"}
mass = []

layout = [sg.Input(justification="r")
        [sg.Button(text = ingredients[0]), sg.Button(text = ingredients[1])],
        [sg.Button(text = ingredients[2]),sg.Button(text = ingredients[3])],
        [sg.Push(), sg.Text(key = "mass_remaining"), sg.Push]]

window = sg.Window("Spice Dispenser", layout, size=(350,420))