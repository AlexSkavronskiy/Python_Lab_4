from tkinter import *
import random
import string
import pyglet

# Включаем музыку
mus = pyglet.resource.media("Witcher.mp3")
mus.play()

def clicked():  # Функция срабатывающая при нажатии кнопки

    # Генерация рандомной строки из цифр и букв
    text = [random.choice(string.ascii_lowercase + string.digits if i != 5 else string.ascii_uppercase)
            for i in range(10000)]

    res = "Welcome the\nworld Witcher\n"
    l = "{}".format(txt.get())  # Считываем введеное 3-x значное число
    if not l or len(l) != 3:
        lbl.configure(text='Введите 3-х значное число\n\n')

    else:
        number = int(l)
        lbl.configure(text=res + str(''.join(text[0:5])) + '-' + str(''.join(text[number + 1:number + 5])) + '-' +
                       str(''.join(text[2 * number + 1:2 * number + 4])) + '-' +
                       str(''.join(text[3 * number + 1:3 * number + 3])))



# Создаем окно
window = Tk()
window.title("Встань на путь Ведьмака")
window.geometry('850x620')
lbl = Label(window, text="\n\n", font=('Comic Sans MS', 18, 'bold'))
lbl.grid(column=0, row=0)

# Создаем строку для ввода
txt = Entry(window, width=10, font=('Comic Sans MS', 15, 'bold'), bg='black',
             fg='lime')
txt.grid(column=1, row=0)

# Создаем кнопку
btn = Button(window, text='Сгенирировать \n ключ', bg='black',
             fg='lime', font=('Comic Sans MS', 12, 'bold'), command=clicked)


btn.grid(column=1, row=1)

# Добавляем картинку
window.image = PhotoImage(file='Witcher.png')
bg_logo = Label(window, image=window.image)
bg_logo.grid(row=1, column=0)

window.mainloop()

pyglet.app.run()