from tkinter import *
from tkinter.ttk import *
from Frame.frameCommanThings import FrameCommonThings


class FrameSecond(FrameCommonThings):

    def Frame_2(self):
        frame = LabelFrame(
            self.r,
            text='Fees Submission'
        )
        frame.grid(row=1, column=0)
        frame_Entry_element = LabelFrame(frame)

        self.search_student_layout(frame, frame_Entry_element)


    def search_student_layout(self, frame, frame_Entry_element):
        root = LabelFrame(
            frame,
            text='Search Student'
        )
        root.grid(row=0, column=0, rowspan=5)

        Label(root, text='Roll Number').grid(row=0, column=0, **self.grid_data)
        RollNumber = Entry(root)

        RollNumber.grid(row=1, column=0, **self.grid_data)

        bu = Button(root, text="Search", command=lambda: self.Search(root, RollNumber, bu, frame_Entry_element))
        bu.grid(row=3, column=0, **self.grid_data)
        RollNumber.bind('<Return>', lambda a: self.Search(root, RollNumber, bu, frame_Entry_element))

    def Search(self, r, Entry_obj, button_obj, frame_Entry_element):

        frame_Entry_element.grid(row=0, column=1)

        self.loop_one(self.Entry_name_Fees_Submission, frame_Entry_element)

        root = LabelFrame(r)
        root.grid(row=4, column=0, **self.grid_data)
        rollNumber = Entry_obj.get()
        if rollNumber == '000':
            for i in self.Entry_name_New_Student:
                Label(root, text=i).pack()
            Entry_obj['state'] = DISABLED
            button_obj['text'] = 'X'
            button_obj['command'] = lambda: self.DeSearch(root, Entry_obj, button_obj, r, frame_Entry_element)

    def DeSearch(self, root, Entry_obj, button_obj, r, f):
        Entry_obj['state'] = NORMAL
        button_obj['text'] = 'Search'
        root.grid_remove()
        f.grid_remove()
        button_obj['command'] = lambda: self.Search(r, Entry_obj, button_obj, f)