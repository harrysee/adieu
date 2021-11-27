from tkinter import *
from tkinter import messagebox

from _Adoption_book import Adoption_book
from adieu_main import adieuMain
from parcel_add import ParceAdieuAdd
from seller_info import SellerInfo
from user_info import UserInfo


class ParcelUpdate():
    def __init__(self, title):
        self.engien = Adoption_book()
        self.parcelUpdateGUI(title)
        self.seller = []

    def parcelUpdateGUI(self, title, seller):
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
        btn_update = Button(self.root, width=10, text='수정', bg='#F0AD48', command=self.updateEvent, relief='flat', bd=10, fg='#B96F00')
        btn_back = Button(self.root, width=10, text='취소', bg='#F0AD48', command=self.cancelEvent, relief='flat', bd=10, fg='#B96F00')

        # 입력받기
        inputFrame1 = Frame(self.root, bg=bg_color, width=330, height=400)
        inputFrame2 = Frame(self.root, bg=bg_color, width=100, height=200)
        name = Label(inputFrame1, width=15, relief="flat", bd=13, fg="gray", text="이름")
        species = Entry(inputFrame1, width=15, relief="flat", bd=13, fg="gray")
        age = Entry(inputFrame1, width=15, relief="flat", bd=13, fg="gray")
        place = Entry(inputFrame1, width=15, relief="flat", bd=13, fg="gray")
        add_infor = Entry(inputFrame2, width=52, relief="flat", bd=13, fg="gray")
        user_infor = Entry(inputFrame2, width=35, relief="flat", bd=13, fg="gray")
        self.inputList = [name, species, age, place, add_infor, user_infor]  # 입력 받을 리스트

        # hint
        self.inputList[1].insert(0, '종류')
        self.inputList[2].insert(0, '나이')
        self.inputList[3].insert(0, '장소')
        self.inputList[4].insert(0, '추가설명')
        self.inputList[5].insert(0, '사용자 정보')

        # hint 이벤트
        self.inputList[1].bind('<Button-1>', lambda x: self.hintEvent(event=species))
        self.inputList[2].bind('<Button-1>', lambda x: self.hintEvent(event=age))
        self.inputList[3].bind('<Button-1>', lambda x: self.hintEvent(event=place))
        self.inputList[4].bind('<Button-1>', lambda x: self.hintEvent(event=add_infor))

        # tab 이벤트
        self.inputList[1].bind('<FocusIn>', lambda x: self.hintEvent(event=species))
        self.inputList[2].bind('<FocusIn>', lambda x: self.hintEvent(event=age))
        self.inputList[3].bind('<FocusIn>', lambda x: self.hintEvent(event=place))
        self.inputList[4].bind('<FocusIn>', lambda x: self.hintEvent(event=add_infor))

        # 화면에 출력
        inputFrame1.place(x=300, y=80)
        inputFrame2.place(x=90, y=300)
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

        # 분양자 버튼 생성
        seller_btn = {}

        for i, d in enumerate(self.seller):
            btn = Button(self.root, padx=60, text=i, pady=10, fg='#B96F00', bg='#F0AD48', command=lambda x=i: self.sellerEvent(x))
            btn.grid(row=i, column=0)
            seller_btn[i] = btn

        seller_btn.pack(x=580, y=15)

        self.play()

    def draw_info(self, list):  # gui 정보넣을 라벨 리스트
        # 정보가져오기
        # [name, species, age, gender, add_infor, user_infor] 순서대로
        info = self.engien.get_animal_info(self.thisAnimal)
        keys = ['','species','pat_age','user','pat_gender','pat_etc']

        list[0].config('text', self.thisAnimal) # 처음엔 이름넣기

        # 뿌리기
        for i in range(1, list):
            list[i].config('text', info[keys[i]])

        # 분양신청자 id 가져오기
        apply_list = list(info['apply_users'])

        for i in apply_list:
            self.seller.append(i)

    # 클릭 시 분양자 정보 이동
    def sellerEvent(self, id):
        self.root.destroy()
        SellerInfo("분양자 정보", userid=id)

        # 분양자 리스트에서서 삭제
        self.seller.remove(id)

    def updateEvent(self):
        # 수정 클릭 시 메인화면
        self.root.destroy()

        for info in self.inputList:
            if info['foreground']!='black': # 입력 안되엇을경우
                messagebox.showinfo("입력오류", info.get()+" 입력하시오.")
                return
        message = self.engien.sign_up(self.inputList, self.gender_var)
        if message != True:
            messagebox.showinfo("오류", message)  # 등록이 성공적으로 안되면 이유 리턴
            return
        messagebox.showinfo("안내", "게시물 수정 완료!!")
        adieuMain("메인화면")


    def cancelEvent(self):
        # 취소 클릭 시 사용자화면
        self.root.destroy()
        UserInfo("사용자정보")

    # 클릭 시 입력
    def hintEvent(self, event):  # 눌렀을때 글자 넣을수 있게
        event.config(fg='black')
        event.delete(0,END)

    def play(self):
        self.root.mainloop()


if __name__ == '__main__':
    ParceAdieuEdit('분양수정 및 분양자 확인')