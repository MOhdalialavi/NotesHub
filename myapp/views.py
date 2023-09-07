from django.shortcuts import redirect, render,get_object_or_404
from .models import Category, Class, Subject, Note, Syllabus
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def index(request):
    categories = Category.objects.all()
    return render(request, 'index.html', {'categories': categories})

def login(request):
    print("login ka apge mai aagaya")
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print("User is athenticatind")
        user = authenticate(request, username=username, password=password)
        if user is not None:

            return redirect('/admin')

        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    else:
        return render(request, 'login.html')


    
@login_required
def admin_view(request):
    return render(request, 'admin2.html')

def logout_view(request):
    logout(request)
    return redirect('/')

def category_view(request, category_name):
    category = get_object_or_404(Category, name=category_name)
    classes = Class.objects.filter(category=category)
    return render(request, 'category.html', {'category': category, 'classes': classes})

def class_view(request, category_name, class_name):
    category = get_object_or_404(Category, name=category_name)
    class_obj = get_object_or_404(Class, name =class_name ,category=category)
    subjects = Subject.objects.filter(class_name=class_obj)
    return render(request, 'class.html', {'category': category, 'class_obj': class_obj, 'subjects': subjects})



def board(request, category_name, class_name, subject_name):
    category = get_object_or_404(Category, name=category_name)
    class_obj = get_object_or_404(Class, name =class_name ,category=category)
    subject = get_object_or_404(Subject, name=subject_name, class_name=class_obj)
    notes = Note.objects.filter(subject=subject)
    syllabi = Syllabus.objects.filter(subject=subject)
    return render(request, 'board.html', {'category': category, 'class': class_obj, 'subject': subject, 'notes': notes, 'syllabi': syllabi})
  