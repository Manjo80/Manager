from django.db import models
from .common import ActiveModel

class Group(ActiveModel):
    name = models.CharField(max_length=120, unique=True, db_index=True)

    def __str__(self):
        return self.name
