from django.db import models


class Option(models.Model):
    option = models.CharField(max_length=50)

    def __str__(self):
        return self.option


class Activity(models.Model):
    phrase_portuguese = models.TextField(null=False, blank=False)
    phrase_kokama = models.TextField(null=False, blank=False)
    
    options = models.ManyToManyField(
        Option,
        through='Contain',
        through_fields=('activity', 'options'),
        )

    def __str__(self):
        return self.id


class Contain(models.Model):
    activity = models.ForeignKey(
        Activity,
        on_delete=models.PROTECT
    )

    options = models.ForeignKey(
        Option,
        on_delete=models.PROTECT
    )
