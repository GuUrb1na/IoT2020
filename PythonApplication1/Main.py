#* =====================================================IMPORTS============================================================= * /
from tkinter import *
from PIL import ImageTk,Image
from Foco import Foco
from Pokemon import pokemon
import requests
import json
import paho.mqtt.publish as publish
import paho.mqtt.client as mqtt
#* ========================================================================================================================== * /



#* =====================================================VARIABLES============================================================= * /
BROKER= 'mqtt.eclipse.org'
LLAVE = 'ace631675c238f9f0c4d45772ccbe994'
CIUDAD = 'Heroica Guaymas'
topicoT = 'WeatherApp_URB'
topicoH = 'HumedadApp_URB'
topicoS = 'Switch_URB'
client = mqtt.Client("Richi")
BUTTONSIZE = (180,100)

#* ========================================================================================================================== * /

#* =====================================================MAIN============================================================= * /
Response = requests.get("http://api.weatherstack.com/current?access_key=" + LLAVE + "&query=" + CIUDAD + "&units=m" )
datos = Response.json()['current']

Temperatura = datos['temperature']
Humedad = datos['humidity']

client.connect(BROKER, 1883, 60)
client.publish(topicoT, Temperatura)
client.publish(topicoH, Humedad)
#* ================================================================================================================== * /



#* ================================================IMAGENES====================================================== * /
bgPath = Image.open("Resources/SailorMoon.png")
focoPath = Image.open("Resources/Foco.jpg").resize(BUTTONSIZE)
pkmnPath = Image.open("Resources/Pokemon.png").resize(BUTTONSIZE)
#* ============================================================================================================== * /



#* ================================================VENTANA====================================================== * /
raiz=Tk()
raiz.title("Proyecto final")
raiz.geometry("640x477")
miFrame=Frame(raiz)
#* ============================================================================================================== * /



#* ================================================INICIALIZACIONES====================================================== * /
background =ImageTk.PhotoImage(bgPath)
focoImg=ImageTk.PhotoImage(focoPath)
pkmnImg=ImageTk.PhotoImage(pkmnPath)
#* ============================================================================================================== * /



#* ================================================WIDGETS====================================================== * /
background_label = Label(raiz, image=background)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

focoBtn = Button(raiz, image=focoImg, command=Foco).place(x=20, y=50)
focoLbl = Label(raiz, text=topicoS, bg='#4b9ea4', fg='#cc3338', font=('arial', 20)).place(x=30, y=155)

tempLbl = Label(raiz, text="Temperatura", bg='#4b9ea4', fg='Yellow', font=('arial', 10)).place(x=230, y=50)
tempTxt = Label(raiz, text=Temperatura, bg='#4b9ea4', fg='Yellow', font=('arial', 30)).place(x=245, y=75)
topicoTLbl = Label(raiz, bg='#4b9ea4', fg='Yellow', text=topicoT, font=('arial', 8)).place(x=220, y=125)

humLbl = Label(raiz, text="Humedad",  bg='#4b9ea4', fg='#cc3338', font=('arial', 10)).place(x=350, y=50)
humTxt = Label(raiz, text=Humedad,  bg='#4b9ea4', fg='#cc3338', font=('arial', 30)).place(x=355, y=75)
topicoHLbl = Label(raiz, bg='#4b9ea4', fg='#cc3338', text=topicoH, font=('arial', 8)).place(x=330, y=125)

pkmnBtn = Button(raiz, image=pkmnImg, command=pokemon).place(x=440, y=50)
pkmnLbl = Label(raiz, text="PKMN_URB", bg='#4b9ea4', fg='#cc3338', font=('arial', 20)).place(x=450, y=155)
#* ============================================================================================================== * /
raiz.mainloop()
