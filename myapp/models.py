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

# class Note(models.Model):
#     subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
#     title = models.CharField(max_length=100 , unique=True)
#     pdf = models.FileField(upload_to='pdfs/')

#     def __str__(self):
#         return self.title

class Syllabus(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    title = models.CharField(max_length=100 ,unique=True)
    pdf = models.FileField(upload_to='pdfs/' )

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        super().save(*args,**kwargs)
        HTN = HashTableSyllabus(syllabus=self,syl_id=hash(self.title))
        HTN.save()
    
class Notes(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    title = models.CharField(max_length=100 ,unique=True)
    pdf = models.FileField(upload_to='pdfs/' )

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        super().save(*args,**kwargs)
        HTN = HashTableNotes(note=self,not_id=hash(self.title))
        HTN.save()

    
class HashTableNotes(models.Model):
    note = models.OneToOneField(Notes, on_delete=models.CASCADE)
    not_id = models.BigIntegerField()

    def __str__(self):
        return str(self.not_id)
    
class HashTableSyllabus(models.Model):
    syllabus = models.OneToOneField(Syllabus, on_delete=models.CASCADE)
    syl_id = models.BigIntegerField()

    def __str__(self):
        return str(self.syl_id)
    
class Update(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    link=models.CharField(max_length=50)
    date_published = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Meta:
    verbose_name_plural = 'Categories'