from app.models import Task


class TaskReassigningService:
    def __init__(self):
        pass

    def __call__(self):
        tasks = self.fetch_open_tasks()

        for task in tasks:
            self.assign_task(task)
            self.emit_events(task)

    @staticmethod
    def fetch_open_tasks():
        return Task.objects.filter_active()

    @staticmethod
    def assign_task(task):
        task.close()
        task.save()

    @staticmethod
    def emit_events(task):
        pass
