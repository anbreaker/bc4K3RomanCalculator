from tkinter import *
from tkinter import ttk

HEIGHTBTN = 50
WIDTHBTN = 68


class CalcButton(ttk.Frame):
    def __init__(self, parent, text, command, wbtn=1, hbtn=1):
        ttk.Frame.__init__(self, parent, width=wbtn *
                           WIDTHBTN, height=hbtn*HEIGHTBTN)

        self.pack_propagate(0)

        # Estlios
        s = ttk.Style()
        s.theme_use('alt')
        s.configure('my.TButton', font=('Helvetica', '14', 'bold'))

        self.__btn = ttk.Button(
            self, text=text, command=command, style='my.TButton')
        self.__btn.pack(side=TOP, expand=True, fill=BOTH)


class Display(ttk.Frame):
    cadena = '_'
    __maxNumbers = 12

    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, width=WIDTHBTN*4, height=HEIGHTBTN)

        self.pack_propagate(0)
        self.__lbl = ttk.Label(self, text=self.cadena)

        # Estlios
        s = ttk.Style()
        s.theme_use('alt')
        s.configure('my.TLabel', font='Helvetica 12')

        self.__lbl = ttk.Label(self, text='_', style='my.TLabel',
                               anchor=E, background='black', foreground='white')
        self.__lbl.pack(side=TOP, fill=BOTH, expand=TRUE)

    def pinta(self, caracter):
        if len(self.cadena) >= self.__maxNumbers:
            return

        if self.cadena == '_':
            self.cadena = ''
        else:
            self.cadena += caracter

        self.__lbl.config(text=self.cadena)

    def clear(self):
        self.cadena = '_'
        self.__lbl.config(text=self.cadena)


class Selector(ttk.Frame):

    def __init__(self, parent):
        self.tipus = 'Roman'

        ttk.Frame.__init__(self, parent, width=WIDTHBTN, height=HEIGHTBTN)

        self.pack_propagate(0)

        self.__rbR = ttk.Radiobutton(
            self, text='Roman', variable=self.tipus, value='Roman')
        self.__rbA = ttk.Radiobutton(
            self, text='Arabic', variable=self.tipus, value='Arabic')

        self.__rbR.pack(side=TOP, fill=BOTH, expand=True)
        self.__rbA.pack(side=TOP, fill=BOTH, expand=True)


class Calculator(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)

        # Display
        self.pantalla = Display(self)
        self.pantalla.grid(column=0, row=0, columnspan=4)

        # Botones calculadora
        self.buttonDell = CalcButton(
            self, text='Del', command=self.pantalla.clear, wbtn=3)
        self.buttonDell.grid(column=0, row=1, columnspan=3)

        # ÷
        self.buttonDiv = CalcButton(self, text="÷", command=None)
        self.buttonDiv.grid(column=3, row=1)

        self.buttonC = CalcButton(
            self, text="C", command=lambda: self.pantalla.pinta('C'))
        self.buttonC.grid(column=0, row=2)
        self.buttonD = CalcButton(
            self, text="D", command=lambda: self.pantalla.pinta('D'))
        self.buttonD.grid(column=1, row=2)
        self.buttonM = CalcButton(
            self, text="M", command=lambda: self.pantalla.pinta('M'))
        self.buttonM.grid(column=2, row=2)
        self.buttonMul = CalcButton(
            self, text="x", command=lambda: self.pantalla.pinta('x'))
        self.buttonMul.grid(column=3, row=2)

        self.buttonX = CalcButton(self, text="X", command=None)
        self.buttonX.grid(column=0, row=3)
        self.buttonL = CalcButton(self, text="L", command=None)
        self.buttonL.grid(column=1, row=3)
        self.buttonPI = CalcButton(self, text="(", command=None)
        self.buttonPI.grid(column=2, row=3)
        self.buttonSub = CalcButton(self, text="-", command=None)
        self.buttonSub.grid(column=3, row=3)

        self.buttonI = CalcButton(self, text="I", command=None)
        self.buttonI.grid(column=0, row=4)
        self.buttonV = CalcButton(self, text="V", command=None)
        self.buttonV.grid(column=1, row=4)
        self.buttonPD = CalcButton(self, text=")", command=None)
        self.buttonPD.grid(column=2, row=4)
        self.buttonAdd = CalcButton(self, text="-", command=None)
        self.buttonAdd.grid(column=3, row=4)

        self.buttonEqu = CalcButton(self, text="=", command=None, wbtn=2)
        self.buttonEqu.grid(column=2, row=5, columnspan=2)

        self.Selector = Selector(self)
        self.Selector.grid(column=0, row=5)
