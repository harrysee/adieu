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

    def check_all(self, input_list, gender):
        self.input_list = input_list

        for info in self.input_list:
            if info.get() == '':
                return info + '를 입력하세요'
            elif info.get() == False:
                print('꒦꒷꒷꒦꒦꒷잘못 입력했습니다(>_<｡)💦 다시 입력하세요꒦꒷꒷꒦꒷꒦꒷')

        # 동물 정보
        self.set_pat()

        # 동물 나이
        self.set_pat_age()

    def set_pat(self):    # [name, species, age, place, add_infor, user_infor]
        self.pat_name = self.name_check(self.input_list[0].get())
        self.species = self.input_list[1].get()
        self.etc = self.input_list[4].get()
        self.user = self.input_list[5].get()
        age = self.set_pat_age()
        if age != 'true':
            return age
        self.pat_age = self.input_list[2].get()
        return 'ok'


    def name_check(self, name):
        from json_use import UseJSON
        js = UseJSON()
        animals = js.get_animals_json()
        for key in animals.keys():
            if name in key:     # 이미 이름이 있다면
                if key[-1].isdecimal():
                    name += str(int(key[-1])+1)
                    break
                name += '0'
        return name


    def set_pat_age(self):
        age = self.input_list[2].get()
        if age.isdigit() == True:
            self.pat_age = int(age)
            return 'true'
        else:
            return '나이를 제대로 입력해주십시오'

    def __str__(self):
        return (f'이름:{self.pat_name}\t나이:{self.pat_age}\t성별:{self.pat_gender}\t종류:{self.species}\t기타사항:{self.etc}')