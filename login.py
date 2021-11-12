from tkinter import *
from adieu_main import adieuMain


class LoginAdieu():

    def __init__(self, title):
        root = Tk()
        root.title(title)
        root.geometry('745x580')
        root.configure(bg="#FFC978")
        root.resizable(0, 0)
        self.root = root
        # 프레임 설정
        self.mainFrame = Frame(self.root, bg='#FFC978')
        self.mainFrame.pack(expand=True)
        
        # logo 설정
        logo_img = PhotoImage(file='img/Adieu.png')
        logo = Label(self.mainFrame, image=logo_img, bg="#FFC978", anchor='center')

        # id , password 입력칸 설정
        self.id = Entry(self.mainFrame, width=30,relief="flat",bd=10,fg="gray")
        self.pw = Entry(self.mainFrame, width=30,relief="flat",bd=10,fg="gray")
        self.id.insert(0,"input userId")
        self.pw.insert(0,"input userPassword")
        self.id.bind("<Button-1>",self.focusId)
        self.pw.bind("<Button-1>",self.focusPw)
        self.pw.bind("<FocusIn>",self.focusPw)

<<<<<<< HEAD
        self.loginBtn = Button(self.mainFrame,width=30, relief="flat", bd=10, text="로그인", command=self.loginEvent, bg="#F0AD48", fg="#B96F00")
=======
        self.loginBtn = Button(self.mainFrame,width=30, relief="flat", bd=10,
                               text="로그인",command=self.loginEvent, bg="#F0AD48",fg="#B96F00")
>>>>>>> e4932598133accbe67d43544ebfa854deafdc43f
        # 화면 띄우기
        logo.pack(padx=10, pady=30)
        self.id.pack(padx=10, pady=5)
        self.pw.pack(padx=10, pady=5)
        self.loginBtn.pack(padx=10,pady=30)
        self.play()

    def focusId(self,event):    # id입력칸
        self.id.config(fg="black")
        self.id.delete(0, END)

    def focusPw(self,event):    # pw입력칸 설정
        self.pw.config(fg="black")
        self.pw.delete(0,END)

    def loginEvent(self):
        # 로그인 맞는지 확인하고 메인 진입
        self.root.destroy()
        adieuMain("메인")

    def play(self):
        self.root.mainloop()


if __name__ == '__main__':
    l = LoginAdieu("로그인 화면")