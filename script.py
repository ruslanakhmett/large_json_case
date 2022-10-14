import ijson


with open('./p10.json', 'r') as file_p10:
    with open('./sisyphus.json', 'r') as file_sisyphus: 
        for p10_package in ijson.items(file_p10, "packages"):
            # for sis_package in ijson.items(file_sisyphus, "packages"):
            if p10_package not in ijson.items(file_sisyphus, "packages"):
                print(p10_package)
