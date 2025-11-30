import tkinter as tk

class Window:
    def __init__(self):
        window = tk.Tk()
        window.title("Simple Calc")

        f1 = tk.Frame(window, relief="solid", bd=2, padx=2, pady=2)
        f2 = tk.Frame(window, relief="solid", bd=2, padx=2, pady=2)

        # Frame 1
        self.eq = "0"
        large_font = ('Verdana',21)
        self.entryVar = tk.StringVar(value=self.eq)

        eqEntry = tk.Entry(f1, bg="yellow", width=11, textvariable=self.entryVar,font=large_font, justify='right')
        delButton = tk.Button(f1, text="del", height=2, width=6, command=self.delete)
        eqEntry.pack(side=tk.LEFT, padx=4)
        delButton.pack(side=tk.LEFT, padx=0)

        # Frame 2
        buttonList = ["7","8","9","+","c",
                      "4","5","6","-","(",
                      "1","2","3","*",")",
                      "0",".","=","/"," "]

        rowIdx=0
        colIdx=0

        butList=[None] * 20
        i = 0

        for btn in buttonList:
            butList[i] = tk.Button(f2, text=btn, height=3, width=6, command=(lambda char=btn: self.butEvent(char)))
            butList[i].grid(row=rowIdx, column=colIdx)
            if btn==" ": butList[i]['state'] = 'disabled'
            i += 1
            colIdx += 1
            if colIdx > 4:
                colIdx = 0
                rowIdx += 1

        f1.pack(pady=2)
        f2.pack()

        window.mainloop()

    def butEvent(self,key):
        if key=="c":
            self.eq="0"
        elif key=="=":
            self.eq = str(eval(self.eq))
        else:
            if self.eq=="0":
                self.eq = key
            else:
                self.eq += key

        self.entryVar.set(self.eq)

    def delete(self):
        self.eq = self.eq[0:len(self.eq)-1]
        if len(self.eq)==0: eq = "0"
        self.entryVar.set(self.eq)

a = Window()
