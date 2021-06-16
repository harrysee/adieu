from Adoption_book import Adoption_book
def print_menu():
    print('-------- 가이드 --------')
    print('1. 로그아웃 및 로그인')
    print('2. 게시물 둘러보기')
    print('3. 동물종류별 검색')
    print('4. 반려동물 입양신청하기')
    print('5. 분양 게시물 등록하기')
    print('6. 내 정보 확인하기')
    print('7. 종료하기')

    num = input('원하는 가이드번호 선택 >> ')
    return num

def main():
    user = Adoption_book()
    while True:
        num = int(print_menu())  # 사용할 메뉴 선택
        if num==1:
            user.set_user() # 새로 로그인
        elif num ==2:
            user.show_animals() # 게시물 둘러보기
        elif num ==3:
            user.search_animal()  # 동물 종류별 검색
        elif num ==4:
            user.put_animals()  # 입양신청
        elif num ==5:
            user.up_animal()    # 분양 게시물 등록
        elif num ==6:
            user.check()    # 내정보 확인
        elif num == 7: # 종료
            print('종료되었습니다.')
            break
        else:
            print('- 잘못 입력하셨습니다. 다시 입력하세요 -')

if __name__ == '__main__':  # __name__ : 파이썬 내장 변수
# main이 name일 때 실행한다.
    main()