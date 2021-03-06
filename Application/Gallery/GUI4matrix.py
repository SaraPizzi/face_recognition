import tkinter as tk
import keras
from PIL import ImageTk
from keras_preprocessing import image
from Application.Gallery.gallery_matrix import WatchList
import os
import numpy as np


class GUI4matrix:
    def __init__(self, version):
        self.gallery = WatchList(version)
        self.path = version+"Dataset/Image"
        self.files = os.listdir(self.path)
        self.n_of_subfolders = 0
        self.path = self.path + '/' + self.files[self.n_of_subfolders]
        print(self.files)
        self.root = tk.Tk()
        self.create_GUI()

    def create_GUI(self):
        self.root.title('Gallery')
        self.root.config(background='#262626')

        self.panel = tk.Label(self.root, background="#141414")
        self.panel.grid(row=0, column=0, columnspan=2, rowspan=4, ipadx=1, ipady=1, padx=4, pady=4)

        btn_load = tk.Button(self.root, text='Load', command=self.preview)
        btn_load.grid(row=4, column=2, sticky="e", padx=2, pady=5)

        self.text_area = tk.Text(self.root, height=1, width=80)
        self.text_area.grid(row=3, column=2, columnspan=2, padx=4, pady=4, ipadx=1, ipady=1)
        self.label4area = tk.Label(self.root, text="Insert name",  background="#262626", foreground="#ffffff")
        self.label4area.grid(row=2, column=2, columnspan=2, sticky="sw", ipadx=1, ipady=1, padx=4)

        self.text_path = tk.Text(self.root, height=1, width=80)
        self.text_path.insert("end", self.path)
        self.text_path.grid(row=1, column=2, columnspan=2, padx=4, pady=4, ipadx=1, ipady=1)
        self.label4path = tk.Label(self.root, text="Path of .jpeg",  background="#262626", foreground="#ffffff")
        self.label4path.grid(row=0, column=2, columnspan=2, sticky="sw", ipadx=1, ipady=1, padx=4)

        btn = tk.Button(self.root, text='Store', command=self.store_item)
        btn.grid(row=4, column=3, sticky="w", padx=2, pady=5)

    def change_path(self):
        self.path = self.text_path.get("1.0", "end-1c")
        print(self.path)

    def preview(self):
        img = image.load_img(self.path, target_size=(224, 224))
        img = ImageTk.PhotoImage(img)
        self.panel.img = img
        self.panel.config(image=img)

    def store_item(self):
        self.name = self.text_area.get("1.0", "end-1c")
        self.gallery.add_id(image.load_img(self.path, target_size=(224, 224)), self.name)
        self.gallery.load_gallery()


path = np.loadtxt("../path.txt", dtype=np.str)
app = GUI4matrix(str(path))
app.root.mainloop()