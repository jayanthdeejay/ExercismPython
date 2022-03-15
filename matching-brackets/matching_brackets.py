def is_paired(input_string):
    """Given a string containing brackets [], braces {}, parentheses (), 
    or any combination thereof, verify that any and all pairs are matched and nested correctly.
    """
    stack = ['N']
    dict = {']': '[', '}': '{', ')': '('}
    for char in input_string:
        if char in dict.keys():
            if stack.pop() != dict[char]:
                return False
        elif char in dict.values():
            stack.append(char)

    return len(stack) == 1
