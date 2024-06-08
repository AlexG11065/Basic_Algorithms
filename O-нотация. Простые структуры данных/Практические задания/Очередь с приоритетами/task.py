"""
Priority Queue
Queue priorities are from 0 to 10
"""
from typing import Any

from collections import deque


class PriorityQueue:
    HIGH_PRIORITY = 0  # наивысший приоритет
    LOW_PRIORITY = 10  # наименьший приоритет

    def __init__(self):
        self.pr_queue = {priority: deque() for priority in range(self.HIGH_PRIORITY, self.LOW_PRIORITY + 1)}
        # self.pr_queue = [deque() for _ in range(self.HIGH_PRIORITY, self.LOW_PRIORITY + 1)]
        #  использовать deque для реализации очереди с приоритетами

    def enqueue(self, elem: Any, priority: int = 0) -> None:
        """
        Добавление элемент в конец очереди c учетом приоритета

        :param elem: Элемент, который должен быть добавлен
        :param priority: Приоритет добавляемого элемента
        """
        #  реализовать метод enqueue
        self.pr_queue[priority].append(elem)

    def dequeue(self) -> Any:
        """
        Извлечение элемента из начала очереди.

        :raise: IndexError - Ошибка, если очередь пуста

        :return: Извлеченный с начала очереди элемент.
        """
        for prior_value in self.pr_queue.values():
            if prior_value:
                return prior_value.popleft()
        raise IndexError("Очередь пуста")
        #  реализовать метод dequeue

    def peek(self, ind: int = 0, priority: int = 0) -> Any:
        """
        Просмотр произвольного элемента, находящегося в очереди, без его извлечения.

        :param ind: Индекс элемента (отсчет с начала, 0 - первый с начала элемент в очереди, 1 - второй с начала элемент в очереди с указанным приоритетом, и т.д.)
        :param priority: Приоритет очереди

        :raise: TypeError - если указан не целочисленный тип индекса
        :raise: IndexError - если индекс вне границ очереди

        :return: Значение просмотренного элемента
        """
        if not isinstance(ind, int):
            raise TypeError(f"--> {ind} <-- не является целочисленным типом данных")

        if not 0 <= ind < len(self.pr_queue):
            raise IndexError(f"{ind} не входит в границы очереди")

        priority_ind = self.pr_queue[priority]
        return priority_ind[ind]
        #  реализовать метод peek

    def clear(self) -> None:
        """ Очистка очереди. """
        # TODO реализовать метод clear
        for prior_value in self.pr_queue.values():
            prior_value.clear()

    def __len__(self):
        """ Количество элементов в очереди. """
        quantity_elem = 0
        for num in self.pr_queue.values():
            quantity_elem += len(num)
        return quantity_elem  #  реализовать метод __len__


if __name__ == "__main__":
    from collections import deque

    q = PriorityQueue()
    # pr = 0
    # index = 1

    q.enqueue(1, 0)
    q.enqueue(2, 0)
    q.enqueue(3, 0)
    print(q.pr_queue)
    print(q.__len__())
    # q.clear()
    # print(q.pr_queue)
    # print(q.peek())
    # print(q.peek(1, 0))
    # print(q.peek(20, 0))
    # print(q.peek(0, 0))
    # print(q.pr_queue)
    # print(q.pr_queue[pr][index])


