from PIL import Image, ImageTk
import tkinter as tk
import os

folder_path = 'D:/Programming/Python/GUI/Images' # if u want to display images then u have to put path here
list_of_files = os.listdir(folder_path)
num_files = len(list_of_files)

window = tk.Tk()
window.title('Image viewer')

# window.iconbitmap('Images/1.jpeg')

# Images name
my_img1 = ImageTk.PhotoImage(Image.open('Images/1.jpeg'))
my_img2 = ImageTk.PhotoImage(Image.open('Images/2.jpg'))
my_img3 = ImageTk.PhotoImage(Image.open('Images/3.jpg'))
my_img4 = ImageTk.PhotoImage(Image.open('Images/4.jpg'))

image_list = [my_img1, my_img2, my_img3, my_img4]

status = tk.Label(window, text='Image 1 of ' + str(num_files), bd=1, relief=tk.SUNKEN, anchor=tk.E)

my_label = tk.Label(image=my_img1)
my_label.grid(row=0, column=0, columnspan=3)

def forward(image_number):
    global my_label
    global forwardBtn
    global backwardBtn

    my_label.grid_forget()

    my_label = tk.Label(image=image_list[image_number-1])

    forwardBtn = tk.Button(window,text='>>',command=lambda:forward(image_number+1))

    backwardBtn = tk.Button(window,text='<<',command=lambda:backward(image_number-1))

    if image_number == num_files:
        forwardBtn = tk.Button(window,text='>>', state=tk.DISABLED)

    my_label.grid(row=0, column=0, columnspan=3) 
    forwardBtn.grid(row=1, column=2)
    backwardBtn.grid(row=1, column=0)

    status = tk.Label(window, text='Image ' + str(image_number) + ' of ' + str(num_files), bd=1, relief=tk.SUNKEN, anchor=tk.E)

    status.grid(row=2, column=0, columnspan=3, sticky=tk.W+tk.E)


def backward(image_number):
    global my_label
    global forwardBtn
    global backwardBtn

    my_label.grid_forget()

    my_label = tk.Label(image=image_list[image_number-1])

    forwardBtn = tk.Button(window,text='>>',command=lambda:forward(image_number+1))

    backwardBtn = tk.Button(window,text='<<',command=lambda:backward(image_number-1))

    if image_number == 1:
        backwardBtn = tk.Button(window,text='<<', state=tk.DISABLED)

    my_label.grid(row=0, column=0, columnspan=3) 
    forwardBtn.grid(row=1, column=2)
    backwardBtn.grid(row=1, column=0)

    status = tk.Label(window, text='Image ' + str(image_number) + ' of ' + str(num_files), bd=1, relief=tk.SUNKEN, anchor=tk.E)

    status.grid(row=2, column=0, columnspan=3, sticky=tk.W+tk.E)

forwardBtn = tk.Button(window,text='>>',command=lambda:forward(2))

exitBtn = tk.Button(window,text='Exit', command=window.quit)

backwardBtn = tk.Button(window,text='<<', command=backward)

forwardBtn.grid(row=1, column=2, pady=10)
exitBtn.grid(row=1, column=1)
backwardBtn.grid(row=1, column=0) 
status.grid(row=2, column=0, columnspan=3, sticky=tk.W+tk.E)

window.mainloop()