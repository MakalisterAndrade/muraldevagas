from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from django.contrib import auth

from jobapp.models import *
from ckeditor.widgets import CKEditorWidget


    

class JobForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        forms.ModelForm.__init__(self, *args, **kwargs)
        self.fields['title'].label = "Nome da vaga:"
        self.fields['location'].label = "Localização :"
        self.fields['salary'].label = "Salário :"
        self.fields['description'].label = "Descrição da vaga :"
        self.fields['tags'].label = "Tags :"
        self.fields['last_date'].label = "Data limite para incrição:"
        self.fields['company_name'].label = "Nome da empresa :"
        self.fields['url'].label = "Website :"


        self.fields['title'].widget.attrs.update(
            {
                'placeholder': 'ex : Analista de software',
            }
        )        
        self.fields['location'].widget.attrs.update(
            {
                'placeholder': 'ex : Ariquemes',
            }
        )
        self.fields['salary'].widget.attrs.update(
            {
                'placeholder': 'R$800 - R$1200',
            }
        )
        self.fields['tags'].widget.attrs.update(
            {
                'placeholder': 'Use vírgula para separar. ex: Python, JavaScript ',
            }
        )                        
        self.fields['last_date'].widget.attrs.update(
            {
                'placeholder': 'YYYY-MM-DD ',
                
            }
        )        
        self.fields['company_name'].widget.attrs.update(
            {
                'placeholder': 'Nome da empresa',
            }
        )           
        self.fields['url'].widget.attrs.update(
            {
                'placeholder': 'https://example.com',
            }
        )    


    class Meta:
        model = Job

        fields = [
            "title",
            "location",
            "job_type",
            "salary",
            "description",
            "tags",
            "last_date",
            "company_name",
            "company_description",
            "url"
            ]

    def clean_job_type(self):
        job_type = self.cleaned_data.get('job_type')

        if not job_type:
            raise forms.ValidationError("Tipo é obrigatório")
        return job_type




    def save(self, commit=True):
        job = super(JobForm, self).save(commit=False)
        if commit:
            
            job.save()
        return job




class JobApplyForm(forms.ModelForm):

    class Meta:
        model = Applicant
        fields = ['job']


class JobBookmarkForm(forms.ModelForm):
    class Meta:
        model = BookmarkJob
        fields = ['job']




class JobEditForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        forms.ModelForm.__init__(self, *args, **kwargs)
        self.fields['title'].label = "Nome da vaga :"
        self.fields['location'].label = "Localização :"
        self.fields['salary'].label = "Salário :"
        self.fields['description'].label = "Descrição da vaga :"
        # self.fields['tags'].label = "Tags :"
        self.fields['last_date'].label = "Prazo para inscrição :"
        self.fields['company_name'].label = "Nome da empresa :"
        self.fields['url'].label = "Website :"


        self.fields['title'].widget.attrs.update(
            {
                'placeholder': 'ex : Software Developer',
            }
        )        
        self.fields['location'].widget.attrs.update(
            {
                'placeholder': 'ex : Ariquemes',
            }
        )
        self.fields['salary'].widget.attrs.update(
            {
                'placeholder': 'R$800 - R$1200',
            }
        )
        # self.fields['tags'].widget.attrs.update(
        #     {
        #         'placeholder': 'Use comma separated. eg: Python, JavaScript ',
        #     }
        # )                        
        self.fields['last_date'].widget.attrs.update(
            {
                'placeholder': 'YYYY-MM-DD ',
            }
        )        
        self.fields['company_name'].widget.attrs.update(
            {
                'placeholder': 'Nome da empresa',
            }
        )           
        self.fields['url'].widget.attrs.update(
            {
                'placeholder': 'https://example.com',
            }
        )    

    
        last_date = forms.CharField(widget=forms.TextInput(attrs={
                    'placeholder': 'Service Name',
                    'class' : 'datetimepicker1'
                }))

    class Meta:
        model = Job

        fields = [
            "title",
            "location",
            "job_type",
            "salary",
            "description",
            "last_date",
            "company_name",
            "company_description",
            "url"
            ]

    def clean_job_type(self):
        job_type = self.cleaned_data.get('job_type')

        if not job_type:
            raise forms.ValidationError("Tipo de vaga é obrigatório")
        return job_type




    def save(self, commit=True):
        job = super(JobEditForm, self).save(commit=False)
      
        if commit:
            job.save()
        return job

