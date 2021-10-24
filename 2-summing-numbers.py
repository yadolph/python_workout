#Задача: написать функцию mysum, которая принимает любое количество аргументов и не использует внутри встроенную sum

def mysum(*args):
    result = int()
    for i in args:
        result += i
    return result

print(mysum(2,3,4,5,6))


# List + starting number

def mysum2(num_lst, start_num=0):
    for i in num_lst:
        start_num += i
    return start_num

print(mysum2([2,3,4,5,6], 10))
print(mysum2([2,3,4,5,6]))

# Write a function that takes a list of numbers. It should return the average

def myavg(num_lst):
    lst_sum = 0
    for i in num_lst:
        lst_sum += i
    return lst_sum / len(num_lst)

print(myavg([2,3,4,5,6]))

# Write a function that takes a list of words (strings). It should return a tuple con-
# taining three integers, representing the length of the shortest word, the length
# of the longest word, and the average word length.

def my_word_avg(word_lst):
    sum_len = 0
    max_len = min_len = len(word_lst[0])
    for word in word_lst:
        if len(word) > max_len:
            max_len = len(word)
        if len(word) < min_len:
            min_len = len(word)
        sum_len += len(word)
    
    return (min_len, max_len, sum_len/len(word_lst))

print(my_word_avg(['afg', 'as', 'asdasd', 'cvcv']))

# Write a function that takes a list of Python objects. Sum the objects that either
# are integers or can be turned into integers, ignoring the others.

def my_obj_sum(obj_lst):
    result = 0
    for obj in obj_lst:
        try:
            result += int(obj)
        except ValueError:
            continue
    return result

print(my_obj_sum([1,2,'3','wassup']))