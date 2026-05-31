# Arca Proteção 

CENTRO UNIVERSITÁRIO LA SALLE DO RIO DE JANEIRO - Unilasalle - RJ
Sistema Web para Gerenciamento de Resgate e Adoção de Animais – Arca Proteção



# Como executar o sistema

### Pré-requisitos

- Python 3.11 ou superior
- pip

### Estrutura do projeto

```
Projeto-ONG/
├── manage.py
├── requirements.txt
├── banco.sqlite3
├── arca_protecao/      # configurações do projeto Django
├── gestao/             # aplicação principal (models, views, forms)
├── templates/          # páginas HTML
└── static/css/         # estilos do sistema
```

### Instalação

1. Clone o repositório:

```bash
git clone <url-do-repositorio>
cd Projeto-ONG
```

2. Crie e ative um ambiente virtual:

**Windows (PowerShell):**

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Aplique as migrations no banco SQLite:

```bash
python manage.py migrate
```

5. Crie o usuário administrador inicial:

```bash
python manage.py criar_usuario_inicial
```

6. (Opcional) Popule o banco com dados de exemplo:

```bash
python manage.py popular_dados
```

### Executar o sistema

```bash
python manage.py runserver
```

Acesse no navegador:

- **Página pública de adoção:** http://127.0.0.1:8000/adocao/
- **Área da instituição (login):** http://127.0.0.1:8000/entrar/
- **Painel administrativo Django:** http://127.0.0.1:8000/admin/

### Credenciais padrão (desenvolvimento)

| Campo | Valor |
|-------|-------|
| Usuário | `admin` |
| Senha | `admin123` |

### Comandos úteis

| Comando | Descrição |
|---------|-----------|
| `python manage.py makemigrations` | Cria arquivos de migration após alterar models |
| `python manage.py migrate` | Aplica as migrations no banco |
| `python manage.py criar_usuario_inicial` | Cria usuário admin para acesso |
| `python manage.py popular_dados` | Insere dados de exemplo |
| `python manage.py createsuperuser` | Cria outro usuário administrador |
| `python manage.py runserver` | Inicia o servidor de desenvolvimento |

### Funcionalidades implementadas

- Cadastro, edição e exclusão de animais, tratamentos, adotantes e adoções
- Alteração de status do animal
- Histórico de adoções com filtros
- Página pública com animais disponíveis para adoção
- Área restrita com login para funcionários da instituição
