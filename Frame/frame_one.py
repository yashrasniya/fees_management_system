from tkinter import *
from tkinter.ttk import *
from Frame.frameCommanThings import FrameCommonThings


class FrameOne(FrameCommonThings):

    def Frame_1(self):
        frame = LabelFrame(
            self.r,
            text='New Student'
        )
        frame.grid(row=0, column=0, ipadx=90)
        self.loop_one(self.Entry_name_New_Student, frame)
