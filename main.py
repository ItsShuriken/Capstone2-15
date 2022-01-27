import csv

filename = 'input.txt'

fields = []
rows = []


def read_csv(filename):
    with open(filename, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
    
        fields = next(csv_reader)
    
        for row in csv_reader:
           rows.append(row)
        
    
        print("Total number of rows: %d"%(csv_reader.line_num))
    

    print('Field names are:' + ', '.join(field for field in fields))


    print('\nFirst 5 rows:\n')
    for row in rows[:5]:
    
        for col in rows:
            print("%10s"%col),
        print('\n')
        
        
def main():
    read_csv(filename)
    
    
if __name__ == "__main__":
    main()