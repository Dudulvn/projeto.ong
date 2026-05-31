from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Cria o usuário inicial para acesso ao sistema'

    def handle(self, *args, **options):
        usuario = 'admin'
        senha = 'admin123'

        if User.objects.filter(username=usuario).exists():
            self.stdout.write(self.style.WARNING('O usuário admin já existe.'))
            return

        User.objects.create_superuser(username=usuario, password=senha, email='admin@arca.local')
        self.stdout.write(self.style.SUCCESS('Usuário admin criado com sucesso.'))
        self.stdout.write('Usuário: admin')
        self.stdout.write('Senha: admin123')
