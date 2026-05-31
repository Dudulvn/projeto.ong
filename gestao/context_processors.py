from .dados_ong import DADOS_ONG


def dados_institucionais(request):
    return {'dados_ong': DADOS_ONG}
