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

def subtract(self, other):
        result = SparseMatrix(self.rows, self.cols)
        for item in self.elements:
            result.set_element(item.row, item.col, item.value)
        for item in other.elements:
            current = result.get_element(item.row, item.col)
            result.set_element(item.row, item.col, current - item.value)
        return result

    def multiply(self, other):
        if self.cols != other.rows:
            raise ValueError("Matrix dimensions do not match for multiplication")
        result = SparseMatrix(self.rows, other.cols)
        for a in self.elements:
            for b in other.elements:
                if a.col == b.row:
                    existing = result.get_element(a.row, b.col)
                    result.set_element(a.row, b.col, existing + a.value * b.value)
        return result

    def print_matrix(self):
        print("\nNon-zero elements in this sparse matrix:")
        if not self.elements:
            print("[Matrix is entirely zero]")
        else:
            for elem in self.elements:
                print(f"Row {elem.row}, Column {elem.col} => Value {elem.value}")

