import json
from _json_use import UseJSON as json

class User:
    def __init__(self):  # 원래 등록된 user들 가져오기
        self.name = ""
        self.id = ''
        self.zip_code = ''
        self.introduce = ''
        self.pw = ''
        self.age = 000000
        self.gender = 'w'
        self.number = ''
        self.input_list = []

    def check_all(self, input_list, gender):
        # inputList : [name, age, id, pw, pw_check, zipcode, call_number, introduce]
        # gender : 성별구분 라디오버튼 잇음 -> 1 = 여자 / 2 = 남자
        # 각자 빈칸 & 형식체크 후 self변수에 값 넣기 / 체크에서 오류날경우 해당 메세지 반환/ 잘들어갔을경우 True반환
        self.input_list = input_list
        for info in self.input_list:
            if info.get() == '':
                return '빈칸을 모두 입력하시오'

        # user 객체 보내기 :이름 입력받기
        check_result = []
        check_result.append(self.set_name())
        check_result.append(self.set_id())
        check_result.append(self.set_pw())
        check_result.append(self.set_age())
        check_result.append(self.set_gender(gender))
        check_result.append(self.set_number())
        check_result.append(self.set_zip_code())
        check_result.append(self.set_introduce())

        # 메세지 반환
        for chk in check_result:
            if chk != True:
                return chk
        return True

    def set_name(self):  # 매개변수로 이름
        self.name = self.input_list[1].get()
        return True  # 이름 없으면 이름 인덱스 반환

    # 중복체크
    def set_id(self):  # 매개변수로 이름
        ids = json.get_user_json(self)
        # 중복되는 이름이 없으면 나옴
        if self.input_list[2] in ids:  # 이미 이름이 있으면 false 반환
            return '이름 중복됨.'
        self.id = self.input_list[2].get()
        return True  # 이름 없으면 이름 인덱스 반환

# 비밀번호 입력
    def set_pw(self):
        pw = self.input_list[3].get()
        pw_check = self.input_list[4].get()
        if len(pw) < 5 :
            return '비밀번호 길이는 5자 이상입니다'
        elif pw != pw_check:
            return '비밀번호 확인이 비밀번호와 맞지 않습니다.'
        self.pw = pw
        return True

    # 나이 입력
    def set_age(self):
        age = self.input_list[1].get()
        if age.isdigit() == True:
            self.age = age
            return True
        else:
            return '나이 숫자로 입력해주십시오'

    # 성별 입력
    def set_gender(self, gender):
        if gender == 1:
            self.gender = '여자'
        elif gender == 2:
            self.gender = '남자'
        return 1

    # 전화번호 입력
    def set_number(self):
        number = self.input_list[6].get()
        if len(number)>=8:
            self.number = number
            return True
        else:
            return '전화번호 8자로 입력해주십시오 ex)01012345678'

    # 소개 입력
    def set_introduce(self):
        intro = self.input_list[7].get()
        self.introduce = intro
        return True

    def set_zip_code(self):
        self.zip_code = self.input_list[5].get()
        return 1

    # 올린 게시물이나 신청한 게시물 동물이름 리스트를 넘겨주면 이름과 종류 리스트를 반환한다.
    def show_uplist(self, this_list):  # 사용자 데이터의 올린게시물 리스트 가져오기
        if len(this_list) == 0:
            return 'none'

        animals = json.get_animals_json(self)
        apply_name = []
        apply_kind = []
        for i in this_list:
            apply_name.append(i)  # 게시물 이름
            apply_kind.append(animals[i]['species'])  # 게시물 종류
            # 올린 동물들 이름과 종류만

        return apply_name, apply_kind  # 이름과 종류 리스트 반환

    # 사용자 정보 확인
    def __str__(self):
        # 사용자 정보로 수정
        return f'  ✔ 이름 : {self.name}\n  ✔ 성별 : {self.gender}\n  ✔ 전화번호 : {self.number}'