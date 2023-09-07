# # admin.py
from django.contrib import admin
from .models import Category, Class, Subject, Note, Syllabus

# class SubjectInline(admin.TabularInline):
#     model = Subject

# class NoteInline(admin.TabularInline):
#     model = Note

# class SyllabusInline(admin.TabularInline):
#     model = Syllabus

# class ClassAdmin(admin.ModelAdmin):
#     inlines = [SubjectInline]

# class CategoryAdmin(admin.ModelAdmin):
#     inlines = [ClassAdmin]

# admin.site.register(Category, CategoryAdmin)
# admin.site.register(Class, ClassAdmin)
# admin.site.register(Subject)
# admin.site.register(Note)
# admin.site.register(Syllabus)
# from django.contrib import admin
# from .models import Category, Subject, Note, Syllabus

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

admin.site.register(Category, CategoryAdmin)
admin.site.register(Class, ClassAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Note, NoteAdmin)
admin.site.register(Syllabus, SyllabusAdmin)