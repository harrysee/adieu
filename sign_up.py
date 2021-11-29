import tkinter.messagebox
from tkinter import *
from tkinter import messagebox
from _Adoption_book import Adoption_book as adoption_engien

class SignUp():
    def __init__(self, title):
        self.draw_GUI(title)
        self.inputList= []
        self.engien = adoption_engien()

    def draw_GUI(self,title):
        bg_color = '#FFC978'  # 배경색
        self.root = Tk()
        self.root.title(title)
        self.root.geometry('745x580+400+100')
        self.root.configure(bg=bg_color)
        self.root.resizable(0, 0)
        # 왼쪽 사이드
        logo_img = PhotoImage(file='img/Adieu.png', width=182, height=87)
        logo = Label(self.root, bg=bg_color, image=logo_img)  # 로고
        photo_img = PhotoImage(file='img/input_img.png')
        photo = Label(self.root, image=photo_img, bg=bg_color, anchor="w")  # 이미지 넣기 왼쪽 정렬
        sign_up_btn = Button(self.root, cursor='hand2', width=16, text='회원가입', bg='#F0AD48',command=self.signUpEvent, relief='flat', bd=10,
                             fg='#B96F00')  # 회원가입 버튼
        cancel_btn = Button(self.root, cursor='hand2', width=16, text='취소', bg='#F0AD48', relief='flat', bd=10, command=self.cancelEvent,
                            fg='#B96F00')  # 취소 버튼

        # 입력받기
        inputFrame = Frame(self.root, bg=bg_color, width=430, height=400)
        name = Entry(inputFrame, width=20, relief="flat", bd=13, fg="gray")
        age = Entry(inputFrame, width=25, relief="flat", bd=13, fg="gray")
        id = Entry(inputFrame, width=25, relief="flat", bd=13, fg="gray")
        pw = Entry(inputFrame, width=30, relief="flat", bd=13, fg="gray")
        pw_check = Entry(inputFrame, width=30, relief="flat", bd=13, fg="gray")
        zipcode = Entry(inputFrame, width=30, relief="flat", bd=13, fg="gray")
        call_number = Entry(inputFrame, width=40, relief="flat", bd=13, fg="gray")
        introduce = Entry(inputFrame, width=40, relief="flat", bd=13, fg="gray")
        self.gender_var = IntVar()  # 여기에 int 형으로 값을 저장한다
        gender_w = Radiobutton(inputFrame, text="여자", value=1, variable=self.gender_var, bg=bg_color)
        gender_m = Radiobutton(inputFrame, text="남자", value=2, variable=self.gender_var, bg=bg_color)
        gender_w.select()  # 기본적으로 여자 선택
        self.inputList = [name, age, id, pw, pw_check, zipcode, call_number, introduce]  # 입력 받을 리스트

        # hint
        self.inputList[0].insert(0, '이름')
        self.inputList[1].insert(0, '나이')
        self.inputList[2].insert(0, 'ID')
        self.inputList[3].insert(0, 'PW')
        self.inputList[4].insert(0, 'PW 확인')
        self.inputList[5].insert(0, '집주소')
        self.inputList[6].insert(0, '전화번호')
        self.inputList[7].insert(0, '소개')

        # hint 이벤트
        self.inputList[0].bind('<Button-1>', lambda x: self.hintEvent(event=name))
        self.inputList[1].bind('<Button-1>', lambda x: self.hintEvent(event=age))
        self.inputList[2].bind('<Button-1>', lambda x: self.hintEvent(event=id))
        self.inputList[3].bind('<Button-1>', lambda x: self.hintEvent(event=pw))
        self.inputList[4].bind('<Button-1>', lambda x: self.hintEvent(event=pw_check))
        self.inputList[5].bind('<Button-1>', lambda x: self.hintEvent(event=zipcode))
        self.inputList[6].bind('<Button-1>', lambda x: self.hintEvent(event=call_number))
        self.inputList[7].bind('<Button-1>', lambda x: self.hintEvent(event=introduce))
        # 탭으로 들어올때 이벤트
        self.inputList[0].bind('<FocusIn>', lambda x: self.hintEvent(event=name))
        self.inputList[1].bind('<FocusIn>', lambda x: self.hintEvent(event=age))
        self.inputList[2].bind('<FocusIn>', lambda x: self.hintEvent(event=id))
        self.inputList[3].bind('<FocusIn>', lambda x: self.hintEvent(event=pw))
        self.inputList[4].bind('<FocusIn>', lambda x: self.hintEvent(event=pw_check))
        self.inputList[5].bind('<FocusIn>', lambda x: self.hintEvent(event=zipcode))
        self.inputList[6].bind('<FocusIn>', lambda x: self.hintEvent(event=call_number))
        self.inputList[7].bind('<FocusIn>', lambda x: self.hintEvent(event=introduce))

        # 화면넣기
        inputFrame.place(x=290, y=80)
        self.inputList[0].pack(pady=5, anchor='w')
        self.inputList[1].pack(pady=5, anchor='w')
        self.inputList[2].pack(pady=5, anchor='w')
        self.inputList[3].pack(pady=5, anchor='w')
        self.inputList[4].pack(pady=5, anchor='w')
        self.inputList[5].pack(pady=5, anchor='w')
        self.inputList[6].pack(pady=5, anchor='w')
        self.inputList[7].pack(pady=5, anchor='w')
        gender_w.pack(pady=5, anchor='w')
        gender_m.place(x=60, y=429)
        photo.place(x=40, y=90)
        sign_up_btn.place(x=65, y=330)
        cancel_btn.place(x=65, y=385)
        logo.place(x=5, y=5)
        self.play()

    def hintEvent(self,event):  # 눌렀을때 글자 넣을수 있게
        if event.get() in ('PW','PW 확인'): event.config(show='●')
        event.config(fg='black')
        event.delete(0,END)
        
    def signUpEvent(self):
        # 회원가입 버튼 눌렀을때
        engien = adoption_engien()
        print(self.inputList[0]['foreground'])
        for info in self.inputList:
            if info['foreground']!='black':
                messagebox.showinfo("입력오류",info.get()+" 입력하시오.")
                return
        message = engien.sign_up(self.inputList, self.gender_var)
        if message != True:
            messagebox.showerror("오류", message)  # 회원가입이 성공적으로 안되면 이유 리턴
            return
        messagebox.showinfo("안내","회원가입 완료!!")
        self.cancelEvent()
        # 아이디 중복 체크
        # 형식 체크
        # 비번 확인 체크

    def cancelEvent(self):
        # 취소 - 시작화면으로 이동
        from start import StartAdieu
        self.root.destroy()
        StartAdieu("시작화면")

    def play(self):
        self.root.mainloop()

if __name__ == '__main__':
    SignUp('회원가입')
