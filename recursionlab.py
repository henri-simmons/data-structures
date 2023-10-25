#!/usr/bin/env python3

# Q1
def sum_q1(num, ans=0):
    if num > 0:
        ans += num
        return sum_q1(num - 1, ans)
    else:
        return ans


# Q2
def reverse_integer(num):
    if num < 10:
        return num
    last_digit = num % 10
    reversed_num = reverse_integer(num // 10) * 10 + last_digit
    return reversed_num

# Q3
def reverse_string(input_str):
    if len(input_str) <= 1:
        return input_str
    else:
        return reverse_string(input_str[1:]) + input_str[0]


#Q4
def reverse_list(lst):
    if len(lst) <= 1:
        return lst
    else:
        return [lst[-1]] + reverse_list(lst[:-1])

print(reverse_list([1,2,3,4,5]))

