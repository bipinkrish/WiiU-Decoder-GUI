import os
from tkinter import *
from tkinter import Place, filedialog, mainloop
from tkinter import Button, Label, ttk
import tkinter as tk

class wiiu: 

        def __init__(self) -> None:

                self.root = tk.Tk()

                self.frm = ttk.Frame(self.root).grid()
                self.root.title('CDecrypt')
                self.root.geometry('800x400')
                #self.root.resizable(False, False)
                screen_width = self.root.winfo_screenwidth()
                screen_height = self.root.winfo_screenheight()
                x_cordinate = int((screen_width/2) - (800/2))
                y_cordinate = int((screen_height/2) - (400/2))
                self.root.geometry("{}x{}+{}+{}".format(800, 400, x_cordinate, y_cordinate))
                self.upload_filevar = tk.StringVar()
                self.upload_foldvar = tk.StringVar()
                
       
                self.home()

        def home(self):
                self.next_btn = tk.Button(self.root, text='select Source folder', command=self.browseFiles, width=20, height=1)
                self.next_btn.place(x=120, y=150)
                self.nxt_btn = tk.Button(self.root, text='select Destination folder', command=self.browseFolder, width=20, height=1)
                self.nxt_btn.place(x=120, y=200)
                self.con_btn = tk.Button(self.root, text='Confirm', command=self.confirm, width=7, height=1)
                self.con_btn.place(x=350, y=280)
                self.cons = tk.Label(self.root, text="                   WHEN YOU CLICK CONFIRM, PROGRESS HAPPENS IN COMMAND PROMPT AND THE APPLICATION \n                  MAY BECOME UNRESPONSIVE JUST MINIMIZE IT WILL BECOME ACTIVE WHNE PROCESS IS FINISHED", font=('calibre', 10, 'bold')).place(x=1, y=50)
                self.opt = tk.Label(self.root, text="(Optional)", font=('calibre', 10)).place(x=160, y=230)


        def browseFiles(self):
                self.upload_filevar = filedialog.askdirectory(initialdir=".", title="Select a Folder")
                tk.Label(self.root, text=self.upload_filevar, font=('calibre', 10, 'bold')).place(x=300,y=150)

        def browseFolder(self):
                self.upload_foldvar = filedialog.askdirectory(initialdir=".", title="Select a Folder")
                tk.Label(self.root, text=self.upload_foldvar, font=('calibre', 10, 'bold')).place(x=300,y=200)
        

        def confirm(self):
                try:
                        self.upload_filevar.replace("/","\\")     
                        os.system(f'start cmd /k cdecrypt.exe "{self.upload_filevar}" "{self.upload_foldvar}"')  
                except:
                        os.system(f'start cmd /k cdecrypt.exe "{self.upload_filevar}"')
                        
                   

root=wiiu()
root = mainloop()           

