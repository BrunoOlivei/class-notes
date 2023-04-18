Por padrão o Django é configurado com SQLite.

Para adicionar um novo documento ao SQLite podemos realizar utilizando o shell disponível pelo manage.py.

```powershell
python manage.py shell
```

Utilizando a linguagem python, cria-se um objeto com os atributos que se deseja armazenar:

```Python
>>> from galeria.models import Fotografia
>>> foto = Fotografia(nome="Nebulosa de Carina", legenda="webbtelescope.org / NASA / James Webb", foto="carina-nebula.png")
>>> foto.save()
```

Para visualizar os registros salvos:

```python
>>> Fotografia.objects.all()
<QuerySet [<Fotografia: Fotografia [nome=Nebulosa de Carina]>]>
```

Para deleter um documento no shell:

```python
>>> Fotografia.objects.filter(id=id).delete()
```

giovana.marreco
rwn6pxp-BXM2aga1jtg