def safe_print_list_integers(my_list=[], x=0):
    printed_count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            printed_count += 1
        except IndexError:
            print()  # Ensure a new line is printed before raising the exception
            raise
        except (ValueError, TypeError):
            continue
    print()  # Ensure a new line is printed after the loop
    return printed_count
