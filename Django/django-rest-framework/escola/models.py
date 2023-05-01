from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    rg = models.CharField(max_length=9, null=False, blank=False)
    cpf = models.CharField(max_length=11, null=False, blank=False)
    data_nascimento = models.DateField(null=False, blank=False)
    celular = models.CharField(max_length=14, default="") # default="": valor padrão
    foto = models.ImageField(blank=True)
    # arquivo = models.FileField(blank=True, default="") 

    def __str__(self):
        return self.nome
    

class Curso(models.Model):
    NIVEIS = (
        ('B', 'Básico'),
        ('I', 'Intermediário'),
        ('A', 'Avançado')
    )
    codigo_curso = models.CharField(max_length=10, null=False, blank=False)
    descricao = models.CharField(max_length=100, null=False, blank=False)
    nivel = models.CharField(max_length=1, null=False, blank=False, choices=NIVEIS, default='B')

    def __str__(self):
        return self.descricao
    

class Matricula(models.Model):
    PERIODOS = (
        ('M', 'Matutino'),
        ('V', 'Vespertino'),
        ('N', 'Noturno')
    )
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE) # on_delete=models.CASCADE: se o aluno for excluído, as matrículas também serão
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE) # on_delete=models.CASCADE: se o curso for excluído, as matrículas também serão
    periodo = models.CharField(max_length=1, null=False, blank=False, choices=PERIODOS, default='M') # choices = PERIODOS: só aceita os valores definidos em PERIODOS
