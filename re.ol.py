import re

ᱛᱽᱛ = 'I love python and javaScript'

match = re.match('I love', ᱛᱽᱛ, re.I)
ᱚᱞ(match)  

span = match.span()
ᱚᱞ(span)     

ᱮᱦᱩᱵ, ᱢᱩᱪᱟᱹᱫ = span
ᱚᱞ(ᱮᱦᱩᱵ, ᱢᱩᱪᱟᱹᱫ)  
ᱵᱷᱮᱥᱩᱛᱟᱢ = ᱛᱽᱛ[ᱮᱦᱩᱵ:ᱢᱩᱪᱟᱹᱫ]
ᱚᱞ(ᱵᱷᱮᱥᱩᱛᱟᱢ)


############################################

import re

ᱛᱽᱛ = 'I love python and javaScript'
ᱥᱩᱢᱟᱱ = re.search('I love', ᱛᱽᱛ, re.I)
ᱚᱞ(ᱥᱩᱢᱟᱱ)  



import re

ᱛᱽᱛ = 'I love python and javaScript'
ᱥᱩᱢᱟᱱ = re.search('I like to teach', ᱛᱽᱛ, re.I)
ᱚᱞ(ᱥᱩᱢᱟᱱ)  


########################################




