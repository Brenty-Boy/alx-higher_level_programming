#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    score = 0
    weight = 0
    for i in my_list:
        weight += i[0] * i[1]
        score += i[1]
        weighted_average = weight / score
        return weighted_average
