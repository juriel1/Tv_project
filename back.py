import os.path
import random
from moviepy.editor import VideoFileClip
from threading import Timer


class Controller:

    def __init__(self):
        self.allPath = None
        self.list = None
        self.length = None

    def MyInit(self):
        self.allPath = str()
        self.allPath = "C:/Users/jurie/Downloads/Base_ser"

    def GetView(self, path: str):
        len, flist = self.GetLength(self, path)
        List = list(flist)
        List.insert(0,"------")
        return List

    def GetLength(self, path: str):
        try:
            self.list = os.listdir(path)
            self.length = len(self.list)
            return self.length, self.list
        except NotADirectoryError:
            return "e", "1"

    def PlayARandomCap(self):
        self.allPath = "C:/Users/jurie/Downloads/Base_ser"
        lengthSeries, listSeries = self.GetLength(self, self.allPath)
        nSerie = random.randint(0, lengthSeries)
        self.allPath += "/" + listSeries[nSerie - 1]
        lengthseason, listSeason = self.GetLength(self, self.allPath)
        nSeason = random.randint(0, lengthseason)
        self.allPath += "/" + listSeason[nSeason - 1]
        lengthCaps, listCaps = self.GetLength(self, self.allPath)
        nCaps = random.randint(0, lengthCaps)
        self.allPath += "/" + listCaps[nCaps - 1]
        self.PlayASelectCap(self, self.allPath)
        clip = VideoFileClip(self.allPath)
        clipDuration = ((clip.duration) / 60) - 1.25
        print(clipDuration)
        self.RePlay(self, clipDuration)

    def RePlay(self, duration: float):
        t = Timer(duration, self.PlayARandomCap, [self])
        t.start()

    def PlayASelectCap(self, path: str):
        print("ahora")
        p = str(path)
        if p.find(" ") != -1:
            p = p.replace(" ", "")
            os.rename(path, p)
        os.system(p)
