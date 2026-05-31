from datetime import date

from django.core.management.base import BaseCommand

from gestao.models import Adocao, Adotante, Animal, Tratamento


class Command(BaseCommand):
    help = 'Popula o banco com dados de exemplo para testes'

    def handle(self, *args, **options):
        if Animal.objects.exists():
            self.stdout.write(self.style.WARNING('O banco já possui dados. Comando não executado.'))
            return

        animal1 = Animal.objects.create(
            nome='Thor',
            especie=Animal.ESPECIE_CAO,
            raca='SRD',
            idade_aproximada=3,
            sexo=Animal.SEXO_MACHO,
            estado_saude='Saudável, vacinado e castrado',
            local_resgate='Centro - Niterói',
            data_resgate=date(2026, 1, 15),
            status=Animal.STATUS_DISPONIVEL,
            observacoes='Animal dócil e sociável.',
        )

        animal2 = Animal.objects.create(
            nome='Luna',
            especie=Animal.ESPECIE_GATO,
            raca='SRD',
            idade_aproximada=2,
            sexo=Animal.SEXO_FEMEA,
            estado_saude='Em recuperação',
            local_resgate='Icaraí - Niterói',
            data_resgate=date(2026, 2, 10),
            status=Animal.STATUS_EM_TRATAMENTO,
            observacoes='Precisa de acompanhamento veterinário.',
        )

        animal3 = Animal.objects.create(
            nome='Mel',
            especie=Animal.ESPECIE_CAO,
            raca='Vira-lata',
            idade_aproximada=5,
            sexo=Animal.SEXO_FEMEA,
            estado_saude='Saudável',
            local_resgate='São Francisco - Niterói',
            data_resgate=date(2025, 11, 20),
            status=Animal.STATUS_DISPONIVEL,
        )

        Tratamento.objects.create(
            animal=animal2,
            data=date(2026, 2, 12),
            descricao='Consulta e medicação para infecção leve',
            veterinario='Dra. Ana Silva',
            observacoes='Retorno em 15 dias.',
        )

        adotante = Adotante.objects.create(
            nome='Maria Oliveira',
            cpf='12345678901',
            telefone='21999990000',
            email='maria@email.com',
            endereco='Rua das Flores, 100 - Niterói/RJ',
        )

        animal_adotado = Animal.objects.create(
            nome='Bob',
            especie=Animal.ESPECIE_CAO,
            raca='SRD',
            idade_aproximada=4,
            sexo=Animal.SEXO_MACHO,
            estado_saude='Saudável',
            local_resgate='Piratininga - Niterói',
            data_resgate=date(2025, 8, 5),
            status=Animal.STATUS_ADOTADO,
        )

        Adocao.objects.create(
            animal=animal_adotado,
            adotante=adotante,
            data_adocao=date(2025, 12, 1),
            observacoes='Adoção realizada com visita prévia.',
        )

        self.stdout.write(self.style.SUCCESS('Dados de exemplo criados com sucesso.'))
        self.stdout.write(f'Animais: {Animal.objects.count()}')
        self.stdout.write(f'Tratamentos: {Tratamento.objects.count()}')
        self.stdout.write(f'Adotantes: {Adotante.objects.count()}')
        self.stdout.write(f'Adoções: {Adocao.objects.count()}')
