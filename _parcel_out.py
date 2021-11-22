class Parcel_out:
    def __init__(self):
        # 동물의 종류
        self.species =''
        # 동물의 이름
        self.pat_name =''
        # 동물의 나이
        self.pat_age = 1
        # 분양동물 기타사항
        self.etc =''
        # 사용자 정보
        self.user = ''

        self.input_list = []

    def check_all(self, input_list):
        self.input_list = input_list

        for info in self.input_list:
            if info.get() == '':
                return info + '를 입력하세요'
            elif info.get() == False:
                print('꒦꒷꒷꒦꒦꒷잘못 입력했습니다(>_<｡)💦 다시 입력하세요꒦꒷꒷꒦꒷꒦꒷')

    def set_pat(self):    # [name, species, age, place, add_infor, user_infor]

        self.pat_name = self.input_list[0]

        self.species = self.input_list[1]

        age = self.input_list[2]
        if age.isdigit() == True:
            self.pat_age = int(age)
            return True
        else:
            return False

        self.etc = self.input_list[4]

        self.user = self.input_list[5]


    def __str__(self):
        return (f'이름:{self.pat_name}\t나이:{self.pat_age}\t성별:{self.pat_gender}\t종류:{self.species}\t기타사항:{self.etc}')