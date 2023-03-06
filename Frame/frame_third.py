from tkinter import *
from tkinter.ttk import *
from Frame.frameCommanThings import FrameCommonThings


class FrameThird(FrameCommonThings):
    def Frame_3(self):
        frame = LabelFrame(
            self.r,
            text='list'
        )

        frame.grid(row=0, column=1, ipady=200, rowspan=2)
        l = Label(frame, text='Choice')
        l.grid(row=0, column=0)
        b = Button(frame, text='Show')
        b.grid(row=0, column=4)
        combobox1 = Combobox(frame, value=[i for i, k in self.frames_three_entrys_data.items()],
                             **self.frames_three_Combobox_propertys)
        combobox2 = Combobox(frame, state='disabled', **self.frames_three_Combobox_propertys)
        combobox3 = Combobox(frame, state='disabled', **self.frames_three_Combobox_propertys)

        combobox1.grid(row=0, column=1, **self.grid_data)
        combobox2.grid(row=0, column=2, **self.grid_data)
        combobox3.grid(row=0, column=3, **self.grid_data)
        combobox1.set(self.NONE)
        # combobox['state']='disabled'
        combobox1.bind('<<ComboboxSelected>>',
                       lambda x: self.callback(self.frames_three_entrys_data, frame * [combobox1,
                                                                                       combobox2,
                                                                                       combobox3
                                                                                 ]))
    def callback(self, list, master, *args):
        self.make_change(master, list[args[0].get()])
        print(args)
        if len(list[args[0].get()]) <= 1:
            for i in args[1:len(args)]:
                i['state'] = 'disabled'
                i.set(self.NONE)
            return
        a = list[args[0].get()][1]
        args[1]['state'] = 'normal'
        args[1]['value'] = [i for i, k in a.items()]
        n = args[1:len(args)]
        args[1].bind('<<ComboboxSelected>>', lambda x: self.callback(a, master, *n))

    def make_change(self, master, list):
        list[0](master)
        list[0].grid(row=0, column=0)


class Frame_Entry:
    @staticmethod
    def FrameEntryMaker(label_frame, *args, **kwargs):
        a,b=[],2
        f=Frame(label_frame)
        f.grid(**kwargs)
        for i in args:
            a.append(i(f))
            a[-1].pack()
        return a




