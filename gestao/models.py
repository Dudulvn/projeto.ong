from django.core.exceptions import ValidationError
from django.db import models


class Animal(models.Model):
    ESPECIE_CAO = 'cao'
    ESPECIE_GATO = 'gato'
    ESPECIE_OUTRO = 'outro'
    ESPECIES = [
        (ESPECIE_CAO, 'Cão'),
        (ESPECIE_GATO, 'Gato'),
        (ESPECIE_OUTRO, 'Outro'),
    ]

    SEXO_MACHO = 'macho'
    SEXO_FEMEA = 'femea'
    SEXOS = [
        (SEXO_MACHO, 'Macho'),
        (SEXO_FEMEA, 'Fêmea'),
    ]

    STATUS_RESGATADO = 'resgatado'
    STATUS_EM_TRATAMENTO = 'em_tratamento'
    STATUS_DISPONIVEL = 'disponivel'
    STATUS_ADOTADO = 'adotado'
    STATUS_CHOICES = [
        (STATUS_RESGATADO, 'Resgatado'),
        (STATUS_EM_TRATAMENTO, 'Em tratamento'),
        (STATUS_DISPONIVEL, 'Disponível para adoção'),
        (STATUS_ADOTADO, 'Adotado'),
    ]

    nome = models.CharField('Nome', max_length=100)
    especie = models.CharField('Espécie', max_length=20, choices=ESPECIES)
    raca = models.CharField('Raça', max_length=100)
    idade_aproximada = models.PositiveIntegerField('Idade aproximada (anos)')
    sexo = models.CharField('Sexo', max_length=10, choices=SEXOS)
    estado_saude = models.TextField('Estado de saúde')
    local_resgate = models.CharField('Local do resgate', max_length=200)
    data_resgate = models.DateField('Data do resgate')
    status = models.CharField(
        'Status',
        max_length=20,
        choices=STATUS_CHOICES,
        default=STATUS_RESGATADO,
    )
    observacoes = models.TextField('Observações', blank=True)

    class Meta:
        db_table = 'animal'
        verbose_name = 'Animal'
        verbose_name_plural = 'Animais'
        ordering = ['-data_resgate', 'nome']

    def __str__(self):
        return self.nome


class Tratamento(models.Model):
    animal = models.ForeignKey(
        Animal,
        on_delete=models.CASCADE,
        related_name='tratamentos',
        verbose_name='Animal',
    )
    data = models.DateField('Data do tratamento')
    descricao = models.TextField('Descrição')
    veterinario = models.CharField('Veterinário', max_length=150)
    observacoes = models.TextField('Observações', blank=True)

    class Meta:
        db_table = 'tratamento'
        verbose_name = 'Tratamento'
        verbose_name_plural = 'Tratamentos'
        ordering = ['-data']

    def __str__(self):
        return f'{self.animal.nome} - {self.data}'


class Adotante(models.Model):
    nome = models.CharField('Nome', max_length=150)
    cpf = models.CharField('CPF', max_length=14, unique=True)
    telefone = models.CharField('Telefone', max_length=20)
    email = models.EmailField('E-mail')
    endereco = models.TextField('Endereço')
    observacoes = models.TextField('Observações', blank=True)

    class Meta:
        db_table = 'adotante'
        verbose_name = 'Adotante'
        verbose_name_plural = 'Adotantes'
        ordering = ['nome']

    def __str__(self):
        return self.nome

    def limpar_cpf(self):
        return ''.join(filter(str.isdigit, self.cpf))

    def clean(self):
        cpf_limpo = self.limpar_cpf()
        if len(cpf_limpo) != 11:
            raise ValidationError({'cpf': 'O CPF deve conter 11 dígitos.'})


class Adocao(models.Model):
    animal = models.ForeignKey(
        Animal,
        on_delete=models.PROTECT,
        related_name='adocoes',
        verbose_name='Animal',
    )
    adotante = models.ForeignKey(
        Adotante,
        on_delete=models.PROTECT,
        related_name='adocoes',
        verbose_name='Adotante',
    )
    data_adocao = models.DateField('Data da adoção')
    observacoes = models.TextField('Observações', blank=True)

    class Meta:
        db_table = 'adocao'
        verbose_name = 'Adoção'
        verbose_name_plural = 'Adoções'
        ordering = ['-data_adocao']

    def __str__(self):
        return f'{self.animal.nome} - {self.adotante.nome}'
