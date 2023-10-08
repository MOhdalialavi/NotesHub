# models.py
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)
    images=models.ImageField(upload_to='images/')
    # slug=models.SlugField(null=False)

    def __str__(self):
        return self.name

class Class(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Subject(models.Model):
    class_name = models.ForeignKey(Class, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)


    def __str__(self):
        return self.name

class Note(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    title = models.CharField(max_length=100 , unique=True)
    pdf = models.FileField(upload_to='pdfs/')

    def __str__(self):
        return self.title

class Syllabus(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    title = models.CharField(max_length=100 ,unique=True)
    pdf = models.FileField(upload_to='pdfs/' )

    def __str__(self):
        return self.title
    

class Update(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    link=models.CharField(max_length=50)
    date_published = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Meta:
    verbose_name_plural = 'Categories'