class SelectionSort:
    def __init__(self, l):
        self.l = l
    def selection_sort(self):
        l = self.l
        for i in range(len(l) - 1):
            min_index = i
            # i = 0; l[i] = 1
            for j in range(i + 1, len(l)):
                if (l[j] < l[min_index]):
                    min_index = j
            l[i], l[min_index] = l[min_index], l[i]

        return l



sort_obj = SelectionSort([42,22, 1,12,3, 2, 98, 101, 66])



# print(sort_obj.selection_sort())
