from django.urls import path

from . import views

urlpatterns = [
    path('', views.pagina_publica_adocao, name='pagina_inicial'),
    path('adocao/', views.pagina_publica_adocao, name='pagina_publica_adocao'),
    path('entrar/', views.pagina_entrar, name='pagina_entrar'),
    path('sair/', views.pagina_sair, name='pagina_sair'),
    path('painel/', views.painel, name='painel'),
    path('animais/', views.listar_animais, name='listar_animais'),
    path('animais/cadastrar/', views.cadastrar_animal, name='cadastrar_animal'),
    path('animais/<int:animal_id>/editar/', views.editar_animal, name='editar_animal'),
    path('animais/<int:animal_id>/excluir/', views.excluir_animal, name='excluir_animal'),
    path('tratamentos/', views.listar_tratamentos, name='listar_tratamentos'),
    path('tratamentos/cadastrar/', views.cadastrar_tratamento, name='cadastrar_tratamento'),
    path(
        'tratamentos/<int:tratamento_id>/editar/',
        views.editar_tratamento,
        name='editar_tratamento',
    ),
    path(
        'tratamentos/<int:tratamento_id>/excluir/',
        views.excluir_tratamento,
        name='excluir_tratamento',
    ),
    path('adotantes/', views.listar_adotantes, name='listar_adotantes'),
    path('adotantes/cadastrar/', views.cadastrar_adotante, name='cadastrar_adotante'),
    path(
        'adotantes/<int:adotante_id>/editar/',
        views.editar_adotante,
        name='editar_adotante',
    ),
    path(
        'adotantes/<int:adotante_id>/excluir/',
        views.excluir_adotante,
        name='excluir_adotante',
    ),
    path('adocoes/', views.listar_adocoes, name='listar_adocoes'),
    path('adocoes/cadastrar/', views.cadastrar_adocao, name='cadastrar_adocao'),
    path('adocoes/<int:adocao_id>/excluir/', views.excluir_adocao, name='excluir_adocao'),
    path('adocoes/historico/', views.historico_adocoes, name='historico_adocoes'),
]
