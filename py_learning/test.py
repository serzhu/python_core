import csv

def write_contacts_to_file(filename, contacts):
    
    with open(filename, 'w', newline ='') as file:
        fieldsnames = contacts[0].keys()
        csv_writer = csv.DictWriter(file, fieldnames = fieldsnames)
        csv_writer.writeheader()
        for row in contacts:
            print(row)
            csv_writer.writerow(rowdict=row)
    

def read_contacts_from_file(filename):
    with open(filename, 'r', newline ='') as file:
        csv_reader = csv.DictReader(file)
        res = []
        for row in csv_reader:
            if row["favorite"] == 'True':
                row["favorite"] = True
            elif row["favorite"] == 'False':
                row["favorite"] = False
            res.append(row)

    
c = [{'name': 'Allen Raymond', 'email': 'nulla.ante@vestibul.co.uk', 'phone': '(992) 914-3792', 'favorite': True}, {'name': 'Chaim Lewis', 'email': 'dui.in@egetlacus.ca', 'phone': '(294) 840-6685', 'favorite': False}]
f = 'test.csv'
write_contacts_to_file(f,c)
read_contacts_from_file(f)