try:
	import tkinter as tk
except ImportError:  # python 2
	import Tkinter as tk
from tkinter import ttk
from PIL import ImageTk


class View(tk.Tk):
	'''
	classdocs
	'''

	PAD = 10

	def __init__(self, controller):
		'''
		Construct
		'''
		super().__init__()

		self.title("Monolingual Helper ")
		self.controller = controller
		self.minsize(610, 415)
		self.maxsize(610, 415)
		self.color = "#c11010"
		self.image = ImageTk.PhotoImage(file="Assets/red.png")
		self.value_var = tk.StringVar()
		self._makeMainFrame()
		self._innerFrames()
		self._make_entry()
		self.createRadioButtons()
		self.enterButton()
		self.resultsBox()


	def main(self):
		self.mainloop()


	def _makeMainFrame(self):
		self.main_frm = ttk.Frame(self)
		self.main_frm.pack(padx=self.PAD, pady=self.PAD)
		self.label = tk.Label(self.main_frm, image=self.image)
		self.label.pack()


	def _innerFrames(self):
		self.leftFrame = tk.Frame(self.main_frm, bg=self.color)
		self.leftFrame.place(relx=0.32, rely=0.095, relwidth=0.50, relheight=0.78, anchor="n")

		self.rightTopFrame = tk.Frame(self.main_frm, bg=self.color)
		self.rightTopFrame.place(relx=0.60, rely=0.26, relwidth=0.37, relheight=0.16)

		self.rightLowerFrame = tk.Frame(self.main_frm, bg=self.color, bd=3)
		self.rightLowerFrame.place(relx=0.60, rely=0.5, relwidth=0.37, relheight=0.25)


	def _make_entry(self):
		self.wordLabel = tk.Label(self.rightTopFrame, text="Enter Word", bg=self.color, fg="white")
		self.wordLabel.place(relx=0, rely=0)
		self.entry = tk.Entry(self.rightTopFrame, textvariable=self.value_var, bd=5, font=('Comic Sans MS', 15))
		self.entry.place(rely=0.35, relwidth=1)

	def createRadioButtons(self):
		self.rbValue = tk.IntVar()
		self.rbValue.set(1)

		self.synonymRadio = tk.Radiobutton(self.rightLowerFrame,
		                                   text="Synonym",
		                                   value=1,
		                                   variable=self.rbValue,
		                                   bg=self.color,
		                                   fg="white")
		self.antonymRadio = tk.Radiobutton(self.rightLowerFrame,
		                                   text="Antonym",
		                                   value=2,
		                                   variable=self.rbValue,
		                                   bg=self.color,
		                                   fg="white")

		self.synonymRadio.place(relx=0)
		self.antonymRadio.place(relx=0.61)

	def enterButton(self):
		caption = ""
		self.BigBtn = tk.Button(self.rightLowerFrame, text="Get List",
		                        command=(lambda button=caption: self.controller.onButtonClick(button)))
		self.BigBtn.place(relx=0, rely=0.35, relwidth=1, relheight=0.6)

	def resultsBox(self):
		self.boxOfResults = tk.Listbox(self.leftFrame, font=("Comic Sans MS", 20))
		self.boxOfResults.place(relx=0.01, rely=0.01, relheight=0.98,relwidth=0.925)

		self.scrollBar = tk.Scrollbar(self.leftFrame, orient=tk.VERTICAL, command=self.boxOfResults.yview, bg="yellow", troughcolor="yellow")
		self.scrollBar.place(relx=0.94, rely=0.01, relheight=0.98)  # grid(row=0, column=1, sticky="nse", rowspan=8)
		self.boxOfResults["yscrollcommand"] = self.scrollBar.set

	def displayResults(self, words):
		self.boxOfResults.delete(0, tk.END)
		for i in words:
			self.boxOfResults.insert(tk.END, i)
