print("\n[+] Now making a dictionary...")

    # Now me must do some string modifications

    # Birthdays first

    birthdate_yy, birthdate_yyy = birthdate[-2:], birthdate[-3:]
    birthdate_yyyy = birthdate[-4:]
    birthdate_xd, birthdate_xm = birthdate[1:2], birthdate[3:4]
    birthdate_dd, birthdate_mm = birthdate[:2], birthdate[2:4]

    wifeb_yy = wifeb[-2:]
    wifeb_yyy = wifeb[-3:]
    wifeb_yyyy = wifeb[-4:]
    wifeb_xd = wifeb[1:2]
    wifeb_xm = wifeb[3:4]
    wifeb_dd = wifeb[:2]
    wifeb_mm = wifeb[2:4]

    kidb_yy = kidb[-2:]
    kidb_yyy = kidb[-3:]
    kidb_yyyy = kidb[-4:]
    kidb_xd = kidb[1:2]
    kidb_xm = kidb[3:4]
    kidb_dd = kidb[:2]
    kidb_mm = kidb[2:4]


    # Convert first letters to uppercase...
    nameup = name.title()
    surnameup = surname.title()
    nickup = nick.title()
    wifeup = wife.title()
    wifenup = wifen.title()
    kidup = kid.title()
    kidnup = kidn.title()
    petup = pet.title()
    companyup = company.title()
    wordsup = [words1.title() for words1 in words]
    word = words+wordsup

    # reverse a name

    rev_name = name[::-1]
    rev_nameup = nameup[::-1]
    rev_nick = nick[::-1]
    rev_nickup = nickup[::-1]
    rev_wife = wife[::-1]
    rev_wifeup = wifeup[::-1]
    rev_kid = kid[::-1]
    rev_kidup = kidup[::-1]

    reverse = [rev_name, rev_nameup, rev_nick, rev_nickup, rev_wife,
               rev_wifeup, rev_kid, rev_kidup]
    rev_n = [rev_name, rev_nameup, rev_nick, rev_nickup]
    rev_w = [rev_wife, rev_wifeup]
    rev_k = [rev_kid, rev_kidup]
    # Let's do some serious work! This will be a mess of code, but who cares? :)

    # Birthdays combinations
    bds = [birthdate_yy, birthdate_yyy, birthdate_yyyy, birthdate_xd,
           birthdate_xm, birthdate_dd, birthdate_mm]
    bdss = []

    for bds1 in bds:
        bdss.append(bds1)
        for bds2 in bds:
            if bds.index(bds1) != bds.index(bds2):
                bdss.append(bds1 + bds2)
                for bds3 in bds:
                    condition = (bds.index(bds1) != bds.index(bds2) and
                                 bds.index(bds2) != bds.index(bds3) and
                                 bds.index(bds1) != bds.index(bds3))
                    if condition:
                        bdss.append(bds1+bds2+bds3)


    # For a woman...
    wbds = [wifeb_yy, wifeb_yyy, wifeb_yyyy, wifeb_xd, wifeb_xm, wifeb_dd, wifeb_mm]
    wbdss = []

    for wbds1 in wbds:
        wbdss.append(wbds1)
        for wbds2 in wbds:
            if wbds.index(wbds1) != wbds.index(wbds2):
                wbdss.append(wbds1+wbds2)
                for wbds3 in wbds:
                    condition = (wbds.index(wbds1) != wbds.index(wbds2) and
                                 wbds.index(wbds2) != wbds.index(wbds3) and
                                 wbds.index(wbds1) != wbds.index(wbds3))
                    if condition:
                        wbdss.append(wbds1+wbds2+wbds3)


    # and a child...
    kbds = [kidb_yy, kidb_yyy, kidb_yyyy, kidb_xd, kidb_xm, kidb_dd, kidb_mm]
    kbdss = []

    for kbds1 in kbds:
        kbdss.append(kbds1)
        for kbds2 in kbds:
            if kbds.index(kbds1) != kbds.index(kbds2):
                kbdss.append(kbds1+kbds2)
                for kbds3 in kbds:
                    condition = (kbds.index(kbds1) != kbds.index(kbds2) and
                                 kbds.index(kbds2) != kbds.index(kbds3) and
                                 kbds.index(kbds1) != kbds.index(kbds3))
                    if condition:
                        kbdss.append(kbds1+kbds2+kbds3)

    # string combinations
    kombinaac = [pet, petup, company, companyup]
    kombina = [name, surname, nick, nameup, surnameup, nickup]
    kombinaw = [wife, wifen, wifeup, wifenup, surname, surnameup]
    kombinak = [kid, kidn, kidup, kidnup, surname, surnameup]

    kombinaa = []
    for kombina1 in kombina:
        kombinaa.append(kombina1)
        for kombina2 in kombina:
            condition = (kombina.index(kombina1) != kombina.index(kombina2) and
                         kombina.index(kombina1.title()) != kombina.index(kombina2.title()))
            if condition:
                kombinaa.append(kombina1+kombina2)

    kombinaaw = []
    for kombina1 in kombinaw:
        kombinaaw.append(kombina1)
        for kombina2 in kombinaw:
            condition = (kombinaw.index(kombina1) != kombinaw.index(kombina2) and
                         kombinaw.index(kombina1.title()) != kombinaw.index(kombina2.title()))
            if condition:
                kombinaaw.append(kombina1+kombina2)

    kombinaak = []
    for kombina1 in kombinak:
        kombinaak.append(kombina1)
        for kombina2 in kombinak:
            condition = (kombinak.index(kombina1) != kombinak.index(kombina2) and
                         kombinak.index(kombina1.title()) != kombinak.index(kombina2.title()))
            if condition:
                kombinaak.append(kombina1+kombina2)


    komb1 = list(komb(kombinaa, bdss))
    komb2 = list(komb(kombinaaw, wbdss))
    komb3 = list(komb(kombinaak, kbdss))
    komb4 = list(komb(kombinaa, CONFIG['years']))
    komb5 = list(komb(kombinaac, CONFIG['years']))
    komb6 = list(komb(kombinaaw, CONFIG['years']))
    komb7 = list(komb(kombinaak, CONFIG['years']))
    komb8 = list(komb(word, bdss))
    komb9 = list(komb(word, wbdss))
    komb10 = list(komb(word, kbdss))
    komb11 = list(komb(word, CONFIG['years']))
    komb12 = komb13 = komb14 = komb15 = komb16 = komb21 = []
    if randnum == "y":
        komb12 = list(concats(word, CONFIG['numfrom'], CONFIG['numto']))
        komb13 = list(concats(kombinaa, CONFIG['numfrom'], CONFIG['numto']))
        komb14 = list(concats(kombinaac, CONFIG['numfrom'], CONFIG['numto']))
        komb15 = list(concats(kombinaaw, CONFIG['numfrom'], CONFIG['numto']))
        komb16 = list(concats(kombinaak, CONFIG['numfrom'], CONFIG['numto']))
        komb21 = list(concats(reverse, CONFIG['numfrom'], CONFIG['numto']))
    komb17 = list(komb(reverse, CONFIG['years']))
    komb18 = list(komb(rev_w, wbdss))
    komb19 = list(komb(rev_k, kbdss))
    komb20 = list(komb(rev_n, bdss))
    komb001 = komb002 = komb003 = komb004 = komb005 = komb006 = []
    if spechars1 == "y":
        komb001 = list(komb(kombinaa, spechars))
        komb002 = list(komb(kombinaac, spechars))
        komb003 = list(komb(kombinaaw, spechars))
        komb004 = list(komb(kombinaak, spechars))
        komb005 = list(komb(word, spechars))
        komb006 = list(komb(reverse, spechars))

