from tkinter import *
from pandas import Series; import numpy as np
#from bidi.algorithm import get_display
from tkinter import filedialog
from PIL import Image
import os
import cv2
import main1

#Load the pre-trained text detection model
#model = cv2.dnn.readNet("text-detection-0001.xml")

def Affiche(text_area,state,label,text,targets_error,colorTrue,colorFalse):
    if  state == "correct":
        color = colorTrue
        positionslex_text = ""
        text_area.configure(fg="black",font=("Times", "12"))
    else:
        color = colorFalse
        positionslex_text = " dans "
        #Red Tags for the error words
        for target_error in targets_error:
            for i,j in findAll(text_area.get("1.0",END),target_error):
                begin, end  = (str(i)+"."+str(j), str(i)+"."+str(j+len(target_error)))
                #print((begin,end)); print("error : ", text_area.get(begin,end))
                positionslex_text += " " + str((i,j+1)) + " "
                text_area.tag_add("bold", begin, end)
    #print("positionslex_text : ",positionslex_text)
    label.config(text = text + state + positionslex_text, fg=color)

def findAll(text,target):
	l=[]
	for line in range(len(text.split("\n"))):
		tgt=text.split("\n")[line].find(target)
		while tgt != -1:
			l.append((line+1,tgt))
			tgt=text.split("\n")[line].find(target,tgt+len(target)+1,len(text.split("\n")[line]))
	return l


root = Tk()

root.title('Interface graphique qui verifie les versets du coran')
root.geometry('900x500')

# Labels
label1 = Label(root, 
            text = "entrer les versets", 
            font="Arial 12 bold",
            activebackground="lightblue", activeforeground="black",
            relief="flat", bd=0, highlightthickness=0,
            highlightcolor="blue", highlightbackground="blue",
            pady=10, padx=10, cursor="hand2")
label1.pack(pady=10)

# Entry
text_area = Text(root, 
                wrap="word", 
                width = 100, 
                height = 10,
                font=("Times", "12"),
                #background='#F0D28F'
                )
text_area.pack()

# Function
def verify():
    #Get text from text Area
    text = text_area.get("1.0", END)

    #NO input
    if len(text)==1:
        return 0

    # Check the Lexical
    main1.lex.input(text)
    main1.resultLexer = "correct"
    targets_error = []
    while 1:
        tok = main1.lex.token()
        if not tok:
            break
    
    targets_error = Series(main1.positionLexerError['value'], dtype=np.object0).unique().tolist()
    print("targets_error for lexer: ",targets_error)
    text_area.tag_configure("bold", font = ("Times", "14"),foreground = "red")
    Affiche(text_area,main1.resultLexer,label2,"Lexique du text est ",targets_error,"#00FF00","#FF0000")

    targets_error = []

    # Check the syntax
    main1.resultParser = "correct"
    res = main1.parser.parse(text)
    targets_error = Series(main1.positionParserError['value'], dtype=np.object0).unique().tolist()
    print("targets_error for Parser: ",targets_error)
    Affiche(text_area,main1.resultParser,label3,"Syntaxe du text est ",targets_error,"#00FF00","#FF0000")

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

def VerifyFromCam():
    file_path="./images/frames/frame.png"
    try:
        # Launch camera
        #Initialize the video capture
        cam=cv2.VideoCapture(0)
        while cam.isOpened():
            #Capture a frame from the video
            _, frame = cam.read()

            #Convert the frame to a blob
            blob = cv2.dnn.blobFromImage(frame, swapRB=True, crop=False)

            # Set the input to the pre-trained text detection model
            model.setInput(blob)

            # Run the model and get the output
            output = model.forward()

            # Loop over the output and draw bounding boxes around the detected text
            for detection in output[0, 0, :, :]:
                confidence = detection[2]
                if confidence > 0.5:
                    x = detection[3] * frame.shape[1]
                    y = detection[4] * frame.shape[0]
                    w = detection[5] * frame.shape[1]
                    h = detection[6] * frame.shape[0]
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

            #Show the frame
            cv2.imshow("Camera",frame)

            #Check if the user pressed the escape key
            if cv2.waitKey(1) == ord(" "):
                break
        
        #Release the Camera
        cam.release()
        #Destroy all windows
        cv2.destroyAllWindows()

        #Save the last frame as image in file_path
        cv2.imwrite(file_path,frame)

        #Convert image to text with tesseract ocr
        os.system(f"tesseract {file_path} out -l ara")

        # Open the file out
        f = open("./out.txt", 'rb')

        text = f.read().decode('utf-8').replace("\r","")
        
        text_area.delete("1.0","end")
        text_area.insert("1.0", text)
        verify()
    except:
        print("Error : ",IOError)

#Frame Buttons
frame = Frame(root)
frame.pack(pady=20)

# Button 1
button1 = Button(frame, 
            text = "Verify",
            width = 15, height = 2, 
            command = verify,  
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
button1.pack(side=LEFT)

#Button 2
img = PhotoImage(file="./images/img3.png")
button2 = Button(frame, image=img, command = VerifyFromFile)
button2.pack(side=LEFT, padx=20)


#Button 3
img1 = PhotoImage(file="./images/img3.png")
button3 = Button(frame, image=img1, command = VerifyFromCam)
button3.pack(side=LEFT, padx=20)

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
