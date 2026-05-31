from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models.deletion import ProtectedError
from django.shortcuts import get_object_or_404, redirect, render

from .forms import (
    FormularioAdocao,
    FormularioAdotante,
    FormularioAnimal,
    FormularioLogin,
    FormularioTratamento,
)
from .models import Adocao, Adotante, Animal, Tratamento


def pagina_publica_adocao(request):
    animais = Animal.objects.filter(status=Animal.STATUS_DISPONIVEL)
    contexto = {
        'animais': animais,
        'total_disponiveis': animais.count(),
    }
    return render(request, 'publico/inicio.html', contexto)


def pagina_entrar(request):
    if request.user.is_authenticated:
        return redirect('painel')

    if request.method == 'POST':
        formulario = FormularioLogin(request.POST)
        if formulario.is_valid():
            usuario = authenticate(
                request,
                username=formulario.cleaned_data['usuario'],
                password=formulario.cleaned_data['senha'],
            )
            if usuario is not None:
                login(request, usuario)
                return redirect('painel')
            messages.error(request, 'Usuário ou senha inválidos.')
    else:
        formulario = FormularioLogin()

    return render(request, 'gestao/login.html', {'formulario': formulario})


def pagina_sair(request):
    logout(request)
    return redirect('pagina_publica_adocao')


@login_required
def painel(request):
    contexto = {
        'total_animais': Animal.objects.count(),
        'total_disponiveis': Animal.objects.filter(status=Animal.STATUS_DISPONIVEL).count(),
        'total_adotados': Animal.objects.filter(status=Animal.STATUS_ADOTADO).count(),
        'total_adotantes': Adotante.objects.count(),
        'total_adocoes': Adocao.objects.count(),
    }
    return render(request, 'gestao/inicio.html', contexto)


@login_required
def listar_animais(request):
    animais = Animal.objects.all()
    return render(request, 'gestao/lista_animais.html', {'animais': animais})


