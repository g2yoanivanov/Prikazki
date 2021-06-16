from django.db import models
from ckeditor.fields import RichTextField


class Subject(models.Model):
    subject = models.CharField(max_length=256)

    def __str__(self):
        return f"{self.subject}"


class Comment(models.Model):
    subject = models.ForeignKey(Subject, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    comment = RichTextField(blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.name, self.date_added)