import random
import form_x_paths as x_paths
import product_opinions


def generate_input_keywords(data):
    number_of_factors = random.choice([1, 2, 3])
    factors_sample = random.sample(data, number_of_factors)
    return ', '.join(factors_sample)


def select_cultural_prefs_level():
    return random.choices(x_paths.local_culture_preferences, weights=(10, 5, 10, 60, 20), k=1)[0]


def select_specific_product_features():
    return random.choices(x_paths.specific_product_features, weights=(90, 10), k=1)[0]


def select_influence_level():
    return random.choices(x_paths.influences, weights=(10, 10, 10, 40, 10), k=1)[0]


def select_product_adaptation():
    return random.choices(x_paths.product_cultural_adaptations, weights=(80, 20), k=1)[0]


def select_advertising_level():
    return random.choices(x_paths.advertising_perceptions, weights=(20, 10, 10, 30, 80), k=1)[0]


def select_design_perception():
    return random.choices(x_paths.product_designs, weights=(20, 10, 10, 60, 10), k=1)[0]


def select_ethnicity():
    return random.choices(x_paths.ethnicity, weights=(10, 10, 50, 10, 10, 10, 10, 10), k=1)[0]


def select_country():
    return random.choices(x_paths.countries, weights=(60, 10, 20, 10, 10), k=1)[0]


def select_adaptation():
    return random.choices(x_paths.adaptations, weights=(5, 95), k=1)[0]


def get_adaptation_example(industry_type):
    match industry_type:
        case x_paths.it:
            return random.choices(product_opinions.it)
        case x_paths.marketing:
            return random.choices(product_opinions.marketing)
        case x_paths.sales:
            return random.choices(product_opinions.sales)
        case x_paths.manufacturing:
            return random.choices(product_opinions.manufacturing)
        case x_paths.entertainment:
            return random.choices(product_opinions.entertainment)
        case x_paths.health:
            return random.choices(product_opinions.beauty)
        case x_paths.education:
            return random.choices(product_opinions.education)
        case x_paths.hospitality:
            return random.choices(product_opinions.hospitality)
        case x_paths.other_industry:
            return random.choices(product_opinions.other)
