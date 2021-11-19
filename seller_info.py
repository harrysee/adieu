from tkinter import *

from _Adoption_book import Adoption_book


class SellerInfo():
    def __init__(self,title, userid):
        self.engien = Adoption_book()
        self.thisUserInfo,self.userid= self.engien.get_user_info(userid),userid
        self.sellerGUI(title)

    def sellerGUI(self, title):
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
        name_info = Label(self.root, width=17,anchor='w', text=self.thisUserInfo['name'], bg='#fff', relief='flat', bd=10,
                             fg='#000')  # 회원가입 버튼
        age_info = Label(self.root,anchor='w', width=17, text=self.thisUserInfo['age'], bg='#fff', relief='flat', bd=10,
                            fg='#000')  # 취소 버튼
        id_info = Label(self.root, width=17,anchor='w', text=self.userid, bg='#fff', relief='flat', bd=10,
                            fg='#000')  # 취소 버튼
        intro_info = Label(self.root, width=17,anchor='w', text=self.thisUserInfo['introduce'], bg='#fff', relief='flat', bd=10,
                            fg='#000')  # 취소 버튼

        # 하단 버튼
        ok_btn = Button(self.root, cursor='hand2', width=13, text='분양수락', bg='#F0AD48', relief='flat', bd=8, command=self.okEvent,
                          fg=text_color)  # 회원가입 버튼
        no_btn = Button(self.root, cursor='hand2', width=13, text='분양거절', bg='#F0AD48', relief='flat', bd=8, command=self.noEvent,
                            fg=text_color)  # 취소 버튼

        #컨테이너
        write_posts = LabelFrame(self.root, labelanchor='n',width=200, height=200,text="등록한 게시물",fg=text_color,bg=bg_color)
        apply_posts = LabelFrame(self.root, labelanchor='n',width=200, height=200,text="신청한 게시물",fg=text_color,bg=bg_color)
        writelist = Listbox(write_posts, selectmode='single', height=0)
        applylist = Listbox(apply_posts, selectmode='single', height=0)
        writelist.bind("<Double-Button-1>",self.writeItemEvent)
        applylist.bind("<Double-Button-1>",self.applyItemEvent)
        
        # 리스트 아이템들 추가
        self.draw_postList(self.thisUserInfo['up_list'], writelist)
        self.draw_postList(self.thisUserInfo['pick_list'], applylist)

        # 화면넣기
        write_posts.place(x=280,y=85)
        apply_posts.place(x=510,y=85)
        writelist.pack(padx=20,pady=10)
        applylist.pack(padx=20,pady=10)
        ok_btn.place(x=488, y=516)
        no_btn.place(x=611, y=516)
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
            listbox.insert(END, ' ' + animal['species'] + '   :   ' + post)

    def okEvent(self):
        # 분양수락 버튼 눌렀을때
        # 사용자- 신청리스트 및 게시물-신청리스트에서 삭제
        # 메시지박스로 정보 전달
        pass

    def noEvent(self):
        # 분양거절 - 사용자- 신청리스트 및 게시물-신청리스트에서 삭제 후 시작화면으로 이동
        pass

    def writeItemEvent(self,event):
        # 등록한 게시물 클릭했을때
        pass
    
    def applyItemEvent(self,event):
        # 신청한 게시물 클릭했을때
        pass

    def play(self):
        self.root.mainloop()


if __name__ == '__main__':
    SellerInfo('분양자 정보화면')

