from tkinter import *
from PIL import Image, ImageTk
import requests
from io import BytesIO


def load_image(url):
    try:
        response = requests.get(url)
        response.raise_for_status() # эта строчка необходима для обработки исключений
        image_data = BytesIO(response.content) # Читаем байты из ответа в объект BytesIO
                                            # кладём сюда и открываем изображение с помощью PIL
        img = Image.open(image_data) # Открываем изображение с помощью PIL
        return ImageTk.PhotoImage(img) # если всё соответствует вернуть картинку (фото)
        except Exception as e:
        print(f"Ошибка при загрузке изображения: {e}")
        return None # если найдёт ошибу ничего не возвращать


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
