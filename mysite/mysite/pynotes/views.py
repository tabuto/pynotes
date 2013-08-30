# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect,Http404
from django.shortcuts import render, get_object_or_404,render_to_response
from models import Note, NoteType, NoteForm, NoteTypeForm, UserForm
from django.forms.models import inlineformset_factory
from datetime import datetime
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.template import RequestContext


@login_required(login_url='/mysite/pynotes/welcome/')
def get_body(request,note_id):
    if request.is_ajax():
        print 'get_body AJAX called for id '+str(id)
        body =  Note.objects.get(id=note_id).body
        return render_to_response('ajax.html',
                                  { 'selected_body':body,'note_id':note_id},
                                  context_instance = RequestContext(request))
    else:
         print 'Not ajaxRequest '
         raise Http404

@login_required(login_url='/mysite/pynotes/welcome/')
def get_note_type_list(request):
    if request.is_ajax():
        print 'get_note_type_list called for id '+str(id)
        type_list = NoteType.objects.all().order_by('desc')
        return render_to_response('ajax.html',
                                  { 'selected_body':body,'type_list':type_list},
                                  context_instance = RequestContext(request))
    else:
         print 'Not ajaxRequest '
         raise Http404


def user_registration(request):
    if request.method == 'POST': # If the form has been submitted...
        uf = UserForm(request.POST)
        if uf.is_valid():
            username_id = request.POST['username']
            pswd = request.POST['password']
            email = request.POST['email']
            user = User.objects.create_user(username_id, email, pswd)
            user.save()
            print 'User succesfully registered!'

    return HttpResponseRedirect('/mysite/pynotes/')

def pynotes_login(request):
    if request.method == 'POST': # If the form has been submitted...
    
        if 'register_sub' in request.POST:
            uf = UserForm()
            return render(request,"register.html", 
                      {'sezione':{'titolo':'Registration'}, 'errors': None,'userform':uf})
        else :
            # do unsubscribe
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
  note_list = Note.objects.filter(owner=request.user.id).order_by('pub_date')
  print 'size: ' + str(len(note_list))
  return render(request,"home.html", 
                            {'sezione':{'titolo':'Note Collection'}, 'note_list': note_list})
  
@login_required(login_url='/mysite/pynotes/welcome/')
def note_form(request, note_id=None):
    type_list = NoteType.objects.all().order_by('desc')
    
    if note_id:
        note = Note.objects.get(id=note_id)
        data = {
        'id':note.id,
         'title': note.title,
         'body': note.body,
         'type': note.type
         }
        form = NoteForm(initial=data)
    else:
        form = NoteForm()
    
    return render(request,"note_form.html", 
                            {'sezione':{'titolo':'Edit Add Note '}, 'type_list': type_list,'form':form,'note_id':note_id})

@login_required(login_url='/mysite/pynotes/welcome/')
def note_type_form(request):  
    type_list = NoteType.objects.all().order_by('desc')
    form = NoteTypeForm()    
    return render(request,"note_type_form.html", 
                            {'sezione':{'titolo':'Edit Add Note Type '}, 'type_list': type_list,'form':form})

@login_required(login_url='/mysite/pynotes/welcome/')
def note_detail(request,note_id):
    selected = Note.objects.get(id=note_id,owner_id=request.user.id)
    return render(request,"note_detail.html", 
                            {'sezione':{'titolo':'Note Detail '}, 'selected': selected})

@login_required(login_url='/mysite/pynotes/welcome/')
def edit_note(request, note_id):
    print 'edit note_id '+ str(note_id)
    return note_list(request)

@login_required(login_url='/mysite/pynotes/welcome/')
def edit_note_type(request, note_type_id):
    print 'edit note_type_id '+ str(note_type_id)
    return note_list(request)

@login_required(login_url='/mysite/pynotes/welcome/')
def del_note(request, note_id):
    print 'delete note_id '+ str(note_id)
    note = Note.objects.get(id=note_id)
    note.delete()
    return note_list(request)

@login_required(login_url='/mysite/pynotes/welcome/')
def add_new_note_type(request):
    
     if request.is_ajax():
        print 'get_note_type_list AJAX called for '
        form = NoteTypeForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            form.save()
            print 'note type saved'
        type_list = NoteType.objects.all().order_by('desc')
        form = NoteTypeForm() # An unbound form
        return render_to_response('note_type_form.html',
                                  { 'sezione':{'titolo':'Edit Add Note Type '},'type_list':type_list, 'form':form},
                                  context_instance = RequestContext(request))
    
     elif request.method == 'POST': # If the form has been submitted...
        form = NoteTypeForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            form.save()
            print 'note type saved'
        type_list = NoteType.objects.all().order_by('desc')
        form = NoteTypeForm() # An unbound form
        return render(request,"note_type_form.html", 
                            {'sezione':{'titolo':'Edit Add Note Type '}, 'type_list': type_list,'form':form})
            

@login_required(login_url='/mysite/pynotes/welcome/')
def add_new_note(request,note_id=None):
    if request.method == 'POST': # If the form has been submitted...
        form = NoteForm(request.POST) # A form bound to the POST data
        if note_id:
            print note_id
            form = NoteForm(request.POST,instance=get_object_or_404(Note, id=note_id)) 
        if form.is_valid(): # All validation rules pass 
            note = form.save(commit=False)
            note.pub_date = datetime.now()
            note.owner=request.user
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
    print 'new type saved'
    return render(request,"note_form.html", 
                            {'sezione':{'titolo':'Edit Add Note '}, 'type_list': type_list})
    