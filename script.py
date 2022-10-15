import json


with open('./p10.json', 'r') as file:
    for line in file:
        p10_data = json.loads(line)

with open('./sisyphus.json', 'r') as file:
    for line in file:
        sis_data = json.loads(line)


all_in_p10 = [str(item) for item in p10_data['packages']]
all_in_sis = [str(item) for item in sis_data['packages']]

only_in_p10 = list(set(all_in_p10) - set(all_in_sis))
only_in_sis = list(set(all_in_sis) - set(all_in_p10))

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump({'case_1': only_in_p10}, f, ensure_ascii=False, indent=4)
    
with open('data2.json', 'w', encoding='utf-8') as f:
    json.dump({'case_2': only_in_sis}, f, ensure_ascii=False, indent=4)