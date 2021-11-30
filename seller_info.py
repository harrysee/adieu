from tkinter import *
from tkinter import messagebox

from _Adoption_book import Adoption_book

class SellerInfo():
    def __init__(self, title, userid):
        self.engien = Adoption_book()
        self.thisUserInfo = self.engien.get_user_info(userid)
        self.userid = userid
        self.sellerGUI(title)

    def sellerGUI(self, title):
        text_color = '#B96F00'
        bg_color = '#FFC978'  # 배경색
        self.root = Tk()
        self.root.title(title)
        self.root.geometry('745x580+400+100')
        self.root.configure(bg=bg_color)
        self.root.resizable(0, 0)

        # 왼쪽 사이드
        logo_img = PhotoImage(file='img/Adieu.png', width=182, height=87)
        logo = Label(self.root, bg=bg_color, image=logo_img,cursor='hand2')  # 로고
        logo.bind('<Button-1>',self.moveMain)

        photo_img = PhotoImage(file='img/input_img.png')
        photo = Label(self.root, image=photo_img, bg=bg_color, anchor="w")  # 이미지 넣기 왼쪽 정렬
        name_info = Label(self.root, width=17, anchor='w', text=self.thisUserInfo['name'], bg='#fff', relief='flat',
                          bd=10, fg='#000')
        age_info = Label(self.root, anchor='w', width=17, text=self.thisUserInfo['age'], bg='#fff', relief='flat',
                         bd=10, fg='#000')
        id_info = Label(self.root, width=17, anchor='w', text=self.userid, bg='#fff', relief='flat', bd=10,
                        fg='#000')  # 취소 버튼
        intro_info = Label(self.root, width=17, anchor='w', text=self.thisUserInfo['introduce'], bg='#fff',
                           relief='flat', bd=10, fg='#000')  # 취소 버튼

        # 하단 버튼
        ok_btn = Button(self.root, cursor='hand2', width=13, text='분양수락', bg='#F0AD48', relief='flat', bd=8,
                        command=self.okEvent, fg=text_color)  # 회원가입 버튼
        no_btn = Button(self.root, cursor='hand2', width=13, text='분양거절', bg='#F0AD48', relief='flat', bd=8,
                        command=self.noEvent, fg=text_color)  # 취소 버튼

        # 컨테이너
        write_posts = LabelFrame(self.root, labelanchor='n', width=200, height=200, text="등록한 게시물", fg=text_color,
                                 bg=bg_color)
        apply_posts = LabelFrame(self.root, labelanchor='n', width=200, height=200, text="신청한 게시물", fg=text_color,
                                 bg=bg_color)
        self.writelist = Listbox(write_posts, selectmode='single', height=0)
        self.applylist = Listbox(apply_posts, selectmode='single', height=0)
        self.writelist.bind("<Double-Button-1>", self.writeItemEvent)
        self.applylist.bind("<Double-Button-1>", self.applyItemEvent)

        # 리스트 아이템들 추가
        self.draw_postList(self.thisUserInfo['up_list'], self.writelist)
        self.draw_postList(self.thisUserInfo['pick_list'], self.applylist)

        # 화면넣기
        write_posts.place(x=280, y=85)
        apply_posts.place(x=510, y=85)
        self.writelist.pack(padx=20, pady=10)
        self.applylist.pack(padx=20, pady=10)
        ok_btn.place(x=488, y=516)
        no_btn.place(x=611, y=516)
        photo.place(x=40, y=90)
        name_info.place(x=65, y=300)
        age_info.place(x=65, y=355)
        id_info.place(x=65, y=410)
        intro_info.place(x=65, y=465)
        logo.place(x=5, y=5)
        self.play()
        
    def moveMain(self,e): # 로고누르면 이동
        self.root.destroy()
        from adieu_main import adieuMain
        adieuMain("메인")

    def draw_postList(self, postList, listbox):
        for post in postList:  # 등록한게시물이나 신청한 게시물에 잇는 동물이름으로 정보 가져와서 처리하기
            print(post)
            animal = self.engien.get_animal_info(post)
            listbox.insert(END, ' ' + animal[5] + '   :   ' + post)

    def okEvent(self):
        # 분양수락 - 사용자-신청리스트 및 게시물-신청리스트에서 삭제
        # 작성자에게 분양자 전화번호 전달
        seller = self.engien.get_user_info(self.thisUserInfo)
        keys = ['', 'name', 'age', 'id', 'pw', 'pw_check', 'zipcode', 'call_number', 'introduce']
        call = seller[keys[7]]
        messagebox.showinfo('전화번호:', call)

        # 분양자에게 작성자의 주소와 전화번호 전달

        # 게시물 수락
        self.users[Adoption_book.NOWUSER]['pick_check'] = 1

        from parcel_update import ParcelUpdate
        self.root.destroy()
        ParcelUpdate.sellerEvent('분양수정 및 분양자 확인', self.userid)

    def noEvent(self):
        # 분양거절 - 사용자- 신청리스트 및 게시물-신청리스트에서 삭제 후 시작화면으로 이동

        # 게시물 거절
        self.users[Adoption_book.NOWUSER]['pick_check'] = -1

        self.root.destroy()
        from parcel_update import ParcelUpdate
        ParcelUpdate.sellerEvent('분양수정 및 분양자 확인', self.userid)

    def writeItemEvent(self, event):
        # 등록한 게시물 클릭했을때
        selectedItem = self.writelist.curselection()
        getValue = self.thisUserInfo['up_list'][selectedItem[0]]
        self.root.destroy()
        from parcel_infor import ParceAdieuInfor
        ParceAdieuInfor('게시물 정보 및 분양 신청', getValue)

    def applyItemEvent(self, event):
        # 신청한 게시물 클릭했을때
        selectedItem = self.applylist.curselection()
        getValue = self.thisUserInfo['pick_list'][selectedItem[0]]
        self.root.destroy()
        from parcel_infor import ParceAdieuInfor
        ParceAdieuInfor('게시물 정보 및 분양 신청', getValue)

    def play(self):
        self.root.mainloop()


if __name__ == '__main__':
    SellerInfo('분양자 정보화면')