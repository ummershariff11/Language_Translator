from textblob import TextBlob
import pycountry as check_lang

dict1 = dict(arabic='ar', amharic='am', basque='eu', bengali='bn', english='en', portuguese='pt', bulgarian='bg',
             catalan='ca', cherokee='chr', czech='cs', danish='da', dutch='nl', estonian='et', filipino='fil',
             finnish='fi', french='fr', german='de', greek='el', gujarati='gu', hebrew='iw', hindi='hi', hungarian='hu',
             icelandic='is', indonesian='id', italian='it', japanese='ja', kannada='kn', korean='ko', latvian='lv',
             lithuanian='lt', malay='ms', malayalam='ml', marathi='mr', norwegian='no', polish='pl', romanian='ro',
             russian='ru', serbian='sr', chinese='zh', slovak='sk', slovenian='sl', spanish='es', swahili='sw',
             swedish='sv', tamil='ta', telugu='te', thai='th', turkish='tr', urdu='ur', ukrainian='uk', vietnamese='vi',
             welsh='cy', persian='fa', panjabi='pa', punjabi='pa')


def word_translate(a, b):
    blob = TextBlob(a)
    for name in b:
        translate_language = map_language(name)
        print(f"The translated text in {name} is : {blob.translate(to=translate_language)}\n")


def map_language(lang):
    return dict1.get(lang)


word_input = input("Enter a sentence you wish to detect/translate: ")
L = TextBlob(word_input)
language = L.detect_language()
my_language = check_lang.languages.get(alpha_2=language)
print(f"\nThe language you have entered is in {my_language.name}")

input_lang = input(f'\nEnter a list of languages you want this sentence "{L}" to be translated in\n'
                   'NOTE: please enter the language names separated by space \n').lower()
lang_list = input_lang.split(" ")

word_translate(word_input, lang_list)

