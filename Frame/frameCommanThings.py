import data
from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *
import pyperclip as pc


class FrameCommonThings(data.Data):
    def Save(self, l):
        a = ''
        b = 1
        for i in l:
            if i.get().upper() != 'SELECT AN OPTION' and i.get().upper() != '':
                a += i.get() + '\n'
                b += 1
            else:
                print('Fill all Entrys')
                self.Warning(f'Entry No. {b} is Empty!')
                return
        print(a)
        for i in l:
            i.delete(0, 10000000)

    def loop_one(self, list, root):
        new_list_entry = []
        new_list_Label = []

        n = 1
        for i in list:
            k = list[i]
            if k[0] == Combobox:

                new_list_entry.append(k[0](root, value=k[2]))
                new_list_entry[-1].grid(
                    row=n,
                    column=2,
                    padx=8,
                    pady=2,
                    ipadx=40)
            else:
                new_list_entry.append(k[0](root))
                new_list_entry[-1].grid(row=n, column=2, padx=8, pady=2, ipadx=50)
            v = new_list_entry[-1]

            new_list_entry[-1].bind('<Control-Key-u>', lambda a, n=v: self.ShortKeys(n, n.get().upper()))
            new_list_entry[-1].bind('<Control-Key-l>', lambda a, n=v: self.ShortKeys(n, n.get().lower()))
            new_list_entry[-1].bind('<Control-Key-t>', lambda a, n=v: self.ShortKeys(n, n.get().title()))
            new_list_entry[-1].bind('<Control-Key-C>', lambda a: self.Copy_Past(new_list_entry, 'copy'))
            new_list_entry[-1].bind('<Control-Key-V>', lambda a: self.Copy_Past(new_list_entry, 'paste'))
            new_list_Label.append(Label(root, text=i))

            new_list_Label[-1].grid(row=n, column=1, padx=3, pady=2)
            n += 1
        new_list_entry[-1].bind('<Return>', (lambda x: self.Save(new_list_entry)))
        Save = Button(root, text='Save', command=lambda: self.Save(new_list_entry))
        Save.grid(row=n, column=1, padx=3, pady=2, columnspan=2, ipadx=100)
        return new_list_entry

    def Warning(self, message):
        showwarning(title='Warning', message=message)

    def ShortKeys(self, a, b):
        a.delete(0, 1000000000)
        a.insert(0, b)

    def Copy_Past(self, list, type):
        if type == 'copy':
            a = ''
            for i in list:
                a += i.get() + '\n'
            pc.copy(a)
        elif type == 'paste':
            b = pc.paste().split('\n')
            if len(b) == 1:
                return
            n = 0
            for a in list:
                a.delete(0, 1000000000)
                try:
                    a.insert(0, b[n])
                    print(b)
                except IndexError as a:
                    print(a)
                    return
                n += 1
