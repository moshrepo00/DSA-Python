class BubbleSort:

    def __init__(self, a_list):
        self.a_list = a_list
    def bubble_sort_unoptimized(self):
        a_list = self.a_list
        for i in range(len(a_list)):
            for j in range(len(a_list) - 1):
                if a_list[j + 1] < a_list[j]:
                    a_list[j], a_list[j + 1] = a_list[j + 1], a_list[j]

        return a_list
    
    def bubble_sort_optimization_1(self):
        a_list = self.a_list
        has_swapped = True
        while (has_swapped):
            has_swapped = False
            for i in range(len(a_list) - 1):
                if a_list[i + 1] < a_list[i]:
                    a_list[i], a_list[i + 1] = a_list[i + 1], a_list[i]
                    has_swapped = True
        return a_list
    
    def bubble_sort_optimization_2(self):
        a_list = self.a_list
        has_swapped = True
        iterations = 0;
        while (has_swapped):
            has_swapped = False
            for i in range(len(a_list) - iterations - 1):
                if a_list[i + 1] < a_list[i]:
                    a_list[i], a_list[i + 1] = a_list[i + 1], a_list[i]
                    has_swapped = True
            iterations += 1
        return a_list

a = BubbleSort([2, 12, 1, 29, 5, 34])
# print('implementation 1 ',  a.bubble_sort_unoptimized())
# print('implementation 2 ',  a.bubble_sort_optimization_1())
# print('implementation 3 ',  a.bubble_sort_optimization_2())
