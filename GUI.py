try:
	import tkinter
except ImportError:  # python 2
	import Tkinter as tkinter

import Synonym
import Antonym

# Creating a window
mainWindow = tkinter.Tk()
mainWindow.title("Monolingual Helper")
mainWindow.geometry("500x300-8-200")
mainWindow["padx"] = 8
mainWindow["pady"] = 8
mainWindow.minsize(500, 300)
mainWindow.maxsize(500, 300)

mainWindow.columnconfigure(0, weight=5)
mainWindow.columnconfigure(1, weight=1)
mainWindow.columnconfigure(2, weight=1)
mainWindow.columnconfigure(3, weight=1)
mainWindow.rowconfigure(0, weight=1)
mainWindow.rowconfigure(1, weight=1)
mainWindow.rowconfigure(2, weight=1)
mainWindow.rowconfigure(3, weight=1)

# Creating a ListBox to show the results
boxOfResults = tkinter.Listbox(mainWindow, font=("Comic Sans MS",20))
boxOfResults.grid(row=0, column=0, sticky="nwes", rowspan=8)
boxOfResults.config(border=2, relief="sunken")

# Creating Scroll Bar
scrollBar = tkinter.Scrollbar(mainWindow, orient=tkinter.VERTICAL, command=boxOfResults.yview)
scrollBar.grid(row=0, column=1, sticky="nsw", rowspan=8)
boxOfResults["yscrollcommand"] = scrollBar.set

# Creating Word Entry with　 Label
wordLabel = tkinter.Label(mainWindow, text="Enter Word")
wordLabel.grid(row=0, column=2, sticky="ws")
wordEntry = tkinter.Entry(mainWindow, font=('Comic Sans MS',15),)
wordEntry.grid(row=1, column=2, sticky="wn")

# # Creating Radio Buttons for Synonym & Antonym
rbValue = tkinter.IntVar()
rbValue.set(1)

synonymRadio = tkinter.Radiobutton(mainWindow, text="Synonym", value=1, variable=rbValue)
antonymRadio = tkinter.Radiobutton(mainWindow, text="Antonym", value=2, variable=rbValue)

synonymRadio.grid(row=1, column=2, sticky="w")
antonymRadio.grid(row=1, column=2, sticky="e")

# Creating a button
def retrieveSynoOrAnto():
	userInput = wordEntry.get()
	synonyms = Synonym.getSynonym(userInput)
	antonyms = Antonym.getAntonym(userInput)

	boxOfResults.delete(0, tkinter.END)

	if rbValue.get() == 1:
		for i in synonyms:
			boxOfResults.insert(tkinter.END, i)

	else:
		for j in antonyms:
			boxOfResults.insert(tkinter.END, j)

button = tkinter.Button(mainWindow, text="Get List", command=retrieveSynoOrAnto)
button.grid(row=2, column=2, sticky="new")

mainWindow.mainloop()