import random
import form_x_paths as x_paths


# 1
def select_age():
    return random.choices(x_paths.age_groups, weights=(5, 15, 65, 15), k=1)[0]


# 2
def select_education():
    return random.choices(x_paths.education, weights=(5, 30, 60, 5), k=1)[0]


# 3
def select_industry():
    return random.choices(x_paths.industry, weights=(0, 7, 30, 0), k=1)[0]


# 4
def select_entrepreneur():
    return random.choices(x_paths.entrepreneur, weights=(67, 33, 0), k=1)[0]


# 5
def select_familiarity():
    return random.choices(x_paths.familiarity, weights=(70, 25, 0, 5, 0), k=1)[0]


# 6
def select_technologies():
    return random.choices(x_paths.technologies, weights=(20, 20, 20, 20, 20), k=1)[0]


# 7
def select_extent():
    return random.choices(x_paths.extent, weights=(60, 35, 0, 5, 0), k=1)[0]


# 8
def select_biggest_challenges():
    return random.choices(x_paths.biggest_challenges, weights=(20, 20, 20, 20, 20), k=1)[0]


# 9
def select_digital_lowers():
    return random.choices(x_paths.digitalization_lowers, weights=(0, 5, 0, 35, 60), k=1)[0]


# 10
def select_digital_tools():
    return random.choices(x_paths.digital_tools, weights=(0, 0, 0, 35, 65), k=1)[0]


# 12
def select_government_policies():
    return random.choices(x_paths.government_policies, weights=(10, 45, 20, 25, 0), k=1)[0]


# 13
def select_financial_institutions():
    return random.choices(x_paths.financial_institutions, weights=(15, 35, 25, 15, 10), k=1)[0]


# 14
def select_online_platforms():
    return random.choices(x_paths.online_platforms, weights=(45, 35, 0, 15, 5), k=1)[0]


# 15
def select_future_impact():
    return random.choices(x_paths.future_impacts, weights=(40, 35, 5, 20, 0), k=1)[0]


# 16
def select_skills():
    return random.choices(x_paths.skills, weights=(20, 20, 20, 20, 20), k=1)[0]
