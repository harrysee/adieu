from tkinter import *
from adieu_main import adieuMain

class ParceAdieuEdit():
    def __init__(self, title):
        bg_color = '#FFC978'  # 배경색
        self.root = Tk()
        self.root.title(title)
        self.root.geometry('745x580')
        self.root.configure(bg=bg_color)
        self.root.resizable(0, 0)

        # 프레임 설정
        self.mainFrame = Frame(self.root, bg=bg_color)
        self.mainFrame.pack(expand=True)

        # logo 설정
        logo_img = PhotoImage(file='img/Adieu.png', width=200, height=87)
        logo = Label(self.root, bg=bg_color, image=logo_img)

        photo = Frame(self.root, bg='#F0AD48', width=300, height=230)
        # button 설정
        btn_update = Button(self.root, width=10, text='수정', bg='#F0AD48', command=self.subscriptionEvent, relief='flat', bd=10, fg='#B96F00')
        btn_back = Button(self.root, width=10, text='취소', bg='#F0AD48', command=self.subscriptionEvent, relief='flat', bd=10, fg='#B96F00')

        # 입력받기
        inputFrame1 = Frame(self.root, bg=bg_color, width=330, height=400)
        inputFrame2 = Frame(self.root, bg=bg_color, width=100, height=200)
        name = Entry(inputFrame1, width=15, relief="flat", bd=13, fg="gray")
        species = Entry(inputFrame1, width=15, relief="flat", bd=13, fg="gray")
        age = Entry(inputFrame1, width=15, relief="flat", bd=13, fg="gray")
        place = Entry(inputFrame1, width=15, relief="flat", bd=13, fg="gray")
        add_infor = Entry(inputFrame2, width=52, relief="flat", bd=13, fg="gray")
        user_infor = Entry(inputFrame2, width=35, relief="flat", bd=13, fg="gray")
        inputList = [name, species, age, place, add_infor, user_infor]  # 입력 받을 리스트

        # hint
        inputList[0].insert(0, '이름')
        inputList[1].insert(0, '종류')
        inputList[2].insert(0, '나이')
        inputList[3].insert(0, '장소')
        inputList[4].insert(0, '추가설명')
        inputList[5].insert(0, '사용자 정보')

        # hint 이벤트
        inputList[0].bind('<Button-1>', lambda x: self.hintEvent(event=name))
        inputList[1].bind('<Button-1>', lambda x: self.hintEvent(event=species))
        inputList[2].bind('<Button-1>', lambda x: self.hintEvent(event=age))
        inputList[3].bind('<Button-1>', lambda x: self.hintEvent(event=place))
        inputList[4].bind('<Button-1>', lambda x: self.hintEvent(event=add_infor))
        inputList[5].bind('<Button-1>', lambda x: self.hintEvent(event=user_infor))

        # tab 이벤트
        inputList[0].bind('<FocusIn>', lambda x: self.hintEvent(event=name))
        inputList[1].bind('<FocusIn>', lambda x: self.hintEvent(event=species))
        inputList[2].bind('<FocusIn>', lambda x: self.hintEvent(event=age))
        inputList[3].bind('<FocusIn>', lambda x: self.hintEvent(event=place))
        inputList[4].bind('<FocusIn>', lambda x: self.hintEvent(event=add_infor))
        inputList[5].bind('<FocusIn>', lambda x: self.hintEvent(event=user_infor))

        # 화면에 출력
        inputFrame1.place(x=360, y=80)
        inputFrame2.place(x=90, y=340)
        logo.place(x=10, y=5)
        photo.place(x=100, y=90)
        btn_update.place(x=470, y=500)
        btn_back.place(x=590, y=500)
        name.pack(padx=15, pady=10, anchor='w')
        species.pack(padx=15, pady=10, anchor='w')
        age.pack(padx=15, pady=10, anchor='w')
        place.pack(padx=15, pady=5, anchor='w')
        add_infor.pack(padx=10, pady=5, anchor='w')
        user_infor.pack(padx=10, pady=5, anchor='w')
        self.play()

    def subscriptionEvent(self):
        self.root.destroy()
        adieuMain("분양신청")

    # 클릭 시 입력
    def hintEvent(self,event):  # 눌렀을때 글자 넣을수 있게
        event.config(fg='black')
        event.delete(0,END)

    def play(self):
        self.root.mainloop()


if __name__ == '__main__':
    ParceAdieuEdit('분양신청')