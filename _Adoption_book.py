import json

from parcel_out import Parcel_out
from _user import User

class Adoption_book:
    def __init__(self):
        self.animals = self.get_animals_json()    # 등록된 동물들
        self.users = self.get_user_json()     # 유저 데이터
        # self.users = []   # 저장된 유저들
        #현재 유저
        # 처음 객체 생성 시 무조건 로그인
        self.test()     # 테스트 코드
        self.now_user = ''

    # 로그인
    def login(self, name, pw):
        #로그인 한 이름과 비밀번호가 일치하면 로그인 성공
        if name in self.users and self.users[name][pw] == pw:
            self.now_user = name   # 로그인 성공이면 true 리턴
        return 0

    def sign_up(self):
        # 유저리스트 유저정보 넣기
        new = User(self.users)
        new.set_all()
        self.users[new.name]= {
            "pw" : new.pw,
            'age' : new.age,
            'gender': new.gender,
            'call_number': new.number,
            'up_list': [],
            'pick_list' : []
        }
        self.set_user_json()
        print('가입성공')
        if new.name in self.users==1:
            return 1    # 정상적으로 들어가면 트루
        return 0

    def get_user_json(self):   # userdata 가져오기
        file_path = "/datas/users_data.json"
        with open(file_path, "r") as json_file:
            json_data = json.load(json_file)
        return json_data

    def set_user_json(self):   # userdata 저장하기
        file_path = "/datas/users_data.json"
        with open(file_path, "w") as out_file:
            json.dump(self.users, out_file,indent=4)
        self.users = self.get_user_json()

    def get_animals_json(self):  # animals 가져오기
        file_path = "/datas/animals_book.json"
        with open(file_path, "r") as json_file:
            json_data = json.load(json_file)
        return json_data

    def set_animals_json(self):  # animals 저장하기
        file_path = "/datas/animals_book.json"
        with open(file_path, "w") as out_file:
            json.dump(self.animals, out_file, indent=4)

    # 입양하고 싶은 동물 종류별 검색
    def search_animal(self):
        # 동물 종류 중복제거
        search_kind = set()
        for a in self.animals:
            search_kind.add(a.species)

        # 동물 종류 보여주기
        search_kind = list(search_kind)
        for i, a in enumerate(search_kind):
            print(f' εïз  {i + 1}. {a}')

        # 해당되는 종의 동물 모두 출력
        select = int(input('검색할 동물번호 » ')) - 1
        for ani in self.animals:
            if ani.species == search_kind[select]:
                print('┍————————————— /ᐠ｡ꞈ｡ᐟ\ —————————————┑')
                print(f'             {ani.pat_name}의 정보   ')
                print(ani)  # 선택한 동물의 자세한 정보 보여주기
                print('┕————————————————————————————————-┙')

    # 입양할 동물들 목록 보여주기 - 종류 . 이름
    def show_animals(self):
        animals_zip = list()
        # 등록된 동물 없을 경우 none 리턴
        if len(self.animals)==0:
            return 'none'

        # 동물의 기본적인 이름 - 종류 번호붙여서 출력
        for key in self.animals.keys():
            pair = (self.animals[key]['species'],key,self.animals[key]['pat_age'])
            animals_zip.append(pair)
        return animals_zip  # 보여줄 목록 반환


    def animal_info(self, select): # 자세히 보기 : 동물 이름가져와서 구하기
        # 선택한 동물 정보 반환
        return [select,
                self.animals[select]['species'],
                self.animals[select]['pat_age'],
                self.animals[select]['pat_gender'],
                self.animals[select]['pat_gender'],
                self.animals[select]['user']]
            

    # 입양 신청하기
    def put_animals(self,animalname):
        # 신청한 동물 인덱스에 있는 객체의 신청내역에 신청한 사용자의 이름을 넣는다
        self.animals[animalname]['apply_users'].appand(self.now_user)
        # 신청하는 사용자의 신청내역에 신청한 동물을 추가한다.
        self.users[self.now_user]['pick_list'].append(animalname)
        self.set_animals_json()
        self.set_user_json()

    # 게시물 등록
    def up_animal(self):
        new = Parcel_out()
        new.set_pat()
        self.animals[new.pat_name] = {
            'species' : new.species,       # 종류
            'pat_age' : new.pat_age,            # 나이
            'user'    : self.now_user,
            'pat_gender' : new.pat_gender, # 성별
            'pat_etc' : new.etc,     # 기타사항
            'apply_users' : [],     # 분양신청한 사용자들
        }
        self.users[self.now_user]['up_list'].append(new.pat_name) # 현재 사용자 객체의 올린 게시물 리스트에 게시물 올린거 추가
        self.set_animals_json(self.animals)
        self.set_user_json()

    # test하기 위한 기본 사용자들
    def test(self):
        #########사용자들######
        # 사용자 1 - vina
        vina = User(self.users)
        vina.name = 'vina'
        vina.pw = '1234'
        vina.age = '991115'
        vina.gender = '여자'
        vina.number = '01025825852'
        self.users.append(vina)

        # 사용자 2- nono
        nono = User(self.users)
        nono.name = 'nono'
        nono.pw = 'nnnn'
        nono.age = '060912'
        nono.gender = '여자'
        nono.number = '01042514263'
        self.users.append(nono)

        # 사용자 3 - nono
        nara = User(self.users)
        nara.name = 'nara'
        nara.pw = 'na2419'
        nara.age = '04'
        nara.gender = '여자'
        nara.number = '01042514263'
        self.users.append(nara)

        # 사용자 5 - daniel
        daniel = User(self.users)
        daniel.name = 'daniel'
        daniel.pw = '0308'
        daniel.age = '20000308'
        daniel.gender = '여자'
        daniel.number = '01098792433'
        self.users.append(daniel)

        # 사용자 4 - alex
        alex = User(self.users)
        alex.name = 'alex'
        alex.pw = '0101'
        alex.age = '860708'
        alex.gender = '남자'
        alex.number = '01032415768'
        self.users.append(alex)

        # 사용자 6 - hoon
        hoon = User(self.users)
        hoon.name = 'hoon'
        hoon.pw = '1118'
        hoon.age = '20040118'
        hoon.gender = '남자'
        hoon.number = '01049852736'
        self.users.append(hoon)

        #######게시물 올리기#####
        # vina - 게시물1
        토깽이 = Parcel_out()
        토깽이.species = '토끼'
        토깽이.pat_name ='토깽이'
        토깽이.pat_age = 5
        토깽이.pat_gender = '암컷'
        토깽이.etc ='당근을 좋아함'

        # vina - 게시물2
        행복이 = Parcel_out()
        행복이.species = '고양이'
        행복이.pat_name = '행복이'
        행복이.pat_age = 2
        행복이.pat_gender = '암컷'
        행복이.etc = '우리집 고양이 츄르를 좋아해'

        # nono - 게시물1
        꼬꼬 = Parcel_out()
        꼬꼬.species = '병아리'
        꼬꼬.pat_name = '꼬꼬'
        꼬꼬.pat_age = 6
        꼬꼬.pat_gender = '수컷'
        꼬꼬.etc = '병아리 옆구리 부상을 입음'

        # alex - 게시물1
        햄토리 = Parcel_out()
        햄토리.species = '햄스터'
        햄토리.pat_name = '햄토리'
        햄토리.pat_age = 1
        햄토리.pat_gender = '암컷'
        햄토리.etc = '해바라기 씨를 좋아함'

        # alex - 게시물2
        몽이 = Parcel_out()
        몽이.species = '앵무새'
        몽이.pat_name = '몽이'
        몽이.pat_age = 2
        몽이.pat_gender = '암컷'
        몽이.etc = '"안녕"과 "사랑해"를 할 수 있음'


        # daniel - 게시물1
        보리 = Parcel_out()
        보리.species = '강아지'
        보리.pat_name = '보리'
        보리.pat_age = 6
        보리.pat_gender = '수컷'
        보리.etc = '관절이 좋지 않으니 주의 바람'

        # hoon - 게시물1
        포키 = Parcel_out()
        포키.species = '거북이'
        포키.pat_name = '포키'
        포키.pat_age = 9
        포키.pat_gender = '암컷'
        포키.etc = '옛날에 등딱지를 다쳐서 흉터가 있음'

        # hoon - 게시물1
        독도 = Parcel_out()
        독도.species = '거북이'
        독도.pat_name = '독도'
        독도.pat_age = 11
        독도.pat_gender = '수컷'
        독도.etc = '사실 자라인지 헷갈림'

        # hoon - 게시물2
        휴지 = Parcel_out()
        휴지.species = '고양이'
        휴지.pat_name = '휴지'
        휴지.pat_age = 1
        휴지.pat_gender = '수컷'
        휴지.etc = '길 고양이이며, 피부병이\n있었지만 지금은 완치함, 사람들을 좋아함'

        #######게시물 등록하기######
        self.animals.append(토깽이)
        vina.up_list.append(토깽이)
        self.animals.append(행복이)
        vina.up_list.append(행복이)
        self.animals.append(꼬꼬)
        nono.up_list.append(꼬꼬)
        self.animals.append(햄토리)
        alex.up_list.append(햄토리)
        self.animals.append(몽이)
        alex.up_list.append(몽이)
        self.animals.append(보리)
        daniel.up_list.append(보리)
        self.animals.append(포키)
        hoon.up_list.append(포키)
        self.animals.append(독도)
        hoon.up_list.append(독도)
        self.animals.append(휴지)
        hoon.up_list.append(휴지)

        ####### 신청하기 ########
        꼬꼬.applys.append(vina)
        vina.pick_list.append(꼬꼬)
        꼬꼬.applys.append(daniel)
        daniel.pick_list.append(꼬꼬)

        행복이.applys.append(nono)
        nono.pick_list.append(행복이)

        햄토리.applys.append(nara)
        nara.pick_list.append(햄토리)
        몽이.applys.append(nara)
        nara.pick_list.append(몽이)

        보리.applys.append(hoon)
        hoon.pick_list.append(보리)
        보리.applys.append(nono)
        nono.pick_list.append(보리)

        휴지.applys.append(vina)
        vina.pick_list.append(휴지)
        휴지.applys.append(alex)
        alex.pick_list.append(휴지)
        휴지.applys.append(nara)
        nara.pick_list.append(휴지)







    
