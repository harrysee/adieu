from tkinter import *
import tkinter.ttk

from _Adoption_book import Adoption_book



class adieuMain():
    def __init__(self,title):
        self.engein =  Adoption_book()
        self.mainGUI(title)

    def mainGUI(self, title):
        self.TEXTCOLOR = '#B96F00'
        self.BACKGROUND = '#FFC978'  # 배경색
        self.root = Tk()
        self.root.title(title)
        self.root.geometry('745x580')
        self.root.configure(bg=self.BACKGROUND)
        self.root.resizable(0, 0)

        # 동물검색
        logo_img = PhotoImage(file='img/Adieu.png', width=182, height=87)
        logo = Label(self.root,bg=self.BACKGROUND,image=logo_img)

        # 왼쪽 사이드
        cartegoryFrame = Frame(self.root, bg=self.BACKGROUND )
        s_cat = Label(cartegoryFrame, text="고양이", fg=self.TEXTCOLOR, bg=self.BACKGROUND, pady=5, cursor="hand2")
        s_cat.bind('<ButtonRelease-1>', lambda x: self.search_species(event=s_cat))
        s_cat.pack()
        s_dog = Label(cartegoryFrame, text="강아지", fg=self.TEXTCOLOR, bg=self.BACKGROUND, pady=5, cursor="hand2")
        s_dog.bind('<ButtonRelease-1>', lambda x: self.search_species(event=s_dog))
        s_dog.pack()
        s_bird = Label(cartegoryFrame, text="새", fg=self.TEXTCOLOR, bg=self.BACKGROUND, pady=5, cursor="hand2")
        s_bird.bind('<ButtonRelease-1>', lambda x: self.search_species(event=s_bird))
        s_bird.pack()
        s_etc = Label(cartegoryFrame, text="기타", fg=self.TEXTCOLOR, bg=self.BACKGROUND, pady=5, cursor="hand2")
        s_etc.bind('<ButtonRelease-1>', lambda x: self.search_species(event=s_etc))
        s_etc.pack()

        photo_img = PhotoImage(file='img/search_img.png')
        search = Label(self.root, image=photo_img,bg=self.BACKGROUND)

        # 오른쪽 사이드
        animalList = Frame(self.root, width=900, height=900, bg=self.BACKGROUND)
        self.animalView = tkinter.ttk.Treeview(animalList,height= 20,columns=["species","name","age","applycnt"])
        self.animalView.bind("<Double-Button-1>",self.click_item)
        # treeView 사용 기본항목 포함 4개
        # scrollbar(animalList)
        # scrollbar.pack(side='right', fill="y")

        self.animalView.column('#0', width=70,anchor="center")   # 해당 속성이 차지하는 비율 
        self.animalView.heading('#0', text="등록번호",anchor="center")    # 해당속성의 번호
        self.animalView.column('#1',width=120,anchor="center")
        self.animalView.heading('#1',text="분류",anchor="center")
        self.animalView.column('#2',width=180,anchor="center")
        self.animalView.heading('#2',text="이름",anchor="center")
        self.animalView.column('#3',width=80,anchor="center")
        self.animalView.heading('#3',text="나이",anchor="center")
        self.animalView.column('#4', width=70, anchor="center")
        self.animalView.heading('#4', text="신청수", anchor="center")

        self.draw_animal_list(self.engein.show_animals())
        # scrollbar.config(command=self.animalView.yview)
        # self.animalView.config(yscrollcommand=scrollbar.set)

        # 오른쪽 위 로그아웃, 사용자
        logout = Label(self.root,text="로그아웃",fg=self.TEXTCOLOR,bg=self.BACKGROUND,cursor="left_side")
        user = Label(self.root, text='사용자',fg= self.TEXTCOLOR,bg=self.BACKGROUND,cursor="center_ptr")
        logout.bind('<ButtonRelease-1>',self.logout_event)
        user.bind('<ButtonRelease-1>',self.user_event)

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

    def draw_animal_list(self,treelist):    # 동물들 리스트 그리기
        for i in range(len(treelist)):
            # 번호, 종류, 이름, 나이 순으로 들어감
            self.animalView.insert('', 'end', text=i, values=treelist[i], iid=str(i) + "번")

    def click_item(self,evnet): # item 클릭 시 선택한 게시물 가져와서 이름 매개변수로 동물 상세보기로 넘김
        selectedItem = self.animalView.focus()
        getValue = self.animalView.item(selectedItem).get('values')
        print(getValue[1])
        from parcel_infor import ParceAdieuInfor
        ParceAdieuInfor('게시물 정보', getValue[1])    # 선택한 동물 이름 넘겨주기

    def logout_event(self,evnet):   # 로그아웃 -> 첫화면
        self.root.destroy()
        from start import StartAdieu
        StartAdieu("처음 화면")

    def search_species(self,event):   # 동물 종류별 검색
        pass

    def user_event(self,event): # 사용자클릭햇을때 -> 사용자화면
        self.root.destroy()
        from user_info import UserInfo
        UserInfo('사용자 정보')
        
    def play(self):
        self.root.mainloop()

if __name__ == '__main__':
    adieuMain('메인')

