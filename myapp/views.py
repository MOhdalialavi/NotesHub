from django.shortcuts import redirect, render,get_object_or_404
from django.http import Http404, HttpResponse, FileResponse
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.template.defaultfilters import slugify


def index(request):
    categories = Category.objects.all()
    updates = Update.objects.all()[:5]
    classes=Class.objects.all()
    return render(request, 'index.html', {'categories': categories,'updates': updates,'classes': classes})

# def login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         print("User is athenticatind")
#         user = authenticate(request, username=username, password=password)
#         if user is not None:

#             return redirect('/admin')

#         else:
#             return render(request, 'login.html', {'error': 'Invalid credentials'})
#     else:
#         return render(request, 'login.html')


    
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
    class_obj = get_object_or_404(Class, name=class_name, category=category)
    subject = get_object_or_404(Subject, name=subject_name, class_name=class_obj)
    
    note = Notes.objects.filter(subject=subject).first()
    hashtitle = None

    if note:
        print("hiii")
        hashtitle = get_object_or_404(HashTableNotes, note=note)
        # Note: Don't use hashtitle[0], as get_object_or_404 returns a single object, not a queryset.

    syllabi = Syllabus.objects.filter(subject=subject).first()
    titlehash = None

    if syllabi:
        print('hooo')
        titlehash = get_object_or_404(HashTableSyllabus, syllabus=syllabi)
        # Note: Don't use titlehash[0], as get_object_or_404 returns a single object, not a queryset.

    return render(request, 'board.html', {
        'category': category,
        'class': class_obj,
        'subject': subject,
        'note': note,
        'syllabi': syllabi,
        'hashtitle': hashtitle,
        'titlehash': titlehash
    })

# def board(request, category_name, class_name, subject_name):
    category = get_object_or_404(Category, name=category_name)
    class_obj = get_object_or_404(Class, name =class_name ,category=category)
    subject = get_object_or_404(Subject, name=subject_name, class_name=class_obj)
    note = Note.objects.filter(subject=subject)
    if (isinstance(note,Notes)):  
        print("hiii")
        hashtitle=get_object_or_404(HashTableNotes ,note=note )
        hashtitle=hashtitle[0] #.namehash
    else:
        hashtitle=Http404()
    syllabi = Syllabus.objects.filter(subject=subject)
    if (isinstance(syllabi,Syllabus)):
        print(syllabi)
        titlehash=get_object_or_404(HashTableSyllabus,syllabus=syllabi)
        titlehash=titlehash[0] #.namehash
    else:
        titlehash=Http404()
    # hashtitlesy=HashTableSyllabus.objects.filter(syllabus=syllabi[0])
    return render(request, 'board.html',
                   {'category': category, 'class': class_obj,
                    'subject': subject, 'note': note, 'syllabi': syllabi,
                    "hashtitle":hashtitle,"titlehash":titlehash
                   }
                    )
def about(request):
    return render(request,"about.html")

# def download_notes(request, file_id):
    hashtitle = get_object_or_404(HashTableNotes, not_id=int(file_id))

    if isinstance(hashtitle, HashTableNotes):
        note = get_object_or_404(Notes, id=hashtitle.note_id)
        if isinstance(note, Notes):
            response = FileResponse(note.pdf, content_type='application/pdf')
            response['Content-Disposition'] = f'inline; filename="{note.title}.pdf"'
            return response
    else:
        return HttpResponse("File not found")

def download_notes(request, file_id):
    hashtitle = get_object_or_404(HashTableNotes, not_id=int(file_id))

    if isinstance(hashtitle, HashTableNotes):
        note = get_object_or_404(Notes, id=hashtitle.note_id)
        if isinstance(note, Notes):
            response = FileResponse(note.pdf, content_type='application/force-download')
            response['Content-Disposition'] = f'inline; filename="{note.title}.pdf"'
            return response
    else:
        return HttpResponse("File not found")

def download_syllabus(request, syb_id):
    titlehash = get_object_or_404(HashTableSyllabus, syl_id=int(syb_id))

    if isinstance(titlehash, HashTableSyllabus):
        syllabus = get_object_or_404(Syllabus, id=titlehash.syllabus_id)
        if isinstance(syllabus, Syllabus):
            # response = FileResponse(syllabus.pdf, content_type='application/pdf')
            response = FileResponse(syllabus.pdf, content_type='application/force-download')
            response['Content-Disposition'] = f'inline; filename="{syllabus.title}.pdf"'
            return response
    else:
        return HttpResponse("File not found")