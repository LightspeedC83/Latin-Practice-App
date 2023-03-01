# yes, that's an excellent point, thank you for asking. there is most certainly a better way to do this, I am just lazy
# source = https://dcc.dickinson.edu/latin-core-list1
with open("word_files/medium_database/medium.xml","r", encoding="utf-8") as mdatabase, open("word_files/medium_database/medium_output.txt","w", encoding="utf-8") as output:
    key = -1

    headword = ""
    definition = ""
    part_of_speech = ""
    semantic_group = ""
    frequency = ""

    for entry in mdatabase:

        if "key=" in entry: # identifies the object we are currently working with
            output.write(f"{key}|{headword}|{definition}|{part_of_speech}|{semantic_group}|{frequency}"+"\n")
            key+=1
            
        else:
            if "![CDATA" in entry:  #if we are currently looking at the headword
                headword = entry[entry.index(">")+1 : entry.index("</a>")]

            elif "field_definition" in entry:  #if we're looking at the definition
                definition = entry[entry.index(">")+1 : entry.index("</")]

            elif "field_part_of_speech" in entry:  #if we're looking at pos
                part_of_speech = entry[entry.index(">")+1 : entry.index("</")]

            elif "field_semantic_group" in entry:  #if we're looking at semantic group
                semantic_group = entry[entry.index(">")+1 : entry.index("</")]

            elif "field_frequency_rank" in entry:  #if we're looking at frequency
                frequency = entry[entry.index(">")+1 : entry.index("</")]