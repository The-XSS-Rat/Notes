#!python3
from FileFunctions import *

makeMenu(top)

for file in glob.glob("*.*"):
    print(file)
    btnFileName = tkinter.Button(top, text=file,command= lambda file=file: openFile(file))
    btnFileName.pack()

top.mainloop()




