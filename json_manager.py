import json
import os


def read_json():
    # Primeramente ingreso a la ruta y confirmo que existe el archivo que voy a leer
    # Entonces si no existe este archivo entonces quiero que crees el archivo
    if not os.path.isfile("data.json"):
        # Aca estoy diciendo que abra el archivo y que tenga permiso de escritura 'w' y lo voy a coocar con el alias de 'file' (as file)
        with open('data.json', 'w') as file:
            json.dump([], file)

    with open('data.json', 'r') as file:
        data = json.load(file)
    return data


def write_json(data):
    with open('data.json', 'w') as file:
        # json.dump toma los datos del primer argumento y los reescribe en el segundo argumento
        json.dump(data, file)
