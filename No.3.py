#!/usr/bin/env python
# coding: utf-8

# In[5]:


def decimal_to_binary(num):
    if num == 0:
        return "0"
    integer_part = int(num)
    binary_integer = bin(integer_part).replace("0b", "")

    fractional_part = num - integer_part
    binary_fraction = ""

    while fractional_part and len(binary_fraction) < 10: 
        fractional_part *= 2
        bit = int(fractional_part)
        binary_fraction += str(bit)
        fractional_part -= bit

    return binary_integer + ("." + binary_fraction if binary_fraction else "")

num = float(input("Enter a number: "))
binary_representation = decimal_to_binary(num)
binary_representation


# In[ ]:




