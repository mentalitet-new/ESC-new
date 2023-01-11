import clr
clr.AddReference("Starter/StarterLib")
from StarterLib import Class1

start = Class1()

class Searcher:
    def __init__(self):
        self._start = Class1()
        self.camera = []

    def search(self):
        try:
            # self._start.DeleteTable()
            self.camera = []
            for device in [self._start.DynaColor(), self._start.Sunell(), self._start.Unv(), self._start.Milesight()]:
                for device_item in device:
                    if device_item == None:
                        continue
                    cam = device_item.split(',')
                    self.camera.append(cam)
            return self.camera
        except Exception as er:
            print(f"functon starter() error:  {er}")



if __name__ == "__main__":
    s = Searcher()
    print(s.search())
