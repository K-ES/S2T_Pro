class S2T:
    def __init__(self, query_text: str):
        """
        Инициализация объекта S2T, который будет содержать текст SQL-запроса.

        :param query_text: текст SQL-запроса
        """
        self.query_text = query_text  # Сохраняем текст запроса
        self.ctes = []  # Список для хранения объектов CTE, если они будут добавлены позже

    def __str__(self):
        """
        Возвращает текст SQL-запроса.
        """
        return self.query_text

    def add_cte(self, cte):
        """
        Добавляет объект CTE в список CTE, если они есть.

        :param cte: объект CTE, который нужно добавить
        """
        self.ctes.append(cte)

    def get_ctes(self):
        """
        Возвращает список всех CTE в запросе.
        """
        return self.ctes

    def get_query(self):
        """
        Возвращает полный SQL-запрос.
        """
        return self.query_text