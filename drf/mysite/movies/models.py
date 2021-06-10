from django.db import models


# Create your models here.
class Moviedata(models.Model):

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.typ = self.typ.lower()
        return super(Moviedata, self).save(*args, **kwargs)

    name = models.CharField(max_length=200)
    duration = models.FloatField()
    rating = models.FloatField()
    typ = models.CharField(max_length=200, default='action')
    image = models.ImageField(upload_to='images/', default='images/none/noimg.jpg')
