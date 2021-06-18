class Parcel_out:
    def __init__(self):
        # 동물의 종류
        self.species = ''
        # 동물의 이름
        self.pat_name = ''
        # 동물의 나이
        self.pat_age = 1
        # 동물의 성별
        self.pat_gender = ''
        # 분양동물 기타사항
        self.etc = ''
        # 입양신청자 리스트
        self.applys = []

    # 동물 정보 입력
    def set_pat(self):
        self.pat_name = input('분양할 동물의 이름을 입력하세요 → ')

        while True:
            age = input('분양할 동물의 나이를 입력하세요 → ')
            if age.isdigit() == True:
                self.pat_age = int(age)
                break
            else:
                input('잘못 입력했습니다(>_<｡)💦 숫자만 입력해주세요')

        while True:
            gender = input('분양할 동물의 성별을 입력하세요 (w|m) → ')
            if gender == 'w' :
                self.pat_gender = '암컷'
                break
            elif  gender == 'm':
                self.pat_gender = '수컷'
                break
            else:
                input('잘못 입력했습니다(>_<｡)💦 다시 입력해주세요')

        self.species = input('분양할 동물 종을 입력하세요 → ')
        self.etc = input('분양할 동물의 기타사항을 입력하세요 → ')

    def __str__(self):
        return (f'  이름:{self.pat_name}\n  나이:{self.pat_age}\n  성별:{self.pat_gender}\n  종류:{self.species}\n  기타사항:{self.etc}')
