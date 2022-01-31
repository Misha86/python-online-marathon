"""2 question 6 sprint"""
import json
import logging

logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')


def parse_user(output_file, *input_files):
    def get_name(dct):
        if "name" in dct and dct["name"] not in list(map(lambda x: x["name"], users_list)):
            users_list.append(dct)
    with open(output_file, "w") as res_file:
        users_list = []
        for file in input_files:
            try:
                with open(file, 'r') as f:
                    json.load(f, object_hook=get_name)
            except FileNotFoundError:
                logging.error(f"File {file} doesn't exist")
        json.dump(users_list, res_file, indent=4)


if __name__ == '__main__':
    parse_user("user3.json", "user1.json", "user2.json")
