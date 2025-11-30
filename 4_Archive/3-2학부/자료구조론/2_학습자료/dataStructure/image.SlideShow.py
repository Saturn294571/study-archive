from tkinter import filedialog
import tkinter as tk
from PIL import ImageTk, Image
import os
from dataStructure import myLib
import threading

class Window:
    def __init__(self):
        self.window=tk.Tk()
        self.window.title("Image Viewer")
        self.window.geometry("640x480")
        self.window.resizable(False, False)

        # 메뉴바를 윈도우에 추가한다.
        menubar = tk.Menu(self.window)
        menu_1 = tk.Menu(menubar, tearoff=0)
        menu_2 = tk.Menu(menubar, tearoff=0)
        menu_1.bind('<<MenuSelect>>')
        menu_2.bind('<<MenuSelect>>')

        menu_1.add_command(label="Open", command=self.dirSelect)
        menu_1.add_command(label="Close", command=self.close)
        menu_2.add_command(label="next", command=self.next)
        menubar.add_cascade(label="Dir", menu=menu_1)
        menubar.add_cascade(label="Image", menu=menu_2)

        self.window.config(menu=menubar)

        # 이미지 라벨을 추가한다.
        self.imgLabel = tk.Label(self.window, width=400, height=400, relief='solid')
        self.imgLabel.pack()
        self.window.mainloop()

    # 메뉴에서 close 가 선택되었을 때 수행한다.
    def close(self):
        self.window.quit()
        self.window.destroy()

    # 파일을 선택한다.
    def dirSelect(self):
        global pngLists
        selDir = filedialog.askdirectory(initialdir="/", title="Select directory")
        # print(selDir)
        pngfiles = [x for x in os.listdir(selDir) if x.endswith(".png")]
        # print(pngfiles)

        pngLists = myLib.CircleLinkedList()
        for fname in pngfiles:
            pngLists.append(selDir + "/" + fname)
        pngLists.print()
        selFile = pngLists.getCurrent()
        self.fileSelect(selFile)

    def fileSelect(self, selFile):
        # 초기 디렉토리를 루트로 지정하고 파일을 선택하면 해당 파일명을 selFile에 입력한다.
        print(selFile)
        self.image = Image.open(selFile)
        print(self.image.size[0], self.image.size[1])
        # 해당 이미지의 크기를 400, 400으로 resize 한다.
        if self.image.size[1] > self.image.size[0]:
            hSize = int((400 * self.image.size[0] / self.image.size[1]))
            vSize = 400
        else:
            hSize = 400
            vSize = int((400 * self.image.size[1] / self.image.size[0]))

        self.image = self.image.resize((hSize,vSize), Image.ANTIALIAS)
        self.image = ImageTk.PhotoImage(self.image)
        self.imgLabel.config(image = self.image)

    def next(self):
        selFile = pngLists.moveNext()
        self.fileSelect(selFile)
        threading.Timer(1, self.next).start()

a = Window()