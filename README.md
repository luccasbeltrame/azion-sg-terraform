# azion-sg-terraform

1 - Criar usuario API e NetworkLists

1.1 - Criar usario token seguindo as orientações da Documentação:
 - https://www.azion.com/pt-br/documentacao/produtos/api/v3/authentication/

1.2 - Listar as Networklists e coletar o ID
 - https://www.azion.com/pt-br/documentacao/produtos/api/v3/network-lists/

2 - Terraform e Python

2.1 - Alterar os campos do azion_border.py
     preencher o 'Authorization': '' com a instruções 1.1
     preencher o 'id': '' com as instruções 1.2

2.1 Aplicar o terraform 

```terraform init```
```terraform plan```
```terra apply```



