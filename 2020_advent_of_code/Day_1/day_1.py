num_set = set()

with open("input_1.txt") as input:
    for line in input:
        num_set.add(int(line))

# part I
for a in num_set:
    for b in num_set:
        sum = a + b
        if sum == 2020:
            print (a, '* ', b, ' is: ', a * b)
            break

# part II
for a in num_set:
    for b in num_set:
        for c in num_set:
            sum = a + b + c
            if sum == 2020:
                print (a, '*', b, '*' , c, ' is: ', a * b * c)
                break
