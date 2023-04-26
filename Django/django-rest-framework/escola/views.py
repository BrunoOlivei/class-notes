from django.http import JsonResponse 

def alunos(request):
    '''Retorna uma lista de alunos'''
    if request.method == 'GET': # Seo método for GET
        aluno = {"id": 1, "nome": "Guilherme"}
        return JsonResponse(aluno) # Retorna um JSON
