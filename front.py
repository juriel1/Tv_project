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
        self.pathSerie = None
        self.pathSeason = None
        self.myFont = None

    def OnApp(self):
        Controller.MyInit(Controller)
        self.Window(self)
        #self.Style(self)
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
            command=lambda: self.SerieButtons(self,Controller.GetView(Controller,self.pathBass)),
        )
        btnViewSeries.grid(row=1, column=0, ipadx=60, ipady=30, padx=(0, 0), pady=(37, 37))
    def SerieButtons(self, list):
        y = 0
        for i in list:
            y +=1
            BTN.CreateSerie(BTN,list[y-1],self.pathBass,y,self.canvasSeries,self.canvasSeason,self.canvasCaps)

class BTN():
    def __int__(self):
        self.canvasSerie = None
        self.canvasSeason = None
        self.canvasCap = None
        self.pathBass = None
        self.name = None
        self.ypos = None


    def CreateCap(self,name_,path_,ypos_,canvascap=tk.Canvas):
        self.canvasCap = canvascap
        self.name = name_
        self.pathBass = path_
        self.ypos = ypos_

        self.canvasCap.create_window(
            100,100*ypos_,
            window=ttk.Button(
                self.canvasCap,text=str("S-"+name_),
                command=lambda : Controller.PlayASelectCap(Controller,path_),
                width=27
            )
        )
    def RolCap(self,list,path_):
        y = 0
        for i in list:
            y += 1
            BTN.CreateCap(BTN, list[y - 1],str(path_+"/"+list[y-1]), y,self.canvasCap)

    def CreateSeason(self,name_,path_,ypos_,canvasseason=tk.Canvas,canvascap=tk.Canvas):
        self.canvasSeason = canvasseason
        self.canvasCap = canvascap
        self.name = name_
        self.pathBass = path_
        self.ypos = ypos_

        self.canvasSeason.create_window(
            100,100*ypos_,
            window=ttk.Button(
                self.canvasSeason,text=str("S-"+name_),
                command=lambda : self.RolCap(self,Controller.GetView(Controller,str(self.pathBass)),path_),
                width=27
            )
        )
    def RolSeason(self,list,path_):
        y = 0
        for i in list:
            y += 1
            BTN.CreateSeason(BTN, list[y - 1], str(path_+"/"+list[y-1]),y, self.canvasSeason,self.canvasCap)
    def CreateSerie(self,name_,path_,ypos_,canvasserie = tk.Canvas,canvasseason = tk.Canvas,canvascap = tk.Canvas):
        self.canvasSerie = canvasserie
        self.canvasSeason = canvasseason
        self.canvasCap = canvascap
        self.name = name_
        self.pathBass = path_
        self.ypos = ypos_

        self.canvasSerie.create_window(
            100,100*self.ypos,
            window=ttk.Button(
                self.canvasSerie,text=str("S-"+name_),
                command=lambda : self.RolSeason(self,Controller.GetView(Controller,str(self.pathBass+"/"+name_)),str(self.pathBass+"/"+name_)),
                width=27
            )
        )