from parcel_out import Parcel_out
from user import User

class Adoption_book:
    def __init__(self):
        self.animals=[]     # 등록된 동물들
        self.users = []   # 저장된 유저들
        #현재 유저
        # 처음 객체 생성 시 무조건 로그인
        self.test()
        while self.set_user() == -1:
            print('-로그인 실패-')# 회원가입이랑 로그인 둘다 안되었을 때


    # 새로 로그인
    def set_user(self):
        if input('회원가입 : 0 | 로그인 : 1\n>> ')=='1':
            sainup_id = input('이름 입력 : ')
            sainup_pw = input('비밀번호 입력 : ')
            
            #로그인 한 이름과 비밀번호가 일치하면 로그인 성공
            for i in self.users:
                if sainup_pw == i.pw and sainup_id == i.name:
                    self.now_user = i
                    print('로그인 성공')
                    return 0
            return -1
        else:
            # 유저리스트에 가입한 유저객체 넣기
            new = User(self.users)
            new.set_all()
            self.users.append(new)
            print('가입성공')
            self.set_user()

            
    # 입양하고 싶은 동물 종류별 검색
    def search_animal(self):
        # 동물 종류 중복제거
        search_kind = set()
        for a in self.animals:
            search_kind.add(a.species)

        # 동물 종류 보여주기
        search_kind = list(search_kind)
        for i, a in enumerate(search_kind):
            print(f'{i + 1}. {a}')

        # 해당되는 종의 동물 모두 출력
        select = int(input('검색할 동물번호 >> ')) - 1
        for ani in self.animals:
            if ani.species == search_kind[select]:
                print(ani)

    # 입양할 동물들 목록 보여주기 - 종류 . 이름
    def show_animals(self):
        # 동물의 기본적인 이름 - 종류 번호붙여서 출력
        for i, a in enumerate(self.animals):
            print(f'{i+1}. {a.species} - {a.pat_name}\n\t 설명 : {a.explane}')
        
        # 자세히 보고 싶은 동물 선택하면 동물의 정보 출력
        select = input('자세히보기 (없으면 엔터) >> ')
        while select !='':
            print(a[i - 1])  # 선택한 동물의 자세한 정보 보여주기
            select = input('자세히보기 >> (그만보기: 엔터)')


    # 입양 신청하기
    def put_animals(self):
        self.show_animals()
        select_apply = input('신청할 동물번호 : ')

        # 신청한 동물 인덱스에 있는 객체의 신청내역에 신청한 사용자의 이름을 넣는다
        self.animals[select_apply].applys.append(self.user.pat_name)
        # 신청하는 사용자의 신청내역에 신청한 동물을 추가한다.
        self.user.pick_list.append(self.animals[select_apply])
        print('신청되었습니다 ! ')

    # 게시물 등록
    def up_animal(self):
        new = Parcel_out()
        new.set_pat()
        self.now_user.up_list.append(new) # 현재 사용자 객체의 올린 게시물 리스트에 게시물 올린거 추가

    # 사용자 정보 확인 및 신청한 동물, 분양한 동물 확인
    def check(self):
        print(self.now_user)
        print('--------- 등록한 게시물 ---------')
        self.now_user.show_uplist()
        print('--------- 입양희망한 반려동물 ---------')
        self.now_user.show_picklist()

    def test(self):
        vina = User(self.users)
        vina.name = 'vina'
        vina.pw = '1234'
        vina.age = '040810'
        vina.gender = 'w'
        vina.number = '01025825852'
        self.users.append(vina)

        vina

        nono = User(self.users)
        nono.name = 'nono'
        nono.pw = 'nnnn'
        nono.age = '060912'
        nono.gender = 'w'
        nono.number = '01042514263'
        self.users.append(nono)







    
