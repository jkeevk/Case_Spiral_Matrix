from typing import List


def get_matrix(file: str) -> List[int]:
    """
    Получает матрицу из указанного файла.  
    Затем возвращает её в виде одномерного списка, полученнго путем обхода матрицы. 
    По спирали: против часовой стрелки, начиная с левого верхнего угла.

    """
    with open(file, "rb") as file:
        byte_lines = [i for i in file.readlines()[1::2]]
    decoded_lines = [row.decode("utf-8") for row in byte_lines]

    matrix = []
    for row in decoded_lines:
        matrix.append(list(map(int, (row.replace("|", "").split()))))

    n, m = len(matrix), len(matrix[0])
    # Создаем нулевую матрицу размером 'n x m'
    zero_matrix = [[0] * m for _ in range(n)]
    # Направление смещения
    row_dir, col_dir = 1, 0
    # Стартовые координаты
    row, column = 0, 0
    result = []
    for counter in range(1, n * m + 1):

        current_num = matrix[row][column]
        result.append(current_num)

        zero_matrix[row][column] = counter
        # Работает только с False(0) или True(1), поэтому нужна заполненная нулями матрица
        if zero_matrix[(row + row_dir) % n][(column + col_dir) % m]:
            row_dir, col_dir = -col_dir, row_dir  # поворачиваем
        row += row_dir
        column += col_dir
    return result


if __name__ == "__main__":
    file = 'matrix.txt'
    TRAVERSAL = [10, 50, 90, 130, 140, 150, 160, 120, 80, 40, 30, 20, 60, 100, 110, 70]
    assert get_matrix(file) == TRAVERSAL
