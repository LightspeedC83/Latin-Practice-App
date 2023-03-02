import nouns
import dickinson_database as dickinson_db


noun_list = []

# parsing through the dickinson database
for entry in dickinson_db.data:

    # if it is a noun:
    if "noun" in entry[3].lower() and "pronoun" not in entry[3].lower():
        # determining the declension
        declension = 0
        for x in entry[3]:
            if x.isdigit():
                declension = int(x)
                break
        
        if declension == 2 and entry[1][-2] == "n":
            declension = 2.5
        if declension == 3 and entry[1][-2] == "n":
            declension = 3.5

        ###################### YOU NEED TO COME BACK AND DEAL WITH INDECLINABLE NOUNS   
        if declension ==0:
            continue 
        #####################

        # getting the stem
        if declension in [3, 3.5]:
            pass
        elif declension == 1:
            stem = entry[1].split()[0][:-1] 
        else:
            stem = entry[1].split()[0][:-2]
        
        noun_list.append(nouns.Noun(p_parts=entry[1], stem=stem, declension=declension, gender=entry[1][-2], definition=entry[2]))

for x in noun_list:
    print(x.decline())
