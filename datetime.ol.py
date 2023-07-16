import datetime

ᱚᱞ(ᱫᱤᱨ(datetime))


##################################

from datetime import datetime

ᱱᱤᱛ = datetime.ᱱᱤᱛ()
ᱚᱞ(ᱱᱤᱛ) 


#######################################


from datetime import datetime

ᱱᱟᱣᱟ_ᱵᱚᱪᱦᱚᱨ = datetime(2023, 3, 15)
ᱚᱞ(ᱱᱟᱣᱟ_ᱵᱚᱪᱦᱚᱨ)


#######################################

from datetime import datetime

# Current date and time
ᱱᱤᱛ = datetime.ᱱᱤᱛ()

# Get the time in HH:MM:SS format
t = ᱱᱤᱛ.strftime('%H:%M:%S')
ᱚᱞ('time:', t)

# Format time as mm/dd/YYYY, HH:MM:SS
ᱚᱠᱛᱟ_ᱢᱮᱫ = ᱱᱤᱛ.strftime('%m/%d/%Y, %H:%M:%S')
ᱚᱞ('time one:', ᱚᱠᱛᱟ_ᱢᱮᱫ)

# Format time as dd/mm/YYYY, HH:MM:SS
ᱚᱠᱛᱟ_ᱵᱟᱨ = ᱱᱤᱛ.strftime('%d/%m/%Y, %H:%M:%S')
ᱚᱞ('time two:', ᱚᱠᱛᱟ_ᱵᱟᱨ)


###########################################################


from datetime import datetime

ᱫᱤᱱ_ᱵᱟᱵᱮᱨ = "23 July, 2023"
ᱚᱞ("date_string =", ᱫᱤᱱ_ᱵᱟᱵᱮᱨ)

ᱫᱤᱱ_ᱡᱮᱱᱤᱥᱦ = datetime.strptime(ᱫᱤᱱ_ᱵᱟᱵᱮᱨ, "%d %B, %Y")
ᱚᱞ("date_object =", ᱫᱤᱱ_ᱡᱮᱱᱤᱥᱦ)


############################################################



from datetime import time

# time(hour = 0, minute = 0, second = 0)
a = ᱚᱠᱛᱟ()
ᱚᱞ("a =", a)

# time(hour, minute and second)
b = ᱚᱠᱛᱟ(10, 30, 50)
ᱚᱞ("b =", b)

# time(hour, minute and second)
c = ᱚᱠᱛᱟ(hour=10, minute=30, second=50)
ᱚᱞ("c =", c)

# time(hour, minute, second, microsecond)
d = ᱚᱠᱛᱟ(10, 30, 50, 200555)
ᱚᱞ("d =", d)


########################################################