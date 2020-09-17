import csv


def make_list(file):
    list_name = []
    with open('names.txt', 'r') as make_ls:
        for nm in make_ls:
            list_name.append(str(nm).strip())
    with open(file, 'r') as sch:
        reader = csv.DictReader(sch)
        for row in reader:
            data = row['NAME']
            list_name.append(str(data))
    unique_name = set(list_name)
    list_name = list(unique_name)
    print(list_name)
    with open('names_test.txt', 'w') as make_ls_w:
        for idl in list_name:
            make_ls_w.write(str(idl)+'\n')


def translate_export(file):
    pass


print(make_list('export.csv'))
