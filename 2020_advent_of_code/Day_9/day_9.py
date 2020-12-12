
def open_file(file_name):
    clear_list = []
    with open(file_name, 'r') as input:
        for line in input.read().splitlines():
            clear_list.append(int(line))
    return clear_list

def expose_weekness(input_data):
    max_search_len = 25
    file_len = len(input_data) # 100
    next_el = 25 # 25th
    while next_el < file_len:
        el_value = input_data[next_el] #25
        counter = 1
        check_list = []
        while counter < max_search_len:
            el_sum = 0
            el_list =[]
            el_1 = input_data[next_el - counter] # 24
            el_list.append(el_1)
            sub_counter = 2
            while sub_counter <= 25:
                el_2 = input_data[next_el - sub_counter] # 23
                el_sum = el_1 + el_2
                check_list.append(el_sum)
                el_list.append(el_2)
                sub_counter += 1
            counter += 1
        if el_value not in check_list:
            el_list.reverse()
            return([el_value, next_el])
        next_el += 1
    return None

def break_xmas_encryption(weak_num, weak_num_id, full_list):
    """Checks for the group of numbers that sums up to 
a week number and ads its smallest and bigger numbem."""
    x = 0
    y = 1
    while x <= len(full_list):
        range_sum = sum(full_list[x:y])
        # if range_sum != 0:
            # print(f"x: {x}, y: {y}, sum: {range_sum}")
        if range_sum == weak_num:
            min_value = min(full_list[x:y])
            max_value = max(full_list[x:y])
            final_code = min_value + max_value
            return(final_code)
        elif range_sum < weak_num:
            y += 1
        else:
            x += 1
    return None


def main():
    input_file = open_file('input.txt')
    corrupted_nums = expose_weekness(input_file)
    week_num = corrupted_nums[0]
    week_num_id = corrupted_nums[1]
    break_point = break_xmas_encryption(week_num, week_num_id, input_file)
    print(break_point)
    print(break_xmas_encryption.__doc__)


if __name__ == '__main__':
    main()
