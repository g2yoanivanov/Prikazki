from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


class Author(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=64)
    nationality = models.CharField(max_length=32)
    date_of_birth = models.DateField()
    date_of_death = models.DateField()
    biography = RichTextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name}"


class FairyTale(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=256)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    content = RichTextField(blank=True, null=True)
    image = models.ImageField(null=True, blank=True)
    times_read = models.IntegerField(default=1)

    def __str__(self):
        return '%s - %s' % (self.title, self.author)
