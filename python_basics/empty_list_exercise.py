empty_list = []
print("empty_list", empty_list)



filled_list = [10, 20 , 30]
print("filled_list", filled_list)
foo = 0
another_filled_list = ['a', 'b', foo]
print("another_filled_list:", another_filled_list)



list_constructor = list()
print("list_constructor:", list_constructor)

sequential_numbers = [number for number in range(10)]
print("sequential_numbers", sequential_numbers)

sequential_numbers.reverse()
print("reversed sequential_numbers", sequential_numbers)
print("sequential_numbers", sequential_numbers)
sequential_numbers.sort()
print("sorted sequential_numbers", sequential_numbers)

a_list = [10, 40, 2, 1, 0]
print("new sorted list", sorted(a_list))
print("a_list", a_list)

# some interesting tricks
ten_times = [0] * 10
print("ten_times", ten_times)
print("concatenated lists: filled_list + another_filled_list = ", filled_list + another_filled_list)