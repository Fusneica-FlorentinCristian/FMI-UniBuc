zilele_saptamanii={
    1:"Luni",
    2:"Marti",
    3:"Miercuri",
    4:"Joi",
    5:"Vineri",
    6:"Sambata",
    0:"Duminica"
}
lunile_anului={
    1:"Ianuarie",
    2:"Februarie",
    3:"Martie",
    4:"Aprilie",
    5:"Mai",
    6:"Iunie",
    7:"Iulie",
    8:"August",
    9:"Septembrie",
    10:"Octombrie",
    11:"Noiembrie",
    12:"Decembrie"
}
zile_luna={
    1:31,
    2:28,
    3:31,
    4:30,
    5:31,
    6:30,
    7:31,
    8:31,
    9:30,
    10:31,
    11:30,
    12:31
}

# 7. Știind că 1 ianuarie 1702 a picat într-o zi de duminică, să se citească de la tastatură o dată mai
# recentă, și să se spună în ce zi a săptămânii cade aceasta.
# Puteți să faceți 2 cazuri - în care inputul este dat de forma "1 10 2019", sau "1 octombrie 2019".
# Folosiți funcția range() pentru a itera printre ani, respectiv instrucțiuni if/elif/else pentru a trata
# cazurile de ani bisecți. Puteți folosi un dicționar sau o listă pe post de switch/case ca să aflați în ce zi a
# săptămânii pică data respectivă.
#
#
# Formula pentru an bisect (leap year) este:
# if (year is not divisible by 4) then (it is a common year)
# else if (year is not divisible by 100) then (it is a leap year)
# else if (year is not divisible by 400) then (it is a common year)
# else (it is a leap year)