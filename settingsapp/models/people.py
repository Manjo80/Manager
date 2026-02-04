from django.db import models
from .common import ActiveModel

class Person(ActiveModel):
    short = models.CharField(max_length=20, unique=True, db_index=True)
    codename = models.CharField(max_length=80, blank=True, default="")

    def __str__(self):
        return f"{self.short}" + (f" ({self.codename})" if self.codename else "")
