from tkinter import *

from _Adoption_book import Adoption_book
from adieu_main import adieuMain
from user_info import UserInfo


class EditUserInfo():
    def __init__(self, title):
        text_color = '#B96F00'
        bg_color = '#FFC978'  # 배경색
        bd_relief = "flat"     # 테두리 타입
        engien = Adoption_book()
        userInfo, userId= engien.get_user_info('nowuser')
        
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
        edit_btn = Button(self.root, cursor='hand2', width=16, text='정보수정', command=self.subscriptionEvent, bg='#F0AD48', relief='flat', bd=10,
                             fg=text_color)  # 회원가입 버튼
        cancel_btn = Button(self.root, cursor='hand2', width=16, text='취소', command=self.cancelEvent, bg='#F0AD48', relief='flat', bd=10,
                            fg=text_color)  # 취소 버튼

        # 입력받기
        inputFrame = Frame(self.root, bg=bg_color, width=430, height=400)
        name = Entry(inputFrame, width=20, relief=bd_relief, bd=13, fg="gray")
        age = Entry(inputFrame, width=25, relief=bd_relief, bd=13, fg="gray")
        id = Entry(inputFrame, width=25, relief=bd_relief, bd=13, fg="gray")
        pw = Entry(inputFrame, width=30, relief=bd_relief, bd=13, fg="gray")
        pw_check = Entry(inputFrame, width=30, relief=bd_relief, bd=13, fg="gray")
        zipcode = Entry(inputFrame, width=30, relief=bd_relief, bd=13, fg="gray")
        call_number = Entry(inputFrame, width=40, relief=bd_relief, bd=13, fg="gray")
        introduce = Entry(inputFrame, width=40, relief=bd_relief, bd=13, fg="gray")
        inputList = [name, age, id, pw, pw_check, zipcode, call_number, introduce]  # 입력 받을 리스트

        # hint
        inputList[0].insert(0, userInfo['name'])
        inputList[1].insert(0, userInfo['age'])
        inputList[2].insert(0, userId)
        inputList[3].insert(0, userInfo['pw'])
        inputList[4].insert(0, userInfo['pw'])
        inputList[5].insert(0, userInfo['zip_code'])
        inputList[6].insert(0, userInfo['call_number'])
        inputList[7].insert(0, userInfo['introduce'])

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
        name.pack(pady=5, anchor='w')
        age.pack(pady=5, anchor='w')
        id.pack(pady=5, anchor='w')
        pw.pack(pady=5, anchor='w')
        pw_check.pack(pady=5, anchor='w')
        zipcode.pack(pady=5, anchor='w')
        call_number.pack(pady=5, anchor='w')
        introduce.pack(pady=5, anchor='w')
        photo.place(x=40, y=90)
        edit_btn.place(x=65, y=330)
        cancel_btn.place(x=65, y=385)
        logo.place(x=5, y=5)
        self.play()

    def hintEvent(self, event):  # 눌렀을때 글자 넣을수 있게
        event.config(fg='black')
        event.delete(0, END)

    def signUpEvent(self):
        # 회원가입 버튼 눌렀을때
        # 아이디 중복 체크
        # 형식 체크
        # 비번 확인 체크
        pass

    def subscriptionEvent(self):
        # 수정 - 사용자 정보 볁경 후 시작화면으로 이동
        pass

    def cancelEvent(self):
        # 취소 - 시작화면으로 이동
        self.root.destroy()
        adieuMain("메인")

    def play(self):
        self.root.mainloop()


if __name__ == '__main__':
    EditUserInfo('사용자 정보 수정화면')

