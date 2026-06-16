# Koji je vaš spol?
muski = '/html/body/div[1]/div[2]/form[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/span[1]/div[1]/div[1]/label[1]/div[1]/div[1]/div[1]'
zenski = '/html/body/div[1]/div[2]/form[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/span[1]/div[1]/div[2]/label[1]/div[1]/div[1]/div[1]'
preferiramNeOdgovoriti = '/html/body/div[1]/div[2]/form[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/span[1]/div[1]/div[3]/label[1]/div[1]/div[1]/div[1]'
genders = [muski, zenski, preferiramNeOdgovoriti]

# Kojoj dobnoj skupini pripadate?
age1824 = '/html/body/div[1]/div[2]/form[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/span[1]/div[1]/div[1]/label[1]/div[1]/div[1]/div[1]'
age2534 = '/html/body/div[1]/div[2]/form[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/span[1]/div[1]/div[2]/label[1]/div[1]/div[1]/div[1]'
age3544 = '/html/body/div[1]/div[2]/form[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/span[1]/div[1]/div[3]/label[1]/div[1]/div[1]/div[1]'
age4554 = '/html/body/div[1]/div[2]/form[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/span[1]/div[1]/div[4]/label[1]/div[1]/div[1]/div[1]'
age55IViseGodina = '/html/body/div[1]/div[2]/form[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/span[1]/div[1]/div[5]/label[1]/div[1]/div[1]/div[1]'
ageGroups = [age1824, age2534, age3544, age4554, age55IViseGodina]

# Koja je vaša najviša razina završenog obrazovanja?
osnovnaSkola = '/html/body/div[1]/div[2]/form[1]/div[2]/div[1]/div[2]/div[3]/div[1]/div[1]/div[2]/div[1]/div[1]/span[1]/div[1]/div[1]/label[1]/div[1]/div[1]/div[1]'
srednjaSkola = '/html/body/div[1]/div[2]/form[1]/div[2]/div[1]/div[2]/div[3]/div[1]/div[1]/div[2]/div[1]/div[1]/span[1]/div[1]/div[2]/label[1]/div[1]/div[1]/div[1]'
preddiplomskiStudijPrvostupnik = '/html/body/div[1]/div[2]/form[1]/div[2]/div[1]/div[2]/div[3]/div[1]/div[1]/div[2]/div[1]/div[1]/span[1]/div[1]/div[3]/label[1]/div[1]/div[1]/div[1]'
diplomskiStudijIliVise = '/html/body/div[1]/div[2]/form[1]/div[2]/div[1]/div[2]/div[3]/div[1]/div[1]/div[2]/div[1]/div[1]/span[1]/div[1]/div[4]/label[1]/div[1]/div[1]/div[1]'
education_groups = [osnovnaSkola, srednjaSkola, preddiplomskiStudijPrvostupnik, diplomskiStudijIliVise]

# Koliko često kupujete proizvode ili usluge putem interneta?
svakodnevno = '/html/body/div[1]/div[2]/form[1]/div[2]/div[1]/div[2]/div[4]/div[1]/div[1]/div[2]/div[1]/div[1]/span[1]/div[1]/div[1]/label[1]/div[1]/div[1]/div[1]'
nekolikoPutaTjedno = '/html/body/div[1]/div[2]/form[1]/div[2]/div[1]/div[2]/div[4]/div[1]/div[1]/div[2]/div[1]/div[1]/span[1]/div[1]/div[2]/label[1]/div[1]/div[1]/div[1]'
nekolikoPutaMjesecno = '/html/body/div[1]/div[2]/form[1]/div[2]/div[1]/div[2]/div[4]/div[1]/div[1]/div[2]/div[1]/div[1]/span[1]/div[1]/div[3]/label[1]/div[1]/div[1]/div[1]'
nekolikoPutaGodisnje = '/html/body/div[1]/div[2]/form[1]/div[2]/div[1]/div[2]/div[4]/div[1]/div[1]/div[2]/div[1]/div[1]/span[1]/div[1]/div[4]/label[1]/div[1]/div[1]/div[1]'
gotovoNikad = '/html/body/div[1]/div[2]/form[1]/div[2]/div[1]/div[2]/div[4]/div[1]/div[1]/div[2]/div[1]/div[1]/span[1]/div[1]/div[5]/label[1]/div[1]/div[1]/div[1]'
shopping_frequencies = [svakodnevno, nekolikoPutaTjedno, nekolikoPutaMjesecno, nekolikoPutaGodisnje, gotovoNikad]

