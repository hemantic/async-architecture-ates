from app.models import Task


class TaskUpdatingService:
    def __init__(self):
        pass

    def __call__(self, task, update):
        self.execute_update(task, update)
        self.emit_events(task)

    @staticmethod
    def execute_update(task, update):
        """Обновляет задачу

        Метод обновляет задачу, вызывая соответствующией действия над моделью
        """
        task = Task(index=task.id, **update)
        task.save()
        return task

    @staticmethod
    def emit_events(task):
        """Отравляет события по обновленной задаче

        Метод отправляет необходимые CUD и BE события по обновленной задаче
        """
