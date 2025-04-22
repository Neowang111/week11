def findMaxInList(numbers):

    max_value = numbers[0]

    for num in numbers:
        if num > max_value:
            max_value = num
    
    return max_value

my_list = [3, 10, 5, 8, 20, 15]
result = findMaxInList(my_list)
print("The max is:", result)
