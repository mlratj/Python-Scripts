
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
            el_1 = input_data[next_el - counter] # 24
            sub_counter = 2
            while sub_counter <= 25:
                el_2 = input_data[next_el - sub_counter] # 23
                el_sum = el_1 + el_2
                check_list.append(el_sum)
                sub_counter += 1
            counter += 1
        if el_value not in check_list:
            return(el_value)
        next_el += 1
    return None

def main():
    input_file = open_file('input.txt')
    corrupted_num = expose_weekness(input_file)
    print(corrupted_num)

if __name__ == '__main__':
    main()