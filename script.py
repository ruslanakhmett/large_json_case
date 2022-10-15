import ijson
import json
import codecs


# with open('./p10.json') as json_file:
#     data = json.load(json_file)
    
# with codecs.open('your_file.json', 'w', encoding='utf-8') as f:
#     json.dump(data, f, ensure_ascii=True)


# with open('./sisyphus.json') as json_file2:
#     data2 = json.load(json_file2)
    
# with codecs.open('your_file2.json', 'w', encoding='utf-8') as f:
#     json.dump(data2, f, ensure_ascii=True)


# with open('./your_file.json', 'r') as file_p10:
#     with open('./your_file2.json', 'r') as file_sisyphus: 
#         for p10_package in ijson.items(file_p10, "packages.item"):
            
#             for sis_package in ijson.items(file_sisyphus, "packages.item"):
#             # if p10_package not in ijson.items(file_sisyphus, "packages.item"):
#                 print(p10_package['name'] == sis_package['name'])

# a = {'name': 'i586-zziplib-devel', 'epoch': 0, 'version': '0.13.72', 'release': 'alt1', 'arch': 'x86_64-i586', 'disttag': 'sisyphus+278032.100.1.2', 'buildtime': 1625982256, 'source': ''}
# b = {'name': '0ad', 'epoch': 1, 'version': '0.0.26', 'release': 'alt0_3_alpha', 'arch': 'aarch64', 'disttag': 'sisyphus+307408.100.1.1', 'buildtime': 1664204458, 'source': '0ad'}



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


print(len(only_in_p10), len(only_in_sis))


