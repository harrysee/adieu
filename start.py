from tkinter import *
from login import LoginAdieu
from sign_up import SignUp

class StartAdieu():
    def __init__(self, title):
        root = Tk()
        root.title(title)
        root.geometry('745x580')
        root.configure(bg="#FFC978")
        self.root = root

        # 프레임 설정
        self.mainFrame = Frame(self.root, bg='#FFC978')
        self.mainFrame.pack(expand=True)

        # logo 설정
        loog_img = PhotoImage(file='img/Start_logo.png')
        logo = Label(self.mainFrame, image=loog_img, bg='#FFC978', anchor='center')

        # button 설정
        self.btn_login = Button(self.mainFrame, width=30, relief="flat", command=self.loginEvent, bd=10, text="로그인", bg="#F0AD48", fg="#B96F00")
        self.btn_new_login = Button(self.mainFrame, width=30, relief="flat", command=self.newloginEvent, bd=10, text="회원가입", bg="#F0AD48", fg="#B96F00")

        # 화면에 출력
        logo.pack(padx=10, pady=30)
        self.btn_login.pack(padx=10, pady=5)
        self.btn_new_login.pack(padx=10, pady=5)
        self.play()

    def loginEvent(self):
        self.root.destroy()
        LoginAdieu("로그인")

    def newloginEvent(self):
        self.root.destroy()
        SignUp("회원가입")

    def play(self):
        self.root.mainloop()


if __name__ == '__main__':
    l = StartAdieu("처음 화면")