'''divide the first step's data into double/triple/quatary/penta words ,and write them into four files'''

file_second_step_double = open('file_second_step_double.txt','w')
file_second_step_triple = open('file_second_step_triple.txt','w')
file_second_step_quatary = open('file_second_step_quatary.txt','w')
file_second_step_penta = open('file_second_step_penta.txt','w')


with open("file_first_step_finish.txt", "r") as f:
    # if line.isspace():
    # newline = line + '\n'
    for strs in f:
        strs_list = strs.strip('\r\n').split(" ")

        if len(strs_list) == 2:
            file_second_step_double.write(strs)

        elif len(strs_list) == 3:
            file_second_step_triple.write(strs)

        elif len(strs_list) == 4:
            file_second_step_quatary.write(strs)

        else:
            file_second_step_penta.write(strs)