
with open("word_files/noun_lists/third_declension/noun_list_third_combined.txt", "r", encoding="utf8") as f, open("word_files/noun_lists/third_declension/noun_list_third_combined_removed_duplicates.txt", "w", encoding="utf8") as f2:
    listed = []
    for entry in f:
        listed.append(entry.strip())
    
    listed1 = listed[:]
    duplicates = []
    for x in listed:
        listed1.remove(x)
        for y in listed1:
            if x[0:x.index(',')] == y[0:y.index(',')]:
                duplicates.append(x)
    
    
    for x in listed:
        match = False
        for d in duplicates:
            if x == d:
                match = True
                break
        if not match:
            f2.write(x+"\n")
