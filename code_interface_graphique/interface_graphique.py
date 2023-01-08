#from tkinter import *
#from pandas import Series
#import main1

from tkinter import *
from pandas import Series; import numpy as np
from bidi.algorithm import get_display
from tkinter import filedialog
from PIL import Image
import os
import cv2
import main1



def findAll(text,target):
	l=[]
	for line in range(len(text.split("\n"))):
		tgt=text.split("\n")[line].find(target)
		while tgt != -1:
			l.append((line+1,tgt))
			tgt=text.split("\n")[line].find(target,tgt+len(target)+1,len(text.split("\n")[line]))
	return l


root = Tk()

root.title('Verificateur lexicale et syntaxique')
root.geometry('900x500')

# Labels
label1 = Label(root, 
            text = "Entrer le texte", 
            font="Arial 12 bold",
            activebackground="lightblue", activeforeground="black",
            relief="flat", bd=0, highlightthickness=0,
            highlightcolor="blue", highlightbackground="blue",
            pady=10, padx=10, cursor="hand2")
label1.pack(pady=10)

# Entry
text_area = Text(root, width = 100, height = 10)
text_area.pack()

# Function
def verify():
    text = text_area.get("1.0", END)
    text_area.tag_configure("bold", font = ("Times", "14", "bold"))

    if len(text)==1:
        return 0
    # Check the Lexical
    main1.lex.input(text)
    main1.resultLexer = "correct"
    print("GUI.py")

    while 1:
        tok = main1.lex.token()
        if not tok:
            break
    if  main1.resultLexer == "correct":
        color = "#00FF00" 
    else:
        color = "#FF0000"
        n=main1.positionLexerError['length']
        targets_error = [i for i in Series(main1.positionLexerError['value'].split("\n")[:]).unique().tolist() if len(i)>0]
        print("--------------------")
        print("Targets error: ",targets_error)

        #Red Tags for the error words
        for target_error in targets_error:
            #print(findAll(text, target_error))
            for i,j in findAll(text,target_error):
                #print(text[j-1:j-1+n+1])
                begin, end  = (str(i)+"."+str(j), str(i)+"."+str(j+n))
                print((begin,end))
                print("error : ", text_area.get(begin,end))
                text_area.tag_configure("bold", foreground = "red")
                text_area.tag_add("bold", begin, end)
        label3.config(text = "Syntaxe du text est " + main1.resultParser, fg="#FF0000")

    label2.config(text = "Lexique du text est " + main1.resultLexer, fg=color)
    
    # Check the syntax
    main1.resultParser = "correct"
    res = main1.parser.parse(text)
    if  main1.resultParser == "correct":
        color = "#00FF00" 
    else:
        color = "#FF0000"
        n=main1.positionParserError['length']
        targets_error = [i for i in Series(main1.positionParserError['value'].split("\n")[:]).unique().tolist() if len(i)>0]
        print("--------------------")
        print("Targets error: ",targets_error)

        #Red Tags for the error words
        for target_error in targets_error:
            #print(findAll(text, target_error))
            for i,j in findAll(text,target_error):
                #print(text[j-1:j-1+n+1])
                begin, end  = (str(i)+"."+str(j), str(i)+"."+str(j+n))
                print((begin,end))
                print("error : ", text_area.get(begin,end))
                text_area.tag_configure("bold", foreground = "orange")
                text_area.tag_add("bold", begin, end)
    label3.config(text = "Syntaxe du text est " + main1.resultParser, fg=color)
    return


def VerifyFromFile():
    try:
        # Create a file dialog box
        file_path = filedialog.askopenfilename()

        if file_path.split(".")[-1] in ["png","jpg","jpge","gif"]:
            #Convert image to text with tesseract ocr
            os.system(f"tesseract {file_path} out -l ara")
            # Open the file out
            f = open("./out.txt", 'rb')
        else:
            # Open the file
            f = open(file_path, 'rb')

        text = f.read().decode('utf-8').replace("\r","")
        
        text_area.delete("1.0","end")
        text_area.insert("1.0", text)
        verify()
    except IOError:
        print("Error : ",IOError)



# Button
button1 = Button(root, 
            text = "Verify",
            width = 15, height = 2, 
            command =  verify,  
            bg="blue", 
            fg="white", 
            font="Arial 12 bold",
            activebackground="lightblue", 
            activeforeground="black",
             relief = RAISED, 
            bd=0, 
            highlightthickness=3,
            highlightcolor="blue", 
            highlightbackground="white",
            pady=10, padx=10, 
            cursor="hand2")
button1.pack(pady=20)


button2 = Button(root, 
            text = "importer_fichier",
            width = 15, height = 2, 
            command = VerifyFromFile,  
            bg="blue", 
            fg="white", 
            font="Arial 12 bold",
            activebackground="lightblue", 
            activeforeground="black",
             relief = RAISED, 
            bd=0, 
            highlightthickness=3,
            highlightcolor="blue", 
            highlightbackground="white",
            pady=10, padx=10, 
            cursor="hand2")
button2.pack(pady=20)







#Label for result Lexer
label2 = Label(root, 
            text = "", 
            font="Arial 12 bold",
            activebackground="lightblue", activeforeground="black",
            relief="flat", bd=0, highlightthickness=0,
            highlightcolor="blue", highlightbackground="blue",
            pady=10, padx=10, cursor="hand2")
label2.pack()

#Label for result Parser
label3 = Label(root, 
            text = "", 
            font="Arial 12 bold",
            activebackground="lightblue", activeforeground="black",
            relief="flat", bd=0, highlightthickness=0,
            highlightcolor="blue", highlightbackground="blue",
            pady=10, padx=10, cursor="hand2")
label3.pack(pady=20)
root.mainloop()


