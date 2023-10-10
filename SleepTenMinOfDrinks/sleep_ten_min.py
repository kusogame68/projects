# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 01:19:24 2023

@author: User
"""

class itemshop():
    
    def __init__(self,shopname):
        self.shopname=shopname
        self.items={}
        
    def showMenu(self):
        print('{:*^20}'.format(self.shopname))
        print('{:^20}'.format('(1).新增品項'))
        print('{:^20}'.format('(2).刪除品項'))
        print('{:^20}'.format('(3).修改品項'))
        print('{:^20}'.format('(4).目前品項'))
        print('{:^20}'.format('(5).清除品項'))
        print('{:^20}'.format('(6).離開'))
        print('{:*^20}'.format(self.shopname))   
        
    def add(self):
        while True:
            item=input('請輸入新品項:(q:quit)')
            if item.lower()=='q':
                break
            elif item in self.items:
                print('已有該品項')            
            else:
                try:
                    price=int(input(f'請輸入{item} 價格:'))
                    self.items[item]=price            
                except ValueError:
                    print('價格有誤，請重新輸入!')
                else:
                    print(f'品項{item} 新增完畢!')
                    
    def edit(self):
        while True:
            item=input('請輸入刪除品項:(q:quit)')
            if item.lower()=='q':
                break 
            elif item not in self.items:
                print('無該品項')            
            else:
                del self.items[item]
                print(f'品項{item} 刪除完畢!')
                
    def delete(self):
        while True:
            item=input('請輸入修改品項:(q:quit)')
            if item.lower()=='q':
                break
            elif item not in self.items:            
                print('無該品項') 
            else:
                try:
                    price=int(input(f'請輸入{item} 價格:'))
                    self.items[item]=price
                except ValueError:
                    print('價格有誤，請重新輸入!')
                else:
                    print(f'品項{item} 價格修改完畢!')  
        
    def view(self):
        if len(self.items)==0:
            print('目前無品項')
        else:
            print('目前品項')
            for key,value in self.items.items():                
                print(f'{key}={value}',end=' ')
            print()

    def clear(self):
        if input('是否確定刪除所有品項?(y/n)').lower()=='y':
            self.items.clear()   
            print('全品項刪除')



shop=itemshop('在睡10分鐘飲料店')
    
while True:
    
    shop.showMenu()  
    
    while True:
        try:
            choice=int(input('請輸入功能選擇:'))
        except Exception as e:
            print(e)
        else:
            break
    
    if choice==6:
        print('離開程式')    
        break
    
    elif choice==1:
        shop.add()
    
    elif choice==2:
        shop.edit()
        
    elif choice==3:
        shop.delete()
        
    elif choice==4:
        shop.view()
    
    elif choice==5:
        shop.clear()
    
    input('請按任一鍵...')
    

        