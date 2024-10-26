import requests
from typing import List


def get_matrix(url: str) -> List[int]:
    """
    Получает матрицу с указанного URL.  
    Затем возвращает её в виде одномерного списка, полученнго путем обхода матрицы. 
    По спирали: против часовой стрелки, начиная с левого верхнего угла.

    """
    response = requests.get(url)
    raw_matrix = response.content.decode("utf-8")
    matrix = []
    # Проходим по каждой строке
    for line in raw_matrix.strip().split("\n"):
        # Пропускаем строки, начинающиеся с '+'
        if not line.startswith("+"):
            # Убираем символы '|' и пробелы, а затем разбиваем на числа
            cleaned_line = line.replace("|", "").strip()
            if cleaned_line:  # Проверяем, что строка не пустая
                matrix.append(list(map(int, cleaned_line.split())))

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
    url = "https://raw.githubusercontent.com/avito-tech/python-trainee-assignment/main/matrix.txt"

    TRAVERSAL = [10, 50, 90, 130, 140, 150, 160, 120, 80, 40, 30, 20, 60, 100, 110, 70]

    assert get_matrix(url) == TRAVERSAL
