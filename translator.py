from numpy import choose
from textblob import TextBlob
inputText = ""
outputLang = ""
def lineBreak():
  return "================================================================================";

def translate(inputText, outputLang):
  try:
    blob = TextBlob(inputText)
    print("Vertimas:")
    print(lineBreak() + "\n" + str(blob.translate(from_lang='en', to=outputLang)) + "\n" + lineBreak())
  except:
    print(lineBreak() + "\n" + "Nepavyko išversti įvesto teksto į pasirinktą kalbą" + "\n" + lineBreak())

def chooseLang():
  return str(input("Įveskite kalbos į kurią versite tekstus trumpinį (pvz. lt, en, de)" + "\n" + lineBreak() + "\n"))

def getInput():
  return str(input("Įveskite savo pasirinkimą arba tekstą kurį norite išversti:" + "\n" + lineBreak() + "\n"))

while True:
  print("""Pasirinkite norimą veiksmą:
Norėdami išversti tekstą įveskite: norimą tekstą;
Norėdami pasirinkti kalbą įveskite: 1;
Norėdami baigti darbą įveskite: -1;""")  
  print(lineBreak());
  option = getInput()
  if option == "1":
    outputLang = chooseLang()
    print(lineBreak())
  elif option == "-1":
    print(lineBreak())
    break
  else:
    if option == "":
      print("Norėdami išversti tekstą pirma jį įveskite")
      inputText = getInput()
    elif outputLang == "":
      print("Norėdami išversti tekstą pirma pasirinkite kalbą į kurią norite jį išversti")
      outputLang = chooseLang()
      print(lineBreak())
    translate(option, outputLang) 
print("Darbas su programa baigtas")

