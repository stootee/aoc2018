from day5_input import inp as inp


def reducer(adjusted_input):
    finished = False
    while not finished:
        cntr = 0
        last_read = (None, None)
        for x in adjusted_input:
            cntr += 1
            polarity = 1
            if ord(x) < 97:
                polarity = 0
            current_read = (x.lower(), polarity)
            if current_read[0] == last_read[0] and current_read[1] != last_read[1]:
                # print adjusted_input
                # print "BOOM!", current_read, last_read, cntr
                # print adjusted_input[:cntr - 2]
                # print adjusted_input[cntr:]
                adjusted_input = adjusted_input[:cntr - 2] + adjusted_input[cntr:]
                break

            last_read = current_read
        if cntr - 1 == len(adjusted_input):
            finished = True

    return adjusted_input

# print len(reducer(inp))

# PART 2

for letter in range(0, 26):
    altered_inp = inp.replace(chr(letter + 65), '').replace(chr(letter + 97), '')
    print chr(letter + 65)
    print len(reducer(altered_inp))


