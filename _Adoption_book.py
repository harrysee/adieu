import json

from _parcel_out import Parcel_out
from _user import User
from _json_use import UseJSON as json

class Adoption_book:
    NOWUSER = ''   # static 변수
    def __init__(self):
        self.animals = json.get_animals_json(self)    # 등록된 동물들
        self.users = json.get_user_json(self)     # 유저 데이터
        #현재 유저
        # 처음 객체 생성 시 무조건 로그인
        # self.test()     # 테스트 코드

    # 로그인

    def login(self, name, pw):
        #로그인 한 이름과 비밀번호가 일치하면 로그인 성공
        if (name in self.users) and (self.users[name]['pw'] == pw):
            Adoption_book.NOWUSER = name   # 로그인 성공이면 true 리턴
            print(Adoption_book.NOWUSER)
            return 1
        return 0

    def sign_up(self, user_input_list, gender): # inputList : Gui 입력 엔트리들 담겨있음
        # inputList : [name, age, id, pw, pw_check, zipcode, call_number, introduce]
        # gender : 성별구분 라디오버튼 잇음 -> 1 = 여자 / 2 = 남자
        # 유저리스트 유저정보 넣기
        new = User()
        check = new.check_all(user_input_list, gender)

        if check != True : return check     # 형식체크 / 메세지 반환
        self.users[new.id] = {
            "name": new.name,
            "pw": new.pw,
            "age": new.age,
            "gender": new.gender,
            "call_number": new.number,
            "zip_code": new.zip_code,
            "introduce": new.introduce,
            "up_list": [],
            "pick_list": []
        }
        json.set_user_json(self, self.users)
        print('가입성공')
        if new.id in self.users:
            return 1    # 정상적으로 들어가면 트루
        return "회원가입 실패"

    # 사용자 정보 수정
    def update_user(self, user_input_list, gender, up, pick): # inputList : Gui 입력 엔트리들 담겨있음
        # inputList : [name, age, id, pw, pw_check, zipcode, call_number, introduce]
        # gender : 성별구분 라디오버튼 잇음 -> 1 = 여자 / 2 = 남자
        # 유저리스트 유저정보 넣기
        new = User()
        check = new.check_all(user_input_list, gender)

        if check != True : return check     # 형식체크 / 메세지 반환

        self.users[new.id] = {
            "name": new.name,
            "pw": new.pw,
            "age": new.age,
            "gender": new.gender,
            "call_number": new.number,
            "zip_code": new.zip_code,
            "introduce": new.introduce,
            "up_list": up,
            "pick_list": pick
        }
        json.set_user_json(self, self.users)

        if new.id in self.users:
            return 1    # 정상적으로 들어가면 트루
        return "회원가입 실패"

    def get_user_info(self, userid):    # 사용자 정보 반환 [이름, 나이, id,소개]
        return (self.users[Adoption_book.NOWUSER], Adoption_book.NOWUSER) if userid == 'nowuser' else self.users[userid]

    # 입양하고 싶은 동물 종류별 검색
    def search_animal(self, select_kind):  # 선택한 동물종류 가져와서 검색하기
        search_list = list()

        for key in self.animals:
            if self.animals[key]['species'] == select_kind:
                pair = (self.animals[key]['species'], key, self.animals[key]['pat_age'], len(self.animals[key]['apply_users']) )
                search_list.append(pair)
        return search_list     # 검색한 리스트 반환

    # 입양할 동물들 목록 보여주기 - 종류 . 이름
    def show_animals(self):
        animals_zip = list()
        # 등록된 동물 없을 경우 - 리턴
        if len(self.animals)==0:
            return '-'

        # 동물의 기본적인 이름 - 종류 번호붙여서 출력
        for key in self.animals.keys():
            pair = (self.animals[key]['species'],key,self.animals[key]['pat_age'], len(self.animals[key]['apply_users']))
            animals_zip.append(pair)
        return animals_zip  # 보여줄 목록 반환


    def get_animal_info(self, select): # 자세히 보기 : 동물 이름가져와서 구하기
        # 선택한 동물 정보 리스트로 반환
        infolist = []
        keys = ['pat_gender','pat_age','place','pat_etc','user','species','apply_users']
        for key in keys:
            infolist.append(self.animals[select][key])
        return infolist

    # 입양 신청하기
    def put_animals(self, animalname):
        # 신청한 동물 인덱스에 있는 객체의 신청내역에 신청한 사용자의 이름을 넣는다
        apply_list = self.animals[animalname]['apply_users']
        apply_list.append(Adoption_book.NOWUSER)
        # 신청하는 사용자의 신청내역에 신청한 동물을 추가한다.
        self.users[Adoption_book.NOWUSER]['pick_list'].append((animalname,0))   # 0:미정 / 1:수락/ -1:거절
        json.set_animals_json(self, self.animals)
        json.set_user_json(self, self.users)
        return True

    # 게시물 등록
    def up_animal(self, list, gender, species):  # 게시물 리스트
        new = Parcel_out()
        check = new.set_pat(list, gender,species,False)   # [name, species, age, place, add_infor, user_infor]
        if check != 'ok':
            return check
        self.animals[new.pat_name] = {
            'species' : new.species,       # 종류
            'pat_age' : new.pat_age,            # 나이
            'user'    : Adoption_book.NOWUSER,
            'pat_gender' : new.pat_gender, # 성별
            'pat_etc' : new.etc,     # 기타사항
            'place'   : new.place,
            'apply_users' : [],     # 분양신청한 사용자들
        }
        json.set_animals_json(self,self.animals)
        json.set_user_json(self, self.users)
        return 'ok'

    # 게시물 수정
    def update_animal(self, list, gender, species, seller):  # 게시물 리스트
        new = Parcel_out()
        check = new.set_pat(list, gender, species,True)  # [name, species, age, place, add_infor, user_infor]
        if check != 'ok':
            return check
        self.animals[new.pat_name] = {
            'species': new.species,  # 종류
            'pat_age': new.pat_age,  # 나이
            'pat_gender': new.pat_gender,  # 성별
            'pat_etc': new.etc,  # 기타사항
            'place': new.place,
            'user' : self.NOWUSER,
            'apply_users': seller  # 분양신청한 사용자들
        }
        json.set_animals_json(self, self.animals)
        json.set_user_json(self, self.users)
        return 'ok'

if __name__ == '__main__':
    Adoption_book()





    
