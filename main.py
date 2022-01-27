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
        
    
       # print("Total number of rows: %d"%(csv_reader.line_num))
    

    #print('Field names are:' + ', '.join(field for field in fields))


    #print('\nFirst 5 rows:\n')

   # for col in rows[:5]:
   #     print("%10s"%col),
  #  print('\n')
        


class TestCSV(unittest.TestCase):
    
    
    def test_csv_read(self):
        
        expected = [['A', 'A'], ['B', 'B'], ['C', 'C'], ['D', 'CH'], ['E', 'D'], ['F', 'E'], ['G', 'F'], ['H', 'G'], 
        ['I', 'H'], ['J', 'I'], ['K', 'J'], ['L', 'K'], ['M', 'L'], ['N', 'LL'], ['O', 'M'], ['P', 'N'], ['Q', 'Ñ'], ['R', 'O'], 
        ['S', 'P'], ['T', 'Q'], ['U', 'R'], ['V', 'S'], ['W', 'T'], ['X', 'U'], ['Y', 'V'], ['Z', 'W'], ['a', 'X'], ['b', 'Y'], ['c', 'Z'], 
        ['d', 'a'], ['e', 'b'], ['f', 'c'],  ['g', 'ch'], ['h', 'd'], ['i', 'e'], ['j', 'f']]
        self.assertEqual(expected, rows)
        
    
    

def main():
    read_csv(filename)
    unittest.main()
    
    
if __name__ == "__main__":
    main()