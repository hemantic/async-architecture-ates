import uuid

from django.db import models


class TasksQuerySet(models.QuerySet):
    def filter_active(self):
        return self.filter(status=Task.Status.ACTIVE)


class Task(models.Model):
    class Status(models.TextChoices):
        ACTIVE = "active", "Активна"
        CLOSED = "closed", "Закрыта"

    objects = TasksQuerySet.as_manager()

    #: Публичный ID задачи
    public_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    #: Заголовок задачи
    title = models.CharField(max_length=1023)

    #: Описание задачи
    description = models.TextField(blank=True, default='')

    #: Статус задачи
    status = models.CharField(max_length=255, choices=Status.choices, default=Status.ACTIVE)

    #: Комиссия за назначение задачи
    fee = models.DecimalField(max_digits=7, decimal_places=2, default=0)

    #: Выплата за закрытие задачи
    reward = models.DecimalField(max_digits=7, decimal_places=2, default=0)

    #: Дата создание задачи
    created_at = models.DateTimeField(auto_now_add=True)

    #: Дата последнего обновления задачи
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "task"
        verbose_name = "task"
        verbose_name_plural = "tasks"

        indexes = [
            models.Index(fields=["status"]),
        ]

        ordering = ["-created_at"]

    def __str__(self):
        return self.title

    def close(self):
        self.status = self.Status.CLOSED
