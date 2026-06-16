import random
import form_x_paths as x_paths


# Koji je vaš spol?
def select_gender():
    return random.choices(x_paths.genders, weights=(35, 62, 3), k=1)[0]


# Kojoj dobnoj skupini pripadate?
def select_age():
    return random.choices(x_paths.ageGroups, weights=(45, 30, 15, 7, 3), k=1)[0]


# Koja je vaša najviša razina završenog obrazovanja?
def select_education():
    return random.choices(x_paths.education_groups, weights=(2, 25, 40, 33), k=1)[0]


# Koliko često kupujete proizvode ili usluge putem interneta?
def select_shopping_frequency():
    return random.choices(x_paths.shopping_frequencies, weights=(8, 25, 45, 18, 4), k=1)[0]


# Koje digitalne kanale najčešće koristite? (možete odabrati više odgovora)
def select_digital_channels():
    return random.choices(x_paths.digital_channels, weights=(10, 10, 0, 5, 0, 10, 10), k=1)[0]


# Jeste li u posljednjih 6 mjeseci primijetili digitalnu reklamnu poruku brenda koja se odnosila na ekološku održivost ili društvenu odgovornost?
def select_digital_commercial_messages():
    return random.choices(x_paths.digital_commercial_messages, weights=(28, 45, 20, 7), k=1)[0]


# Koje vrste sadržaja su vam se najviše utisnule u pamćenje? (možete odabrati više odgovora)
def select_digital_content_types():
    return random.choices(x_paths.digital_content_types, weights=(10, 10, 0, 5, 0, 10), k=1)[0]


# Za svaku tvrdnju označite u kojoj mjeri se ona odnosi na vas: 1 = uopće se ne odnosi, 2 = uglavnom ne, 3 = niti da niti ne, 4 = uglavnom da, 5 = u potpunosti se odnosi


# Brendovi koji komuniciraju ekološke vrijednosti djeluju mi vjerodostojno.
def select_brand_ecology():
    return random.choices(x_paths.brand_ecology, weights=(5, 10, 20, 40, 25), k=1)[0]


# Ekološke i društveno odgovorne kampanje poboljšavaju moju ukupnu sliku o brendu.
def select_ecology():
    return random.choices(x_paths.ecology, weights=(3, 8, 15, 42, 32), k=1)[0]


# Brend koji aktivno komunicira svoju društvenu odgovornost doživljavam kao pouzdanijeg od onih koji to ne čine.
def select_brand_company():
    return random.choices(x_paths.brand_company, weights=(5, 10, 18, 42, 25), k=1)[0]


# Smatram da brendovi koji koriste zeleni marketing zapravo samo žele privući kupce, a ne istinski doprinijeti okolišu.
def select_green_marketing():
    return random.choices(x_paths.green_marketing, weights=(8, 15, 25, 32, 20), k=1)[0]


# Kad vidim kampanju brenda s ekološkom porukom, osjećam da brend dijeli moje vrijednosti.
def select_brand_campaign():
    return random.choices(x_paths.brand_campaign, weights=(7, 12, 25, 38, 18), k=1)[0]


# Za svaku tvrdnju označite u kojoj mjeri se ona odnosi na vas: 1 = uopće se ne odnosi, 2 = uglavnom ne, 3 = niti da niti ne, 4 = uglavnom da, 5 = u potpunosti se odnosi

# Spreman/na sam platiti višu cijenu za proizvod brenda koji aktivno promiče ekološke vrijednosti.
def select_higher_price():
    return random.choices(x_paths.higher_price, weights=(10, 18, 25, 32, 15), k=1)[0]


# Ekološka ili CSR poruka u digitalnoj kampanji povećava vjerojatnost da ću kupiti taj proizvod.
def select_csr_messages():
    return random.choices(x_paths.csr_messages, weights=(5, 12, 22, 40, 21), k=1)[0]


# Preporučio/la bih prijateljima ili obitelji brend koji dosljedno komunicira svoju ekološku i društvenu odgovornost.
def select_recommendations():
    return random.choices(x_paths.recommendations, weights=(4, 8, 18, 42, 28), k=1)[0]


# Izbjegavam kupnju od brendova za koje znam da ne poštuju ekološke standarde ili etiku rada.
def select_avoid():
    return random.choices(x_paths.avoid, weights=(8, 12, 22, 38, 20), k=1)[0]


# Kada brend koji pozitivno percipiram počne komunicirati ekološke vrijednosti, to dodatno povećava moju namjeru da kupim njegove proizvode.
def select_positive_feedback():
    return random.choices(x_paths.positive_feedback, weights=(4, 10, 18, 42, 26), k=1)[0]


# U kojoj mjeri su vam osobno važne ekološke i društvene vrijednosti u svakodnevnom životu?
def select_ecological_values():
    return random.choices(x_paths.ecological_values, weights=(3, 8, 20, 42, 27), k=1)[0]


# Smatram da se poduzeća trebaju aktivno baviti rješavanjem ekoloških i društvenih problema, a ne samo ostvarivati profit.
def select_company_ecology():
    return random.choices(x_paths.company_ecology, weights=(3, 7, 15, 40, 35), k=1)[0]


# Imate li još nešto za dodati o temi digitalnog marketinga temeljenog na vrijednostima?
def select_response():
    return random.choices(x_paths.responses)
