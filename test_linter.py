import os
import sys


def calculate_discount(price, discount):
    final_price = price - (price * discount)
    return final_price

print(calculate_discount(1000, 0.15))
