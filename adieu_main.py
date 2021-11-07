from tkinter import *
import tkinter.ttk


class adieuMain():
    def __init__(self, title):
        self.root = Tk()
        self.root.title(title)
        self.root.geometry('745x580')
        self.root.configure(bg="#FFC978")

        # 동물검색
        logo_img = PhotoImage(file='img/Adieu.png',width=182,height=87)
        logo = Label(self.root,bg="#FFC978",image=logo_img)

        # 왼쪽 사이드
        cartegoryFrame = Frame(self.root, bg="#FFC978" )
        for i in range(5):
            text = Label(cartegoryFrame,text="동물이름"+str(i), fg='#B96F00',bg="#FFC978",pady=5,cursor="hand2"
                                                                                                    "")
            text.pack()
        photo_img = PhotoImage(file='img/search_img.png')
        search = Label(self.root, image=photo_img,bg="#FFC978")

        # 오른쪽 사이드
        animalList = Frame(self.root, width=900, height=900, bg="#FFC978")
        self.animalView = tkinter.ttk.Treeview(animalList,height= 20,columns=["species","name","age"])
        self.animalView.bind("<ButtonRelease-1>",self.click_item)
        # treeView 사용 기본항목 포함 4개
        # scrollbar(animalList)
        # scrollbar.pack(side='right', fill="y")

        self.animalView.column('#0', width=70,anchor="center")   # 해당 속성이 차지하는 비율 
        self.animalView.heading('#0', text="num",anchor="center")    # 해당속성의 이름
        self.animalView.column('#1',width=150,anchor="center")
        self.animalView.heading('#1',text="species",anchor="center")
        self.animalView.column('#2',width=200,anchor="center")
        self.animalView.heading('#2',text="name",anchor="center")
        self.animalView.column('#3',width=80,anchor="center")
        self.animalView.heading('#3',text="age",anchor="center")

        treelist = [("A","동물이름", 65), ("B","동물이름", 66), ("C","동물이름", 67), ("D","동물이름", 68), ("E","동물이름", 69),
                    ("A","동물이름", 65), ("B","동물이름", 66), ("C","동물이름", 67), ("D","동물이름", 68), ("E","동물이름", 69),
                    ("A","동물이름", 65), ("B","동물이름", 66), ("C","동물이름", 67), ("D","동물이름", 68), ("E","동물이름", 69)]

        for i in range(len(treelist)):
            self.animalView.insert('', 'end', text=i, values=treelist[i], iid=str(i) + "번")

        # scrollbar.config(command=self.animalView.yview)
        # self.animalView.config(yscrollcommand=scrollbar.set)

        # 오른쪽 위 로그아웃, 사용자
        logout = Label(self.root,text="로그아웃",fg="#B96F00",bg="#FFC978",cursor="left_side")
        user = Label(self.root, text='사용자',fg= '#B96F00',bg="#FFC978",cursor="center_ptr")
        logout.bind('<ButtonRelease-1>',self.logout_event)

        # 화면 보여주기
        self.animalView.pack(side='left')
        cartegoryFrame.pack(side='left',fill="y")
        animalList.place(x=200, y=90)
        logout.place(x=600,y=15)
        user.place(x=660,y=15)
        cartegoryFrame.place(x=50,y=150)
        search.place(x=15, y=90)
        logo.place(x=10,y=5)
        self.play()

    def click_item(self,evnet): # item 클릭 시 실행
        selectedItem = self.animalView.focus()
        getValue = self.animalView.item(selectedItem).get('values')
        print(getValue)

    def logout_event(self,evnet):
        self.root.destroy()
        from login import loginAdieu
        loginAdieu("로그인화면")
        
    def play(self):
        self.root.mainloop()


