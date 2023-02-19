with open("word_files/noun_lists/third_declension/noun_list_third_combined.txt", "w", encoding = "utf-8") as output, open("word_files/noun_lists/third_declension/noun_list_third_1.txt", encoding="utf8") as f1, open("word_files/noun_lists/third_declension/noun_list_third_2.txt", encoding="utf8") as f2, open("word_files/noun_lists/third_declension/noun_list_third_3.txt", encoding="utf8") as f3,  open("word_files/noun_lists/third_declension/noun_list_third_4.txt", encoding="utf8") as f4: 
    # getting and formatting list of words from file 1
    list_a = []
    list_b = []
    list_c = []
    list_d = []
    for file,list in zip([f1,f2,f3,f4], [list_a, list_b, list_c, list_d]):
        i = 1
        temp = None
        check = False
        for entry in file:
            if i % 2 == 1 and not entry.strip()=="":
                temp = entry
                check = True
            elif check:
                list.append([temp.strip(), entry.strip()])
                check = False
            i+=1


    # comparing the lists for repeated words
    matching = []
    lists = [list_a, list_b, list_c, list_d]
    for list in lists:
        lists.remove(list)
        for other in lists:
            for x in list:
                for y in other:
                    if x[0:x[0].index(",")+1] == y[0:y[0].index(",")+1]:
                        matching.append(x)
                        break

    # writing the combined list to the output file
    lists = [list_a, list_b, list_c, list_d]
    for list in lists:
        for item in list:
            match = False
            for m in matching:
                if m[0][0:m[0].index(",")] == item[0][0:item[0].index(",")]:
                    match=True
                    break
            if not match:
                output.write(item[0] + " | " + item[1] + "\n")

    for m in matching:
        output.write(m[0] + " | " + m[1] + "\n")