# Koje digitalne kanale najčešće koristite? (možete odabrati više odgovora)
instagram = '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div[1]/div[1]/label/div/div[1]/div[2]'
facebook = '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div[1]/div[2]/label/div/div[1]/div[2]'
youtube = '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div[1]/div[3]/label/div/div[1]/div[2]'
tiktok = '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div[1]/div[4]/label/div/div[1]/div[2]'
linkedIn = '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div[1]/div[5]/label/div/div[1]/div[2]'
website = '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div[1]/div[6]/label/div/div[1]/div[2]'
newsLetter = '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div[1]/div[7]/label/div/div[1]/div[2]'
digital_channels = [instagram, facebook, youtube, tiktok, linkedIn, website, newsLetter]

# Jeste li u posljednjih 6 mjeseci primijetili digitalnu reklamnu poruku brenda koja se odnosila na ekološku održivost ili društvenu odgovornost?
daCesto = '/html/body/div[1]/div[2]/form[1]/div[2]/div[1]/div[2]/div[6]/div[1]/div[1]/div[2]/div[1]/div[1]/span[1]/div[1]/div[1]/label[1]/div[1]/div[1]/div[1]'
daPovremeno = '/html/body/div[1]/div[2]/form[1]/div[2]/div[1]/div[2]/div[6]/div[1]/div[1]/div[2]/div[1]/div[1]/span[1]/div[1]/div[2]/label[1]/div[1]/div[1]/div[1]'
rijetko = '/html/body/div[1]/div[2]/form[1]/div[2]/div[1]/div[2]/div[6]/div[1]/div[1]/div[2]/div[1]/div[1]/span[1]/div[1]/div[3]/label[1]/div[1]/div[1]/div[1]'
neNisamPrimijetio = '/html/body/div[1]/div[2]/form[1]/div[2]/div[1]/div[2]/div[6]/div[1]/div[1]/div[2]/div[1]/div[1]/span[1]/div[1]/div[4]/label[1]/div[1]/div[1]/div[1]'
digital_commercial_messages = [daCesto, daPovremeno, rijetko, neNisamPrimijetio]

# Koje vrste sadržaja su vam se najviše utisnule u pamćenje? (možete odabrati više odgovora)
co2 = '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[7]/div/div/div[2]/div[1]/div[1]/label/div/div[1]/div[2]'
recycle = '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[7]/div/div/div[2]/div[1]/div[2]/label/div/div[1]/div[2]'
fair_trade = '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[7]/div/div/div[2]/div[1]/div[3]/label/div/div[1]/div[2]'
good_care = '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[7]/div/div/div[2]/div[1]/div[4]/label/div/div[1]/div[2]'
equality = '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[7]/div/div/div[2]/div[1]/div[5]/label/div/div[1]/div[2]'
not_remember = '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[7]/div/div/div[2]/div[1]/div[6]/label/div/div[1]/div[2]'
digital_content_types = [co2, recycle, fair_trade, good_care, equality, not_remember]

# Za svaku tvrdnju označite u kojoj mjeri se ona odnosi na vas: 1 = uopće se ne odnosi, 2 = uglavnom ne, 3 = niti da niti ne, 4 = uglavnom da, 5 = u potpunosti se odnosi

# Brendovi koji komuniciraju ekološke vrijednosti djeluju mi vjerodostojno.
brendoviEkologija1 = '/html/body/div[1]/div[2]/form[1]/div[2]/div[1]/div[2]/div[8]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/span[1]/div[2]/div[1]/div[1]'
brendoviEkologija2 = '/html/body/div[1]/div[2]/form[1]/div[2]/div[1]/div[2]/div[8]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/span[1]/div[3]/div[1]/div[1]'
brendoviEkologija3 = '/html/body/div[1]/div[2]/form[1]/div[2]/div[1]/div[2]/div[8]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/span[1]/div[4]/div[1]/div[1]'
brendoviEkologija4 = '/html/body/div[1]/div[2]/form[1]/div[2]/div[1]/div[2]/div[8]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/span[1]/div[5]/div[1]/div[1]'
brendoviEkologija5 = '/html/body/div[1]/div[2]/form[1]/div[2]/div[1]/div[2]/div[8]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/span[1]/div[6]/div[1]/div[1]'
brand_ecology = [brendoviEkologija1, brendoviEkologija2, brendoviEkologija3, brendoviEkologija4, brendoviEkologija5]

