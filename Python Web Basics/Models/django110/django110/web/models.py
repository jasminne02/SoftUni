from django.db import models


class Department(models.Model):
    name = models.CharField(default=1, max_length=15)


class Project(models.Model):
    name = models.CharField(
        max_length=30,
    )

    deadline = models.DateField()


class Employees(models.Model):
    first_name = models.CharField(
        max_length=30,
        null=True
    )

    last_name = models.CharField(
        max_length=30,
        null=True
    )

    level = models.CharField(
        max_length=4,
        choices=(
            ('jr.', 'Junior'),
            ('mid.', 'Middle'),
            ('sr.', 'Senior'),
        ),
        verbose_name='Seniority level'
    )

    department = models.ForeignKey(
        Department,
        on_delete=models.SET_NULL,
        null=True
    )

    projects = models.ManyToManyField(Project)
