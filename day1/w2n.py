string = input("Enter a string: ")
my_dict = {'0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'}
for item in string:
  if item in my_dict.keys():
    string = string.replace(item, my_dict[item])
print(string)