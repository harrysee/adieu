from tkinter import *
from tkinter import messagebox

from _Adoption_book import Adoption_book
from adieu_main import adieuMain
from seller_info import SellerInfo
from user_info import UserInfo

class ParcelUpdate():
    def __init__(self, title, selec):
        self.engien = Adoption_book()
        self.thisAnimal = self.engien.get_animal_info(selec)
        self.animalkey = selec
        self.parcelUpdateGUI(title,selec)
        self.seller = []        # 분양자들 이름 리스트

    def parcelUpdateGUI(self, title,selec):
        bg_color = '#FFC978'  # 배경색
        self.root = Tk()
        self.root.title(title)
        self.root.geometry('745x580+400+100')
        self.root.configure(bg=bg_color)
        self.root.resizable(0, 0)

        # 기존 정보 가져오기
        self.inputList = self.thisAnimal

        # 프레임 설정
        self.mainFrame = Frame(self.root, bg=bg_color)
        self.mainFrame.pack(expand=True)
        self.sellerFrame = LabelFrame(self.root, bg = bg_color,padx=5, labelanchor='n', width=100, height=400, text='신청한 사용자')

        # 객체 설명
        info1 = ['이름', '나이', '장소', '성별']
        info2 = ['세부설명', '종류']

        # logo 설정
        logo_img = PhotoImage(file='img/Adieu.png', width=200, height=87)
        logo = Label(self.root, bg=bg_color, image=logo_img,cursor='hand2')
        logo.bind('<Button-1>',self.moveMain)

        # 동물 타이틀 이미지 넣기
        photo_img = PhotoImage(file='img/animal_img.png')
        photo = Label(self.root, image=photo_img, bg=bg_color, anchor="w")  # 이미지 넣기 왼쪽 정렬
        # button 설정
        btn_update = Button(self.root, width=10, text='수정', bg='#F0AD48', command=self.updateEvent, relief='flat', bd=10, fg='#B96F00')
        btn_back = Button(self.root, width=10, text='삭제', bg='#F0AD48', command=self.deleteEvent, relief='flat', bd=10, fg='#B96F00')

        # 입력받기
        infoFrame1 = Frame(self.root, bg=bg_color, width=350, height=400)
        infoFrame2 = Frame(self.root, bg=bg_color, width=100, height=200)
        inputFrame1 = Frame(self.root, bg=bg_color, width=330, height=400)
        inputFrame2 = Frame(self.root, bg=bg_color, width=100, height=200)
        name = Label(inputFrame1, width=15, relief="flat", bd=13, fg="gray")
        age = Entry(inputFrame1, width=15, relief="flat", bd=13, fg="gray")
        place = Entry(inputFrame1, width=15, relief="flat", bd=13, fg="gray")
        add_infor = Entry(inputFrame2, width=52, relief="flat", bd=13, fg="gray")
        self.gender_ani = IntVar()  # 여기에 int 형으로 값을 저장한다
        gender_w = Radiobutton(self.root, text="암컷", value=1, variable=self.gender_ani, bg=bg_color)
        gender_m = Radiobutton(self.root, text="수컷", value=2, variable=self.gender_ani, bg=bg_color)
        self.species_var = IntVar()     # 동물 종류 입력받을 var
        species_0 = Radiobutton(self.root, text="고양이", value=0, variable=self.species_var, bg=bg_color)
        species_1 = Radiobutton(self.root, text="강아지", value=1, variable=self.species_var, bg=bg_color)
        species_2 = Radiobutton(self.root, text="새", value=2, variable=self.species_var, bg=bg_color)
        species_3 = Radiobutton(self.root, text="기타", value=3, variable=self.species_var, bg=bg_color)
        spacelist = [(species_0,species_1,species_2,species_3),(gender_m,gender_w)]
        self.inputList = [name, age, place, add_infor]  # 입력 받을 리스트 # 입력 받을 리스트
        
        # 미리 힌트로 데이터 세팅
        self.draw_info(self.inputList, spacelist,selec)

        self.inputList[1].bind('<Button-1>', lambda x: self.hintEvent(event=age))
        self.inputList[2].bind('<Button-1>', lambda x: self.hintEvent(event=place))
        self.inputList[3].bind('<Button-1>', lambda x: self.hintEvent(event=add_infor))

        # tab 이벤트
        self.inputList[1].bind('<FocusIn>', lambda x: self.hintEvent(event=age))
        self.inputList[2].bind('<FocusIn>', lambda x: self.hintEvent(event=place))
        self.inputList[3].bind('<FocusIn>', lambda x: self.hintEvent(event=add_infor))

        # input 받아야하는 엔트리 타이틀 달기
        for i, d in enumerate(info1):   # 오른쪽 부분
            text = Label(infoFrame1, bg=bg_color, width=10, text=d, fg='#333')
            text.pack(padx=10, pady=20)

        for i, d in enumerate(info2):   # 밑에부분
            text = Label(infoFrame2, bg=bg_color, width=10, text=d, fg='#333')
            text.pack(padx=10, pady=16)

        # 화면에 출력
        self.sellerFrame.place(x=640,y=60)
        name.pack(padx=15, pady=10, anchor='w')
        gender_w.place(x=410, y=290, anchor='w')
        gender_m.place(x=470, y=290, anchor='w')
        age.pack(padx=15, pady=10, anchor='w')
        place.pack(padx=15, pady=5, anchor='w')
        add_infor.pack(padx=10, pady=5, anchor='w')
        species_0.place(x=160, y=420, anchor='w')
        species_1.place(x=240, y=420, anchor='w')
        species_2.place(x=310, y=420, anchor='w')
        species_3.place(x=360, y=420, anchor='w')
        infoFrame1.place(x=380, y=80)
        inputFrame1.place(x=460, y=80)
        infoFrame2.place(x=50, y=340)
        inputFrame2.place(x=150, y=340)
        logo.place(x=10, y=5)
        photo.place(x=100, y=90)
        btn_update.place(x=470, y=500)
        btn_back.place(x=590, y=500)

        self.play()

    def moveMain(self,e):
        self.root.destroy()
        from adieu_main import adieuMain
        adieuMain("메인")

    def draw_info(self, list, field, selec):  # gui에 저장된 게시물 미리 세팅하기 (entry리스트, [종류튜플, 성별튜플], 선택한 동물)
        # 정보가져오기
        # [name, species, age, gender, add_infor, user_infor] 순서대로
        info = self.engien.get_animal_info(selec)
        list[0].configure(text=selec) # 처음엔 이름넣기

        # 뿌리기
        for i in range(1, len(list)):
            list[i].insert(0, info[i])

        field[0][0 if info[5]=='고양이' else 1 if info[5]=='강아지' else 2 if info[5]=='새' else 3].select()   # 동물 종류 따라서
        field[1][0 if info[0]=='암컷' else 1].select()   # 동물 성별 따라서

        # 분양신청자 id 가져오기
        apply_list = info[6]

        # 신청한 분양자 버튼 생성
        seller_btn = []
        for i, d in enumerate(apply_list):
            btn = Button(self.sellerFrame, padx=13, text=d, pady=5, fg='#B96F00', bg='#F0AD48',
                         command=lambda x=i: self.sellerEvent(d))
            btn.grid(row=i, column=0)
            print(btn)
            seller_btn.append(btn)

    # 클릭 시 분양자 정보 이동
    def sellerEvent(self, id):
        print(id)
        self.root.destroy()
        SellerInfo("분양자 정보", userid=id)

        # # 작성자에게 분양자 전화번호 전달
        # seller = self.engien.get_user_info(id)
        # keys = ['name', 'age', 'id', 'pw', 'pw_check', 'zipcode', 'call_number', 'introduce']
        # call = seller[keys[6]]
        # messagebox.showinfo('분양자 작성자 전화번호:', call)
        #
        # # 분양자 리스트에서서 삭제
        # self.seller.remove(id)

    def updateEvent(self):
        # 수정 클릭 시 메인화면
        # 분양자 리스트 추가
        seller = self.thisAnimal[6]
        print(seller)

        message = self.engien.update_animal(self.inputList, self.gender_ani, self.species_var, seller)
        if message != 'ok':
            messagebox.showinfo("오류", message)  # 등록이 성공적으로 안되면 이유 리턴
            return

        messagebox.showinfo("안내", "게시물 수정 완료!!")

        self.root.destroy()
        adieuMain("메인화면")

    def deleteEvent(self):
        # 취소 클릭 시 사용자화면
        self.engien.delete_animal(self.animalkey)
        self.root.destroy()
        UserInfo("사용자정보")

    # 클릭 시 입력
    def hintEvent(self, event):  # 눌렀을때 글자 넣을수 있게
        event.config(fg='black')
        event.delete(0,END)

    def play(self):
        self.root.mainloop()


if __name__ == '__main__':
    ParcelUpdate('분양수정 및 분양자 확인','dfs0')