simple_dict = {
    'a': 1,
    'b': 2
}
print(simple_dict.items())
# even cube added to dictionary
my_dict = {k: v**3 for k, v in simple_dict.items()if v % 2 == 0}
print(my_dict)
your_dict = {num: num+10 for num in [1, 2, 3]}
print(your_dict)
