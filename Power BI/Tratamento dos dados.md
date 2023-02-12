# Substituição de valores

Mesclar consultas pode ser útil para traduzir valores de uma coluna, por exemplo, trazer o nome de uma cidade baseada no código IBGE

![[Pasted image 20230211193957.png]]

Escolhe a tabela cujo deseja mesclar as consultas e seleciona as colunas que farão referência umas as outras:

![[Pasted image 20230211194102.png]]

```Dax
= Table.NestedJoin(#"Extracted Text After Delimiter", {"order_status"}, tradução, {"Inglês"}, "tradução", JoinKind.LeftOuter)
```

## Adicionar coluna personalizada

```
= Table.AddColumn(#"Changed Type", "Coluna Personalizada", each if [payment_type] = "#credit_card" then "Cartão de crédito" 
else if [payment_type] = "#boleto" then "Boleto"
else if [payment_type] = "#voucher" then "Voucher" 
else if [payment_type] = "#debit_card" then "Cartão de débito" 
else if [payment_type] = "#not_defined" then "Não definido" else null)
```

# Caminho dados

Podemos criar um parâmetro com o caminho dos dados assim, sempre que houver uma alteração no caminho, não será necessário alterar o `source` (fonte) de cada dado:

![[Pasted image 20230211200224.png]]

Escolha **Novo Parâmetro**

Nomeie o novo parâmetro para reconhece-lo, escolha o tipo de dado para texto e insira o valor:
![[Pasted image 20230211200634.png]]

Uma nova consulta irá surgir com o valor do caminho:

![[Pasted image 20230211200710.png]]

Assim podemos inserir nos código de cada consulta que possua o mesmo endereço o parâmetro criado:

```
= Csv.Document(File.Contents(CaminhoPasta & "olist_order_items_dataset.csv"),[Delimiter=",", Columns=7, Encoding=1252, QuoteStyle=QuoteStyle.None])
```

[Power BI: parâmetros e exportação de modelos | Alura](https://www.alura.com.br/artigos/power-bi-parametros-e-exportacao-de-modelos)

