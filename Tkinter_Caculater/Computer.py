# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 02:02:05 2023

@author: Johnson
"""
import tkinter as tk

class Computer:
    def __init__(self,title=None,geometry=None,resizable=False,iconbitmap=None):
        self.title=title
        self.geometry=geometry
        self.resizable=resizable
        self.iconbitmap=iconbitmap
        self.win=self.get_win()

    def get_win(self):
        self.win=tk.Tk()
        self.win.title(self.title)
        self.win.geometry(self.geometry)
        self.win.resizable(self.resizable,self.resizable)
        self.win.iconbitmap(self.iconbitmap)
        self.interface()
        self.win.mainloop()    

    def interface(self):
        font1=('標楷體',15)
        font2=('微軟正黑體',15)
        font3=('Arial',10)
        font4=('Arial',15)
        btn_text='(,),←,C,7,8,9,/,4,5,6,*,1,2,3,-,0,.,+,='.split(',')
        
        self.frame1=tk.Frame(self.win,bg='black')
        self.frame2=tk.Frame(self.win)
        self.frame1.pack(fill='x')
        self.frame2.pack(fill='x')
        
        self.str_var=tk.StringVar() 
        
        # frame1
        self.entry1=tk.Entry(self.frame1,font=font4,justify='right',bg='#00FFFF')
        self.label1=tk.Label(self.frame1,font=font1,textvariable=self.str_var,bg='black',fg='yellow',anchor='e') 
        self.entry1.pack(fill='x',padx=3,pady=3)
        self.label1.pack(fill='x')
        
        # frame2
        # 使用迴圈方式產生按鈕
        for i in range(len(btn_text)):
            x=btn_text[i]
            if x=='C':
                button=tk.Button(self.frame2,text=x,width=15,height=2,command=self.clear)
            elif x=='←':
                button=tk.Button(self.frame2,text=x,width=15,height=2,command=self.remove)
            elif x=='=':
                button=tk.Button(self.frame2,text=x,width=15,height=2,command=self.caculate)
            else:
                button=tk.Button(self.frame2,text=x,width=15,height=2,command=lambda x=x:self.btn(x))
            # 利用計數一列元素
            button.grid(row=i//4,column=i%4,padx=3,pady=3)
        
        del font1,font2,font3,font4,btn_text,x,button

    def btn(self,x):
        self.entry1.insert('end',x)
        
    def clear(self):
        self.entry1.delete(0,'end')
        self.str_var.set('')
        
    def remove(self):
        self.entry1.delete(len(self.entry1.get())-1,'end')
        
    def caculate(self):
        try:
            self.str_var.set(eval(self.entry1.get()))
        except ZeroDivisionError:
            self.str_var.set('除數不能為0')
        except Exception as e:
            self.str_var.set('輸入錯誤')
        return

if __name__=='__main__':
    app=Computer(title='計算機',iconbitmap=r'..\Image\com.ico')
    app