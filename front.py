import tkinter as tk
import tkinter.font
import tkinter.ttk as ttk


from ttkthemes.themed_style import ThemedStyle

from back import Controller


class app:
    def __init__(self):
        self.window = None
        self.canvasBtn = None
        self.canvasSeries = None
        self.canvasSeason = None
        self.canvasCaps = None
        self.pathBass = None
        self.myFont = None

    def OnApp(self):
        Controller.MyInit(Controller)
        self.Window(self)
        self.Style(self)
        self.ScrollBarsANDCanvas(self)
        self.Buttons(self)
        self.window.mainloop()

    def GetCanvas(self):
        return self.canvasCaps

    def Window(self):
        self.window = tk.Tk()
        self.window.geometry("1020x720")
        self.window.config(bg='#414344')
        self.pathBass = "C:/Users/jurie/Downloads/Base_ser"

    def Style(self):
        style = ThemedStyle(self.window)
        index = style.themes.index('equilux')
        style.set_theme(style.themes[index])
        #style_ = ThemedStyle(self.window)
        #index = style_.themes.index('equilux')
        self.myFont=("TkDefaultFont",10,"bold")
        s = ttk.Style()
        s.configure(style.themes[index], font=self.myFont)

    def ScrollBarsANDCanvas(self):
        # Btn
        self.canvasBtn = tk.Canvas(self.window, bg='#414344', width=200, height=675,)
        self.canvasBtn.grid(column=1, row=0, pady=10)
        # Series
        self.canvasSeries = tk.Canvas(self.window, bg='#414344', width=200, height=675, scrollregion=(0, 0, 9000, 9000))
        vbarSeries = ttk.Scrollbar(self.window, orient='vertical')
        vbarSeries.grid(column=3, row=0,ipady=100)
        vbarSeries.config(command=self.canvasSeries.yview)
        self.canvasSeries.config(yscrollcommand=vbarSeries.set)
        self.canvasSeries.grid(column=2, row=0, pady=10)
        # Season
        self.canvasSeason = tk.Canvas(self.window, bg='#414344', width=200, height=675, scrollregion=(0, 0, 9000, 9000))
        vbarSeason = ttk.Scrollbar(self.window, orient='vertical')
        vbarSeason.grid(column=5, row=0,ipady=100)
        vbarSeason.config(command=self.canvasSeason.yview)
        self.canvasSeason.config(yscrollcommand=vbarSeason.set)
        self.canvasSeason.grid(column=4, row=0, pady=10)
        # Caps
        self.canvasCaps = tk.Canvas(self.window, bg='#414344', width=200, height=675, scrollregion=(0, 0, 9000, 9000))
        vbarCaps = ttk.Scrollbar(self.window,orient='vertical')
        vbarCaps.grid(column=7, row=0,ipady=100)
        vbarCaps.config(command=self.canvasCaps.yview)
        self.canvasCaps.config(yscrollcommand=vbarCaps.set)
        self.canvasCaps.grid(column=6, row=0, pady=10)


    def Buttons(self):
        btnStartRandom = ttk.Button(
            self.canvasBtn,
            text="Start Random",
            command=lambda: Controller.PlayARandomCap(Controller)
        )
        btnStartRandom.grid(row=0, column=0, ipadx=60, ipady=30, padx=(0, 0), pady=(37,37))
        btnViewSeries = ttk.Button(
            self.canvasBtn,
            text="View Series",
            command=lambda: self.GetButtons(self, Controller.GetView(Controller, self.pathBass), "View Series", ""),
        )
        btnViewSeries.grid(row=1, column=0, ipadx=60, ipady=30, padx=(0, 0), pady=(37, 37))

    def GetButtons(self, list, father: str, gFather: str):
        if list != "1":
            for i in range(0, len(list)):
                if str(father)[0] == "V":
                    if i !=0:
                        self.canvasSeries.create_window(
                            100, 100 * i,
                            window=ttk.Button(
                                self.canvasSeries, text=str("S-" + list[i]),
                                command=lambda: self.GetButtons(self,Controller.GetView(Controller,str(self.pathBass + "/" + str(list[i]))),str(list[i]),""),
                                width=27
                            ))
                    else:
                        self.canvasSeries.create_window(
                            100, 100 * i,
                            window=ttk.Button(
                                self.canvasSeries, text=str("S-" + list[i]),
                                width=27
                            ))
                elif (str(father)[0] == "S"):
                    if i !=0:
                            self.canvasSeason.create_window(
                            100, 100 * i,
                            window=ttk.Button(
                                self.canvasSeason, text=str("T-" + list[i]),
                                command=lambda:
                                self.GetButtons(self,Controller.GetView(Controller,str(self.pathBass + "/" + father + "/" +list[i])), list[i],str(father)),
                                width=27
                            ))
                    else:
                        self.canvasSeason.create_window(
                            100, 100 * i,
                            window=ttk.Button(
                                self.canvasSeason, text=str("T-" + list[i]),
                                width=27
                            ))
                elif str(father)[0] == "T":
                    if i != 0:
                        self.canvasCaps.create_window(
                            100, 100 * i,
                            window=ttk.Button(
                                self.canvasCaps, text=str("C-" + list[i]),
                                command=lambda:
                                Controller.PlayASelectCap(Controller,self.pathBass + "/" + gFather + "/" + father + "/" +list[i]),
                                width=27
                            ))
                    else:
                        self.canvasCaps.create_window(
                            100, 100 * i,
                            window=ttk.Button(
                                self.canvasCaps, text=str("C-" + list[i]),
                                width=27
                            ))
                else:
                    if i != 0:
                        self.canvasSeason.create_window(
                            100, 100 * i,
                            window=ttk.Button(
                                self.canvasSeason, text=str("T-" + list[i]),
                                command=lambda:
                                self.GetButtons(self, Controller.GetView(Controller,str(self.pathBass + "/" + str(father) + "/" + list[i])),list[i], str(father)),
                                width=27
                            ))
                    else:
                        self.canvasSeason.create_window(
                            100, 100 * i,
                            window=ttk.Button(
                                self.canvasSeason, text=str("T-" + list[i]),
                            ))
