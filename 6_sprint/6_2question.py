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
                            users_name_list.append(dct["name"])
                            users_list.append(dct)
                    json.load(f, object_hook=get_name)
            except FileNotFoundError:
                logging.error(f"File {file} doesn't exist")
        json.dump(users_list, res_file, indent=4)


if __name__ == '__main__':
    parse_user("user3.json", "user1.json", "user2.json")
