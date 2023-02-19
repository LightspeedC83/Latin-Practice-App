with open("word_files/noun_lists/first_declension/noun_list_first_combined.txt", encoding="utf8") as d1, open("word_files/noun_lists/second_declension/noun_list_second_combined.txt", encoding="utf8") as d2, open("word_files/noun_lists/second_declension_neuter/noun_list_second_neuter_combined.txt", encoding="utf8") as d2n, open("word_files/noun_lists/third_declension/noun_list_third_combined_removed_duplicates.txt", encoding="utf8") as d3, open("word_files/noun_lists/fourth_declension/noun_list_fourth_combined.txt", encoding="utf8") as d4, open("word_files/noun_lists/fifth_declension/noun_list_fifth_combined_checked.txt", encoding="utf8") as d5:
    first, second, second_n, third, fourth, fifth = [],[],[],[],[],[]
    for list, file in zip([first, second, second_n, third, fourth, fifth], [d1,d2,d2n,d3,d4,d5]):
        for entry in file:
            formatted = [entry[0:entry.index("|")].strip(), entry[entry.index("|")+1:].strip()]
            for gender in [" f", " f.", " m", " m.", " n", " n."]:
                if gender in formatted[0]:
                    formatted[0] = formatted[0][0:formatted[0].index(gender)] + f" ({gender.strip()})"
            list.append(formatted)
    
    for list in [first, second, second_n, third, fourth, fifth]:
        for entry in list:
            # print(entry)