"""2 question 6 sprint"""
import json
import logging

logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')


def parse_user(output_file, *input_files):
    with open(output_file, "w") as res_file:
        users_name_list = []
        users_list = []
        for file in input_files:
            try:
                with open(file, 'r') as f:
                    def get_name(dct):
                        if "name" in dct and dct["name"] not in users_name_list:
                            val = dct.get('name')
                            users_name_list.append(val)
                            users_list.append(dct)
                            return dct
                    json.load(f, object_hook=get_name)
            except FileNotFoundError:
                logging.error(f"File {file} doesn't exists")
        json.dump(users_list, res_file, indent=4)


def parse_user2(output_file, *input_files):
    with open(output_file, "w") as res_file:
        users_list = []
        for file in input_files:
            try:
                with open(file, 'r') as f:
                    users_list.extend(json.load(f))
            except FileNotFoundError:
                logging.error(f"File {file} doesn't exists")
        name_list = list(set(map(lambda x: x['name'], users_list)))

        def filter_name(dct):
            if dct["name"] in name_list:
                name_list.remove(dct["name"])
                return True
        users_list_f = filter(filter_name, users_list)
        json.dump(list(users_list_f), res_file, indent=4)


if __name__ == '__main__':
    parse_user("user3.json", "user1.json", "user2.json")
