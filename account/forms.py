from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm

from account.models import User


class EmployeeRegistrationForm(UserCreationForm):


    def __init__(self, *args, **kwargs):
        UserCreationForm.__init__(self, *args, **kwargs)
        self.fields['gender'].required = True
        self.fields['first_name'].label = "Nome:"
        self.fields['last_name'].label = "Sobrenome:"
        self.fields['password1'].label = "Senha:"
        self.fields['password2'].label = "Confirmar senha:"
        self.fields['email'].label = "Email:"
        self.fields['gender'].label = "Gênero:"
        self.fields['cv'].label = "Currículo: "
        self.fields['telefone_number'].label = "Telefone: "

        self.fields['first_name'].widget.attrs.update(
            {
                'placeholder': 'Insira seu nome',
            }
        )
        self.fields['last_name'].widget.attrs.update(
            {
                'placeholder': 'Insira seu sobrenome',
            }
        )
        self.fields['email'].widget.attrs.update(
            {
                'placeholder': 'Insira Email',
            }
        )        
        self.fields['telefone_number'].widget.attrs.update(
            {
                'placeholder': 'Insira seu contato',
            }
        )
        self.fields['password1'].widget.attrs.update(
            {
                'placeholder': 'Insira senha',
            }
        )
        self.fields['password2'].widget.attrs.update(
            {
                'placeholder': 'Confirmar senha',
            }
        )
        self.fields['cv'].widget.attrs.update(
            {
                'placeholder': 'Insira seu currículo em pdf',
            }
        )

    class Meta:

        model=User

        fields = ['first_name', 'last_name', 'email','telefone_number', 'password1', 'password2', 'cv', 'gender']

    def clean_gender(self):
        gender = self.cleaned_data.get('gender')
        if not gender:
            raise forms.ValidationError("Gênero é obrigatório")
        return gender

    def save(self, commit=True):
        user = UserCreationForm.save(self,commit=False)
        user.role = "employee"
        if commit:
            user.save()
        return user


class EmployerRegistrationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        UserCreationForm.__init__(self, *args, **kwargs)
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['first_name'].label = "Nome do empregador"
        self.fields['last_name'].label = "Endereço do empregador"
        self.fields['password1'].label = "Senha"
        self.fields['password2'].label = "Confirmar senha"

        self.fields['first_name'].widget.attrs.update(
            {
                'placeholder': 'Insira o nome',
            }
        )
        self.fields['last_name'].widget.attrs.update(
            {
                'placeholder': 'Insira o endereço',
            }
        )
        self.fields['email'].widget.attrs.update(
            {
                'placeholder': 'Insira o email',
            }
        )
        self.fields['password1'].widget.attrs.update(
            {
                'placeholder': 'Senha',
            }
        )
        self.fields['password2'].widget.attrs.update(
            {
                'placeholder': 'Confirmar senha',
            }
        )
    class Meta:

        model=User

        fields = ['first_name', 'last_name', 'email', 'password1', 'password2',]


    def save(self, commit=True):
        user = UserCreationForm.save(self,commit=False)
        user.role = "employer"
        if commit:
            user.save()
        return user
    
    def clean_telefone_number(self):
        telefone_number = self.cleaned_data.get('telefone_number')
        if telefone_number and not telefone_number.isdigit():
            raise forms.ValidationError("O número de telefone deve conter apenas dígitos.")
        return telefone_number


class UserLoginForm(forms.Form):
    email =  forms.EmailField(
    widget=forms.EmailInput(attrs={ 'placeholder':'Email',})
) 
    password = forms.CharField(strip=False,widget=forms.PasswordInput(attrs={
        
        'placeholder':'Senha',
    }))

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")

        if email and password:
            self.user = authenticate(email=email, password=password)
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                raise forms.ValidationError("Cadastro não encontrado.")

            if not user.check_password(password):
                raise forms.ValidationError("Senhas não são iguais.")

            if not user.is_active:
                raise forms.ValidationError("Cadastro não ativo, contate o admin.")

        return super(UserLoginForm, self).clean(*args, **kwargs)

    def get_user(self):
        return self.user



class EmployeeProfileEditForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(EmployeeProfileEditForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].label = "Nome:"
        self.fields['last_name'].label = "Sobrenome:"
        self.fields['cv'].label = "Currículo: "
        self.fields['telefone_number'].label = "Telefone: "
    
    def clean_telefone_number(self):
        telefone_number = self.cleaned_data.get('telefone_number')
        if telefone_number and not telefone_number.isdigit():
            raise forms.ValidationError("O número de telefone deve conter apenas dígitos.")
        return telefone_number
    class Meta:
        model = User
        fields = ["first_name", "last_name","telefone_number","cv", "gender"]