# Ekološke i društveno odgovorne kampanje poboljšavaju moju ukupnu sliku o brendu.
ekologija1 = '/html/body/div[1]/div[2]/form[1]/div[2]/div[1]/div[2]/div[8]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[4]/span[1]/div[2]/div[1]/div[1]'
ekologija2 = '/html/body/div[1]/div[2]/form[1]/div[2]/div[1]/div[2]/div[8]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[4]/span[1]/div[3]/div[1]/div[1]'
ekologija3 = '/html/body/div[1]/div[2]/form[1]/div[2]/div[1]/div[2]/div[8]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[4]/span[1]/div[4]/div[1]/div[1]'
ekologija4 = '/html/body/div[1]/div[2]/form[1]/div[2]/div[1]/div[2]/div[8]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[4]/span[1]/div[5]/div[1]/div[1]'
ekologija5 = '/html/body/div[1]/div[2]/form[1]/div[2]/div[1]/div[2]/div[8]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[4]/span[1]/div[6]/div[1]/div[1]'
ecology = [ekologija1, ekologija2, ekologija3, ekologija4, ekologija5]

# Brend koji aktivno komunicira svoju društvenu odgovornost doživljavam kao pouzdanijeg od onih koji to ne čine.
brendoviDrustvo1 = '/html/body/div[1]/div[2]/form[1]/div[2]/div[1]/div[2]/div[8]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[6]/span[1]/div[2]/div[1]/div[1]'
brendoviDrustvo2 = '/html/body/div[1]/div[2]/form[1]/div[2]/div[1]/div[2]/div[8]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[6]/span[1]/div[3]/div[1]/div[1]'
brendoviDrustvo3 = '/html/body/div[1]/div[2]/form[1]/div[2]/div[1]/div[2]/div[8]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[6]/span[1]/div[4]/div[1]/div[1]'
brendoviDrustvo4 = '/html/body/div[1]/div[2]/form[1]/div[2]/div[1]/div[2]/div[8]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[6]/span[1]/div[5]/div[1]/div[1]'
brendoviDrustvo5 = '/html/body/div[1]/div[2]/form[1]/div[2]/div[1]/div[2]/div[8]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[6]/span[1]/div[6]/div[1]/div[1]'
brand_company = [brendoviDrustvo1, brendoviDrustvo2, brendoviDrustvo3, brendoviDrustvo4, brendoviDrustvo5]

# Smatram da brendovi koji koriste zeleni marketing zapravo samo žele privući kupce, a ne istinski doprinijeti okolišu.
zeleniMarketing1 = '/html/body/div[1]/div[2]/form[1]/div[2]/div[1]/div[2]/div[8]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[8]/span[1]/div[2]/div[1]/div[1]'
zeleniMarketing2 = '/html/body/div[1]/div[2]/form[1]/div[2]/div[1]/div[2]/div[8]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[8]/span[1]/div[3]/div[1]/div[1]'
zeleniMarketing3 = '/html/body/div[1]/div[2]/form[1]/div[2]/div[1]/div[2]/div[8]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[8]/span[1]/div[4]/div[1]/div[1]'
zeleniMarketing4 = '/html/body/div[1]/div[2]/form[1]/div[2]/div[1]/div[2]/div[8]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[8]/span[1]/div[5]/div[1]/div[1]'
zeleniMarketing5 = '/html/body/div[1]/div[2]/form[1]/div[2]/div[1]/div[2]/div[8]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[8]/span[1]/div[6]/div[1]/div[1]'
green_marketing = [zeleniMarketing1, zeleniMarketing2, zeleniMarketing3, zeleniMarketing4, zeleniMarketing5]

