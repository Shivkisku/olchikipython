ᱩᱢᱮᱨ = ᱤᱱᱛ(ᱤᱱᱯᱩᱛ("Enter your age: "))
ᱡᱩᱫᱤ ᱩᱢᱮᱨ >= 18:
    ᱚᱞ("You are old enough to learn to drive.")
ᱮᱨᱨ:
    ᱚᱞ(f"You need {18 - ᱩᱢᱮᱨ} more years to learn to drive.")



######################################################################

ᱤᱱᱟ_ᱩᱢᱟᱨ = ᱤᱱᱛ(ᱤᱱᱯᱩᱛ("Enter my age: "))
ᱟᱢᱟ_ᱩᱢᱟᱨ = ᱤᱱᱛ(ᱤᱱᱯᱩᱛ("Enter your age: "))
ᱡᱩᱫᱤ ᱤᱱᱟ_ᱩᱢᱟᱨ > ᱟᱢᱟ_ᱩᱢᱟᱨ:
    ᱚᱞ(f"I am {ᱤᱱᱟ_ᱩᱢᱟᱨ - ᱟᱢᱟ_ᱩᱢᱟᱨ} years older than you.")
elif ᱤᱱᱟ_ᱩᱢᱟᱨ == ᱟᱢᱟ_ᱩᱢᱟᱨ:
    ᱚᱞ("Our ages are the same.")
ᱮᱨᱨ:
    ᱚᱞ(f"You are {ᱟᱢᱟ_ᱩᱢᱟᱨ - ᱤᱱᱟ_ᱩᱢᱟᱨ} years older than me.")



#############################################################################


ᱪᱟᱸᱫᱚ = ᱤᱱᱯᱩᱛ("Enter month: ")
ᱡᱩᱫᱤ ᱪᱟᱸᱫᱚ in ['September', 'October', 'November']:
    ᱚᱞ("Autumn")
elif ᱪᱟᱸᱫᱚ in ['December', 'January', 'February']:
    ᱚᱞ("Winter")
elif ᱪᱟᱸᱫᱚ in ['March', 'April', 'May']:
    ᱚᱞ("Spring")
elif ᱪᱟᱸᱫᱚ in ['June', 'July', 'August']:
    ᱚᱞ("Summer")
ᱮᱨᱨ:
    ᱚᱞ("Enter the month correctly.")


##############################################################


ᱡᱚ = ['banana', 'orange', 'mango', 'lemon']
ᱱᱩᱛᱩᱢ = ᱤᱱᱯᱩᱛ("Enter a fruit: ")
ᱡᱩᱫᱤ ᱱᱩᱛᱩᱢ not in ᱡᱚ:
    ᱡᱚ.append(ᱱᱩᱛᱩᱢ)
    ᱚᱞ(ᱡᱚ)
ᱮᱨᱨ:
    ᱚᱞ("That fruit already exists in the list.")