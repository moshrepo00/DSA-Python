from collections import ChainMap


def find_largest(numbers):
    max = numbers[0]
    for number in numbers:
        if number > max:
            max = number

    return max


result = find_largest([1, 2, 4, 5, 6, 1])


def disemvowel(string_):
    vowels = ['a', 'e', 'i', 'o', 'u']
    str_arr = string_.split()
    result_arr = []
    for str_item in str_arr:
        char_arr = list(str_item)
        result_word_list = [
            item for item in char_arr if item.lower() not in vowels]
        result_word = ''.join(result_word_list)
        result_arr.append(result_word)
    return ' '.join(result_arr)


def friend(x):
   return [friend_item for friend_item in x if len(friend_item) == 4]


def filter_list(l):
    return [item for item in l if type(item) is not str]


def convert():
    keys = ['Ten', 'Twenty', 'Thirty']
    values = [10, 20, 30]
    return {k: v for k, v in zip(keys, values)}


def concat_dict():
    dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
    dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
    concat = {**dict1, **dict2}
    return concat


def accest_elem():
    sampleDict = {
        "class": {
            "student": {
                "name": "Mike",
                "marks": {
                    "physics": 70,
                    "history": 80
                }
            }
        }
    }


def init_default():
    employees = ['Kelly', 'Emma', 'John']
    defaults = {"designation": 'Application Developer', "salary": 8000}
    result = dict.fromkeys(employees, defaults)
    print(result)


def extract():
    sampleDict = {
        "name": "Kelly",
        "age": 25,
        "salary": 8000,
        "city": "New york"

    }
    return {k: v for k, v in sampleDict.items() if k == 'name' or k == 'salary'}


def del_keys():
    sampleDict = {
        "name": "Kelly",
        "age": 25,
        "salary": 8000,
        "city": "New york"
    }

    return {k: sampleDict[k] for k in list(sampleDict) if k != 'name' and k != 'salary'}


def del_keys_set():
    sampleDict = {
        "name": "Kelly",
        "age": 25,
        "salary": 8000,
        "city": "New york"
    }
    keysToRemove = ["name", "salary"]

    return {k: sampleDict[k] for k in sampleDict.keys() - keysToRemove}


def check_if_value_exists():
    sampleDict = {'a': 100, 'b': 200, 'c': 300}
    return 200 in sampleDict.values()

# IMPORTANT variables appear to be block scoped


def rename_key():
    sampleDict = {
        "name": "Kelly",
        "age": 25,
        "salary": 8000,
        "city": "New york"
    }
    sampleDict['location'] = sampleDict['city']
    del sampleDict['city']
    return sampleDict


def min_val():
    sampleDict = {
        'Physics': 82,
        'Math': 65,
        'history': 75
    }

    return sorted(sampleDict.values(), reverse=True)[0]


def min_key():
    sampleDict = {
        'Physics': 82,
        'Math': 65,
        'history': 75
    }

    return sorted(sampleDict.items(), key=lambda item: item[1])[0][0]


def update_val():
    sampleDict = {
        'emp1': {'name': 'Jhon', 'salary': 7500},
        'emp2': {'name': 'Emma', 'salary': 8000},
        'emp3': {'name': 'Brad', 'salary': 6500}
    }

    for k, v in sampleDict.items():
        if v['name'] == 'Brad':
            v['salary'] = 8500

    return sampleDict


