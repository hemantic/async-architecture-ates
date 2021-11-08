from app.models import Task


class TaskCreatingService:
    """
    Сервис обновления задачи
    """
    def __init__(self):
        pass

    def __call__(self, task_data):
        task = self.execute_create(task_data)

        self.emit_events(task)

    @staticmethod
    def execute_create(task_data):
        """Записывает задачу в БД

        Метод производит запись задачи в БД, вызываю соответсвующий метод модели
        """
        return Task.objects.craeate(**task_data)

    @staticmethod
    def emit_events(task):
        """Отравляет события по созданной задаче

        Метод отправляет необходимые CUD и BE события по созданной задаче
        """
