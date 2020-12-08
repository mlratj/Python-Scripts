def open_file(file_name):
    clear_list = []
    index = 0
    space_str = ' '
    with open(file_name, 'r') as input:
        for line in input:
            line = line.strip()
            indexed_line = f"{index}{space_str}{line}"
            index += 1
            clear_list.append(indexed_line)
    return clear_list

def instructions_list(string_list):
    instructions_list = []
    for line in string_list:
        single_instruction = line.split(' ')
        instructions_list.append(single_instruction)
    return instructions_list

def accumulator(instructions):
    value = 0
    start_point = 0
    i = 0
    used_commands = []
    while True:
        curr_index = instructions[i][0]
        if curr_index in used_commands:
            break
        if instructions[i][1] == 'nop':
            i += 1
            used_commands.append(curr_index)
        elif instructions[i][1] == 'jmp':
            i += int(instructions[i][2])
            used_commands.append(curr_index)
        elif instructions[i][1] == 'acc':
            value += int(instructions[i][2])
            i += 1
            used_commands.append(curr_index)
    return value

def main():
    input_list = open_file("input.txt")
    all_instructions = instructions_list(input_list)
    final_value = accumulator(all_instructions)
    print(final_value)

if __name__ == "__main__":
    main()