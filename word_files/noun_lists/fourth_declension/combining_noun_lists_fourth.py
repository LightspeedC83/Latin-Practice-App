with open("word_files/noun_lists/fourth_declension/noun_list_fourth_combined.txt", "w", encoding = "utf-8") as output, open("word_files/noun_lists/fourth_declension/noun_list_fourth_1.txt") as f1, open("word_files/noun_lists/fourth_declension/noun_list_fourth_2.txt", encoding="utf8") as f2: 
    # getting and formatting list of words from file 1
    list_a = []
    list_b = []
    for file,list in zip([f1,f2], [list_a, list_b]):
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

    # comparing the two lists for repeated words
    matching = []
    for x in list_a:
        for y in list_b:
            if x[0][0:x[0].index(",")] == y[0][0:y[0].index("-")-1]:
                matching.append(x)
                break
    
    # writing the combined list to the output file
    for x in list_a:
        if x not in matching:
            output.write(x[0] + " | " + x[1] + "\n")
    for y in list_b:
        match = False
        for m in matching:
           if m[0][0:m[0].index(",")] == y[0][0:y[0].index("-")-1]:
               match = True
        
        if not match:
            output.write(y[0] + " | " + y[1] + "\n")
    for m in matching:
        output.write(m[0] + " | " + m[1] + "\n")
