#!/usr/bin/python3
def magic_calculation(a, b):
    result = 0  # equivalent to LOAD_CONST 0 and STORE_FAST result

    # equivalent to SETUP_LOOP and FOR_ITER over range(1, 3)
    for i in range(1, 3):
        try:
            if i > a:  # equivalent to COMPARE_OP > and POP_JUMP_IF_FALSE
                raise Exception('Too far')  # equivalent to LOAD_GLOBAL Exception and RAISE_VARARGS

            # equivalent to BINARY_POWER, BINARY_TRUE_DIVIDE, and INPLACE_ADD
            result += (a ** b) / i
        except Exception:  # equivalent to SETUP_EXCEPT and POP_TOPs
            result = b + a  # equivalent to BINARY_ADD and STORE_FAST result
            break  # equivalent to BREAK_LOOP

    return result  # equivalent to RETURN_VALUE
