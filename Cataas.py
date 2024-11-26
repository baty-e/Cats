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

        img.thumbnail((550, 550), Image.Resampling.LANCZOS)

        return ImageTk.PhotoImage(img) # если всё соответствует вернуть картинку (фото)
    except Exception as e:
        print(f"Ошибка при загрузке изображения: {e}")
        return None # если найдёт ошибу ничего не возвращать


def set_image():
    img = load_image(url)
    if img:
        label.config(image=img)
        label.image = img  # Сохраняем ссылку на изображение


def open_new_window():
    img = load_image(url)

    if img:
        global k
        new_window = Toplevel()
        new_window.title("Картинка с котиком")
        new_window.geometry(f"550x550+{w2+k}+{h2+k}")
        label = Label(new_window, image=img)
        label.image = img  # Сохраняем ссылку на изображение
        k+=25
        label.pack()
k = 40

def exit():
    window.destroy()


window = Tk()
window.title("Cats!")

w = window.winfo_screenwidth()
h = window.winfo_screenheight()
w2 = w//2 - 250
h2 = h//2 - 350
window.geometry(f"550x550+{w2}+{h2}")

# update_button = Button(window, text="Обновить", command=set_image)
# update_button.pack(anchor=NE)

label = Label()
label.pack()


menu_bar = Menu(window)
window.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Файл", menu=file_menu)
file_menu.add_command(label="Загрузить фото", command=open_new_window)
file_menu.add_separator()
file_menu.add_command(label="Выход", command=exit)


url = 'https://cataas.com/cat'

set_image() # Вызываем функцию прописанную выше для установки первого полученного изображения в метку

window.mainloop()
