#* =====================================================IMPORTS============================================================= * /
from tkinter import *
import paho.mqtt.publish as publish
import paho.mqtt.client as mqtt
#* ========================================================================================================================== * /

#* =====================================================VARIABLES============================================================= * /
BROKER= "mqtt.eclipse.org"
TOPICO = "Switch_URB"
#* ========================================================================================================================== * /

def Foco():
    #Ventana
    root=Tk()
    root.title("Foco")
    miFrame=Frame(root)
    topicoLbl = Label(root, text=TOPICO, font=('arial', 25)).pack()
    lbl = Label(root, text='')
    #Ventana
    def on_connect(client, userdata, flags, rc): 
        client.subscribe(TOPICO) 

    def on_message(client, userdata, msg):  
        if str(msg.payload) == "b'1'":
           print(1)
           root.configure(bg='yellow')
           lbl.configure(text='Encendido', fg='black', bg='yellow', font=('arial', 100))
           
        if str(msg.payload) == "b'0'":
           print(0)
           root.configure(bg='black')
           lbl.configure(text='Apagado', fg='white', bg='black', font=('arial', 100))

        lbl.pack()
        

    client = mqtt.Client("Richi")  
    client.on_connect = on_connect  
    client.on_message = on_message  
    client.connect(BROKER, 1883, 60)
    client.loop_start()
    root.mainloop()