@login_required
def cadastrar_animal(request):
    if request.method == 'POST':
        formulario = FormularioAnimal(request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Animal cadastrado com sucesso.')
            return redirect('listar_animais')
    else:
        formulario = FormularioAnimal()

    return render(
        request,
        'gestao/formulario_animal.html',
        {'formulario': formulario, 'titulo': 'Cadastrar Animal'},
    )


@login_required
def editar_animal(request, animal_id):
    animal = get_object_or_404(Animal, pk=animal_id)

    if request.method == 'POST':
        formulario = FormularioAnimal(request.POST, instance=animal)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Animal atualizado com sucesso.')
            return redirect('listar_animais')
    else:
        formulario = FormularioAnimal(instance=animal)

    return render(
        request,
        'gestao/formulario_animal.html',
        {'formulario': formulario, 'titulo': 'Editar Animal'},
    )


@login_required
def excluir_animal(request, animal_id):
    animal = get_object_or_404(Animal, pk=animal_id)

    if request.method == 'POST':
        try:
            animal.delete()
            messages.success(request, 'Animal excluído com sucesso.')
        except ProtectedError:
            messages.error(
                request,
                'Não é possível excluir um animal com adoção registrada.',
            )
        return redirect('listar_animais')

    return render(
        request,
        'gestao/confirmar_exclusao.html',
        {
            'titulo': 'Excluir Animal',
            'mensagem': f'Deseja realmente excluir o animal {animal.nome}?',
            'url_voltar': 'listar_animais',
        },
    )


@login_required
def listar_tratamentos(request):
    tratamentos = Tratamento.objects.select_related('animal')
    return render(request, 'gestao/lista_tratamentos.html', {'tratamentos': tratamentos})


@login_required
def cadastrar_tratamento(request):
    if request.method == 'POST':
        formulario = FormularioTratamento(request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Tratamento cadastrado com sucesso.')
            return redirect('listar_tratamentos')
    else:
        formulario = FormularioTratamento()

    return render(
        request,
        'gestao/formulario_tratamento.html',
        {'formulario': formulario, 'titulo': 'Cadastrar Tratamento'},
    )


@login_required
def editar_tratamento(request, tratamento_id):
    tratamento = get_object_or_404(Tratamento, pk=tratamento_id)

    if request.method == 'POST':
        formulario = FormularioTratamento(request.POST, instance=tratamento)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Tratamento atualizado com sucesso.')
            return redirect('listar_tratamentos')
    else:
        formulario = FormularioTratamento(instance=tratamento)

    return render(
        request,
        'gestao/formulario_tratamento.html',
        {'formulario': formulario, 'titulo': 'Editar Tratamento'},
    )


@login_required
def excluir_tratamento(request, tratamento_id):
    tratamento = get_object_or_404(Tratamento, pk=tratamento_id)

    if request.method == 'POST':
        tratamento.delete()
        messages.success(request, 'Tratamento excluído com sucesso.')
        return redirect('listar_tratamentos')

    return render(
        request,
        'gestao/confirmar_exclusao.html',
        {
            'titulo': 'Excluir Tratamento',
            'mensagem': f'Deseja realmente excluir o tratamento de {tratamento.animal.nome}?',
            'url_voltar': 'listar_tratamentos',
        },
    )


@login_required
def listar_adotantes(request):
    adotantes = Adotante.objects.all()
    return render(request, 'gestao/lista_adotantes.html', {'adotantes': adotantes})


@login_required
def cadastrar_adotante(request):
    if request.method == 'POST':
        formulario = FormularioAdotante(request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Adotante cadastrado com sucesso.')
            return redirect('listar_adotantes')
    else:
        formulario = FormularioAdotante()

    return render(
        request,
        'gestao/formulario_adotante.html',
        {'formulario': formulario, 'titulo': 'Cadastrar Adotante'},
    )


@login_required
def editar_adotante(request, adotante_id):
    adotante = get_object_or_404(Adotante, pk=adotante_id)

    if request.method == 'POST':
        formulario = FormularioAdotante(request.POST, instance=adotante)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Adotante atualizado com sucesso.')
            return redirect('listar_adotantes')
    else:
        formulario = FormularioAdotante(instance=adotante)

    return render(
        request,
        'gestao/formulario_adotante.html',
        {'formulario': formulario, 'titulo': 'Editar Adotante'},
    )


@login_required
def excluir_adotante(request, adotante_id):
    adotante = get_object_or_404(Adotante, pk=adotante_id)

    if request.method == 'POST':
        try:
            adotante.delete()
            messages.success(request, 'Adotante excluído com sucesso.')
        except ProtectedError:
            messages.error(
                request,
                'Não é possível excluir um adotante com adoção registrada.',
            )
        return redirect('listar_adotantes')

    return render(
        request,
        'gestao/confirmar_exclusao.html',
        {
            'titulo': 'Excluir Adotante',
            'mensagem': f'Deseja realmente excluir o adotante {adotante.nome}?',
            'url_voltar': 'listar_adotantes',
        },
    )


@login_required
def listar_adocoes(request):
    adocoes = Adocao.objects.select_related('animal', 'adotante')
    return render(request, 'gestao/lista_adocoes.html', {'adocoes': adocoes})


@login_required
def cadastrar_adocao(request):
    if request.method == 'POST':
        formulario = FormularioAdocao(request.POST)
        if formulario.is_valid():
            adocao = formulario.save()
            animal = adocao.animal
            animal.status = Animal.STATUS_ADOTADO
            animal.save()
            messages.success(request, 'Adoção registrada com sucesso.')
            return redirect('listar_adocoes')
    else:
        formulario = FormularioAdocao()

    return render(
        request,
        'gestao/formulario_adocao.html',
        {'formulario': formulario, 'titulo': 'Registrar Adoção'},
    )


@login_required
def excluir_adocao(request, adocao_id):
    adocao = get_object_or_404(Adocao, pk=adocao_id)

    if request.method == 'POST':
        animal = adocao.animal
        adocao.delete()
        if not Adocao.objects.filter(animal=animal).exists():
            animal.status = Animal.STATUS_DISPONIVEL
            animal.save()
        messages.success(request, 'Adoção excluída com sucesso.')
        return redirect('listar_adocoes')

    return render(
        request,
        'gestao/confirmar_exclusao.html',
        {
            'titulo': 'Excluir Adoção',
            'mensagem': (
                f'Deseja realmente excluir a adoção de {adocao.animal.nome} '
                f'por {adocao.adotante.nome}?'
            ),
            'url_voltar': 'listar_adocoes',
        },
    )


@login_required
def historico_adocoes(request):
    adocoes = Adocao.objects.select_related('animal', 'adotante')
    nome_animal = request.GET.get('nome_animal', '').strip()
    nome_adotante = request.GET.get('nome_adotante', '').strip()
    data_inicio = request.GET.get('data_inicio', '').strip()
    data_fim = request.GET.get('data_fim', '').strip()

    if nome_animal:
        adocoes = adocoes.filter(animal__nome__icontains=nome_animal)
    if nome_adotante:
        adocoes = adocoes.filter(adotante__nome__icontains=nome_adotante)
    if data_inicio:
        adocoes = adocoes.filter(data_adocao__gte=data_inicio)
    if data_fim:
        adocoes = adocoes.filter(data_adocao__lte=data_fim)

    contexto = {
        'adocoes': adocoes,
        'nome_animal': nome_animal,
        'nome_adotante': nome_adotante,
        'data_inicio': data_inicio,
        'data_fim': data_fim,
    }
    return render(request, 'gestao/historico_adocoes.html', contexto)
