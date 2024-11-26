from tkinter import *
from PIL import Image, ImageTk
import requests
from io import BytesIO


def load_image(url):
    try:
        response = requests.get(url)
        response.raise_for_status()




window = Tk()
window.title("Cats!")
window.geometry("600x480")

label = Label()
label.pack()

url = 'https://cataas.com/cat'
img = load_image(url) # функцию load_image для загрузки сбора изображений создадим сами

if img:
    # Устанавливаем изображение в метку
    label.config(image=img)
    # Необходимо сохранить ссылку на изображение, чтобы избежать сборки мусора
    label.image = img


window.mainloop()
