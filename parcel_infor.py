from tkinter import *
from tkinter import messagebox

from _Adoption_book import Adoption_book
from adieu_main import adieuMain

class ParceAdieuInfor():
    def __init__(self, title, selecanimal): # 타이틀, 선택한동물이름
        self.engien = Adoption_book()
        self.thisAnimal = selecanimal
        self.ParceInfoGUI(title)

    def ParceInfoGUI(self, title):
        self.TEXTCOLOR = 'black'
        self.BGCOLOR = '#FFC978'  # 배경색
        self.root = Tk()
        self.root.title(title)
        self.root.geometry('745x580')
        self.root.configure(bg=self.BGCOLOR)
        self.root.resizable(0, 0)

        # 프레임 설정
        self.mainFrame = Frame(self.root, bg=self.BGCOLOR)
        self.mainFrame.pack(expand=True)

        # logo 설정
        logo_img = PhotoImage(file='img/Adieu.png', width=200, height=87)
        logo = Label(self.root, bg=self.BGCOLOR, image=logo_img)

        photo_img = PhotoImage(file='img/animal_img.png', width=300, height=230)
        photo = Label(self.root, bg=self.BGCOLOR, image=photo_img)
        # button 설정
        btn_sub = Button(self.root, width=13, text='분양신청', bg='#F0AD48', command=self.subscriptionEvent, relief='flat', bd=10, fg='#B96F00')
        
        # 정보 화면
        inputFrame1 = Frame(self.root, bg=self.BGCOLOR, width=380, height=400)
        inputFrame2 = Frame(self.root, bg=self.BGCOLOR, width=100, height=200)
        name = Label(inputFrame1, width=15, relief="flat", bd=13, fg=self.TEXTCOLOR)
        species = Label(inputFrame1, width=15, relief="flat", bd=13, fg=self.TEXTCOLOR)
        age = Label(inputFrame1, width=15, relief="flat", bd=13, fg=self.TEXTCOLOR)
        gender = Label(inputFrame1, width=15, relief="flat", bd=13, fg=self.TEXTCOLOR)
        add_infor = Label(inputFrame2, width=52, relief="flat", bd=13, fg=self.TEXTCOLOR)
        user_infor = Label(inputFrame2, width=35, relief="flat", bd=13, fg=self.TEXTCOLOR)
        inputList = [name, species, age, gender, add_infor, user_infor]  # 입력 받을 리스트

        self.draw_info(inputList)

        # 화면에 출력
        inputFrame1.place(x=360, y=80)
        inputFrame2.place(x=90, y=340)
        logo.place(x=10, y=5)
        photo.place(x=100, y=90)
        btn_sub.place(x=540, y=500)
        name.pack(padx=15, pady=10, anchor='w')
        species.pack(padx=15, pady=10, anchor='w')
        age.pack(padx=15, pady=10, anchor='w')
        gender.pack(padx=15, pady=5, anchor='w')
        add_infor.pack(padx=10, pady=5, anchor='w')
        user_infor.pack(padx=10, pady=5, anchor='w')
        self.play()

    def draw_info(self, list):  # gui 정보넣을 라벨 리스트
        # 정보가져오기
        # [name, species, age, gender, add_infor, user_infor] 순서대로
        info = self.engien.get_animal_info(self.thisAnimal)
        keys = ['','species','pat_age','user','pat_gender','pat_etc']

        list[0].config('text', self.thisAnimal) # 처음엔 이름넣기

        # 뿌리기
        for i in range(1,list):
            list[i].config('text',info[keys[i]])


    def subscriptionEvent(self):
        result = self.engien.put_animals(self.thisAnimal)
        if result==False:
            messagebox.showerror('입양신청오류', '입양신청 실패')
            return
        messagebox.showinfo()('신청완료', f'빈려동물 {self.thisAnimal} 입양신청되었습니다.')
        self.root.destroy()
        adieuMain("메인")       # 분양신청 후 페이지로 넘어감

    def play(self):
        self.root.mainloop()


if __name__ == '__main__':
    ParceAdieuInfor('게시물 정보 및 분양 신청')