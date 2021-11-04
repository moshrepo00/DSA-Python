class InsertionSort:
    def __init__(self, l):
        self.l = l
    
    def insertion_sort(self):
        l = self.l
        for i in range(1, len(l)):
            current_value = l[i]
            current_position = i
            while current_position > 0 and l[current_position - 1] > l[current_position]:
                l[current_position], l[current_position - 1] = l[current_position - 1], current_value
                current_position -=1
        return l

    def insertion_sort_callback(self, callback_func):
        l = self.l
        for i in range(1, len(l)):
            current_value = l[i]
            current_position = i
            while current_position > 0 and callback_func(l[current_position - 1], l[current_position]):
                l[current_position], l[current_position - 1] = l[current_position - 1], current_value
                current_position -= 1
        return l


insertion_obj = InsertionSort(
    [4, 22, 41, 40, 27, 30, 36, 16, 42, 37, 14, 39, 3, 6, 34, 9, 21, 2, 29, 47])

print(insertion_obj.insertion_sort())


class Coordinates:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return str.format("({},{})", self.x, self.y)


A = Coordinates(1, 2)
B = Coordinates(4, 4)
C = Coordinates(3, 1)
D = Coordinates(10, 0)

insertion_obj_2 = InsertionSort([A,B,C,D])


results = insertion_obj_2.insertion_sort_callback(lambda a, b: a.x > b.x)
for result in results:
    print(result)




