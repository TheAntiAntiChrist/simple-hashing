import hashlib
from tkinter import *

mainWindow = Tk()
mainWindow.title("Hasher")
mainWindow.minsize(730,150)
mainWindow.iconbitmap("hasherIcon.ico")

inputLabel = Label(master=mainWindow,text="Data to be hashed:").grid(row=0,column=0,padx=10,pady=10)
outputLabel = Label(master=mainWindow,text="Hashed data:").grid(row=1,column=0,padx=10,pady=10)

inputEntry = Entry(master=mainWindow,width=80)
inputEntry.grid(row=0,column=1,columnspan=2,padx=10,pady=10)
outputEntry = Entry(master=mainWindow,width=80,state="readonly")
outputEntry.grid(row=1,column=1,columnspan=2,padx=10,pady=10)

hashMode = IntVar()
hashMode.set(224)
radio224 = Radiobutton(master=mainWindow,text="sha224",variable=hashMode,value=224).grid(row=3,column=0,padx=10,pady=10)
radio256 = Radiobutton(master=mainWindow,text="sha256",variable=hashMode,value=256).grid(row=3,column=1,padx=10,pady=10)
radio384 = Radiobutton(master=mainWindow,text="sha384",variable=hashMode,value=384).grid(row=3,column=2,padx=10,pady=10)
radio512 = Radiobutton(master=mainWindow,text="sha512",variable=hashMode,value=512).grid(row=3,column=3,padx=10,pady=10)

def hashIt(toBeHashed,hashMode):
    if hashMode.get() == 512:
        hashedData = hashlib.sha512(toBeHashed.encode())
        return hashedData.hexdigest()
    elif hashMode.get() == 384:
        hashedData = hashlib.sha384(toBeHashed.encode())
        return hashedData.hexdigest()
    elif hashMode.get() == 256:
        hashedData = hashlib.sha256(toBeHashed.encode())
        return hashedData.hexdigest()
    elif hashMode.get() == 224:
        hashedData = hashlib.sha224(toBeHashed.encode())
        return hashedData.hexdigest()

def fetchAndHash():
    inputData = inputEntry.get()
    outputData = hashIt(inputData,hashMode)
    outputEntry.config(state=NORMAL)
    outputEntry.delete(0,END)
    outputEntry.insert(0,outputData)
    outputEntry.config(state="readonly")

def RetfetchAndHash(event):
    fetchAndHash()
    
def copyHashOut():
    r = Tk()
    r.withdraw()
    r.clipboard_clear() #Empties the clipboard
    r.clipboard_append(outputEntry.get()) #Adds whatever is in the "Hash output:" box to the clipboard
    r.update() #Updates the clipboard with the text so the data on the clipboard remains after this process is complete and the frame is destroyed
    r.destroy()

mainWindow.bind("<Return>", RetfetchAndHash) #Binds the return key to the hash function
hashButton = Button(master=mainWindow,text="Hash",width=10,command=fetchAndHash).grid(row=0,column=3,padx=10,pady=10)
copyButton = Button(master=mainWindow,text="Copy to Clipboard",width=16,command=copyHashOut).grid(row=1,column=3,padx=10,pady=10)

mainWindow.mainloop()
