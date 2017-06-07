
'''divide the ' single word 'company from origin source data '''

# list_single = []
# list_more = []
file_single = open('file_single.txt','w')
file_more = open('file_more.txt','w')
file_origin = open('file_origin.txt','w')
# f = open("namp_brand_clear.txt")
# line = f.readline()
with open("namp_brand_clear.txt", "r") as f:
    # if line.isspace():
    # newline = line + '\n'
    for strs in f:
        strs_list = strs.strip('\r\n').split(" ")
        if len(strs_list) == 1:
            file_single.write(strs)
            ''' make the flag in order to link sources between steps'''
            ''' let flag more suitable and beautiful'''
            length = len(strs_list[0])
            file_origin.write(strs_list[0])
            for i in range(40-length):
                file_origin.write(' ')
            file_origin.write('          # ' + strs)

        else:
            file_more.write(strs)
            file_origin.write(strs)
        # if strs == ' ':
        #     # newline_more = line + '\n'
        #     file_more.write(line)
        #     break
        #     # print line
        # else:
        #     # newline_single = line + '\n'
        #     file_single.write(line)
        #     # break
        # # file_single.write(line)


    line = f.readline()

file_single.close()
file_more.close()