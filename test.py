test_list = [{'a' : 1, 'b' : 2}, { 'c' : 3, 'd' : 4}]

print(str(test_list))

res = [dict([key, str(value)] for key, value in dicts.items()) for dicts in test_list]

# printing result
print("The modified converted list is : " + str(res))