from app.models import Task


class TaskUpdatingService:
    def __init__(self):
        pass

    def __call__(self, task_data):
        task = self.execute_create(task_data)

        self.emit_events(task)

    @staticmethod
    def execute_create(task_data):
        return Task.objects.craeate(**task_data)

    @staticmethod
    def emit_events(task):
        pass
