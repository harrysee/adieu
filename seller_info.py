from tkinter import *


class SellerInfo():
    def __init__(self, title):
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
        name_info = Label(self.root, width=17,anchor='w', text='이름', bg='#fff', relief='flat', bd=10,
                             fg='#000')  # 회원가입 버튼
        age_info = Label(self.root,anchor='w', width=17, text='나이', bg='#fff', relief='flat', bd=10,
                            fg='#000')  # 취소 버튼
        id_info = Label(self.root, width=17,anchor='w', text='ID', bg='#fff', relief='flat', bd=10,
                            fg='#000')  # 취소 버튼
        intro_info = Label(self.root, width=17,anchor='w', text='소개', bg='#fff', relief='flat', bd=10,
                            fg='#000')  # 취소 버튼

        # 하단 버튼
        ok_btn = Button(self.root, cursor='hand2', width=13, text='분양수락', bg='#F0AD48', relief='flat', bd=8,
                          fg=text_color)  # 회원가입 버튼
        no_btn = Button(self.root, cursor='hand2', width=13, text='분양거절', bg='#F0AD48', relief='flat', bd=8,
                            fg=text_color)  # 취소 버튼

        #컨테이너
        write_posts = LabelFrame(self.root, labelanchor='n',width=200, height=200,text="등록한 게시물",fg=text_color,bg=bg_color)
        apply_posts = LabelFrame(self.root, labelanchor='n',width=200, height=200,text="신청한 게시물",fg=text_color,bg=bg_color)
        writelist = Listbox(write_posts, selectmode='single', height=0)
        applylist = Listbox(apply_posts, selectmode='single', height=0)
        testlist = [('강아지','또미'),('앵무새 ','탁구'),('고양이','축복이'),('고양이','행복이'),('거북이','독도'),('병아리','꼬꼬'),
                    ('강아지','또미'),('앵무새 ','탁구'),('고양이','축복이'),('고양이','행복이'),('거북이','독도'),('병아리','꼬꼬'),
                    ('강아지','또미'),('앵무새 ','탁구'),('고양이','축복이'),('고양이','행복이'),('거북이','독도'),('병아리','꼬꼬')]
        writelist.bind("<ButtonRelease-1>",self.writeItemEvent)
        applylist.bind("<ButtonRelease-1>",self.applyItemEvent)

        for i in testlist:
            writelist.insert(END,' '+ i[0]+'   :   '+i[1])
            applylist.insert(END,' '+ i[0]+'   :   '+i[1])

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

    def okEvent(self):
        # 분양수락 버튼 눌렀을때
        # 분양자 정보 보내기
        pass

    def noEvent(self):
        # 분양거절 - 시작화면으로 이동
        pass

    def writeItemEvent(self):
        # 등록한 게시물 클릭했을때
        pass
    
    def applyItemEvent(self):
        # 신청한 게시물 클릭했을때
        pass

    def play(self):
        self.root.mainloop()


if __name__ == '__main__':
    SellerInfo('분양자 정보화면')

