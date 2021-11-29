from tkinter import *
from tkinter import messagebox

from _Adoption_book import Adoption_book
from adieu_main import adieuMain
from user_info import UserInfo


class EditUserInfo():
    def __init__(self, title):
        self.engien = Adoption_book()
        text_color = '#B96F00'
        bg_color = '#FFC978'  # 배경색
        bd_relief = "flat"     # 테두리 타입
        engien = Adoption_book()
        userInfo, userId= engien.get_user_info('nowuser')
        
        self.root = Tk()
        self.root.title(title)
        self.root.geometry('745x580+400+100')
        self.root.configure(bg=bg_color)
        self.root.resizable(0, 0)
        # 왼쪽 사이드
        logo_img = PhotoImage(file='img/Adieu.png', width=182, height=87)
        logo = Label(self.root, bg=bg_color, image=logo_img, cursor='hand2')  # 로고
        logo.bind('<Button-1>',self.moveMain)


        photo_img = PhotoImage(file='img/input_img.png')
        photo = Label(self.root, image=photo_img, bg=bg_color, anchor="w")  # 이미지 넣기 왼쪽 정렬
        edit_btn = Button(self.root, cursor='hand2', width=16, text='정보수정', command=self.updateEvent, bg='#F0AD48', relief='flat', bd=10,
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
        self.gender_var = IntVar()  # 여기에 int 형으로 값을 저장한다
        gender_w = Radiobutton(inputFrame, text="여자", value=1, variable=self.gender_var, bg=bg_color)
        gender_m = Radiobutton(inputFrame, text="남자", value=2, variable=self.gender_var, bg=bg_color)
        gender_w.select()  # 기본적으로 여자 선택
        self.inputList = [name, age, id, pw, pw_check, zipcode, call_number, introduce]  # 입력 받을 리스트

        # hint
        self.inputList[0].insert(0, userInfo['name'])
        self.inputList[1].insert(0, userInfo['age'])
        self.inputList[2].insert(0, userId)
        self.inputList[3].insert(0, userInfo['pw'])
        self.inputList[4].insert(0, userInfo['pw'])
        self.inputList[5].insert(0, userInfo['zip_code'])
        self.inputList[6].insert(0, userInfo['call_number'])
        self.inputList[7].insert(0, userInfo['introduce'])

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

    def moveMain(self,evnet):
        self.root.destroy()
        from adieu_main import adieuMain
        adieuMain("메인")

    def hintEvent(self, event):  # 눌렀을때 글자 넣을수 있게
        event.config(fg='black')
        event.delete(0, END)

    def updateEvent(self):
        self.engien.sign_up(self.inputList, self.gender_var)
        messagebox.showinfo('안내', '정보수정 완료')
        self.root.destroy()
        UserInfo('사용자 정보')

    def cancelEvent(self):
        # 취소 - 시작화면으로 이동
        self.root.destroy()
        adieuMain("메인")

    def play(self):
        self.root.mainloop()


if __name__ == '__main__':
    EditUserInfo('사용자 정보 수정화면')

