import os
import requests
import tkinter
from tkinter import ttk
from io import *
from PIL import Image, ImageTk


window = tkinter.Tk()
window.geometry("750x550")
window.title("Weather Boy")
window.focus_force()
frame = tkinter.Frame(window)
frame.pack(fill="both", expand=True)

API_KEY = os.getenv("OPENWEATHER_API_KEY")

url = "https://picsum.photos/750/550"  
response = requests.get(url)

img_data = BytesIO(response.content)
img = Image.open(img_data)

tk_img = ImageTk.PhotoImage(img)

label = tkinter.Label(window, image=tk_img)
label.pack()

response2 = requests.get("https://picsum.photos/200/200")
img_data2 = BytesIO(response2.content)
img2 = Image.open(img_data2)
img2 = ImageTk.PhotoImage(img2)

icon = img2
window.iconphoto(True, icon)

def ktc(kelvin):
    celcius = kelvin - 273.15
    return celcius

def submit():
    City = entry.get()
    
    URL = f"http://api.openweathermap.org/data/2.5/weather?q={City}&appid={API_KEY}"


    response = requests.get(URL)
    data = response.json()

    temp_kelvin = data['main']['temp']
    temp_celcius = ktc(temp_kelvin)
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']
    feels_like_kelvin = data['main']['feels_like']
    feels_like_celcius = int(ktc(feels_like_kelvin))
    description = data['weather'][0]['description']

    l1.config(text=f"Temperature of {City} is {int(temp_celcius)}°C")
    l2.config(text=f"Humidity of {City} is {int(humidity)}%")
    l3.config(text=f"Wind speed at the {City} is {int(wind_speed)} m/s")
    l4.config(text=f"It feels like {int(feels_like_celcius)}°C at {City}")
    l5.config(text=f"Description of {City} is {description}")

def entry():
    global entry
    entry = tkinter.Entry(window, font=('BanSchrift SemiBold', 14),borderwidth=3, relief="sunken", bg="#e0cfa8")
    entry.place(relx=0.5, rely=0.3, anchor="center")



    submit_button = tkinter.Button(window, text="Submit", font=('Helvetica', 14), command=submit, bg="#ba933a", relief='sunken')
    submit_button.place(relx=0.5, rely=0.4, anchor="center")

entry()

l1 = tkinter.Label(window, text="Temperature: ", font='BahnSchrift 22', bg='#e0cfa8', relief='raised')
l1.place(relx=0.5, rely=0.6, anchor="center")

l2 = tkinter.Label(window, text="Humidity: ", font='BahnSchrift 22', bg='#d4c094',relief='raised')
l2.place(relx=0.5, rely=0.68, anchor="center")

l3 = tkinter.Label(window, text="Wind speed: ", font='BahnSchrift 22', bg='#d4b777', relief='raised')
l3.place(relx=0.5, rely=0.76, anchor="center")

l4 = tkinter.Label(window, text="Feels like: ", font='BahnSchrift 22', bg='#cfab5b', relief='raised')
l4.place(relx=0.5, rely=0.84, anchor="center")

l5 = tkinter.Label(window, text="Description: ", font='BahnSchrift 22', bg='#ba9747', relief='raised')
l5.place(relx=0.5, rely=0.92, anchor="center")



window.mainloop()
