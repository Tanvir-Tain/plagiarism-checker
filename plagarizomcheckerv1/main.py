from tkinter import *
import nltk
import PyPDF2
from tkinter import filedialog


root = Tk()
root.title("Plagrizom")
root.geometry("500x500")


file2=open("text2.txt","r")
text2=file2.readline()
f1=file2
#str2=''.join(text2)
#vr2=str2.split('.')


# crt txt box

mytext = Text(root,height=20,width=150)
mytext.pack( pady=10)


# this is for output
#mytext2 = Text(root,height=20,width=150)
#mytext2.pack( pady=10)


#clear txt box
def clear_text_box():
    mytext.delete(1.0, END)

# opn pdf
def open_pdf1():
    open_file1 =filedialog.askopenfilename(
        initialdir="D:\my project list\Ai/",
        title="open pdf file ",
        filetypes=(
            ("pdf file","*.pdf"),
            ("All Files", "*.*")))
    if open_file1:
        #open pdf
        pdf_file = PyPDF2.PdfFileReader(open_file1)
        #set the page to read
        page = pdf_file.getPage(0)
        #extrat txt frm pdf
        page_stuff = page.extractText()
        f2=mytext.insert(1.0, page_stuff)
        i = 0

        for line1 in f1:
            i += 1

            for line2 in f2:

                # matching line1 from both files
                if line1 == line2:
                    # print IDENTICAL if similar
                    print("Line ", i, ": IDENTICAL")
                else:
                    print("Line ", i, ":")
                    # else print that line from both files
                    print("\tFile 1:", line1, end='')
                    print("\tFile 2:", line2, end='')
                break
        #add to txt box
#mytext2.insert(1.0, text2)





#crt text reader

def open_text():
    text_file= filedialog.askopenfilename(
        initialdir="D:\my project list\Ai/",
        title="open Text  file ",
        filetypes=(
            ("Text File ","*.Txt"),
            ("All Files", "*.*")))
    text_file = open (text_file,'r')
    stuff= text_file.read()
    mytext.insert(END, stuff)
    global mylabel
    mylabel=Label(root)




    f2= stuff
    i = 0

    for line1 in f1:
        i += 1

        for line2 in f2:

            # matching line1 from both files
            if line1 == line2:
                # print IDENTICAL if similar
                l1= "Line " + i + ": IDENTICAL"

                print("Line ", i, ": IDENTICAL")
            else:
                print("Line ", i, ":")
                print("Line ", i, ":")
                # else print that line from both files
                print("\tFile 1:", line1, end='')
                print("\tFile 2:", line2, end='')
            break




# Create function attribute.




#####################

def open_pdf2():
    open_file2 =filedialog.askopenfilename(
        initialdir="D:\my project list\Ai/",
        title="open pdf file ",
        filetypes=(
            ("pdf file","*.pdf"),
            ("All Files", "*.*")))
    if open_file2:
        #open pdf
        pdf_file = PyPDF2.PdfFileReader(open_file2)
        #set the page to read
        page = pdf_file.getPage(0)
        #extrat txt frm pdf
        page_stuff = page.extractText()
        #add to txt box
        str2=''.join(page_stuff)
        global vr2
        vr2 = str2.split('.')



### insert to txt box

   ###   mytext.insert(1.0,vr or page stuf  )

"""
open_pdf2()
open_pdf1()
listt = []
for z in vr1:
    for y in vr2:
        if z == y:
            listt.append(z)

mytext.insert(1.0,listt)

"""


# crt meue


my_menue = Menu(root)
root.config(menu=my_menue)


file_menu = Menu(my_menue,tearoff=False)
my_menue.add_cascade(label="File",menu=file_menu)
file_menu.add_command(label="open file 1 ",command=open_text)
# file_menu.add_command(label="open file 2 ",command=open_pdf2)
file_menu.add_command(label="clear",command=clear_text_box)
file_menu.add_separator()
file_menu.add_command(label="exit",command=root.quit)

root.mainloop()



