import pprint
from typing import List


def rocket_coasts(table: List[List[int]]) -> List[List[int]]:
    """

    Просчитать минимальные стоимости маршрутов до каждой клетки с учетом возможных перемещений.


    :param table: Таблица размером N*M, где в каждой клетке дана стоимость перемещения в неё
    :return: Таблицу стоимостей перемещения по клеткам
    """
    #  рассчитать таблицу стоимостей перемещений
    n = len(table)
    m = len(table[0])

    table_cost = [[0] * m for i in range(n)]

    table_cost[0][0] = table[0][0]
    for ind in range(1, m):
        table_cost[0][ind] = table_cost[0][ind - 1] + table[0][ind]

    for ind in range(1, n):
        table_cost[ind][0] = table_cost[ind - 1][0] + table[ind][0]

    pprint.pprint(table_cost, width=20)

    for i in range(1, n):
        for j in range(1, m):
            table_cost[i][j] = min(table_cost[i - 1][j], table_cost[i][j-1]) + table[i][j]

    pprint.pprint(table_cost, width=20)

    return table_cost


if __name__ == '__main__':
    coasts_ceil = [
        [2, 7, 9, 3],
        [12, 4, 1, 9],
        [1, 5, 2, 5]
    ]
    total_coasts = rocket_coasts(coasts_ceil)
    print(total_coasts[-1][-1])  # 21
















