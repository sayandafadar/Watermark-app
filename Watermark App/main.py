import tkinter as tk
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont

window = Tk()
window.title("Water Mark Editor")
window.minsize(width=500, height=500)

filename = ''


def choose_image():
    global filename
    filename = filedialog.askopenfilename()
    print('Selected:', filename)
    return filename


def text_upload_action():
    im = Image.open(filename)
    rgb_im = im.convert('RGB')
    width, height = rgb_im.size

    draw = ImageDraw.Draw(rgb_im)
    text = entry.get()

    font = ImageFont.truetype('Google Fonts/Roboto-Black.ttf', 14)
    text_width, text_height = draw.textsize(text, font)

    margin = 20
    x = width - text_width - margin
    y = height - text_height - margin

    draw.text((x, y), text, font=font)
    rgb_im.show()

    rgb_im.save("Images/withLogo.jpg")


def logo_upload_action():
    logo_file = filedialog.askopenfilename()
    print(logo_file)
    logoIm = Image.open(logo_file)

    im = Image.open(filename)


choose_button = tk.Button(window, text='Choose Image', command=choose_image)
choose_button.pack()

# Labels
label = Label(text="Choose the watermark type.")
label.pack()


# Radiobutton
def radio_used():
    print(radio_state.get())


# Variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Text", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Logo", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()

entry = Entry(width=30)
entry.insert(END, string="© Add a copyright name")
entry.pack()

label = Label(text="OR")
label.pack()

button = tk.Button(window, text='Choose Logo', command=logo_upload_action)
button.pack()

button = tk.Button(window, text='Save', command=text_upload_action)
button.pack()

window.mainloop()