# Kad vidim kampanju brenda s ekološkom porukom, osjećam da brend dijeli moje vrijednosti.
kampanjaBrend1 = '/html/body/div[1]/div[2]/form[1]/div[2]/div[1]/div[2]/div[8]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[10]/span[1]/div[2]/div[1]/div[1]'
kampanjaBrend2 = '/html/body/div[1]/div[2]/form[1]/div[2]/div[1]/div[2]/div[8]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[10]/span[1]/div[3]/div[1]/div[1]'
kampanjaBrend3 = '/html/body/div[1]/div[2]/form[1]/div[2]/div[1]/div[2]/div[8]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[10]/span[1]/div[4]/div[1]/div[1]'
kampanjaBrend4 = '/html/body/div[1]/div[2]/form[1]/div[2]/div[1]/div[2]/div[8]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[10]/span[1]/div[5]/div[1]/div[1]'
kampanjaBrend5 = '/html/body/div[1]/div[2]/form[1]/div[2]/div[1]/div[2]/div[8]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[10]/span[1]/div[6]/div[1]/div[1]'
brand_campaign = [kampanjaBrend1, kampanjaBrend2, kampanjaBrend3, kampanjaBrend4, kampanjaBrend5]

# Za svaku tvrdnju označite u kojoj mjeri se ona odnosi na vas: 1 = uopće se ne odnosi, 2 = uglavnom ne, 3 = niti da niti ne, 4 = uglavnom da, 5 = u potpunosti se odnosi

# Spreman/na sam platiti višu cijenu za proizvod brenda koji aktivno promiče ekološke vrijednosti.
visaCijena1 = '/html/body/div[1]/div[2]/form[1]/div[2]/div[1]/div[2]/div[9]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/span[1]/div[2]/div[1]/div[1]'
visaCijena2 = '/html/body/div[1]/div[2]/form[1]/div[2]/div[1]/div[2]/div[9]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/span[1]/div[3]/div[1]/div[1]'
visaCijena3 = '/html/body/div[1]/div[2]/form[1]/div[2]/div[1]/div[2]/div[9]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/span[1]/div[4]/div[1]/div[1]'
visaCijena4 = '/html/body/div[1]/div[2]/form[1]/div[2]/div[1]/div[2]/div[9]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/span[1]/div[5]/div[1]/div[1]'
visaCijena5 = '/html/body/div[1]/div[2]/form[1]/div[2]/div[1]/div[2]/div[9]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/span[1]/div[6]/div[1]/div[1]'
higher_price = [visaCijena1, visaCijena2, visaCijena3, visaCijena4, visaCijena5]

# Ekološka ili CSR poruka u digitalnoj kampanji povećava vjerojatnost da ću kupiti taj proizvod.
csrPoruka1 = '/html/body/div[1]/div[2]/form[1]/div[2]/div[1]/div[2]/div[9]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[4]/span[1]/div[2]/div[1]/div[1]'
csrPoruka2 = '/html/body/div[1]/div[2]/form[1]/div[2]/div[1]/div[2]/div[9]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[4]/span[1]/div[3]/div[1]/div[1]'
csrPoruka3 = '/html/body/div[1]/div[2]/form[1]/div[2]/div[1]/div[2]/div[9]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[4]/span[1]/div[4]/div[1]/div[1]'
csrPoruka4 = '/html/body/div[1]/div[2]/form[1]/div[2]/div[1]/div[2]/div[9]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[4]/span[1]/div[5]/div[1]/div[1]'
csrPoruka5 = '/html/body/div[1]/div[2]/form[1]/div[2]/div[1]/div[2]/div[9]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[4]/span[1]/div[6]/div[1]/div[1]'
csr_messages = [csrPoruka1, csrPoruka2, csrPoruka3, csrPoruka4, csrPoruka5]

