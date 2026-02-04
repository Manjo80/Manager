from django.db import models

class ActiveModel(models.Model):
    active = models.BooleanField(default=True, db_index=True)

    class Meta:
        abstract = True
