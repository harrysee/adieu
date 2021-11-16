import json

class UseJSON():
    def get_user_json(self):   # userdata 가져오기
        file_path = "datas/users_data.json"
        with open(file_path, "rt", encoding='UTF8') as json_file:
            json_data = json.load(json_file)
        return json_data

    def set_user_json(self, users):   # userdata 저장하기
        file_path = "datas/users_data.json"
        with open(file_path, "w") as out_file:
            json.dump(users, out_file,indent=4)

    def get_animals_json(self):  # animals 가져오기
        file_path = "datas/animals_book.json"
        with open(file_path, "rt", encoding='UTF8') as json_file:
            json_data = json.load(json_file)
        return json_data

    def set_animals_json(self, animals):  # animals 저장하기
        file_path = "datas/animals_book.json"
        with open(file_path, "w") as out_file:
            json.dump(animals, out_file, indent=4)