# Preporučio/la bih prijateljima ili obitelji brend koji dosljedno komunicira svoju ekološku i društvenu odgovornost.
preporuka1 = '/html/body/div[1]/div[2]/form[1]/div[2]/div[1]/div[2]/div[9]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[6]/span[1]/div[2]/div[1]/div[1]'
preporuka2 = '/html/body/div[1]/div[2]/form[1]/div[2]/div[1]/div[2]/div[9]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[6]/span[1]/div[3]/div[1]/div[1]'
preporuka3 = '/html/body/div[1]/div[2]/form[1]/div[2]/div[1]/div[2]/div[9]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[6]/span[1]/div[4]/div[1]/div[1]'
preporuka4 = '/html/body/div[1]/div[2]/form[1]/div[2]/div[1]/div[2]/div[9]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[6]/span[1]/div[5]/div[1]/div[1]'
preporuka5 = '/html/body/div[1]/div[2]/form[1]/div[2]/div[1]/div[2]/div[9]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[6]/span[1]/div[6]/div[1]/div[1]'
recommendations = [preporuka1, preporuka2, preporuka3, preporuka4, preporuka5]

# Izbjegavam kupnju od brendova za koje znam da ne poštuju ekološke standarde ili etiku rada.
izbjegavam1 = '/html/body/div[1]/div[2]/form[1]/div[2]/div[1]/div[2]/div[9]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[8]/span[1]/div[2]/div[1]/div[1]'
izbjegavam2 = '/html/body/div[1]/div[2]/form[1]/div[2]/div[1]/div[2]/div[9]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[8]/span[1]/div[3]/div[1]/div[1]'
izbjegavam3 = '/html/body/div[1]/div[2]/form[1]/div[2]/div[1]/div[2]/div[9]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[8]/span[1]/div[4]/div[1]/div[1]'
izbjegavam4 = '/html/body/div[1]/div[2]/form[1]/div[2]/div[1]/div[2]/div[9]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[8]/span[1]/div[5]/div[1]/div[1]'
izbjegavam5 = '/html/body/div[1]/div[2]/form[1]/div[2]/div[1]/div[2]/div[9]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[8]/span[1]/div[6]/div[1]/div[1]'
avoid = [izbjegavam1, izbjegavam2, izbjegavam3, izbjegavam4, izbjegavam5]

# Kada brend koji pozitivno percipiram počne komunicirati ekološke vrijednosti, to dodatno povećava moju namjeru da kupim njegove proizvode.
pozitivnaPercepcija1 = '/html/body/div[1]/div[2]/form[1]/div[2]/div[1]/div[2]/div[9]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[10]/span[1]/div[2]/div[1]/div[1]'
pozitivnaPercepcija2 = '/html/body/div[1]/div[2]/form[1]/div[2]/div[1]/div[2]/div[9]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[10]/span[1]/div[3]/div[1]/div[1]'
pozitivnaPercepcija3 = '/html/body/div[1]/div[2]/form[1]/div[2]/div[1]/div[2]/div[9]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[10]/span[1]/div[4]/div[1]/div[1]'
pozitivnaPercepcija4 = '/html/body/div[1]/div[2]/form[1]/div[2]/div[1]/div[2]/div[9]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[10]/span[1]/div[5]/div[1]/div[1]'
pozitivnaPercepcija5 = '/html/body/div[1]/div[2]/form[1]/div[2]/div[1]/div[2]/div[9]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[10]/span[1]/div[6]/div[1]/div[1]'
positive_feedback = [pozitivnaPercepcija1, pozitivnaPercepcija2, pozitivnaPercepcija3, pozitivnaPercepcija4, pozitivnaPercepcija5]

# U kojoj mjeri su vam osobno važne ekološke i društvene vrijednosti u svakodnevnom životu?
uopćeNisuVazne = '/html/body/div[1]/div[2]/form[1]/div[2]/div[1]/div[2]/div[10]/div[1]/div[1]/div[2]/div[1]/div[1]/span[1]/div[1]/div[1]/label[1]/div[1]/div[1]/div[1]'
uglavnomNisuVazne = '/html/body/div[1]/div[2]/form[1]/div[2]/div[1]/div[2]/div[10]/div[1]/div[1]/div[2]/div[1]/div[1]/span[1]/div[1]/div[2]/label[1]/div[1]/div[1]/div[1]'
nitiSuVazneNitiNisuVazne = '/html/body/div[1]/div[2]/form[1]/div[2]/div[1]/div[2]/div[10]/div[1]/div[1]/div[2]/div[1]/div[1]/span[1]/div[1]/div[3]/label[1]/div[1]/div[1]/div[1]'
uglavnomSuVazne = '/html/body/div[1]/div[2]/form[1]/div[2]/div[1]/div[2]/div[10]/div[1]/div[1]/div[2]/div[1]/div[1]/span[1]/div[1]/div[4]/label[1]/div[1]/div[1]/div[1]'
iznimnoSuVazne = '/html/body/div[1]/div[2]/form[1]/div[2]/div[1]/div[2]/div[10]/div[1]/div[1]/div[2]/div[1]/div[1]/span[1]/div[1]/div[5]/label[1]/div[1]/div[1]/div[1]'
ecological_values = [uopćeNisuVazne, uglavnomNisuVazne, nitiSuVazneNitiNisuVazne, uglavnomSuVazne, iznimnoSuVazne]

