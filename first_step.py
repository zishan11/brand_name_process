'''use the list_dict ,divide the company which more than one word ,into which should be check by eye ,and which can still check by computer'''

# file_single = open('file_single.txt','a')
# file_more = open('file_more.txt','a')

'''this is the word list ,use this list to find the similar company words'''

list_dict = ['New Zealand','America','USA','China','Japan','Europe','Asia','Korea',                             #country
             'shanghai','shenzhen','Guangdong','Beijing','City','Taiwan','Shandong','Hangzhou','Chongqing','Fujian',   #city
             'Electronic','elec','tech',  #tech
             'Compan','Limited','Manufacturing','Information','Networks','Digital','Device',
             'Network','Enterprise','System','Internet','Industr','Security',
             'system','Computer','University','Group','Software','Logic','Control','Wireless',   #type
             'communicat','Elevator','International','Lab','Research','Solution','Science',
             'Video','imaging','television','Vision','Dynamic','Mechanics',        #other
             'the','Advance','Design']
first_step_finish = open("file_first_step_finish.txt",'w')
first_step_still = open("file_first_step_still.txt",'w')
# line = f.readline()
# while line:
with open('file_more.txt','r') as f:
    for strs in f:
        flag = False
        for word in list_dict:
            if strs.lower().find(word.lower()) != -1:
            # str_list = strs.strip('\r\n').split(' ')
            # for word in str_list:
            #     if word == 'shanghai':
                flag = True
                break

                # strs.replace('word', '\r\n')
                # print strs
            else:
                flag = False


            # else:
            #     first_step_still.write(strs)
        if flag == False:
            first_step_still.write(strs)
        else:
            first_step_finish.write(strs)

                # break
#     for strs in line:
#         if strs == ' ':
#             # newline_more = line + '\n'
#             # file_more.write(line)
#             # break
#             pass
#         else:
#             print line
#             # newline_single = line + '\n'
#             # file_single.write(line)
#             # break
#             # print line
#         # file_single.write(line)
#
#

