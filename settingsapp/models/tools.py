from django.db import models
from .common import ActiveModel

class Tool(ActiveModel):
    name = models.CharField(max_length=120, unique=True, db_index=True)
    photo = models.ImageField(upload_to="tools/", blank=True, null=True)

    def __str__(self):
        return self.name
