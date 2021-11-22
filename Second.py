import yaml
import json


def conversion(filepath, output):
    with open(filepath, 'r', encoding="UTF-8") as yaml_in:
        with open(output, "w", encoding="UTF-8") as json_out:
            yaml_object = yaml.safe_load(yaml_in)
            json.dump(yaml_object, json_out, ensure_ascii=False, sort_keys=True, indent=2)

filepath = r'C:\Users\klodb\Documents\Учеба\Лабы\Инфа\3\schedule.txt'
output = r'C:\Users\klodb\Documents\Учеба\Лабы\Инфа\3\new2.txt'