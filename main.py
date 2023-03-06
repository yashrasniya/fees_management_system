from Frame.frame import *


class Main(Frame):
    def __init__(self, root):
        super().__init__()
        self.r = root
        self.geometry_properties()
        self.Frame_1()
        self.Frame_2()
        self.Frame_3()

    def geometry_properties(self):
        self.r.geometry('1000x600')
        self.r.title('collage project')


if __name__ == '__main__':
    root = Tk()
    a = Main(root)
    root.mainloop()
