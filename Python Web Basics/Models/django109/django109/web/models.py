from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=15)


class Employee(models.Model):
    # Var char(30) => strings with max length 30
    first_name = models.CharField(
        max_length=30,
    )

    last_name = models.CharField(
        max_length=50,
        null=True,
    )

    # int
    years_of_experience = models.PositiveIntegerField()

    # Text => strings with unlimited length
    review = models.TextField()

    start_date = models.DateTimeField()

    email = models.EmailField(
        unique=True,
        editable=False,
    )

    # This will be automatically set on creation
    created_on = models.DateTimeField(
        auto_now_add=True,  # optional
    )

    # This will be automatically set on each 'save'/'update'
    update_on = models.DateTimeField(
        auto_now=True,  # optional
    )

    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
    )
