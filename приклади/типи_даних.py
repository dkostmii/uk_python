from пітон import множина, текст, словник, список, логічне, число, Істина, Хиба, надрукувати

надрукувати(Істина == логічне(1))
надрукувати(Хиба == логічне(0))

шість = sum(список((1, 2, 3)))
надрукувати(шість)

мій_словник = словник(
    слово="діло",
    правда=Істина,
    брехня=Хиба,
    одиниця=число(Істина),
    нуль=число(Хиба),
    двійкове=множина((1, 0, 1)),
    десять=текст(1) + текст(0)
)
надрукувати(мій_словник)