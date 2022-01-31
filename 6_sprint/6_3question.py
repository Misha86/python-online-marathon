"""3 question 6 sprint"""
import json
import jsonschema
from jsonschema import validate
import csv

user_schema = {
    "owner": "user",
    "type": "object",
    "properties": {
        "id": {"type": "number"},
        "name": {"type": "string"},
        "department_id": {"type": "number"},
    },
    "required": ["id", "name", "department_id"]
}

department_schema = {
    "owner": "department",
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "id": {"type": "number"},
            "name": {"type": "string"},
        },
        "required": ["id", "name"]
    }
}


class DepartmentName(Exception):
    pass


class InvalidInstanceError(Exception):
    pass


def validate_json(data, schema):
    try:
        validate(data, schema)
        return data
    except:
        raise InvalidInstanceError(f"Error in {schema['owner']} schema")


def user_with_department(csv_file, user_json, department_json):
    with open(csv_file, 'w') as f, open(user_json) as user_file, open(department_json) as department_file:
        writer = csv.DictWriter(f, fieldnames=["name", "department"])
        writer.writeheader()
        try:
            department_json_load = validate_json(json.load(department_file), department_schema)

            def get_user_department(dct):
                validate_json(dct, user_schema)
                dct.pop('id')
                department_id = dct.pop('department_id')
                department_name = [dep_item.get("name") for dep_item in department_json_load
                                   if dep_item.get('id') == department_id]

                if not department_name:
                    raise DepartmentName(f"Department with id {department_id} doesn't exists")

                dct['department'] = department_name[0]
                return dct

            user_json_load = json.load(user_file, object_hook=get_user_department)
            writer.writerows(user_json_load)

        except InvalidInstanceError as e:
            print(str(e))

        except DepartmentName as e:
            print(str(e))


if __name__ == '__main__':
    # user_instance = {
    #     "id": 1,
    #     "name": "userName",
    #     "department_id": 1
    # }
    #
    # department_instance = {
    #     "id": 1,
    #     "name": "departmentName",
    # }
    # print(validate_json(user_instance, user_schema))
    # print(validate_json(department_instance, department_schema))
    print(user_with_department('csv_file.csv', 'user_json.json', 'department_json.json'))
