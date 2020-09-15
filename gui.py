from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk
import formatter
from formatter import classifier




class Root(Tk):
    def __init__(self):
        self.path  = "test"
        super(Root, self).__init__()
        self.title("HandWritten Digit Classifier")
        self.minsize(600 , 400)
        self.maxsize(600 , 400)
        self.resizable(0,0)
        self.pack_propagate(0)
        self.labelFrame = ttk.LabelFrame(self, text = "Digit Classifier")
        self.labelFrame.grid(column = 0, row = 1, padx = 100, pady = 100)
        self.predict()
        self.button()



    def predict(self):
        self.predict = ttk.Button(self.labelFrame, text = "Predict",command = self.prediction)
        self.predict.grid(column = 3, row = 1)





    def button(self):
        self.button = ttk.Button(self.labelFrame, text = "Browse An Image",command = self.fileDialog)
        self.button.grid(column = 1, row = 1)



    def fileDialog(self):

        self.filename = filedialog.askopenfilename(initialdir =  "/", title = "Select A File", filetype =
        (("jpeg files","*.jpg"),("all files","*.*")) )
        self.label = ttk.Label(self.labelFrame, text = "")
        self.label.grid(column = 1, row = 2)
        self.label.configure(text = self.filename)
        img = Image.open(self.filename)
        photo = ImageTk.PhotoImage(img)
        self.path = self.filename
        # self.label2 = Label(image=photo)
        # self.label2.image = photo 
        # self.label2.grid(column=3, row=4)



    def prediction(self):

        self.label3 = ttk.Label(self.labelFrame,text ="")
        self.label.grid(column = 3, row = 3)
        self.label.configure(text = classifier(self.path),font = 30,relief = RIDGE)

root = Root()

root.mainloop()


