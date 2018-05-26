from tkinter import *
from tkinter import font
import tkinter.messageboxg_Tk = Tk()
g_Tk.geometry("400x600+750+200")
DataList = []

def InitTopText():
    TempFont = font.Font(g_Tk, size=20, weight='bold', family = 'Consolas')
    MainText = Label(g_Tk, font = TempFont, text="[서울시 근린시설 검색 App]")
    MainText.pack()
    MainText.place(x=20)
    #…
    InitTopText()
    InitSearchListBox()
    InitInputLabel()
    InitSearchButton()
    InitRenderText()
    InitSendEmailButton()
    InitSortListBox()
    InitSortButton()
    g_Tk.mainloop()
def InitSearchListBox():
    global SearchListBox
    ListBoxScrollbar = Scrollbar(g_Tk)
    ListBoxScrollbar.pack()
    ListBoxScrollbar.place(x=150, y=50)

    TempFont = font.Font(g_Tk, size=15, weight='bold', family='Consolas')
    SearchListBox = Listbox(g_Tk, font=TempFont, activestyle='none',
                            width=10, height=1, borderwidth=12, relief='ridge',
                            yscrollcommand=ListBoxScrollbar.set)

    SearchListBox.insert(1, "도서관")
    SearchListBox.insert(2, "모범음식점")
    SearchListBox.insert(3, "마트")
    SearchListBox.insert(4, "문화시설")
    SearchListBox.pack()
    SearchListBox.place(x=10, y=50)
    ListBoxScrollbar.config(command=SearchListBox.yview)

def InitInputLabel():
    global InputLabel
    TempFont = font.Font(g_Tk, size=15, weight='bold', family='Consolas')
    InputLabel = Entry(g_Tk, font=TempFont, width=26, borderwidth=12, relief='ridge')
    InputLabel.pack()
    InputLabel.place(x=10, y=105)

def InitSearchButton():
    TempFont = font.Font(g_Tk, size=12, weight='bold', family='Consolas')
    SearchButton = Button(g_Tk, font=TempFont, text="검색", command=SearchButtonAction)
    SearchButton.pack()
    SearchButton.place(x=330, y=110)

    