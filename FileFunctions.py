import glob, os
import tkinter
import webbrowser

def openFile(filename):
    filename = filename
    print ("opened file:" + filename)
    webbrowser.open(filename)

def newFile():
    filename = "newFile.txt"
    open(filename, 'w+')
    webbrowser.open(filename)

def makeMenu(top):
    menuBar = tkinter.Menu(top)
    menuBar.add_command(label="New note...", command=newFile)
    menuBar.add_command(label="Search...", command=enterSearchTerm)
    top.config(menu=menuBar)

def search(term):
    directory = os.path.join("Z:\\","Notes")
    for root,dirs,files in os.walk(directory):
        for file in files:
            if file.endswith(".rtf") or file.endswith(".txt"):
               f=open(file, 'r')
               for line in f:
                  if term in line:
                     print ("file: " + os.path.join(root,file))          
                     break
               f.close()
        
               
def enterSearchTerm():
    term = entry.get()
    search(term)

top = tkinter.Tk()
os.chdir("Z:\\Notes")

entry = tkinter.Entry(top)
entry.pack()
