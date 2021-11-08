class TaskClosingService:
    """
    Сервис закрытия задачи
    """
    def __init__(self):
        pass

    def __call__(self, task):
        self.check(task)
        self.close(task)
        self.emit_events(task)

    @staticmethod
    def check(task):
        """Проверяет, можно ли закрыть задачу

        Метод проверят, можно ли закрыть задачу – находится ли она в правильно статусе и проч.
        """
        pass

    @staticmethod
    def close(task):
        """Произоводит закрытие задачи

        Метод закрывает задачу, вызывая соответствующий метод в её модели
        """
        task.close()
        task.save()

    @staticmethod
    def emit_events(task):
        """Отравляет события по закрытой задаче

        Метод отправляет необходимые CUD и BE события по закрытой задаче
        """
