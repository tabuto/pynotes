from django.db import models
from django.forms import ModelForm,Textarea,CharField
from django.forms.models import ModelChoiceField
from datetime import datetime
from django.contrib.auth.models import User  

# Create your models here.

class NoteType(models.Model): 
  desc = models.CharField(max_length=255)
  def __str__(self):
     return self.desc
   

class Note(models.Model): 
  title = models.CharField(max_length=255) 
  type = models.CharField(max_length=255)
  pub_date = models.DateTimeField('pub_date')
  type = models.ForeignKey(NoteType)
  body = models.CharField(max_length=4000)
  owner = models.ForeignKey(User)


class NoteTypeForm(ModelForm):
     desc = CharField(label='Description')
     class Meta:
         model = NoteType
         
  
class NoteForm(ModelForm):
    title = CharField(label='Title',validators=[])
   # body = CharField(label='Note')
    #new_category = CharField(label='Add New Type',validators=[])
    type = ModelChoiceField(queryset=NoteType.objects.all(), initial=0)
    
    class Meta:
        model = Note
        fields = ('title','body','type','id')
        exclude = ('pub_date',)
        widgets = {
            'body': Textarea(attrs={'cols': 70, 'rows': 10}),
            
        }
    def clean_pub_date(self):
        self.cleaned_data['pub_date'] = datetime.now()
        return self.cleaned_data['pub_date'] 
        
   
class UserForm(ModelForm):
    class Meta:
        model = User  
        fields = ('username','email','password')


'''
  title = models.CharField(max_length=255) 
  type = forms.ModelMultipleChoiceField(queryset=NoteType.objects.all().order_by('desc'))
  pub_date = models.DateTimeField('pub_date')
  type = models.ForeignKey(NoteType)
  body = models.CharField(max_length=4000)
'''
