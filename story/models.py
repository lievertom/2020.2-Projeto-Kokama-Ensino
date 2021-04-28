from django.db import models


class Language(models.Model):
    language = models.CharField(max_length=10)

    def __str__(self):
        return self.language

class Story(models.Model):
    language = models.ForeignKey(
        Language,
        on_delete=models.DO_NOTHING,
        db_constraint=False
    )
    title = models.CharField(max_length=50)
    text = models.TextField()

    def __str__(self):
        return self.title
