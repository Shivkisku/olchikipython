ᱫᱚᱦ_ᱪᱚᱢᱯᱟᱱᱤᱮ = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
ᱩᱢᱮᱨ = [22, 19, 24, 25, 26, 24, 25, 24]


ᱚᱞ("length of set is :", ᱞᱮᱱ(ᱫᱚᱦ_ᱪᱚᱢᱯᱟᱱᱤᱮ))


# Add 'Twitter' to ᱫᱚᱦ_ᱪᱚᱢᱯᱟᱱᱤᱮ
ᱫᱚᱦ_ᱪᱚᱢᱯᱟᱱᱤᱮ.ᱥᱮᱞᱮᱫ('Twitter')
ᱚᱞ(ᱫᱚᱦ_ᱪᱚᱢᱯᱟᱱᱤᱮ)

# Insert multiple IT companies at once to the set ᱫᱚᱦ_ᱪᱚᱢᱯᱟᱱᱤᱮ
ᱫᱚᱦ_ᱪᱚᱢᱯᱟᱱᱤᱮ.update(['Infosys', 'Firmonyx'])
ᱚᱞ(ᱫᱚᱦ_ᱪᱚᱢᱯᱟᱱᱤᱮ)


# Remove one of the companies from the set ᱫᱚᱦ_ᱪᱚᱢᱯᱟᱱᱤᱮ
ᱫᱚᱦ_ᱪᱚᱢᱯᱟᱱᱤᱮ.remove('Facebook')
ᱚᱞ(ᱫᱚᱦ_ᱪᱚᱢᱯᱟᱱᱤᱮ)



#######################################################



# Given sets
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

# Join A and B
C = A.union(B)
ᱚᱞ(C)


# Find A intersection B
C = A.intersection(B)
ᱚᱞ(C)


################################################################



#Given sets
ᱩᱢᱮᱨ = [22, 19, 24, 25, 26, 24, 25, 24]

# Convert the ages to a set and compare the length of the list and the set, which one is bigger?
ᱩᱢᱮᱨ_ᱥᱮᱛ = ᱥᱮᱛ(ᱩᱢᱮᱨ)
ᱞᱮᱱ_ᱞᱤᱥᱴ = ᱞᱮᱱ(ᱩᱢᱮᱨ)
ᱞᱮᱱ_ᱥᱮᱛ = ᱞᱮᱱ(ᱩᱢᱮᱨ_ᱥᱮᱛ)
ᱚᱞ("Length of list : ", ᱞᱮᱱ_ᱞᱤᱥᱴ)
ᱚᱞ("Length of set : ", ᱞᱮᱱ_ᱥᱮᱛ)
ᱚᱞ("Length of list is bigger than length of set : ", ᱞᱮᱱ_ᱞᱤᱥᱴ > ᱞᱮᱱ_ᱥᱮᱛ)






