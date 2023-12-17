original_dict = {'Boys': [72, 68, 70, 69, 74], 'Girls': [63, 65, 69, 62, 61]}

list_of_dicts = [{'Boys': boy, 'Girls': girl} for boy, girl in zip(original_dict['Boys'], original_dict['Girls'])]

print(list_of_dicts)
