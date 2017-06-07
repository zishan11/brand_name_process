list_dict = ['New Zealand','America','USA','China','Japan','Europe','Asia','Korea','Universal','Global','Switzerland','India',                             #country
             'shanghai','shenzhen','Guangdong','guangzhou','Beijing','City','Taiwan','Shandong','Nanjing','suzhou','Anhui','Wuhan',
             'Hangzhou','Chongqing','Fujian','Chengdu','dongguan','Huizhou',   #city
              'west','east','north','south',   #direction
             'Electronic','elec','technolo','data','Optical','Product',  #tech
             'Compan','Limited','Manufacturing','Information','Networks','Digital','Device','corporate',
             'Network','Enterprise','System','Internet','Industr','Security','Engineer','Innovation',
             'system','Computer','University','Group','Software','Logic','Control','Wireless','Equipment',   #type
             'communicat','Elevator','International','Lab','Research','Solution','Science',
             'Video','imaging','television','Vision','Dynamic','Mechanics','develop',        #other
             'the','Advance','Design','transmiss','Cinema','Access','Online','Private','Mobile']

file_fourth_step_single = open('file_fourth_step_single.txt','a')
file_fourth_step_double = open('file_fourth_step_double.txt','a')
file_fourth_step_triple = open('file_fourth_step_triple.txt','a')
file_fourth_step_quatary = open('file_fourth_step_quatary.txt','a')
file_fourth_step_penta = open('file_fourth_step_penta.txt','a')

file_third_step_transto_double = open('file_third_step_transto_double.txt','w')
with open('file_second_step_triple.txt','r') as f:
    for strs in f:
        strs_list = strs.strip('\r\n').split(' ')
        # for word in strs_list:

        flag = []
        length = len(strs_list)
        for word in list_dict:
            # if word in list_dict:
            if strs.lower().find(word.lower()) != -1:
                for i in range(length):
                    if strs_list[i].lower().find(word.lower()) != -1:
                        if i in flag:
                            pass
                        else:
                            flag.append(i)

        if len(set(flag)) != length:
            for i in flag:
                strs_list[i] = ' '
        else:
             pass

        if (len(strs_list) - strs_list.count(' ')) == 1:
             word_len = 0
             for word in strs_list:
                 if word == ' ':
                     pass
                 else:
                     word_len = word_len + len(word) + 1
                     file_fourth_step_single.write(word + ' ')

             for i in range(40 - word_len):
                 file_fourth_step_single.write(' ')
             file_fourth_step_single.write('          # ' + strs)
             # strs_list.remove(word)

        elif (len(strs_list) - strs_list.count(' ')) == 2:
             word_len = 0
             for word in strs_list:
                 if word == ' ':
                     pass
                 else:
                     word_len = word_len + len(word) + 1
                     file_fourth_step_double.write(word + ' ')

             for i in range(40 - word_len):
                 file_fourth_step_double.write(' ')
             file_fourth_step_double.write('          # ' + strs)

        elif (len(strs_list) - strs_list.count(' ')) == 3:
             word_len = 0
             for word in strs_list:
                 if word == ' ':
                     pass
                 else:
                     word_len = word_len + len(word) + 1
                     file_fourth_step_triple.write(word + ' ')

             for i in range(40 - word_len):
                 file_fourth_step_triple.write(' ')
             file_fourth_step_triple.write('          # ' + strs)

        elif (len(strs_list) - strs_list.count(' ')) == 4:
             word_len = 0
             for word in strs_list:
                 if word == ' ':
                     pass
                 else:
                     word_len = word_len + len(word) + 1
                     file_fourth_step_quatary.write(word + ' ')

             for i in range(40 - word_len):
                 file_fourth_step_quatary.write(' ')
             file_fourth_step_quatary.write('          # ' + strs)

        else:
             word_len = 0
             for word in strs_list:
                 if word == ' ':
                     pass
                 else:
                     word_len = word_len + len(word) + 1
                     file_fourth_step_penta.write(word + ' ')

             for i in range(40 - word_len):
                 file_fourth_step_penta.write(' ')
             file_fourth_step_penta.write('          # ' + strs)

                # strs_list.remove(word)

        word_len = 0
        for word in strs_list:
            if word == ' ':
                pass
            else:
                word_len = word_len + len(word) + 1
                file_third_step_transto_double.write(word+ ' ')
        # j = 0
        # while strs_list[j]:
        #     file_third_step_transto_single.write(strs_list[j])
        #     j = j+1
        #
        for i in range(40 - word_len):
            file_third_step_transto_double.write(' ')
        file_third_step_transto_double.write('          # ' + strs)