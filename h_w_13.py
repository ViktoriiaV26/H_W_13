import json


def some_func(*args, **kwargs):
    result = {}
    kol = 0
    list_ = []
    list_4 = []
    for i in args:
        list_4.append(i)
        if kol < int(len(args) / len(kwargs)) - 1:
            kol += 1
            continue
        list_.append(list_4)
        kol = 0
        list_4 = []
    print(list_)
    index_ = 0
    for k, v in kwargs.items():
        result[v] = list_[index_]
        index_ += 1
    return result


def load_dict(some_dict, json_path):
    with open(json_path, 'r') as file:
        jf_file = json.load(file)
    with open(json_path, 'w') as file_:
        file_target = jf_file['employee']
        file_target.append(some_dict)
        json.dump(jf_file, file_, indent=4)


result = some_func(10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, name="name_",
                   make="make_", well="well_", good="good_", luck="luck_")
print(result)

load_dict({"id": 4,
            "firstName": "Vika",
            "lastName": "Borysenko",
            "age": 28,
            "is_active": True,
            "rewards": None,
            "salary": 6.5}, json_path="my.json")


def main():
    if __name__ == "main":
        main()


