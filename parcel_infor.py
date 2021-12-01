from tkinter import *
from tkinter import messagebox

from _Adoption_book import Adoption_book


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
        self.root.geometry('745x580+400+100')
        self.root.configure(bg=self.BGCOLOR)
        self.root.resizable(0, 0)

        # 프레임 설정
        self.mainFrame = Frame(self.root, bg=self.BGCOLOR)
        self.mainFrame.pack(expand=True)


        # logo 설정
        logo_img = PhotoImage(file='img/Adieu.png', width=200, height=87)
        logo = Label(self.root, bg=self.BGCOLOR, image=logo_img,cursor='hand2')
        logo.bind('<Button-1>',self.moveMain)

        photo_img = PhotoImage(file='img/animal_img.png')
        photo = Label(self.root, image=photo_img, bg=self.BGCOLOR, anchor="w")  # 이미지 넣기 왼쪽 정렬
        # button 설정
        btn_sub = Button(self.root, width=13, text='분양신청', bg='#F0AD48', command=self.subscriptionEvent, relief='flat', bd=10, fg='#B96F00')

        # 정보 화면
        infoFrame1 = Frame(self.root, bg=self.BGCOLOR, width=350, height=400)
        infoFrame2 = Frame(self.root, bg=self.BGCOLOR, width=100, height=200)
        inputFrame1 = Frame(self.root, bg=self.BGCOLOR, width=430, height=400)
        inputFrame2 = Frame(self.root, bg=self.BGCOLOR, width=100, height=200)
        name = Label(inputFrame1, width=15, relief="flat", bd=13, fg=self.TEXTCOLOR)
        gender = Label(inputFrame1, width=15, relief="flat", bd=13, fg=self.TEXTCOLOR)
        age = Label(inputFrame1, width=15, relief="flat", bd=13, fg=self.TEXTCOLOR)
        place = Label(inputFrame1, width=15, relief="flat", bd=13, fg=self.TEXTCOLOR)
        add_infor = Label(inputFrame2, width=52, relief="flat", bd=13, fg=self.TEXTCOLOR)
        user_infor = Label(inputFrame2, width=35, relief="flat", bd=13, fg=self.TEXTCOLOR)
        spaceies = Label(inputFrame2, width=15, relief="flat", bd=13, fg=self.TEXTCOLOR)
        inputList = [name, gender, age, place, add_infor, user_infor,spaceies]  # 입력 받을 리스트

        self.draw_info(inputList)       # 해당 동물 정보 보여주기

        # 화면에 출력    ------------------------
        infoFrame1.place(x=380, y=80)
        inputFrame1.place(x=460, y=80)
        infoFrame2.place(x=50, y=340)
        inputFrame2.place(x=150, y=340)
        logo.place(x=10, y=5)
        photo.place(x=100, y=90)
        btn_sub.place(x=540, y=500)

        # input 박스 타이틀
        info1 = ['이름', '성별', '나이', '장소']
        info2 = ['세부설명', '게시물 작성자', '종류']

        for i, d in enumerate(info1):   # 왼쪽 수직 타이틀 텍스트 보여주기
            text = Label(infoFrame1, bg=self.BGCOLOR, width=10, text=d, fg='#333')
            text.pack(padx=10, pady=20)

        name.pack(padx=15, pady=10, anchor='w')
        gender.pack(padx=15, pady=10, anchor='w')
        age.pack(padx=15, pady=10, anchor='w')
        place.pack(padx=15, pady=5, anchor='w')

        for i, d in enumerate(info2): # 하단 수평 타이틀 텍스트 보여주기
            text = Label(infoFrame2, bg=self.BGCOLOR, width=10, text=d, fg='#333')
            text.pack(padx=10, pady=15)

        add_infor.pack(padx=10, pady=5, anchor='w')
        user_infor.pack(padx=10, pady=5, anchor='w')
        spaceies.pack(padx=10, pady=5, anchor='w')
        self.play()

    def moveMain(self,e):
        self.root.destroy()
        from adieu_main import adieuMain
        adieuMain("메인")

    def draw_info(self, list):  # gui 정보넣을 라벨 리스트
        # 정보가져오기
        # [name, species, age, gender, add_infor, user_infor] 순서대로
        print(self.thisAnimal)
        info = self.engien.get_animal_info(self.thisAnimal)
        list[0].configure(text=self.thisAnimal)     # 처음엔 이름넣기

        # 뿌리기
        for i in range(1,len(list)):
            list[i].configure(text=info[i-1])

    def subscriptionEvent(self):
        result = self.engien.put_animals(self.thisAnimal)
        if result==False:
            messagebox.showerror('입양신청오류', '입양신청 실패')
            return
        messagebox.showinfo('신청완료', f'빈려동물 {self.thisAnimal} 입양신청되었습니다.')

        self.root.destroy()
        from adieu_main import adieuMain
        adieuMain("메인")       # 분양신청 후 페이지로 넘어감

    def play(self):
        self.root.mainloop()

if __name__ == '__main__':
    ParceAdieuInfor('게시물 정보 및 분양 신청','dd')