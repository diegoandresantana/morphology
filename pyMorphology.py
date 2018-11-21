import tkFileDialog
from Tkinter import *

from PIL import Image, ImageTk

import numpy as np

import cv2

"""
    Morphology Samples (Dilate, Open, Close, Gradient, Top Hat, Black Hat and Dilate+Open+Erode)
    05/09/2018
    Autor: Diego Andre Sant'Ana
    Disciplina: Visao Computacional
    
"""

class TELA:
    def __init__(self):

        font10 = "-family {DejaVu Sans} -size 14 -weight normal -slant"  \
            " roman -underline 0 -overstrike 0"


        self.clicked = False
        self.fingerling = {}

        # janela
        self.window = Tk()
        self.window.title("Image None")
        self.window.attributes('-zoomed', True)

        # lado esquerdo
        self.frameMenuLateral = Frame(self.window)
        self.frameMenuLateral.pack(side=LEFT, anchor=N)

        self.frameControls = LabelFrame(self.frameMenuLateral, text="Controls", padx=5, pady=5)
        self.frameControls.pack(anchor=N, pady=5, padx=5, fill=X)

        self.frameControlsOrganize = Frame(self.frameControls)
        self.frameControlsOrganize.pack(fill=X, expand=False)

        self.selecionaImagem = Button(self.frameControlsOrganize, text="Select Image", padx=5, pady=5,
                                      command=self.selecionaImagem)
        self.selecionaImagem.pack(padx=5, pady=5, expand=True, fill=X)



        self.frameKernel = LabelFrame(self.frameControlsOrganize, text="Kernel", padx=5, pady=5)
        self.frameKernel.pack(anchor=N, pady=5, padx=5, fill=X)

        self.val_kernel=IntVar()
        self.val_kernel.set(1)
        self.imagemOriginal= None

        self.spinboxKernel = Spinbox(self.frameKernel, from_=1.0, to=100.0)
        self.spinboxKernel.place(relx=0.52, rely=0.15, relheight=0.04, relwidth=0.44)
        self.spinboxKernel.configure(activebackground="#f9f9f9")
        self.spinboxKernel.configure(background="white")
        self.spinboxKernel.configure(buttonbackground="wheat")
        self.spinboxKernel.configure(disabledforeground="#b8a786")
        self.spinboxKernel.configure(font=font10)
        self.spinboxKernel.configure(from_="1.0")
        self.spinboxKernel.configure(highlightbackground="black")
        self.spinboxKernel.configure(selectbackground="#c4c4c4")
        self.spinboxKernel.configure(textvariable=self.val_kernel)
        self.spinboxKernel.configure(to="100.0")

        self.spinboxKernel.pack(padx=5, pady=5, expand=True, fill=X)



        self.buttonOpen = Button(self.frameControlsOrganize, text="Run Process", padx=5, pady=5,
                                 command=self.procedimento)
        self.buttonOpen.pack(padx=5, pady=5, expand=True, fill=X)

        # lado direito

        self.frameImages = LabelFrame(self.window, text="Images", padx=5, pady=5)
        self.frameImages.pack(side=RIGHT, pady=5, padx=5, expand=True, fill=BOTH)

        self.frameControlsOrganize2 = Frame(self.frameImages)
        self.frameControlsOrganize2.pack(fill=X, expand=False)
        self.frameControlsOrganize2.columnconfigure(0, weight=3)
        self.frameControlsOrganize2.columnconfigure(1, weight=3)
        self.frameControlsOrganize2.columnconfigure(2, weight=3)
        self.frameControlsOrganize2.grid(row=0, padx=20, sticky="nsew")
        self.frameControlsOrganize2.grid(row=1, padx=20, sticky="nsew")
        self.frameControlsOrganize2.grid(row=2, padx=20, sticky="nsew")

        self.frameImg1 = LabelFrame(self.frameControlsOrganize2, text="Gray", padx=5, pady=5)
        self.frameImg1['width'] = 340
        self.frameImg1['height'] = 240
        self.frameImg1.grid(column=0, row=0)

        # Imagem cinza
        self.frameImg2 = LabelFrame(self.frameControlsOrganize2, text="Erode", padx=5, pady=5)
        self.frameImg2['width'] = 340
        self.frameImg2['height'] = 230
        self.frameImg2.grid(column=1, row=0)

        # inversao de cores
        self.frameImg3 = LabelFrame(self.frameControlsOrganize2, text="Dilate", padx=5, pady=5)
        self.frameImg3['width'] = 340
        self.frameImg3['height'] = 230
        self.frameImg3.grid(column=2, row=0)

        # Contorno
        self.frameImg4 = LabelFrame(self.frameControlsOrganize2, text="Open", padx=5, pady=5)
        self.frameImg4['width'] = 340
        self.frameImg4['height'] = 230
        self.frameImg4.grid(column=0, row=1)

        # 'BINARY',
        self.frameImg5 = LabelFrame(self.frameControlsOrganize2, text="Closed", padx=5, pady=5)
        self.frameImg5['width'] = 340
        self.frameImg5['height'] = 230
        self.frameImg5.grid(column=1, row=1)

        # 'BINARY_INV',
        self.frameImg6 = LabelFrame(self.frameControlsOrganize2, text="Morphological Gradient", padx=5, pady=5)
        self.frameImg6['width'] = 340
        self.frameImg6['height'] = 230
        self.frameImg6.grid(column=2, row=1)

        # 'TRUNC',
        self.frameImg7 = LabelFrame(self.frameControlsOrganize2, text="Top Hat", padx=5, pady=5)
        self.frameImg7['width'] = 340
        self.frameImg7['height'] = 230
        self.frameImg7.grid(column=0, row=2)

        # 'TOZERO','
        self.frameImg8 = LabelFrame(self.frameControlsOrganize2, text="Black Hat", padx=5, pady=5)
        self.frameImg8['width'] = 340
        self.frameImg8['height'] = 230
        self.frameImg8.grid(column=1, row=2)

        #
        self.frameImg9 = LabelFrame(self.frameControlsOrganize2, text="Dilate + Open + Erode", padx=5, pady=5)
        self.frameImg9['width'] = 340
        self.frameImg9['height'] = 230
        self.frameImg9.grid(column=2, row=2)

        self.window.mainloop()

    def click(self, event):
        self.mouseXClick = event.x
        self.mouseYClick = event.y
        self.clicked = True

    def release(self, event):
        # type: (object) -> object
        self.clicked = False

    def carregaImagem(self, img, frame, op):

        labelImg = Label(frame, width=int(340 - 5), height=int(230 - 5))
        labelImg.pack(expand=True, fill=BOTH, padx=5, pady=5)
        imgResize = Image.fromarray(img).resize((340 - 12, 230 - 12), Image.ADAPTIVE)
        imgtk = ImageTk.PhotoImage(image=imgResize)
        labelImg.imgtk = imgtk
        labelImg.configure(image=imgtk)
        if (op == 1):
            self.labelImg1 = labelImg
        elif (op == 2):
            self.labelImg2 = labelImg
        elif (op == 3):
            self.labelImg3 = labelImg
        elif (op == 4):
            self.labelImg4 = labelImg
        elif (op == 5):
            self.labelImg5 = labelImg
        elif (op == 6):
            self.labelImg6 = labelImg
        elif (op == 7):
            self.labelImg7 = labelImg
        elif (op == 8):
            self.labelImg8 = labelImg
        elif (op == 9):
            self.labelImg9 = labelImg

    def procedimento(self):
        if(self.imagemOriginal is None):
            return
        # converte para cinza
        self.img1 = cv2.cvtColor(self.imagemOriginal, cv2.COLOR_BGR2GRAY)
        # Cria a matriz do Kernel
        kernel = np.ones((self.val_kernel.get(), self.val_kernel.get()), np.uint8)
        print(kernel)

        self.img2 = cv2.erode(self.img1, kernel, iterations=1)
        # Realiza a dilatacao
        self.img3 = cv2.dilate(self.img1, kernel, iterations=1)
        # Realiza oeracao Aberta
        self.img4 = cv2.morphologyEx(self.img1, cv2.MORPH_OPEN, kernel)
        # Realiza operacao Fechada
        self.img5 = cv2.morphologyEx(self.img1, cv2.MORPH_CLOSE, kernel)
        # Realiza a operacaoo Gradiente Morphologica
        self.img6 = cv2.morphologyEx(self.img1, cv2.MORPH_GRADIENT, kernel)
        # Morphologica Top Hat
        self.img7 = cv2.morphologyEx(self.img1, cv2.MORPH_TOPHAT, kernel)
        # Morphologica Black Hat
        self.img8 = cv2.morphologyEx(self.img1, cv2.MORPH_BLACKHAT, kernel)

        # Dilate +Open + Erode
        im = cv2.dilate(self.img1, kernel, iterations=1)
        im = cv2.morphologyEx(im, cv2.MORPH_OPEN, kernel)

        self.img9 = cv2.erode(im, kernel, iterations=1)

        for w in (
        self.frameImg2, self.frameImg3, self.frameImg4, self.frameImg5, self.frameImg6, self.frameImg7, self.frameImg8,
        self.frameImg9):
            for f in w.winfo_children():
                f.destroy()

        self.carregaImagem(self.img2, self.frameImg2, 2)
        self.carregaImagem(self.img3, self.frameImg3, 3)
        self.carregaImagem(self.img4, self.frameImg4, 4)
        self.carregaImagem(self.img5, self.frameImg5, 5)
        self.carregaImagem(self.img6, self.frameImg6, 6)
        self.carregaImagem(self.img7, self.frameImg7, 7)
        self.carregaImagem(self.img8, self.frameImg8, 8)
        self.carregaImagem(self.img9, self.frameImg9, 9)



    def selecionaImagem(self):
        options = {

            'title': 'Select type of image permits(JPG or PNG).',
            'filetypes': (("Image JPG", '*.jpg'), ('Image PNG', '*.png'))

        }
        filename = tkFileDialog.askopenfilename(**options)
        if (filename != ''):
            self.file = filename
            self.window.title(self.file)
            self.imagemOriginal = cv2.imread(self.file)

            for w in (
            self.frameImg1, self.frameImg2, self.frameImg3, self.frameImg4, self.frameImg5, self.frameImg6, self.frameImg7,
            self.frameImg8, self.frameImg9):
                for f in w.winfo_children():
                    f.destroy()

            self.carregaImagem(self.imagemOriginal, self.frameImg1, 1)


tela = TELA()
