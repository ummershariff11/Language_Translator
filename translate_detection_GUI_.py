########################################################
# AML 1204 2 | Python Programming in Canada
# Term Project - Transletter
# Created by: Team Hortons
# 20-December-2020 Lambton College
# Instructor: Mohammad Islam
########################################################

# Import Libraries
from tkinter import *
from textblob import TextBlob

dict1 = dict(arabic='ar', amharic='am', basque='eu', bengali='bn', english='en', portuguese='pt', bulgarian='bg',
             catalan='ca', cherokee='chr', czech='cs', danish='da', dutch='nl', estonian='et', filipino='fil',
             finnish='fi', french='fr', german='de', greek='el', gujarati='gu', hebrew='iw', hindi='hi', hungarian='hu',
             icelandic='is', indonesian='id', italian='it', japanese='ja', kannada='kn', korean='ko', latvian='lv',
             lithuanian='lt', malay='ms', malayalam='ml', marathi='mr', norwegian='no', polish='pl', romanian='ro',
             russian='ru', serbian='sr', chinese='zh', slovak='sk', slovenian='sl', spanish='es', swahili='sw',
             swedish='sv', tamil='ta', telugu='te', thai='th', turkish='tr', urdu='ur', ukrainian='uk', vietnamese='vi',
             welsh='cy', persian='fa', panjabi='pa', punjabi='pa')


# Create translate function that will do that translation using textblob function
def translate():
    blob = TextBlob(var.get())
    language = lang.get()
    to_lang = dict1.get(language)
    translation = blob.translate(to=to_lang)
    var1.set(translation)


# Initialize Tkinter root Window with app title
root = Tk()
root.title("TransLetter")

# Create grids and frame that will display the content
frame1 = Frame(root)
frame1.grid(column=0, row=0, sticky=(N, W, E, S))
frame1.columnconfigure(0, weight=1)
frame1.rowconfigure(0, weight=1)
frame1.pack(pady=100, padx=100)

# Create the Language option menu
lang = StringVar(root)
lang.set('2 - Choose Language')
options = ('arabic', 'amharic', 'basque', 'bengali', 'english', 'portuguese', 'bulgarian',
           'catalan', 'cherokee', 'czech', 'danish', 'dutch', 'estonian', 'filipino',
           'finnish', 'french', 'german', 'greek', 'gujarati', 'hebrew', 'hindi', 'hungarian',
           'icelandic', 'indonesian', 'italian', 'japanese', 'kannada', 'korean', 'latvian',
           'lithuanian', 'malay', 'malayalam', 'marathi', 'norwegian', 'polish', 'romanian',
           'russian', 'serbian', 'chinese', 'slovak', 'slovenian', 'spanish', 'swahili',
           'swedish', 'tamil', 'telugu', 'thai', 'turkish', 'urdu', 'ukrainian', 'vietnamese',
           'welsh', 'persian', 'punjabi')
lang_menu = OptionMenu(frame1, lang, *options)
lang_menu.grid(row=3, column=0)

# Create text box that will ask for user input
Label(frame1, text="1 - Enter words to translate").grid(row=1, column=0)
var = StringVar()
textbox = Entry(frame1, textvariable=var).grid(row=2, column=0)

# Create text box that will Output the result of translation
Label(frame1, text="Output").grid(row=6, column=0)
var1 = StringVar()
textbox = Entry(frame1, textvariable=var1).grid(row=7, column=0)

# Create button that will call the translate function
trans_button = Button(frame1, text='3 - Translate', command=translate).grid(row=8, column=0, columnspan=3)

root.mainloop()
