#1
def even_words(string):
    word_list  = string.split()
    total = 0
    for i in word_list:
        if len(i) % 2 == 0:
            total += 1
    return total
text = "Hello my dog"
print(even_words(text))
#2
def is_string_even(string):
    return len(string) % 2 == 0
text1 = "Hello my dog"
print(is_string_even(text))
#3
def is_list_divisible(list1,x):
    for i in list1:
        if i % 2 == 0:
            return True
        else:
            return False
list = [5,3,4,2,7]
y = 2
print(is_list_divisible(list,y))
#4
def get_last_letters(list):
    result = ''
    for i in list:
        result += i[-1]
    return result
list1 = ['hhh','hi']
print(get_last_letters(list1))
#5
def calculate_min_length(list):
    min = len(list[0])
    for i in list:
        if len(i) < min:
            min = len(i)
    return min
list1 = ['hhh','hi','i']
print(calculate_min_length(list1))
#6
def calculate_max_length(list):
    max = 0
    for i in list:
        if len(i) > max:
            max = len(i)
    return max
list1 = ['hhh','hi','i']
print(calculate_max_length(list1))

