#* =====================================================IMPORTS============================================================= * /
from tkinter import messagebox  
import pokebase as pb
import random
import paho.mqtt.publish as publish
import paho.mqtt.client as mqtt
#* ========================================================================================================================== * /

#* =====================================================VARIABLES============================================================= * /
BROKER= "mqtt.eclipse.org"
TOPICO = "PKMN_URB"
global img
#* ========================================================================================================================== * /
def pokemon():
    PKMN = random.randint(1, 898)
    img = pb.SpriteResource('pokemon', PKMN)
    pkmnName = (pb.pokemon(PKMN).name).upper()
    client = mqtt.Client("Richi") 
    client.connect(BROKER, 1883, 60)
    client.publish(TOPICO, img.url)
    messagebox.showinfo(TOPICO,"Se ah enviado el Pokemon: " + pkmnName + " al topico")