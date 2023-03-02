a_long = "ā"
e_long = "ē"
i_long = "ī"
o_long = "ō"
u_long = "ū"

first_declension = [
    # singluar
    "a", # nominative
    "ae", # genitive
    "ae", # dative
    "am", # accusative
    a_long, # ablative
    "a", # vocative

    # plural
    "ae", # nominative
    "arum", # genitive
    i_long+"s", # dative
    a_long+"s", # accusative
    i_long+"s", # ablative
    "ae" # vocative
]

second_declension = [
    # singluar
    "us", # nominative
    i_long, # genitive
    o_long, # dative
    "um", # accusative
    o_long, # ablative 
    "e", # vocative (unless the word ends in '-ius', in which case the vocative ending would be i_long)

    # plural
    i_long, # nominative
    "orum", # genitive
    i_long+"s", # dative
    o_long+"s", # accusative
    i_long+"s", # ablative 
    i_long
]

second_neuter = [
    # singluar
    "um", # nominative
    "i", # genitive
    "o", # dative
    "um", # accusative
    "o", # abative
    "um", # vocative

    # pluaral
    "a", # nominative
    "orum", # genitive
    i_long+"s", # dative
    "a", # accusative
    i_long+"s", # abative
    "a" # vocative
]

third_declension = [
    # singular
    None,
    "is",
    i_long,
    "em",
    "e",
    None,

    # plural
    e_long+"s",
    "um",
    "ibus",
    e_long+"s",
    "ibus",
    e_long+"s"
]

third_neuter = [
    # singular
    None, # nominative
    "is", # genitive
    i_long, # dative
    None, #accusative
    "e", # ablative
    None, # vocative

    # plural
    "a", # nominative
    "um", # genitive
    "ibus", # dative
    "a", #accusative
    "ibus", # ablative
    "a", # vocative
]

fourth_declension = [
    # singular
    "us", # nominative
    u_long+"s", # genitive
    "u"+i_long, # dative (can also be u_long)
    "um", # accusative
    u_long, # ablative
    "us", # vocative

    # plural
    u_long, # nominative
    "uum", # genitive
    "ibus", # dative
    u_long, # accusative
    "ibus", # ablative
    u_long # vocative 
]

fifth_declension = [
    # singular
    e_long+"s", # nominative
    "e"+i_long, # genitive
    "e"+i_long, # dative
    "em", # accusative
    e_long, # ablative
    e_long+"s", # vocative

    # plural
    e_long+"s", # nominative
    e_long+"rum", # genitive
    e_long+"bus", # dative
    e_long+"s", # accusative
    e_long+"bus", # ablative
    e_long+"s" # vocative
]


class Noun:
    """A Latin noun. For the declension argument, the neuter declension will be expressed as 0.5 so 2nd neuter would be 2.5 and 3rd neuter would be 3.5"""
    def __init__(self, p_parts, stem, declension, gender, definition):
        self.p_parts = p_parts
        self.gender = gender
        self.stem = stem
        self.definition = definition
        # setting up the correct endings list for the given declension
        if type(declension) == int and declension in [x for x in range(1,6)]:
            self.declension = [first_declension, second_declension, third_declension, fourth_declension, fifth_declension][declension-1]
        elif declension == 2.5:
            self.declension = second_neuter
        elif declension == 3.5:
            self.declension = third_neuter
        else:
            raise ValueError("the declension parameter must be an int 1-5 or float 2.5 or 3.5")
        
        #chekcing for irregular nouns 
        # making a list of the declined word
        self.declined = []
        for ending in self.declension:
            if ending == None:
                self.declined.append(p_parts)
            else:
                self.declined.append(stem + ending)
    
    # function to print the noun an all of its forms
    def print_declined(self):
        """prints out the word in all its forms"""
        
        names = ["Nominative", "Genitive", "Dative", "Accusative", "Ablative", "Vocative"]
        
        print("-"*25+f"\n{self.p_parts.split()[0]}, {self.gender}. {self.definition}")
        print("-"*25+"\nSingular")
        for form, p_parts in zip(self.declined[0:6],names):
            print(f"\t{p_parts}: {form}")

        print("-"*25+"\nPlural:")
        for form, p_parts in zip(self.declined[6:],names):
            print(f"\t{p_parts}: {form}")
        print("-"*25)
    

# # testing stuff out 
# puella = Noun("puella -ae f.", "puell", 1, "f", "girl")

# puella.print_declined()