class Sorter:

    @staticmethod
    def selectionSort(lst):
        new_lst = []
        for i in range(len(lst)):
            smallest = Sorter.findSmallest(lst)
            new_lst.append(lst.pop(smallest))
        return new_lst

    @staticmethod
    def findSmallest(lst):
        smallest = lst[0]
        smallest_index = 0
        for i in range(1, len(lst)):
            if lst[i] < smallest:
                smallest = lst[i]
                smallest_index = i
        return smallest_index