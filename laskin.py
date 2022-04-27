lasku_tapa = input ("Haluatko laskea kertolaskuja (K) pluslaskuja (P) miinuslaskuja (M) jakolaskuja (J) vai potensseja (PO)? ")
if lasku_tapa == "P":
    eka = input ("Valitse ensimmäinen luku: ")
    toka = input ("Valitse toinen luku: ")
    vastaus = float(eka) + float(toka)
    print (vastaus)
if lasku_tapa == "K":
    eka = input ("Valitse ensimmäinen luku: ")
    toka = input ("Valitse toinen luku: ")
    vastaus = float(eka) * float(toka)
    print (vastaus)
if lasku_tapa == "M":
    eka = input ("Valitse ensimmäinen luku: ")
    toka = input ("Valitse toinen luku: ")
    vastaus = float(eka) - float(toka)
    print (vastaus)
if lasku_tapa == "J":
    eka = input ("Valitse ensimmäinen luku: ")
    toka = input ("Valitse toinen luku: ")
    vastaus = float(eka) / float(toka)
    print (vastaus)
if lasku_tapa == "PO":
    eka = input ("Valitse ensimmäinen luku: ")
    toka = input ("Valitse toinen luku: ")
    vastaus = float(eka) ** float(toka)
    print (vastaus)
