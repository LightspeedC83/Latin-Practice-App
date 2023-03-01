a_long = "ā"
e_long = "ē"
i_long = "ī"
o_long = "ō"
u_long = "ū"

with open ("word_files/noun_lists/one_big_noun_thing.txt", encoding="utf8") as nouns:
    d1,d2,d2n,d3,d3n,d4,d5 = [],[],[],[],[],[],[] #creating all the word lists for each declension. Entries will be in the form: (principle parts, gender, definition)

    for line in nouns: 
        # breaking each word entry into 
        entry = line[0:line.index("|")]
        definition = line[line.index("|")+1:]
        gender = entry[entry.index("("):entry.index(")")+1]

        p_parts = entry[0:entry.index(gender)].strip().split(", ")
        p_parts_new = []
        for x in p_parts:
            if x == "":
                continue
            new = x
            if new[-1] == ",":
                new = new[0:new.index(",")]
            p_parts_new.append(new)
        p_parts=p_parts_new
        
        # seeing if it's first declension
        if p_parts[0][-1] == "a": 
            if len(p_parts) == 1: # if there is only one entry for principle parts and that ends in an a, we assume it's 1st declension
                d1.append((p_parts,gender,definition))
            elif p_parts[1][-2:] == "ae": 
                d1.append((p_parts,gender,definition))

        # checking second and fourth declension (or 3n with nominative ending in us)
        elif p_parts[0][-2:] == "us":
            if len(p_parts) == 1: # it assumes it is second declension if there is only one principle part
                d2.append((p_parts,gender,definition))
            elif p_parts[1][-1:] == "i" or p_parts[1][-1:] == i_long: #classifying as second
                d2.append((p_parts,gender,definition))
            elif p_parts[1][-2:] == "us" or p_parts[1][-2:] == u_long+"s": # classifying as fourth
                d4.append((p_parts,gender,definition))
            else: # if it is third neuter with nominative ending in us
                d3n.append((p_parts,gender,definition))
        
        # checking second neuter
        elif p_parts[0][-2:] == "um":
            if len(p_parts) == 1: # if only 1 pp, it assumes that it is 2n
                d2n.append((p_parts,gender,definition))
            elif p_parts[1][-1:] == "i" or p_parts[1][-1:] == i_long:
                d2n.append((p_parts,gender,definition))
        
        # checking fifth
        elif p_parts[0][-2:] in ["es", f"{e_long}s"]:
            if len(p_parts) == 1: # if only 1 pp it assumes 5th
                d5.append((p_parts,gender,definition))
            elif p_parts[1][-2:] in  ["ei", f"{e_long}i", e_long+i_long, f"e{i_long}"]:
                d5.append((p_parts,gender,definition))

        elif gender in ["n", "n.", "N", "N."]:  # 3rd neuter
            d3n.append((p_parts,gender,definition))
        else: # 3rd declension
            d3.append((p_parts,gender,definition))

    with open("sorted.txt", "w", encoding="utf-8") as output:
        for declension in [d1,d2,d2n,d3,d3n,d4,d5]:
            output.write("\n"+"-"*50+"\n"+"next_declesnion"+"\n"+"-"*50+"\n"*2)
            for x in declension:
                output.write(str(x))
                output.write("\n")
