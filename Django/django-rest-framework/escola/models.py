from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    rg = models.CharField(max_length=9, null=False, blank=False)
    cpf = models.CharField(max_length=11, null=False, blank=False)
    data_nascimento = models.DateField(null=False, blank=False)

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