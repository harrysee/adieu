from datetime import date
class User:
    def __init__(self, us): # 원래 등록된 user들 가져오기
        self.name =""
        self.pw = ''
        self.age = 000000
        self.gender = 'w'
        self.number = ''

        self.us = us
        self.up_list = [] # 올린 게시물
        self.pick_list = []   # 신청한 게시물

    def set_all(self):
        self.set_name(self.us)  # user 객체 보내기 :이름 입력받기
        self.set_pw()  # 비밀번호 설정
        self.set_age()  # 생년월일
        self.set_gender()  # 성별
        self.set_number()  # 전화번호

    # 이름 입력
    def set_name(self, users):  # 매개변수로 이름
        # 중복 체크
        stop = False
        while stop==False: # 중복되는 이름이 없으면 나옴
            stop = True
            name = input('이름 입력 : ')  # 이름
            for u in users: # 있는지 찾기
                if name == u.name:
                    print('- 이름이 중복됩니다 -')
                    stop = False
                    break
        self.name = name

    # 비밀번호 입력
    def set_pw(self):
        self.pw = input('비밀번호 입력 : ')

    # 나이 입력
    def set_age(self):
        while True:
            age = input('생일 ex(20040810) : ')
            if len(age) == 8:
                self.age = age
                break
            else:
                print('잘못 입력했습니다. 다시 입력하세요')

    # 성별 입력 
    def set_gender(self):
        while True:
            gender = input('성별 w/m : ')
            if gender == 'w' or gender == 'm':
                self.gender = gender
                break
            else:
                print('잘못 입력했습니다. 다시 입력하세요')

    
    # 전화번호 입력
    def set_number(self):
        while True:
            number = input('전화번호 (숫자만) : ')

            if number.isdigit() == True:
                self.number = number
                break
            else:
                print('잘못 입력했습니다. 다시 입력하세요')

    # 신청한 동물들 보기
    def show_picklist(self):
        if len(self.pick_list)==0:
            print('[ 없음 ]')
            return
        for i,pick in enumerate(self.pick_list):
            print(f'{i+1}. {pick.pat_name} : {pick.species}')

    # 올린 게시물 보기
    def show_uplist(self):
        if len(self.up_list) == 0:
            print('[ 없음 ]')
            return
        for i, up in enumerate(self.up_list):
            # 올린 동물들 이름과 종류만
            print(f'{i + 1}. {up.pat_name}-{up.species}')
            print(f'신청한 사람 >> {up.applys}')    # 올렸던 동물들에 신청한 사람들 확인
            if input('신청한 사람 정보 보기(y/n) >> ') =='y':
                print(up)   # 신청한 사람 정보 출력

    # 사용자 정보 확인
    def __str__(self):
        # 사용자 정보로 수정
        return f'이름 : {self.name}\n성별 : {self.gender}\n전화번호 : {self.number}'