import FetchGiphy
import tkinter


def showGif():
	result = FetchGiphy.getGifUrl(e1.get())

master = tkinter.Tk()
tkinter.Label(master, text = "Query: ").grid(row = 0)

e1 = tkinter.Entry(master)
e1.grid(row = 0, column = 1)

tkinter.Button(master,  text='OK',  command=showGif).grid(row=1,  column=0,  padx = 4, pady = 4)

master.mainloop()