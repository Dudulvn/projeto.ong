from django import forms

from .models import Adocao, Adotante, Animal, Tratamento


class FormularioAnimal(forms.ModelForm):
    class Meta:
        model = Animal
        fields = [
            'nome',
            'especie',
            'raca',
            'idade_aproximada',
            'sexo',
            'estado_saude',
            'local_resgate',
            'data_resgate',
            'status',
            'observacoes',
        ]
        widgets = {
            'data_resgate': forms.DateInput(attrs={'type': 'date'}),
            'estado_saude': forms.Textarea(attrs={'rows': 3}),
            'observacoes': forms.Textarea(attrs={'rows': 3}),
        }


class FormularioTratamento(forms.ModelForm):
    class Meta:
        model = Tratamento
        fields = ['animal', 'data', 'descricao', 'veterinario', 'observacoes']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),
            'descricao': forms.Textarea(attrs={'rows': 3}),
            'observacoes': forms.Textarea(attrs={'rows': 3}),
        }


class FormularioAdotante(forms.ModelForm):
    class Meta:
        model = Adotante
        fields = ['nome', 'cpf', 'telefone', 'email', 'endereco', 'observacoes']
        widgets = {
            'endereco': forms.Textarea(attrs={'rows': 3}),
            'observacoes': forms.Textarea(attrs={'rows': 3}),
        }

    def clean_cpf(self):
        cpf = ''.join(filter(str.isdigit, self.cleaned_data['cpf']))
        if len(cpf) != 11:
            raise forms.ValidationError('O CPF deve conter 11 dígitos.')
        return cpf


class FormularioAdocao(forms.ModelForm):
    class Meta:
        model = Adocao
        fields = ['animal', 'adotante', 'data_adocao', 'observacoes']
        widgets = {
            'data_adocao': forms.DateInput(attrs={'type': 'date'}),
            'observacoes': forms.Textarea(attrs={'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['animal'].queryset = Animal.objects.exclude(
            status=Animal.STATUS_ADOTADO
        )


class FormularioLogin(forms.Form):
    usuario = forms.CharField(label='Usuário', max_length=150)
    senha = forms.CharField(label='Senha', widget=forms.PasswordInput)
