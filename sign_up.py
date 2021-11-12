from tkinter import *


class SignUp():
    def __init__(self, title):
        bg_color='#FFC978'  # 배경색
        self.root = Tk()
        self.root.title(title)
        self.root.geometry('745x580')
        self.root.configure(bg=bg_color)
        self.root.resizable(0,0)
        # 왼쪽 사이드
        logo_img = PhotoImage(file='img/Adieu.png', width=182, height=87)
        logo = Label(self.root, bg=bg_color, image=logo_img)    # 로고
        photo_img = PhotoImage(file='img/input_img.png')
        photo = Label(self.root, image=photo_img, bg=bg_color, anchor="w")  # 이미지 넣기 왼쪽 정렬
        sign_up_btn = Button(self.root,cursor='hand2', width=16, text='회원가입',bg='#F0AD48',relief='flat',bd=10,fg='#B96F00') # 회원가입 버튼
        cancel_btn = Button(self.root,cursor='hand2', width=16, text='취소',bg='#F0AD48',relief='flat',bd=10,fg='#B96F00')    # 취소 버튼

        # 입력받기
        inputFrame = Frame(self.root, bg=bg_color,width=430,height=400)
        name = Entry(inputFrame, width=20, relief="flat", bd=13, fg="gray")
        age = Entry(inputFrame, width=25, relief="flat", bd=13, fg="gray")
        id = Entry(inputFrame, width=25, relief="flat", bd=13, fg="gray")
        pw = Entry(inputFrame, width=30, relief="flat", bd=13, fg="gray")
        pw_check = Entry(inputFrame, width=30, relief="flat", bd=13, fg="gray")
        zipcode = Entry(inputFrame, width=30, relief="flat", bd=13, fg="gray")
        call_number = Entry(inputFrame, width=40, relief="flat", bd=13, fg="gray")
        introduce = Entry(inputFrame, width=40, relief="flat", bd=13, fg="gray")
        self.gender_var = IntVar()  # 여기에 int 형으로 값을 저장한다
        gender_w = Radiobutton(inputFrame, text="여자", value=1, variable=self.gender_var,bg= bg_color)
        gender_m = Radiobutton(inputFrame, text="남자", value=2, variable=self.gender_var,bg= bg_color)
        gender_w.select()  # 기본적으로 여자 선택
        inputList = [name, age, id, pw, pw_check, zipcode, call_number, introduce]  # 입력 받을 리스트

        # hint
        inputList[0].insert(0, '이름')
        inputList[1].insert(0, '나이')
        inputList[2].insert(0, 'ID')
        inputList[3].insert(0, 'PW')
        inputList[4].insert(0, 'PW 확인')
        inputList[5].insert(0, '집주소')
        inputList[6].insert(0, '전화번호')
        inputList[7].insert(0, '소개')

        # hint 이벤트
        inputList[0].bind('<Button-1>', lambda x: self.hintEvent(event=name))
        inputList[1].bind('<Button-1>', lambda x: self.hintEvent(event=age))
        inputList[2].bind('<Button-1>', lambda x: self.hintEvent(event=id))
        inputList[3].bind('<Button-1>', lambda x: self.hintEvent(event=pw))
        inputList[4].bind('<Button-1>', lambda x: self.hintEvent(event=pw_check))
        inputList[5].bind('<Button-1>', lambda x: self.hintEvent(event=zipcode))
        inputList[6].bind('<Button-1>', lambda x: self.hintEvent(event=call_number))
        inputList[7].bind('<Button-1>', lambda x: self.hintEvent(event=introduce))
        # 탭으로 들어올때 이벤트
        inputList[0].bind('<FocusIn>', lambda x: self.hintEvent(event=name))
        inputList[1].bind('<FocusIn>', lambda x: self.hintEvent(event=age))
        inputList[2].bind('<FocusIn>', lambda x: self.hintEvent(event=id))
        inputList[3].bind('<FocusIn>', lambda x: self.hintEvent(event=pw))
        inputList[4].bind('<FocusIn>', lambda x: self.hintEvent(event=pw_check))
        inputList[5].bind('<FocusIn>', lambda x: self.hintEvent(event=zipcode))
        inputList[6].bind('<FocusIn>', lambda x: self.hintEvent(event=call_number))
        inputList[7].bind('<FocusIn>', lambda x: self.hintEvent(event=introduce))

        # 화면넣기
        inputFrame.place(x=290, y=80)
        inputList[0].pack(pady=5,anchor='w')
        inputList[1].pack(pady=5,anchor='w')
        inputList[2].pack(pady=5,anchor='w')
        inputList[3].pack(pady=5,anchor='w')
        inputList[4].pack(pady=5,anchor='w')
        inputList[5].pack(pady=5,anchor='w')
        inputList[6].pack(pady=5,anchor='w')
        inputList[7].pack(pady=5,anchor='w')
        gender_w.pack(pady=5, anchor ='w')
        gender_m.place(x=60, y=429)
        photo.place(x=40,y=90)
        sign_up_btn.place(x=65,y=330)
        cancel_btn.place(x=65,y=385)
        logo.place(x=5, y=5)
        self.play()

    def hintEvent(self,event):  # 눌렀을때 글자 넣을수 있게
        event.config(fg='black')
        event.delete(0,END)
        
    def signUpEvent(self):
        # 회원가입 버튼 눌렀을때
        # 아이디 중복 체크
        # 형식 체크
        # 비번 확인 체크
        pass
    
    def cancelEvent(self):
        # 취소 - 시작화면으로 이동
        pass

    def play(self):
        self.root.mainloop()

if __name__ == '__main__':
    SignUp('회원가입')

