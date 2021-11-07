from app.models import Task, User


class TaskReassigningService:
    """
    Сервис перераспределения задач между попугами
    """
    def __init__(self):
        pass

    def __call__(self):
        tasks = self.fetch_open_tasks()
        users = self.fetch_users()

        for task in tasks:
            user = self.choose_lucky(users)

            self.assign_task(task, user)
            self.emit_events(task)

    @staticmethod
    def fetch_open_tasks():
        """Получает все открытые задачи

        Метод получает список всех открытых задач через соответствующий метод модели
        """
        return Task.objects.filter_active()

    @staticmethod
    def fetch_users():
        """Получает всех попугов, на которых может быть назначена задача

        Метод получает всех пригодных для назначения задач попугов из БД
        """
        return User.objects.all()

    @staticmethod
    def choose_lucky(users):
        """Выбирает случайного пользователя из списка

        Метод выбирает одного случайного пользователя из переданного ему списка пользователей
        """
        return users.order_by('?').first()

    @staticmethod
    def assign_task(task, user):
        """Назначает задачу

        Метод назначает задачу на переданного попуга
        """
        task.assign(user)
        task.save()

    @staticmethod
    def emit_events(task):
        """Отравляет события по назначенной задаче

        Метод отправляет необходимые CUD и BE события по назначенной задаче
        """
