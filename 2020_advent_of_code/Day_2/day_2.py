import string

def is_int(x):
    if not isinstance(x, int):
        raise TypeError("Provided range doesn't contain numbers.")

def clear_password(x):
    """Trims a string and deletes \n"""
    x.translate({ord(c): None for c in string.whitespace})
    return x

def split(word): 
    return [char for char in word] 

def bool_to_int(boolean):
    """Converts boolean to integer"""
    bool_val = boolean 
    int_val = int(bool_val == True) 
    return int_val

def open_file(file_name, lines):
    with open(file_name, 'r') as input:
        for line in input:
            lines.append(line)

def fix_input_list(lines, fixed_list):
    """Extracts parameters from given txt file into a list"""
    for i in lines:
        single_input = list()
        occuriencies_range = i.partition(' ')[0]
        min_occ = int(occuriencies_range.split('-')[0])
        is_int(min_occ)
        max_occ = int(occuriencies_range.split('-')[1])
        is_int(max_occ)
        letter_occ = i.split(':')[0][-1:]
        password_ext = str(i.split(':')[1])
        password = ''.join(password_ext.split())
        single_input.extend([min_occ, max_occ, letter_occ, password])
        fixed_list.append(single_input)

def password_policy_checker_1(fixed_list):
    correct_password_counter = 0
    for el in fixed_list:
        password = el[3]
        counter = password.count(el[2])
        if el[0] <= counter <= el[1]:
            correct_password_counter += 1
    print('Correct in terms of example no. 1: ',  correct_password_counter)

def password_policy_checker_2(fixed_list):
    correct_password_counter = 0
    for el in fixed_list:
        place_1 = int(el[0])-1
        place_2 = int(el[1])-1
        password = el[3]
        splitted_password = split(password)
        x = 0
        y = 0
        try:
            x = (el[2] == splitted_password[place_1])
            x = bool_to_int(x)
        except IndexError:
            pass
        try:
            y = (el[2] == splitted_password[place_2])
            y = bool_to_int(y)
        except IndexError:
            pass
        total = x + y
        if (total == 1):
            correct_password_counter += 1
    print('Correct in terms of example no. 2: ',  correct_password_counter)


def main():
    # Initializing lists and a variables
    lines = list()
    fixed_list = list()
    open_file('input_2.txt', lines)
    fix_input_list(lines, fixed_list)
    password_policy_checker_1(fixed_list)
    password_policy_checker_2(fixed_list)


if __name__ == '__main__':
    main()

