from datetime import date

from django.db import models


class Employees(models.Model):

    class Meta:
        ordering = ['level']
        verbose_name_plural = "employees"

    LEVEL_JUNIOR = 'Junior'
    LEVEL_MIDDLE = 'Middle'
    LEVEL_SENIOR = 'Senior'

    LEVELS = (
        (LEVEL_JUNIOR, LEVEL_JUNIOR),
        (LEVEL_MIDDLE, LEVEL_MIDDLE),
        (LEVEL_SENIOR, LEVEL_SENIOR),
    )

    first_name = models.CharField(
        max_length=25
    )

    last_name = models.CharField(
        max_length=25
    )

    level = models.CharField(
        max_length=6,
        choices=LEVELS,
        verbose_name='seniority level'
    )

    start_date = models.DateTimeField()

    @property
    def years_of_employment(self):
        return date.today() - self.start_date
