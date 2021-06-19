from parcel_out import Parcel_out
from user import User

class Adoption_book:
    def __init__(self):
        self.animals=[]     # 등록된 동물들
        self.users = []   # 저장된 유저들
        #현재 유저
        # 처음 객체 생성 시 무조건 로그인
        self.test() # 테스트 코드
        while self.set_user() == 0:
            print('꒦꒷꒷꒦꒷꒷로그인 실패꒦꒷꒷꒦꒷꒦')   # 회원가입이랑 로그인 둘다 안되었을 때


    # 새로 로그인
    def set_user(self):
        print('''
        〇
         ｏ
          °
        　┳┳ ∩∩
        　┃┃(･∀･)　☆　　★
        ┏┻┻┷━Ｏ ┏┷┓┏┷┓
        ┃Welcome┠┨★┠┨☆┃
        ┗©━━©┛ ┗©┛┗©┛''')
        s = input('*꧁ 회원가입 : 0 ༺༻ 로그인 : 1 ꧂*\n\t-ꦼ———▸  ')
        if s =='1':
            sainup_id = input('이름 입력 » ')
            sainup_pw = input('비밀번호 입력 » ')
            
            #로그인 한 이름과 비밀번호가 일치하면 로그인 성공
            for i in self.users:
                if sainup_pw == i.pw and sainup_id == i.name:
                    self.now_user = i
                    print('°•°•°•°•°•°로그인 성공•°•°•°•°•°•')
                    return 1
            return 0
        elif s == '0':
            # 유저리스트에 가입한 유저객체 넣기
            new = User(self.users)
            new.set_all()
            self.users.append(new)
            print('가입성공')
            if self.set_user()==1: return 1
            return 0
        else :
            print('꒦꒷꒷꒦꒷꒦입력 오류 > 다시입력하세요꒦꒷꒷꒦꒷꒦')
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
        # 등록된 동물 없을 경우 추가할꺼냐고 묻기
        if len(self.animals)==0:
            print('아직 등록된 동물이 없습니다')
            if input('등록하시겠습니까? y/n » ')=='y':
                self.up_animal()
            return

        # 동물의 기본적인 이름 - 종류 번호붙여서 출력
        for i, a in enumerate(self.animals):
            print(f' εïз {i+1}. {a.species} - {a.pat_name}')
        
        # 자세히 보고 싶은 동물 선택하면 동물의 정보 출력
        select = input('자세히보기 (없으면 엔터) » ')
        while select !='':
            # 번호가 다를 경우
            if (select.isdigit() != True) or (int(select)-1 not in range(len(self.animals))) :
                print('꒦꒷꒷꒦꒷꒦잘못입력했습니다. 해당되는 번호를 입력하세요.꒦꒷꒷꒦꒷꒦')
                select = input('자세히보기 (그만보기: 엔터) » ')
                continue
            # 선택한 동물 정보 보여주기
            select = int(select)
            print('┍————————————— /ᐠ｡ꞈ｡ᐟ\ —————————————┑')
            print(f'           {self.animals[select-1].pat_name}의 정보   ')
            print(self.animals[select-1])  # 선택한 동물의 자세한 정보 보여주기
            print('┕————————————————————————————————-┙')

            select = input('자세히보기 (그만보기: 엔터) >> ')

    # 입양 신청하기
    def put_animals(self):
        self.show_animals()
        select_apply = int(input('''╭┈─── 신청할 동물번호 :ྀ࿐ ˊˎ-
╰┈➤ '''))

        # 신청한 동물 인덱스에 있는 객체의 신청내역에 신청한 사용자의 이름을 넣는다
        self.animals[select_apply].applys.append(self.now_user)
        # 신청하는 사용자의 신청내역에 신청한 동물을 추가한다.
        self.now_user.pick_list.append(self.animals[select_apply])
        print('‿︵‿︵‿︵୨˚̣̣̣͙୧ 신청되었습니다 ୨˚̣̣̣͙୧‿︵‿︵‿︵ ')

    # 게시물 등록
    def up_animal(self):
        new = Parcel_out()
        new.set_pat()
        self.animals.append(new)
        self.now_user.up_list.append(new) # 현재 사용자 객체의 올린 게시물 리스트에 게시물 올린거 추가

    # 사용자 정보 확인 및 신청한 동물, 분양한 동물 확인
    def check(self):
        print('╭──                   ೋ사용자정보              ──╮')
        print(self.now_user)
        print('  ✿ 등록한 게시물 ⚪ ༺⊰━━━━━━━━━━━━━━━─')
        self.now_user.show_uplist()
        print('  ✿ 입양신청한 반려동물 ⚪ ༺⊰━━━━━━━━━━─')
        self.now_user.show_picklist()
        print('╰──                    ೋ                     ──╯')

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

        #########게시물 등록하기#######
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







    
