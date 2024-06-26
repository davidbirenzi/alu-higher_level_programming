#!/usr/bin/python3
multiply_by_2 = __import__('9-multiply_by_2').multiply_by_2

def print_sorted_dictionary(a_dictionary):
    sorted_keys = sorted(a_dictionary.keys())
    for key in sorted_keys:
        print(f"{key}: {a_dictionary[key]}")

a_dictionary = {'John': 12, 'Alex': 8, 'Bob': 14, 'Mike': 14, 'Molly': 16}

print("-- Original dictionary --")
print_sorted_dictionary(a_dictionary)

print("\n-- New dictionary after multiplication by 2 --")
new_dict = multiply_by_2(a_dictionary)
print_sorted_dictionary(new_dict)
