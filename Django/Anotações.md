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


```html
<div class="col-12 col-lg-12" style="margin-bottom: 10px;">
	<label for="nome_cadastro" style="color:#D9D9D9; margin-bottom: 5px;"><b>Nome completo</b></label>
	<input type="text" class="form-control" name="nome_cadastro" placeholder="Ex.: João Silva" required>
</div>
<div class="col-12 col-lg-12" style="margin-bottom: 10px;">
	<label for="email" style="color:#D9D9D9; margin-bottom: 5px;"><b>Email</b></label>
	<input type="email" class="form-control" name="email" placeholder="Ex.: joaosilva@xpto.com" required>
</div>
<div class="col-12 col-lg-6" style="margin-bottom: 10px;">
	<label for="password1" style="color:#D9D9D9; margin-bottom: 5px;"><b>Senha</b></label>
	<input type="password" class="form-control" name="password1" placeholder="Digite sua senha" required>
</div>
<div class="col-12 col-lg-6" style="margin-bottom: 10px;">
	<label for="password2" style="color:#D9D9D9; margin-bottom: 5px;"><b>Confirmação de senha</b></label>
	<input type="password" class="form-control" name="password2" placeholder="Digite sua senha mais uma vez" required>
</div>
<div class="col-12 text-center">
	<button class="btn btn-success col-12" style="padding: top 5px;" type="submit">Criar sua conta</button>
</div>
```


Form
![[Pasted image 20230422125100.png]]

Alert
![[Pasted image 20230422125137.png]]