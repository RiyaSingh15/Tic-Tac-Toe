from tkinter import *
from tkinter import messagebox
class tic:
    def __init__(self):
        self.flag1=str()
        self.flag2=str()
        self.flag3=str()
        self.flag4=str()
        self.flag5=str()
        self.flag6=str()
        self.flag7=str()
        self.flag8=str()
        self.flag9=str()
        self.count=int()
        self.tac()
        
    def tac(self):
        self.window = Tk()
        self.window.title("Tic Tac Toe")
        self.label1=Label(self.window,text="Tic Tac Toe",font=("times",50),foreground="#bdc3c7",background="#2c3e50")
        self.label1.grid(columnspan=2,rowspan=2)
        self.lab=PhotoImage(file=r"tictactoe.png")
        self.labs=self.lab.subsample(2,2)
        self.label2=Label(self.window,image=self.labs)
        self.label2.grid(column=0,rowspan=3)
        self.label3=Label(self.window,text="Play Against",font=("times",20),foreground="#bdc3c7",background="#2c3e50")
        self.label3.grid(column=1,row=2)
        self.cpu=Button(self.window,text="CPU",font=("times",20),foreground="#bdc3c7",background="#2c3e50")
        self.cpu.grid(column=1,row=3)
        self.human=Button(self.window,text="Human",font=("times",20),foreground="#bdc3c7",background="#2c3e50",command=self.onHuman)
        self.human.grid(column=1,row=4)
        self.window.configure(bg='#2c3e50')
        self.window.geometry('400x400')
        self.window.resizable(0,0)
        self.window.mainloop()

    def onHuman(self):
        self.window.destroy()
        self.window=Tk()
        self.label1=Label(self.window,text="Tic Tac Toe",font=("times",50),foreground="#bdc3c7",background="#2c3e50")
        self.label1.grid(columnspan=3,row=0)
        self.one=Button(self.window,height=5,width=15,command=self.xo1)
        self.one.grid(column=0,row=2)
        self.two=Button(self.window,height=5,width=15,command=self.xo2)
        self.two.grid(column=1,row=2)
        self.three=Button(self.window,height=5,width=15,command=self.xo3)
        self.three.grid(column=2,row=2)
        self.four=Button(self.window,height=5,width=15,command=self.xo4)
        self.four.grid(column=0,row=3)
        self.five=Button(self.window,height=5,width=15,command=self.xo5)
        self.five.grid(column=1,row=3)
        self.six=Button(self.window,height=5,width=15,command=self.xo6)
        self.six.grid(column=2,row=3)
        self.seven=Button(self.window,height=5,width=15,command=self.xo7)
        self.seven.grid(column=0,row=4)
        self.eight=Button(self.window,height=5,width=15,command=self.xo8)
        self.eight.grid(column=1,row=4)
        self.nine=Button(self.window,height=5,width=15,command=self.xo9)
        self.nine.grid(column=2,row=4)
        self.window.configure(bg='#2c3e50')
        self.window.geometry('345x345')
        self.window.resizable(0,0)
        self.window.mainloop()
    def xo1(self):
        self.count+=1
        if self.count%2==0:
            self.one.config(text="O",state="disabled")
            self.flag1='o'
        else:
            self.one.config(text="X",state="disabled")
            self.flag1='x'
        self.check()
    def xo2(self):
        self.count+=1
        if self.count%2==0:
            self.two.config(text="O",state="disabled")
            self.flag2='o'
        else:
            self.two.config(text="X",state="disabled")
            self.flag2='x'
        self.check()
    def xo3(self):
        self.count+=1
        if self.count%2==0:
            self.three.config(text="O",state="disabled")
            self.flag3='o'
        else:
            self.three.config(text="X",state="disabled")
            self.flag3='x'
        self.check()
    def xo4(self):
        self.count+=1
        if self.count%2==0:
            self.four.config(text="O",state="disabled")
            self.flag4='o'
        else:
            self.four.config(text="X",state="disabled")
            self.flag4='x'
        self.check()
    def xo5(self):
        self.count+=1
        if self.count%2==0:
            self.five.config(text="O",state="disabled")
            self.flag5='o'
        else:
            self.five.config(text="X",state="disabled")
            self.flag5='x'
        self.check()
    def xo6(self):
        self.count+=1
        if self.count%2==0:
            self.six.config(text="O",state="disabled")
            self.flag6='o'
        else:
            self.six.config(text="X",state="disabled")
            self.flag6='x'
        self.check()
    def xo7(self):
        self.count+=1
        if self.count%2==0:
            self.seven.config(text="O",state="disabled")
            self.flag7='o'
        else:
            self.seven.config(text="X",state="disabled")
            self.flag7='x'
        self.check()
    def xo8(self):
        self.count+=1
        if self.count%2==0:
            self.eight.config(text="O",state="disabled")
            self.flag8='o'
        else:
            self.eight.config(text="X",state="disabled")
            self.flag8='x'
        self.check()
    def xo9(self):
        self.count+=1
        if self.count%2==0:
            self.nine.config(text="O",state="disabled")
            self.flag9='o'
        else:
            self.nine.config(text="X",state="disabled")
            self.flag9='x'
        self.check()
    def check(self):
        if self.flag1=='o' and self.flag2=='o' and self.flag3=='o':
            messagebox.showinfo("Tic Tac Toe","Player 2 Wins")
            self.window.destroy()
            tic()
             
        elif self.flag1=='o' and self.flag5=='o' and self.flag9=='o':
            messagebox.showinfo("Tic Tac Toe","Player 2 Wins")
            self.window.destroy()
            tic()
             
        elif self.flag1=='o' and self.flag4=='o' and self.flag7=='o':
            messagebox.showinfo("Tic Tac Toe","Player 2 Wins")
            self.window.destroy()
            tic()
             
        elif self.flag2=='o' and self.flag5=='o' and self.flag8=='o':
            messagebox.showinfo("Tic Tac Toe","Player 2 Wins")
            self.window.destroy()
            tic()
             
        elif self.flag3=='o' and self.flag5=='o' and self.flag7=='o':
            messagebox.showinfo("Tic Tac Toe","Player 2 Wins")
            self.window.destroy()
            tic()
             
        elif self.flag3=='o' and self.flag6=='o' and self.flag9=='o':
            messagebox.showinfo("Tic Tac Toe","Player 2 Wins")
            self.window.destroy()
            tic()
             
        elif self.flag7=='o' and self.flag8=='o' and self.flag9=='o':
            messagebox.showinfo("Tic Tac Toe","Player 2 Wins")
            self.window.destroy()
            tic()
             
        elif self.flag1=='x' and self.flag2=='x' and self.flag3=='x':
            messagebox.showinfo("Tic Tac Toe","Player 1 Wins")
            self.window.destroy()
            tic()
             
        elif self.flag1=='x' and self.flag5=='x' and self.flag9=='x':
            messagebox.showinfo("Tic Tac Toe","Player 1 Wins")
            self.window.destroy()
            tic()
             
        elif self.flag1=='x' and self.flag4=='x' and self.flag7=='x':
            messagebox.showinfo("Tic Tac Toe","Player 1 Wins")
            self.window.destroy()
            tic()
             
        elif self.flag2=='x' and self.flag5=='x' and self.flag8=='x':
            messagebox.showinfo("Tic Tac Toe","Player 1 Wins")
            self.window.destroy()
            tic()
             
        elif self.flag3=='x' and self.flag5=='x' and self.flag7=='x':
            messagebox.showinfo("Tic Tac Toe","Player 1 Wins")
            self.window.destroy()
            tic()
             
        elif self.flag3=='x' and self.flag6=='x' and self.flag9=='x':
            messagebox.showinfo("Tic Tac Toe","Player 1 Wins")
            self.window.destroy()
            tic()
             
        elif self.flag7=='x' and self.flag8=='x' and self.flag9=='x':
            messagebox.showinfo("Tic Tac Toe","Player 1 Wins")
            self.window.destroy()
            tic()
        
        elif self.count==9:
            messagebox.showinfo("Tic Tac Toe","It's a draw")
            self.window.destroy()
            tic()

tic()