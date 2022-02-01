import csv
import pytest

filename = 'input.txt'

rows = []


def read_csv(file):
    with open(file, 'r', newline='') as csv_file:
        csv_reader = csv.reader(csv_file)
        header = next(csv_reader)
        
        for row in csv_reader:
            rows.append(row)
            
    return rows
    
    
def test_csv_read():
    
    expected = [['A', 'A'], ['B', 'B'], ['C', 'C'], ['D', 'CH'], ['E', 'D'], ['F', 'E'], ['G', 'F'], ['H', 'G'], ['I', 'H'], ['J', 'I'], ['K', 'J'], ['L', 'K'], ['M', 'L'], ['N', 'LL'], ['O', 'M'], ['P', 'N'], ['Q', 'Ñ'], ['R', 'O'], ['S', 'P'], ['T', 'Q'], ['U', 'R'], ['V', 'S'], ['W', 'T'], ['X', 'U'], ['Y', 'V'], ['Z', 'W'], ['a', 'X'], ['b', 'Y'], ['c', 'Z'], ['d', 'a'], ['e', 'b'], ['f', 'c'], ['g', 'ch'], ['h', 'd'], ['i', 'e'], ['j', 'f'], ['k', 'g'], ['l', 'h'], ['m', 'i'], ['n', 'j'], ['o', 'k'], ['p', 'l'], ['q', 'll'], ['r', 'm'], ['s', 'n'], ['t', 'ñ'], ['u', 'o'], ['v', 'p'], ['w', 'q'], ['x', 'r'], ['y', 's'], ['z', 't'], ['', 'u'], ['', 'v'], ['', 'w'], ['', 'x'], ['', 'y'], ['', 'z']]
    assert read_csv(filename) == expected


def main():
    read_csv(filename)
   # unittest.main()
    
    
if __name__ == "__main__":
    main()