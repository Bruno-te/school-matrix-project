# sparse_matrix.py

class MatrixElement:
    def __init__(self, row, col, value):
        self.row = row
        self.col = col
        self.value = value  

class SparseMatrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.elements = []  

    def add_element(self, row, col, value):
        if value != 0:
            elem = MatrixElement(row, col, value)
            self.elements.append(elem)

    def get_element(self, row, col):
        for entry in self.elements:
            if entry.row == row and entry.col == col:
                return entry.value
        return 0  

    def set_element(self, row, col, value):
        for entry in self.elements:
            if entry.row == row and entry.col == col:
                if value == 0:
                    self.elements.remove(entry) 
                else:
                    entry.value = value 
                return
        if value != 0:
            self.add_element(row, col, value)

    def add(self, other):
        result = SparseMatrix(self.rows, self.cols)

        for item in self.elements:
            result.set_element(item.row, item.col, item.value)

        for item in other.elements:
            current = result.get_element(item.row, item.col)
            new_val = current + item.value

