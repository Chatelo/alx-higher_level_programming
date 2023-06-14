#!/usr/bin/python3

def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    product_sum = 0
    weight_sum = 0
    for score, weight in my_list:
        product_sum += score * weight
        weight_sum += weight
    return product_sum / weight_sum