class DNA:
    dna_pairs = dict([
        ('A', 'T'),
        ('T', 'A'),
        ('C', 'G'),
        ('G', 'C')
    ])

    def __str__(self):
        return f'{self.dna_pairs}'

    def __init__(self, dna_string):
        self.dna_string = dna_string

    def get_complement(self):
        dna_str = self.dna_string
        dna_pairs = self.dna_pairs
        dna_list = list(dna_str)
        return ''.join([dna_pairs[item] for item in dna_list])

    def dict_iteration(self, test_str):
        dna_pairs = self.dna_pairs
        for key, value in dna_pairs.items():
            # print(f'{key} -> {value}')
            pass

    def key_value_swap(self):
        test_dict = {
            'one': 1,
            'two': 2,
            'three': 3,
            'four': 4
        }
        new_dict = {}
        for key, value in test_dict.items():
            new_dict[value] = key

        return new_dict

    def get_below(self):
        test_dict = {
            'one': 1,
            'two': 2,
            'three': 3,
            'four': 4
        }
        new_dict = {}
        for key, value in test_dict.items():
            if value <= 2:
                pass
            elif value <= 4:
                new_dict[key] = value
            else:
                pass

        return new_dict

    def get_total(self):
        income = {'apple': 1200, 'orange': 3500, 'banana': 500.00}
        total_income = 0.00
        for value in income.values():
            total_income += value
        return total_income

    def double_income(self):
        income = {'apple': 1200, 'orange': 3500, 'banana': 500.00}
        for k, v in income.items():
            income[k] = v * 2
        return income

    def delete_item_wrong(self):
        income = {'apple': 1200, 'orange': 3500, 'banana': 500.00}
        for key in income.keys():
            if key == 'orange':
                del income[key]
        return income

    def delete_item_correct(self):
        prices = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25}
        for item in list(prices.keys()):
            if item == 'orange':
                del prices[item]

        return prices

    def tups(self):
        prices = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25}
        for item in prices.items():
            print(item)
            print(type(item))  # tuple

    def dict_comprehension(self):
        objects = ['blue', 'apple', 'dog']
        categories = ['color', 'fruit', 'pet']
        a_dict = {key: value for key, value in zip(categories, objects)}
        return a_dict

    def dict_swap(self):
        a_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4}
        new_dict = {value: key for key, value in a_dict.items()}
        return new_dict

    def dict_filter(self):
        a_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4}
        new_dict = {k: v for k, v in a_dict.items() if v <= 2}
        return new_dict

    def dict_calculations(self):
        incomes = {'apple': 5600.00, 'orange': 3500.00, 'banana': 5000.00}
        new_list = [val for val in incomes.values()]
        return sum(new_list)

    def remove_item(self):
        incomes = {'apple': 5600.00, 'orange': 3500.00, 'banana': 5000.00}
        new_dict = {k: v for k, v in incomes.items() if k != 'orange'}
        return new_dict

    def sort_items_by_key(self):
        incomes = {'apple': 5600.00, 'orange': 3500.00,
                   'banana': 5000.00, 'apricot': 1.00, 'cantaloupe': 2.00}
        new_dict = {k: incomes[k] for k in sorted(incomes)}
        return new_dict

    def sort_items_by_value(self):

        incomes = {'apple': 5600.00, 'orange': 3500.00,
                   'banana': 5000.00, 'apricot': 1.00, 'cantaloupe': 2.00}
        # return sorted(incomes.values(), key=by_value)
        # for k,v in sorted(incomes.items(), key=by_value):
        #     print(k, ' -> ', v)

        return sorted(incomes.items(), key=lambda item: item[1])

    def sort_list(self):
        test_list = [1, 3, 4, 2]
        return sorted(test_list, reverse=True)

    def map_example(self):
        def discount(current_price):
            return (current_price[0], round(current_price[1] * 0.95, 2))
        prices = {'apple': 0.40, 'orange': 0.35,
                  'banana': 1.15, 'mango': 10.00}
        result = dict(map(lambda current_price: (
            current_price[0], current_price[1] * 20), prices.items()))

    def filter_example(self):
        prices = {'apple': 0.40, 'orange': 0.35,
                  'banana': 1.15, 'mango': 10.00}
        result = dict(filter(lambda current_price: (
            current_price[1] > 0.7), prices.items()))
        print(result)

    def convert_dict_to_list(self):
        prices = {'apple': 0.40, 'orange': 0.35,
                  'banana': 1.15, 'mango': 10.00}
        return sorted(list(prices))

    def chained_dict(self):
        fruit_prices = {'test': 1}
        vegetable_prices = {'te2st': 0.20}
        chained_dict = ChainMap(fruit_prices, vegetable_prices)
        for k, v in chained_dict.items():
            print(k, ' -> ', v)

    def concat_dict(self):
        fruit_prices = {'apple': 0.40, 'orange': 0.35}
        vegetable_prices = {'pepper': 0.20, 'onion': 0.55}
        concat = {**vegetable_prices, **fruit_prices}
        for k, v in concat.items():
            print(k, ' -> ', v)


dna_obj = DNA('AGGG')
