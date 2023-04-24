from django.apps import AppConfig


class GaleriaConfig(AppConfig):
    '''Configuração da aplicação de galeria'''
    default_auto_field = 'django.db.models.BigAutoField' # Campo padrão
    name = 'apps.galeria' # Nome da aplicação
