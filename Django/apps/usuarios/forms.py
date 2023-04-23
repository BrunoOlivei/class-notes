from django import forms


class LoginForms(forms.Form):
    '''Formulário de login do usuário no sistema'''
    nome_login = forms.CharField( # Campo de nome de login
        label='Nome de Login', # Label do campo
        required=True, # Campo obrigatório
        max_length=100, # Tamanho máximo do campo
        widget=forms.TextInput( # Tipo de campo
            attrs={
                "class": "form-control", # Classe do campo
                "placeholder": "Ex.: João Silva" # Placeholder do campo (texto de exemplo)
            }
        )
    )
    senha = forms.CharField( # Campo de senha
        label='Senha', # Label do campo
        required=True, # Campo obrigatório 
        max_length=70, # Tamanho máximo do campo 
        widget=forms.PasswordInput( # Tipo de campo
            attrs={
                "class": "form-control", # Classe do campo 
                "placeholder": "Digite sua senha" # Placeholder do campo (texto de exemplo)
            }
        )
    )


class CadastroForms(forms.Form): # Formulário de cadastro do usuário no sistema
    nome_cadastro = forms.CharField( # Campo de nome de cadastro
        label='Nome completo', # Label do campo 
        required=True, # Campo obrigatório 
        max_length=100, # Tamanho máximo do campo
        widget=forms.TextInput( # Tipo de campo
            attrs={
                "class": "form-control", # Classe do campo
                "placeholder": "Ex.: João Silva" # Placeholder do campo (texto de exemplo)
            }
        )
    )
    email = forms.EmailField( # Campo de e-mail
        label='E-mail', # Label do campo 
        required=True, # Campo obrigatório 
        max_length=100, # Tamanho máximo do campo
        widget=forms.EmailInput( # Tipo de campo
            attrs={
                "class": "form-control", # Classe do campo
                "placeholder": "Ex.:joaodasilva@gmail.com" # Placeholder do campo (texto de exemplo)
            }
        )
    )
    senha_1 = forms.CharField( # Campo de senha
        label='Senha', # Label do campo 
        required=True, # Campo obrigatório 
        max_length=70, # Tamanho máximo do campo
        widget=forms.PasswordInput( # Tipo de campo
            attrs={
                "class": "form-control", # Classe do campo
                "placeholder": "Digite sua senha" # Placeholder do campo (texto de exemplo)
            }
        )
    )
    senha_2 = forms.CharField( # Campo de confirmação de senha
        label='Confirmação de senha', # Label do campo 
        required=True, # Campo obrigatório
        max_length=70, # Tamanho máximo do campo
        widget=forms.PasswordInput( # Tipo de campo
            attrs={
                "class": "form-control", # Classe do campo
                "placeholder": "Digite sua senha mais uma vez" # Placeholder do campo (texto de exemplo)
            }
        )
    )

    def clean_nome_cadastro(self):
        '''Método para limpar o campo de nome de cadastro e verificar se o nome não contém espaços'''
        nome = self.cleaned_data.get('nome_cadastro') # Pega o valor do campo de nome de cadastro

        if nome: # Verifica se o campo não está vazio
            nome = nome.strip() # Remove os espaços do início e do fim do nome
            if " " in nome: # Verifica se o nome contém espaços
                raise forms.ValidationError("O nome não pode conter espaços") # Lança uma exceção
            else: # Se o nome não contém espaços
                return nome # Retorna o nome
    
    def clean_senha_2(self):
        '''Método para limpar o campo de confirmação de senha e verificar se as senhas são iguais'''
        senha_1 = self.cleaned_data.get('senha_1') # Pega o valor do campo de senha
        senha_2 = self.cleaned_data.get('senha_2') # Pega o valor do campo de confirmação de senha

        if senha_1 and senha_2: # Verifica se os campos não estão vazios
            if senha_1 != senha_2: # Verifica se as senhas são diferentes
                raise forms.ValidationError("As senhas não são iguais") # Lança uma exceção
            else: # Se as senhas são iguais
                return senha_2 # Retorna a senha