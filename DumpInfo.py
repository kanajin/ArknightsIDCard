from ReadCSV import *
import json

def dump_doctor_info():
    dc_info = gen_doctor_info()
    dump_to_file(dc_info, "Source/DrData.json")

def dump_operator_info():
    op_infos = gen_operator_info()
    dump_to_file(op_infos, "Source/BoxData.json")

def dump_to_file(obj, path):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(obj, f, ensure_ascii=False, indent=4)