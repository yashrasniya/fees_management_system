from tkinter import *
from datetime import datetime
from tkcalendar import  DateEntry
from  tkinter.ttk import *

class Data:



        branch = [
            'Computer Science Engineering',
            'Mechanical Engineering',
            'Electronics & Communication',
            'Electronics Engineering',
            'Civil Engineering'
        ]


        Batch = [f"{a}-{a + 4}" for a in range(2014, 1 + int(str(datetime.now()).split("-")[0]))]


        NONE = 'Select an Option'
        Entry_name_New_Student = {
            'Name': [Entry, 'Name'],
            'Father Name': [Entry, 'Father Name'],
            'Batch': [Combobox, 'Batch', Batch],
            'Brach': [Combobox, 'Brach', branch],
            'Mobile Number': [Entry, 'Mobile Number'],
            'Email ID':[Entry, 'Mobile Number'],
            'Roll Number': [Entry, 'Roll Number']

        }


        Entry_name_Fees_Submission = {
            'Date': [DateEntry, 'Date'],
            'Receipt Number': [Entry, 'Receipt Number'],
            'Transaction Number': [Entry, 'Transaction Number'],
            'Semester': [Combobox, 'Semester', 'Semester'],
            'Amount': [Entry, 'Amount']

        }


        Semester = [
            f'{a}-Semester' for a in range(1, 9)
        ]

        grid_data={
            'padx' : 3, 'pady' : 2
        }


        frames_three_entrys_data={
            'Batch':[Combobox,
                {
                    'Branch':[Combobox,
                        {
                            'Name of Student':[],
                            'Semester':[]
                        }

                    ],
                'Date': [DateEntry]
                }
            ],
            'Receipt Number':[Entry],
            'Date':[DateEntry],
            'Transaction Number':[Entry],
            'Roll Number':[Entry],
            'Mobile Number':[Entry]


        }
        frames_three_Combobox_propertys={
            'width':15,
        }

# DateEntry(win, width= 16, background= "magenta3", foreground= "white",bd=2)

