# _______________________________________________1_____________________________________________________

# Необходимо создать из него словарь с ключами “int”, “float”, “str”, “bool”, “none” и
# соответствующим значением из списка.
# Вместо этих значений в списке и их порядок могут быть и другие, напишите код, который будет работать
# с любыми значениями, то есть он должен быть универсальным
# Например из списка
# [True, 2.3, None, “brook”, 5]
# Надо получить:
# {
# “float”: 2.3,
# “bool”: True,
# “none”: None,
# “int”: 5,
# “str”: “brook”
# }

our_dict = {
    "float": [],
    "bool": [],
    "none": [],
    "int": [],
    "str": []
}


class cheking_list:

    def __init__(self, our_list: list):
        self.our_list = our_list

    def filter_list(self):
        for output in self.our_list:
            if float == type(output):
                our_dict["float"].append(output)
            elif bool == type(output):
                our_dict["bool"].append(output)
            elif None == type(output):
                our_dict["none"].append(output)
            elif int == type(output):
                our_dict["int"].append(output)
            elif str == type(output):
                our_dict["str"].append(output)


Result = cheking_list([1, 4.7, "hi", False, None])
Result.filter_list()
print(our_dict)