# Smatram da se poduzeća trebaju aktivno baviti rješavanjem ekoloških i društvenih problema, a ne samo ostvarivati profit.
uopceSeNeSlazem = '/html/body/div[1]/div[2]/form[1]/div[2]/div[1]/div[2]/div[11]/div[1]/div[1]/div[2]/div[1]/div[1]/span[1]/div[1]/div[1]/label[1]/div[1]/div[1]/div[1]'
neSlazemSe = '/html/body/div[1]/div[2]/form[1]/div[2]/div[1]/div[2]/div[11]/div[1]/div[1]/div[2]/div[1]/div[1]/span[1]/div[1]/div[2]/label[1]/div[1]/div[1]/div[1]'
nitiSeSlazemNitiSeNeSlazem = '/html/body/div[1]/div[2]/form[1]/div[2]/div[1]/div[2]/div[11]/div[1]/div[1]/div[2]/div[1]/div[1]/span[1]/div[1]/div[3]/label[1]/div[1]/div[1]/div[1]'
slazemSe = '/html/body/div[1]/div[2]/form[1]/div[2]/div[1]/div[2]/div[11]/div[1]/div[1]/div[2]/div[1]/div[1]/span[1]/div[1]/div[4]/label[1]/div[1]/div[1]/div[1]'
uPotpunostiSeSlazem = '/html/body/div[1]/div[2]/form[1]/div[2]/div[1]/div[2]/div[11]/div[1]/div[1]/div[2]/div[1]/div[1]/span[1]/div[1]/div[5]/label[1]/div[1]/div[1]/div[1]'
company_ecology = [uopceSeNeSlazem, neSlazemSe, nitiSeSlazemNitiSeNeSlazem, slazemSe, uPotpunostiSeSlazem]

responses = [
    # 3x duplicates (highest weight)
    "primijetila sam da sve više brendova koristi zelene poruke, ali rijetko koji zaista nešto mijenja u praksi",
    "primijetila sam da sve više brendova koristi zelene poruke, ali rijetko koji zaista nešto mijenja u praksi",
    "primijetila sam da sve više brendova koristi zelene poruke, ali rijetko koji zaista nešto mijenja u praksi",

    "Rijeci bez akcije su nista",
    "Rijeci bez akcije su nista",
    "Rijeci bez akcije su nista",

    # All others appear exactly once
    "Lijepo je što se radi ovakvo istraživanje, nadam se da će rezultati koristiti tvrtkama da budu iskrenije",
    "Ekološki marketing je dobra stvar, ali treba ga pratiti konkretnim akcijama, inače je samo prazna priča",
    "Ne",
    "Potrosaci ne znaju dovoljno o ovome",
    "Sretno na kolegiju!",
    "cijenim brendove koji to rade iskreno",
    "Na društvenim mrežama vidim puno ekoloških kampanja, ali većinom ih preskačem jer izgledaju svi jednako",
    "više vjerujem brendovima koji imaju konkretne dokaze svojih ekoloških inicijativa, a ne samo lijepe slike",
    "Nisam puno razmisljala o ovome do sad",
    "Sve je vec receno",
    "Vazno!",
    "Mladi sve više paze na ovo.",
    "Ništa",
    "Nema",
    "Instagram pun laznih eko kampanja",
    "Super anketa sretno!",
    "Ekologija nije trend nego nuznost",
    "Pa ne bas",
    ":)",
    "Boo",
    "Ne znam",
    "Jok",
    "…",
    "cijena je ipak presudna",
    "sve je to za profit na kraju",
    "Mislim da su rijetki oni koji kupuju samo zbog ekologije",
    "-",
    "/",
]