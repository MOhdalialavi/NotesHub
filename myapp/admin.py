# # admin.py
from django.contrib import admin
from .models import Category, Class, Subject, Note, Syllabus,Update

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
class ClassAdmin(admin.ModelAdmin):
    list_display=('name','category')

class SubjectAdmin(admin.ModelAdmin):
    
    list_display = ('name', 'class_name')


class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'subject')

class SyllabusAdmin(admin.ModelAdmin):
    list_display = ('title', 'subject')
class updateAdmin(admin.ModelAdmin):
    list_display=('title','content')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Class, ClassAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Note, NoteAdmin)
admin.site.register(Syllabus, SyllabusAdmin)
admin.site.register(Update,updateAdmin)