# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 16:10:50 2023

@author: Johnson
"""
from pathlib import Path
from tkinter import messagebox as msg
from tkinter import ttk
import os
import tkinter as tk

# 以coco設定原型

base_dir=Path(__file__).resolve().parent
bt_dir=os.path.join(base_dir, 'Images\Button_Images')
bg_dir=os.path.join(base_dir, 'Images\Background_Images')
icon_dir=os.path.join(base_dir, 'Images\Icon_Images')

class DrinksMarketSystem:
    title='Drinks Market System'
    geometry='1350x750'
    resizable=False
    iconbitmap=None
    conn=None
    cur=None
    
    def __init__(self):
        DrinksMarketSystem.Index()
        
    class Base(object):
        def __init__(self):
            self.title=DrinksMarketSystem.title
            self.geometry=DrinksMarketSystem.geometry
            self.resizable=DrinksMarketSystem.resizable
            self.iconbitmap=DrinksMarketSystem.iconbitmap
            
        def get_win(self):
            self.win=tk.Tk()
            self.win.protocol("WM_DELETE_WINDOW",self.press_exit)
            self.win.title(self.title)
            self.win.geometry(self.geometry)
            self.win.resizable(self.resizable,self.resizable)
            self.win.iconbitmap(self.iconbitmap)
            self.interface()
            self.win.mainloop()
        
        # 用tk產生圖片
        def make_image(self,file):
            img=tk.PhotoImage(file=file)
            return img
        
        # 導向background存放的path
        def bg_path(self,imagepath):
            fullpath=os.path.join(bg_dir, imagepath)
            return fullpath
        
        # 導向button存放的path
        def bt_path(self,imagepath):
            fullpath=os.path.join(bt_dir, imagepath)
            return fullpath
        
        # 導向icon存放的path
        def icon_path(self,imagepath):
            fullpath=os.path.join(icon_dir, imagepath)
            return fullpath
        
        # 創建客製化背景
        def create_bg(self,filepath):
            fullpath=self.bg_path(imagepath=filepath)
            self.bg_get=self.make_image(fullpath)
            self.canvas=tk.Canvas(self.win,width=1350,height=750)
            self.canvas.create_image(0,0,anchor='nw',image=self.bg_get)
            self.canvas.place(x=0,y=0)
            del fullpath
        
        # 綁定離開功能
        def press_exit(self):
            response=msg.askyesno("Exit","確定要結束嗎?",parent=self.win)
            if response:
                self.win.destroy()
            
    class Index(Base):
        white='#ffffff'
        def __init__(self):
            super().__init__()
            self.iconbitmap=self.icon_path('Index.ico')
            self.win=self.get_win()
        
        # 介面佈局
        def interface(self):
            self.create_bg('Index_bg.png')
            self.emp_button()
            self.man_button()
        
        def login_as(self,where):
            if where=='emp':
                return DrinksMarketSystem.EmployeeLogin()
            return DrinksMarketSystem.ManagerLogin()
        
        def emp_bt_func(self):
            self.win.destroy()
            self.login_as('emp')
        
        def man_bt_func(self):
            self.win.destroy()
            self.login_as('man')
        
        # 創建客製emp_button
        def emp_button(self):
            fullpath=self.bt_path('Emp.png')
            self.emp=self.make_image(fullpath)
            manager_button=tk.Button(self.win,
                                  image=self.emp,
                                  bg=__class__.white,
                                  bd=0,
                                  cursor='hand2',
                                  activebackground=__class__.white,
                                  command=self.emp_bt_func
                                  )
            manager_button.place(x=335,y=310)
            del fullpath
        
        # 創建客製manager_button
        def man_button(self):
            fullpath=self.bt_path('Man.png')
            self.man=self.make_image(fullpath)
            manager_button=tk.Button(self.win,
                                  image=self.man,
                                  bg=__class__.white,
                                  bd=0,
                                  cursor='hand2',
                                  activebackground=__class__.white,
                                  command=self.man_bt_func
                                  )
            manager_button.place(x=890,y=310)
            del fullpath
            
    class ManagerLogin(Base):
        white='#ffffff'
        lightblue='#00ffff'
        fg_color='gray'
        font0=('粗體',22,'bold')
        font1=('粗體',32,'bold')
        font2=('粗體',16,'bold')
        font3=('粗體',12,'bold')
        def __init__(self):
            super().__init__()
            self.title=self.title+' ( Manager )'
            self.iconbitmap=self.icon_path('Login.ico')
            self.win=self.get_win()
        
        def interface(self):
            self.create_bg('Login_bg.png')
            self.head()
            self.alt()
            self.labels()
            self.entrys()
            self.login_butont_bg()
            self.loging_bt()
            
        
        ######尚未設定
        def login(self):
            print( 'login')
            
        def head(self):
            head=tk.Label(self.win,
                           text='Login',
                           font=__class__.font1,
                           bg=__class__.white,
                           )
            head.place(x=615,y=80)
        
        def alt(self):
            alt=tk.Label(self.win,
                           text='Manager',
                           font=__class__.font2,
                           bg=__class__.white,
                           fg=__class__.fg_color
                           )
            alt.place(x=630,y=60)
        
        def labels(self):
            username=tk.Label(self.win,
                           text='Username',
                           font=__class__.font3,
                           bg=__class__.white,
                           fg=__class__.fg_color
                           )
            username.place(x=470,y=200)
            
            password=tk.Label(self.win,
                           text='Password',
                           font=__class__.font3,
                           bg=__class__.white,
                           fg=__class__.fg_color
                           )
            password.place(x=470,y=300)
        
        def entrys(self):
            userentry=ttk.Entry(self.win,
                                font=__class__.font3,
                                width=40,
                                )
            userentry.place(x=515,y=240)
            
            passwordentry=ttk.Entry(self.win,
                                font=__class__.font3,
                                width=40,
                                show='*',
                                )
            passwordentry.place(x=515,y=340)
        
        # 創建login按鈕的背景
        def login_butont_bg(self):
            fullpath=self.bt_path('button.png')
            self.lg_bg=self.make_image(fullpath)
            login_button_background=tk.Label(self.win,
                                              image=self.lg_bg,
                                              bg=__class__.white,
                                              bd=0
                                              )
            login_button_background.place(x=475,y=600)
        
        # 創建login按鈕
        def loging_bt(self):
            manager_button=tk.Button(self.win,
                                  text='Login',
                                  font=__class__.font0,
                                  width=19,
                                  fg=__class__.white,
                                  bg=__class__.lightblue,
                                  bd=0,
                                  cursor='hand2',
                                  activebackground=__class__.lightblue,
                                  command=self.login
                                  )
            manager_button.place(x=500,y=600)
    
    class EmployeeLogin(ManagerLogin):
        def __init__(self):
            self.title=DrinksMarketSystem.title
            self.geometry=DrinksMarketSystem.geometry
            self.resizable=DrinksMarketSystem.resizable
            self.iconbitmap=self.icon_path('Login.ico')
            self.title=DrinksMarketSystem.title+' ( Employee )'
            self.win=self.get_win()
            
        def alt(self):
            alt=tk.Label(self.win,
                           text='Employee',
                           font=__class__.font2,
                           bg=__class__.white,
                           fg=__class__.fg_color
                           )
            alt.place(x=620,y=60)
    
    
            
    # bill
    # manager
    # empolyee
    # customer 
    # inventory 
    # raw_inventory 
    class database():
        pass
    
    class Manager(Base):
        pass
    
    class Empolyee(Base):
        pass
        
    





if __name__=='__main__':
    root=DrinksMarketSystem()
    root
