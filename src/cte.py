class CTE:
    def __init__(self, name: str, query: str):
        """
        Инициализация CTE.

        :param name: имя CTE
        :param query: SQL-запрос внутри CTE
        """
        self.name = name
        self.query = query
        self.dependencies = []  # Зависимости для данного CTE, если они будут добавлены позже

    def add_dependency(self, cte):
        """
        Добавляет зависимость от другого CTE.

        :param cte: объект CTE, от которого зависит текущий CTE
        """
        self.dependencies.append(cte)

    def __str__(self):
        """
        Строковое представление CTE.
        """
        return f"CTE {self.name}: {self.query}"

    def get_query(self):
        """
        Возвращает SQL-запрос CTE.
        """
        return self.query

    def get_dependencies(self):
        """
        Возвращает зависимости для этого CTE.
        """
        return self.dependencies