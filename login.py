from tkinter import *
from tkinter import messagebox

from adieu_main import adieuMain
from _Adoption_book import Adoption_book as adoption_engien


class LoginAdieu():

    def __init__(self, title):
        self.engien = adoption_engien()
        self.loginGUI(title)

    def loginGUI(self, title):
        bg_color = '#FFC978'  # 배경색
        root = Tk()
        root.title(title)
        root.geometry('745x580+400+100')
        root.configure(bg=bg_color)
        root.resizable(0, 0)
        self.root = root
        # 프레임 설정
        self.mainFrame = Frame(self.root, bg=bg_color)
        self.mainFrame.pack(expand=True)

        # logo 설정
        logo_img = PhotoImage(file='img/Adieu.png')
        logo = Label(self.mainFrame, image=logo_img, bg=bg_color, anchor='center')
        logo.bind('<Button-1>', self.moveStart)

        # id , password 입력칸 설정
        self.id = Entry(self.mainFrame, width=30, relief="flat", bd=10, fg="gray")
        self.pw = Entry(self.mainFrame, width=30, relief="flat", bd=10, fg="gray")
        self.id.insert(0, "input userId")
        self.pw.insert(0, "input userPassword")
        self.id.bind("<Button-1>", self.focusId)
        self.pw.bind("<Button-1>", self.focusPw)
        self.pw.bind("<FocusIn>", self.focusPw)

        self.loginBtn = Button(self.mainFrame, width=30, relief="flat", bd=10, text="로그인", command=self.loginEvent,
                               bg="#F0AD48", fg="#B96F00")
        self.loginBtn = Button(self.mainFrame, width=30, relief="flat", bd=10,
                               text="로그인", command=self.loginEvent, bg="#F0AD48", fg="#B96F00")

        # 화면 띄우기
        logo.pack(padx=10, pady=30)
        self.id.pack(padx=10, pady=5)
        self.pw.pack(padx=10, pady=5)
        self.loginBtn.pack(padx=10, pady=30)
        self.play()

    def moveStart(self, evnet):
        self.root.destroy()
        from start import StartAdieu
        StartAdieu("시작화면")

    def focusId(self, event):  # id입력칸
        self.id.config(fg="black")
        self.id.delete(0, END)

    def focusPw(self, event):  # pw입력칸 설정
        self.pw.config(fg="black")
        self.pw.config(show='●')
        self.pw.delete(0, END)

    def loginEvent(self):
        # 로그인 맞는지 확인하고 메인 진입
        if self.id['foreground'] != 'black' and self.pw['foreground'] != 'black':
            messagebox.showerror("입력오류", "아이디와 비번을 모두 입력하시오.")
            return
        if self.engien.login(self.id.get(), self.pw.get()) == False:
            messagebox.showwarning("안내", "아이디나 비번이 일치하지 않습니다.")
            return

        print(self.id.get())


        self.root.destroy()
        adieuMain("메인")

    def play(self):
        self.root.mainloop()


if __name__ == '__main__':
    l = LoginAdieu("로그인 화면")