import csv

def gen_operator_info() -> list:
    reader = []

    with open("Source/arkD.csv", newline='', encoding='utf-8-sig') as csv_file:
        dict_reader = csv.DictReader(csv_file, dialect='excel')
        reader = list(dict_reader)

    return reader

def gen_doctor_info() -> dict:
    info = {}

    with open("Source/DoctorInfo.csv", newline='', encoding='utf-8-sig') as csv_file:
        info_list = [x[1] for x in csv.reader(csv_file)]
        header = ["Name", "ID", "DateIn", "DateNow", "Assistant", "Skin", "LeftSide", "RightSide", "TopSide", "FirstLine", "Gap", "SizeName", "SizeID", "SizeTotal", "TotalToRight", "LevelFont"]

        info = dict(zip(header, info_list))

    return info
