class Parcel_out:
    def __init__(self):
        # 동물의 분류
        self.species =''
        # 동물의 이름
        self.pat_name =''
        # 동물의 나이
        self.pat_age = 1
        self.place = ''
        # 분양동물 기타사항
        self.etc =''
        self.pat_gender = ''

    def set_pat(self, input_list, gender,species, isupdate):    # [name, age, place, add_infor]
        self.input_list = input_list
        if isupdate==True:  # 수정인경우 이름 수정 안함
            self.pat_name = self.input_list[0]['text']
        else:
            self.pat_name = self.name_check(self.input_list[0].get())

        self.species = self.species_check(species)
        self.place = self.input_list[2].get()
        self.etc = self.input_list[3].get()
        age = self.set_pat_age()
        if age != 'true':
            return age
        self.pat_age = self.input_list[1].get()
        self.pat_gender = self.gender_check(gender)
        return 'ok'


    def name_check(self, name):
        from _json_use import UseJSON
        js = UseJSON()
        animals = js.get_animals_json()
        for key in animals.keys():
            if name in key:     # 이미 이름이 있다면
                if key[-1].isdecimal(): # 마지막에 숫자있는지 확인
                    name += ' ('+str(int(key[-1])+1)+')'
                    break
                name += ' (1)'
        return name

    def set_pat_age(self):
        age = self.input_list[1].get()
        if age.isdigit() == True:
            self.pat_age = int(age)
            return 'true'
        else:
            return '나이를 제대로 입력해주십시오'

    def gender_check(self, gender_var):
        if gender_var ==1:
            return '암컷'
        else:
            return '수컷'

    def species_check(self, species):
        field = ['고양이','강아지','새','기타']
        return field[species.get()]
        