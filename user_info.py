from tkinter import *

from _Adoption_book import Adoption_book


class UserInfo():
    def __init__(self, title):
        self.engien = Adoption_book()
        self.user, self.id = self.engien.get_user_info('nowuser')
        self.userGUI(title)

    def userGUI(self, title):
        text_color = '#B96F00'
        bg_color = '#FFC978'  # 배경색
        self.root = Tk()
        self.root.title(title)
        self.root.geometry('745x580')
        self.root.configure(bg=bg_color)
        self.root.resizable(0, 0)

        # 왼쪽 사이드
        logo_img = PhotoImage(file='img/Adieu.png', width=182, height=87)
        logo = Label(self.root, bg=bg_color, image=logo_img)  # 로고
        photo_img = PhotoImage(file='img/input_img.png')
        photo = Label(self.root, image=photo_img, bg=bg_color, anchor="w")  # 이미지 넣기 왼쪽 정렬
        name_info = Label(self.root, width=17, anchor='w', text=self.user['name'], bg='#fff', relief='flat', bd=10,
                          fg='#000')  # 회원가입 버튼
        age_info = Label(self.root, anchor='w', width=17, text=self.user['age'], bg='#fff', relief='flat', bd=10,
                         fg='#000')  # 취소 버튼
        id_info = Label(self.root, width=19, anchor='w', text=self.id, bg='#fff', relief='flat', bd=10,
                        fg='#000')  # 취소 버튼
        intro_info = Label(self.root, width=19, anchor='w', text=self.user['introduce'], bg='#fff', relief='flat', bd=10,
                           fg='#000')  # 취소 버튼

        # 하단 버튼
        edit_btn = Button(self.root, cursor='hand2', width=13, text='정보수정', bg='#F0AD48', relief='flat', bd=8, command= self.editBtnEventListener,
                        fg=text_color)  # 취소 버튼
        add_btn = Button(self.root, cursor='hand2', width=13, text='게시물추가', bg='#F0AD48', relief='flat', bd=8,
                          command=self.addBtnEventListener,fg=text_color)  # 취소 버튼

        # 컨테이너
        write_posts = LabelFrame(self.root, labelanchor='n', width=200, height=200, text="등록한 게시물", fg=text_color,
                                 bg=bg_color)
        apply_posts = LabelFrame(self.root, labelanchor='n', width=200, height=200, text="신청한 게시물", fg=text_color,
                                 bg=bg_color)
        self.writelist = Listbox(write_posts, selectmode='single', height=0)
        self.applylist = Listbox(apply_posts, selectmode='single', height=0)
        self.writelist.bind("<Double-Button-1>", self.writeItemEvent)
        self.applylist.bind("<Double-Button-1>", self.applyItemEvent)

        self.draw_postList(self.user['up_list'],self.writelist)
        self.draw_postList(self.user['pick_list'],self.applylist)

        # 화면넣기
        write_posts.place(x=280, y=85)
        apply_posts.place(x=510, y=85)
        self.writelist.pack(padx=20, pady=10)
        self.applylist.pack(padx=20, pady=10)
        edit_btn.place(x=611, y=516)
        add_btn.place(x=480, y=516)
        photo.place(x=40, y=90)
        name_info.place(x=65, y=300)
        age_info.place(x=65, y=355)
        id_info.place(x=65, y=410)
        intro_info.place(x=65, y=465)
        logo.place(x=5, y=5)
        self.play()

    def draw_postList(self, postList, listbox):
        for post in postList:       # 등록한게시물이나 신청한 게시물에 잇는 동물이름으로 정보 가져와서 처리하기
            animal = self.engien.get_animal_info(post)
            listbox.insert(END, ' ' + animal[5] + '   :   ' + post)

    def writeItemEvent(self, event):
        # 등록한 게시물 클릭했을때
        selectedItem = self.writelist.curselection()
        print(selectedItem)
        getValue = self.user['up_list'][selectedItem[0]]
        from parcel_update import ParcelUpdate
        ParcelUpdate('사용자정보수정 및 분양자확인', getValue)

    def applyItemEvent(self, event):
        # 신청한 게시물 클릭했을때
        selectedItem = self.applylist.curselection()
        getValue = self.user['pick_list'][selectedItem]
        from parcel_infor import ParceAdieuInfor
        ParceAdieuInfor('게시물 정보 및 분양 신청', getValue)

    def editBtnEventListener(self):
        # 수정하기 버튼 리스너
        self.root.destroy()
        from edit_user_info import EditUserInfo
        EditUserInfo('사용자정보수정')

    def addBtnEventListener(self):
        # 게시물 추가 버튼 리스너
        self.root.destroy()
        from parcel_add import ParceAdieuAdd
        ParceAdieuAdd('분양등록')

    def play(self):
        self.root.mainloop()


if __name__ == '__main__':
    UserInfo('사용자 정보화면')

