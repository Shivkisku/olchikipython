ᱡᱚ = ('banana', 'orange', 'mango', 'lemon')
ᱡᱚ = list(ᱡᱚ)
ᱡᱚ[0] = 'apple'
ᱚᱞ(ᱡᱚ)     # ['apple', 'orange', 'mango', 'lemon']
ᱡᱚ = ᱨᱚᱛᱤ(ᱡᱚ)
ᱚᱞ(ᱡᱚ)     # ('apple', 'orange', 'mango', 'lemon')


####################################################################


ᱡᱚ = ('banana', 'orange', 'mango', 'lemon')
ᱚᱞ('orange' in ᱡᱚ) # True
ᱚᱞ('apple' in ᱡᱚ) # False
ᱡᱚ[1] = 'apple' # TypeError: 'tuple' object does not support item assignment



#####################################################################


ᱛᱯ_ᱫᱟᱫᱟ = ('ram', 'bonga', 'som')  
ᱛᱯ_ᱫᱤᱫᱤ = ('sanjli',)  

ᱛᱯ_ᱵᱚᱭᱦᱟ = ᱛᱯ_ᱫᱟᱫᱟ + ᱛᱯ_ᱫᱤᱫᱤ  
ᱚᱞ(ᱛᱯ_ᱵᱚᱭᱦᱟ)  

ᱚᱞ(ᱞᱮᱱ(ᱛᱯ_ᱵᱚᱭᱦᱟ))  



##################################################


ᱡᱚ = ('banana', 'orange', 'mango', 'lemon')  # Creating a tuple with fruit names.
ᱥᱟᱵᱡᱤ = ('Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot')  # Creating a tuple with vegetable names.
ᱡᱟᱱᱣᱟᱨ_ᱫᱚᱵᱟᱲ = ('milk', 'curd')  # Creating a tuple with ᱡᱟᱱᱣᱟᱨ product names.
ᱡᱚᱢᱟᱦ = ᱡᱚ + ᱥᱟᱵᱡᱤ + ᱡᱟᱱᱣᱟᱨ_ᱫᱚᱵᱟᱲ  # Concatenating the fruit, vegetable, and ᱡᱟᱱᱣᱟᱨ product tuples.
ᱚᱞ(ᱡᱚᱢᱟᱦ)  # ᱚᱞing the tuple containing all ᱫᱟᱠᱟ items.



##################################################################

ᱡᱚ = ('banana', 'orange', 'mango', 'lemon')  # Creating a tuple with fruit names.
ᱥᱟᱵᱡᱤ = ('Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot')  # Creating a tuple with vegetable names.
ᱡᱟᱱᱣᱟᱨ_ᱫᱚᱵᱟᱲ = ('milk', 'curd')  # Creating a tuple with ᱡᱟᱱᱣᱟᱨ product names.
ᱡᱚᱢᱟᱦ = ᱡᱚ + ᱥᱟᱵᱡᱤ + ᱡᱟᱱᱣᱟᱨ_ᱫᱚᱵᱟᱲ  # Concatenating the fruit, vegetable, and ᱡᱟᱱᱣᱟᱨ product tuples.
ᱚᱞ(ᱡᱚᱢᱟᱦ)  # ᱚᱞing the tuple containing all ᱫᱟᱠᱟ items.


ᱡᱩᱫᱤ ᱞᱮᱱ(ᱡᱚᱢᱟᱦ) % 2 == 0:
    ᱚᱞ(ᱡᱚᱢᱟᱦ[(ᱞᱮᱱ(ᱡᱚᱢᱟᱦ) // 2) - 1])
    ᱚᱞ(ᱡᱚᱢᱟᱦ[ᱞᱮᱱ(ᱡᱚᱢᱟᱦ) // 2])
ᱮᱨᱨ:
    ᱚᱞ(ᱡᱚᱢᱟᱦ[ᱞᱮᱱ(ᱡᱚᱢᱟᱦ) // 2])


###############################################################################################


ᱱᱚᱨᱫᱤᱪ_ᱫᱤᱥᱚᱢs = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')  # Creating a tuple with ᱱᱚᱨᱫᱤᱪ country names.


ᱡᱩᱫᱤ 'Estonia' in ᱱᱚᱨᱫᱤᱪ_ᱫᱤᱥᱚᱢs:
    ᱚᱞ("Estonia is a ᱱᱚᱨᱫᱤᱪ country")


ᱡᱩᱫᱤ 'Iceland' in ᱱᱚᱨᱫᱤᱪ_ᱫᱤᱥᱚᱢs:
    ᱚᱞ("Iceland is a Nordic country")




