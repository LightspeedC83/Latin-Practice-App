with open("word_files/noun_lists/fifth_declension/noun_list_fifth_combined.txt", "w", encoding = "utf-8") as output, open("word_files/noun_lists/fifth_declension/noun_list_fifth_1.txt", encoding="utf8") as f1, open("word_files/noun_lists/fifth_declension/noun_list_fifth_2.txt", encoding="utf8") as f2, open("word_files/noun_lists/fifth_declension/noun_list_fifth_3.txt", encoding="utf8") as f3: 
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
    list_c = []
    for x in f3:
        list_c.append([x[0:x.index("|")].strip() + ", -ei", x[x.index("|")+1:].strip()])

    # comparing the two lists for repeated words
    matching = []
    for x in list_a:
        for y in list_b:
            if x[0][0:x[0].index(",")] == y[0]:
                matching.append(x)
                break

    for z in list_c:
        for x in list_a:
            if x[0][0:x[0].index(",")] == z[0][0:z[0].index(",")]:
                matching.append(z)
                break
        for y in list_b:
            if y[0] == z[0][0:z[0].index(",")]:
                matching.append(z)
                break

    # writing the combined list to the output file
    for z in list_c:
        if z not in matching:
            output.write(z[0] + " | " + z[1] + "\n")

    for x in list_a:
        match = False
        for m in matching:
            if m[0][0:m[0].index(",")] == x[0][0:x[0].index(",")]:
                match=True
                break
        if not match:
            output.write(x[0] + " | " + x[1] + "\n")

    for y in list_b:
        match = False
        for m in matching:
           if m[0][0:m[0].index(",")] == y[0]:
                match = True
                break
        if not match:
            output.write(y[0] + " | " + y[1] + "\n")

    # for x in matching:
    #     print(x)
    # for m in matching:
    #     output.write(m[0] + " | " + m[1] + "\n")