import random
import form_x_paths as x_paths
import product_opinions


def select_age():
    return random.choices(x_paths.age_span, weights=(10, 85, 5), k=1)[0]


def select_gender():
    return random.choices(x_paths.genders, weights=(61, 35, 4), k=1)[0]


def select_current_living():
    return random.choices(x_paths.current_living, weights=(95, 5), k=1)[0]


def select_reduce_env_impact():
    return random.choices(x_paths.environmental_impacts, weights=(10, 20, 70), k=1)[0]


def select_effective_packaging():
    return random.choices(x_paths.effective_packagings, weights=(30, 70), k=1)[0]


def select_carbon_reducement():
    return random.choices(x_paths.carbon_reducements, weights=(10, 20, 50, 20), k=1)[0]


def select_regulatory_compliance():
    return random.choices(x_paths.regulatory_compliances, weights=(10, 50, 40), k=1)[0]


def select_depletion():
    return random.choices(x_paths.depletions, weights=(5, 45, 50), k=1)[0]


def select_technological_advancements():
    return random.choices(x_paths.technological_advancements, weights=(40, 60), k=1)[0]


def select_infrastructure_limitations():
    return random.choices(x_paths.infrastructure_limitations, weights=(10, 5, 35, 50), k=1)[0]
