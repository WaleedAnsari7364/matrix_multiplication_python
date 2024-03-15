import time

def read_input(filename):
    with open(filename, 'r') as file:
        opcode = int(file.readline().strip())
        data_type = int(file.readline().strip())
        dim1 = tuple(map(int, file.readline().strip().split()))
        mat1 = [list(map(data_type_mapping[data_type], file.readline().strip().split())) for _ in range(dim1[0])]
        dim2 = tuple(map(int, file.readline().strip().split()))
        mat2 = [list(map(data_type_mapping[data_type], file.readline().strip().split())) for _ in range(dim2[0])]
    return opcode, data_type, dim1, mat1, dim2, mat2

def matrix_multiply(mat1, mat2):
    rows1, cols1 = len(mat1), len(mat1[0])
    rows2, cols2 = len(mat2), len(mat2[0])
    if cols1 != rows2:
        raise ValueError("Matrices are not compatible for multiplication")

    result = [[0] * cols2 for _ in range(rows1)]
    for i in range(rows1):
        for j in range(cols2):
            for k in range(cols1):
                result[i][j] += mat1[i][k] * mat2[k][j]
    return result

def write_output(result, data_type):
    with open('output.txt', 'w') as file:
       
        file.write(str(data_type) + '\n')
        
       
        rows = len(result)
        cols = len(result[0])
        file.write("{} {}\n".format(rows, cols))
        
       
        for row in result:
            file.write(' '.join(map(str, row)) + '\n')


data_type_mapping = {
    1: int,
    2: float,
    3: int,
    4: float
}

input_file = input("Enter the name of the input file: ")

opcode, data_type, dim1, mat1, dim2, mat2 = read_input(input_file)

start_time = time.time()
result = matrix_multiply(mat1, mat2)
end_time = time.time()
execution_time = end_time - start_time

print("Execution time: {:.6f} seconds".format(execution_time))

write_output(result, data_type)

