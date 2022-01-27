import csv
import unittest

filename = 'input.txt'

fields = []
rows = []


def read_csv(filename):
    with open(filename, 'r', newline='') as csv_file:
        csv_reader = csv.reader(csv_file)
    
        fields = next(csv_reader)
    
        for row in csv_reader:
           rows.append(row)
        
    
        print("Total number of rows: %d"%(csv_reader.line_num))
    

    print('Field names are:' + ', '.join(field for field in fields))


    print('\nFirst 5 rows:\n')

    for col in rows[:5]:
        print("%10s"%col),
    print('\n')
        


class TestCSV(unittest.TestCase):
    
    def test_csv_read(self):
        self.assertEqual('', '')
        
    
    

def main():
    read_csv(filename)
    unittest.main()
    
    
if __name__ == "__main__":
    main()