from django.apps import AppConfig


class UsuariosConfig(AppConfig):
    '''Configuração da aplicação de usuários'''
    default_auto_field = 'django.db.models.BigAutoField' # Campo padrão
    name = 'apps.usuarios' # Nome da aplicação
