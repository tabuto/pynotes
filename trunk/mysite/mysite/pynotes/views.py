# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from models import Note, NoteType, NoteForm, NoteTypeForm
from django.forms.models import inlineformset_factory
from datetime import datetime
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def pynotes_login(request):
    if request.method == 'POST': # If the form has been submitted...
        username_id = request.POST['username']
        pswd = request.POST['password']
        user = authenticate(username=username_id, password=pswd)
    else:
        user = None
    
    if user is not None:
        if user.is_active:
            login(request, user)
            # Redirect to a success page.
            return HttpResponseRedirect('/mysite/pynotes/')
        else:
            errors_dict = {'L0001':'Account Disabled'}
            return render(request,"error.html", 
                            {'sezione':{'titolo':'Error Page'}, 'errors': errors_dict})
            # Return a 'disabled account' error message
    else:
        errors_dict = {'L0002':'Invalid Login'}
        return render(request,"error.html", 
                      {'sezione':{'titolo':'Error Page'}, 'errors': errors_dict})
        # Return an 'invalid login' error message. 

def pynotes_logout(request):
    logout(request)
    return HttpResponseRedirect('/mysite/pynotes/')

def welcome(request):
      return render(request,"index.html", 
                            {'sezione':{'titolo':'Welcome!'}})

def about(request):
      return render(request,"about.html", 
                            {'sezione':{'titolo':'About Us'}})
def contact(request):
    return render(request,"contact.html", 
                            {'sezione':{'titolo':'Contact'}})
            
@login_required(login_url='/mysite/pynotes/welcome/')
def note_list(request):
  print 'note_list request'
  note_list = Note.objects.all()
  print 'size: ' + str(len(note_list))
  return render(request,"home.html", 
                            {'sezione':{'titolo':'Note Collection'}, 'note_list': note_list})
  
@login_required(login_url='/mysite/pynotes/welcome/')
def note_form(request):
    type_list = NoteType.objects.all().order_by('desc')
    form = NoteForm()
    return render(request,"note_form.html", 
                            {'sezione':{'titolo':'Edit Add Note '}, 'type_list': type_list,'form':form})

@login_required(login_url='/mysite/pynotes/welcome/')
def note_type_form(request):
    type_list = NoteType.objects.all().order_by('desc')
    form = NoteTypeForm()
    return render(request,"note_type_form.html", 
                            {'sezione':{'titolo':'Edit Add Note Type '}, 'type_list': type_list,'form':form})

@login_required(login_url='/mysite/pynotes/welcome/')
def note_detail(request,note_id):
    selected = Note.objects.get(id=note_id)
    return render(request,"note_detail.html", 
                            {'sezione':{'titolo':'Note Detail '}, 'selected': selected})

@login_required(login_url='/mysite/pynotes/welcome/')
def add_new_note_type(request):
     if request.method == 'POST': # If the form has been submitted...
        form = NoteTypeForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            form.save()
            
     type_list = NoteType.objects.all().order_by('desc')
     form = NoteTypeForm() # An unbound form
     return render(request,"note_type_form.html", 
                            {'sezione':{'titolo':'Edit Add Note Type '}, 'type_list': type_list,'form':form})
            

@login_required(login_url='/mysite/pynotes/welcome/')
def add_new_note(request):
    if request.method == 'POST': # If the form has been submitted...
        form = NoteForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass 
            note = form.save(commit=False)
            note.pub_date = datetime.now()
            note.save()
            return HttpResponseRedirect('/mysite/pynotes/')
        else:
            for field in form:
                if field.errors: 
                    print str(field)
                    print field.label_tag
                    print field.errors
            
         # Redirect after POST
         
    
    type_list = NoteType.objects.all().order_by('desc')
    form = NoteForm() # An unbound form
    return render(request, 'note_form.html', {
        'sezione':{'titolo':'Edit Add Note '},
        'form': form,'type_list': type_list
    })

@login_required(login_url='/mysite/pynotes/welcome/')    
def new_type(request):
    to_add = NoteType()
    to_add.desc = request.POST['new_type_desc']
    to_add.objects.save()
    type_list = NoteType.objects.all().order_by('desc')
    return render(request,"note_form.html", 
                            {'sezione':{'titolo':'Edit Add Note '}, 'type_list': type_list})
    