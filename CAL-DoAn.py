from tkinter import*


cal=Tk()

cal.title("MAY TINH BO TUI NHOM 3")

operator=""

text_Input=StringVar()
text_Input.set("K58.Vinh University...")
#=======================================================================
def btnClick(numbers):
    global operator
    operator=operator + str(numbers)
    text_Input.set(operator)

def bntClearDisplay():
    global operator
    operator=""
    text_Input.set("")

def btnEnqualsInput():
    try:
        global operator
        sumup=str(eval(operator))
        text_Input.set(sumup)
        operator=""
    except:
        text_Input.set(" Lỗi ")
        operator=""


# Khung màn hi`nh
txtDisplay = Entry(cal,font=('aria', 40,'bold'), textvariable=text_Input, bd=30, insertwidth=4,
                   bg="teal", justify='right').grid(columnspan=4)


btnClear=Button(cal,padx=3,pady=10,bd=8, fg="yellow",font=('aria', 20,'bold'),
            text="OFF",bg="brown",command= bntClearDisplay).grid(row=1,column=3)
btn7=Button(cal,padx=20,pady=10,bd=8, fg="black",font=('aria', 20,'bold'),
            text="pi",bg="yellow",command=lambda:btnClick(3.14)).grid(row=1,column=0)
btn7=Button(cal,padx=26,pady=10,bd=8, fg="black",font=('aria', 20,'bold'),
            text="e",bg="yellow",command=lambda:btnClick(2.71)).grid(row=1,column=1)
btn7=Button(cal,padx=30,pady=10,bd=8, fg="black",font=('aria', 20,'bold'),
            text=",",bg="grey",command=lambda:btnClick(".")).grid(row=1,column=2)
#========================================================================
btn7=Button(cal,padx=25,pady=10,bd=8, fg="black",font=('aria', 20,'bold'),
            text="7",bg="grey",command=lambda:btnClick(7)).grid(row=2,column=0)

btn8=Button(cal,padx=25,pady=10,bd=8, fg="black",font=('aria', 20,'bold'),
            text="8",bg="grey",command=lambda:btnClick(8)).grid(row=2,column=1)

btn9=Button(cal,padx=25,pady=10,bd=8, fg="black",font=('aria', 20,'bold'),
            text="9",bg="grey",command=lambda:btnClick(9)).grid(row=2,column=2)

addition=Button(cal,padx=22,pady=10,bd=8, fg="black",font=('aria', 20,'bold'),
            text="+",command=lambda:btnClick("+"),bg="bisque").grid(row=2,column=3)
#=======================================================================
btn4=Button(cal,padx=25,pady=10,bd=8, fg="black",font=('aria', 20,'bold'),
            text="4",bg="grey",command=lambda:btnClick(4)).grid(row=3,column=0)

btn5=Button(cal,padx=25,pady=10,bd=8, fg="black",font=('aria', 20,'bold'),
            text="5",bg="grey",command=lambda:btnClick(5)).grid(row=3,column=1)

btn6=Button(cal,padx=25,pady=10,bd=8, fg="black",font=('aria', 20,'bold'),
            text="6",bg="grey",command=lambda:btnClick(6)).grid(row=3,column=2)

addition=Button(cal,padx=25,pady=10,bd=8, fg="black",font=('aria', 20,'bold'),
            text="-",command=lambda:btnClick("-"),bg="bisque").grid(row=3,column=3)
#======================================================================
btn1=Button(cal,padx=25,pady=10,bd=8, fg="black",font=('aria', 20,'bold'),
            text="1",bg="grey",command=lambda:btnClick(1)).grid(row=4,column=0)

btn2=Button(cal,padx=25,pady=10,bd=8, fg="black",font=('aria', 20,'bold'),
            text="2",bg="grey",command=lambda:btnClick(2)).grid(row=4,column=1)

btn3=Button(cal,padx=25,pady=10,bd=8, fg="black",font=('aria', 20,'bold'),
            text="3",bg="grey",command=lambda:btnClick(3)).grid(row=4,column=2)

addition=Button(cal,padx=25,pady=10,bd=8, fg="black",font=('aria', 20,'bold'),
            text="*",command=lambda:btnClick(
                "*"),bg="bisque").grid(row=4,column=3)
#========================================================================
btn0=Button(cal,padx=25,pady=10,bd=8, fg="black",font=('aria', 20,'bold'),
            text="0",bg="grey",command=lambda:btnClick(0)).grid(row=5,column=0)

btnClear=Button(cal,padx=22,pady=10,bd=8, fg="yellow",font=('aria', 20,'bold'),
            text="C",bg="brown",command= bntClearDisplay).grid(row=5,column=1)

btnEnquals=Button(cal,padx=25,pady=10,bd=8, fg="black",font=('aria', 20,'bold'),
            text="=",bg="bisque",command=btnEnqualsInput).grid(row=5,column=2)

addition=Button(cal,padx=27,pady=10,bd=8, fg="black",font=('aria', 20,'bold'),
            text="/",command=lambda:btnClick("/"),bg="bisque").grid(row=5,column=3)
#=========================================================================
btn7=Button(cal,padx=18,pady=22,bd=8, fg="white",font=('aria', 14,'bold'),
            text="Bảo",command=lambda:btnClick("Bảo"),bg="black").grid(row=6,column=0)

btn8=Button(cal,padx=17,pady=22,bd=8, fg="white",font=('aria', 14,'bold'),
            text="Đức",command=lambda:btnClick("Đức"),bg="black").grid(row=6,column=1)

btn9=Button(cal,padx=21,pady=22,bd=8, fg="white",font=('aria', 14,'bold'),
            text="Đạt",command=lambda:btnClick("Đạt"),bg="black").grid(row=6,column=2)

addition=Button(cal,padx=23,pady=22,bd=8, fg="white",font=('aria', 14,'bold'),
            text="N3",command=lambda:btnClick("Nhóm3"),bg="black").grid(row=6,column=3)


cal.mainloop()
