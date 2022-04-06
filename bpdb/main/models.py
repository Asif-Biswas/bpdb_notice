from django.db import models
from django.core.validators import FileExtensionValidator
from ckeditor.fields import RichTextField
from django.utils import timezone

# Create your models here.

class Notice(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextField()
    pdf = models.FileField(upload_to='pdf/', blank=True, null=True, validators=[FileExtensionValidator(['pdf'])])
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class Update(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextField()
    pdf = models.FileField(upload_to='pdf/', blank=True, null=True, validators=[FileExtensionValidator(['pdf'])])
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title