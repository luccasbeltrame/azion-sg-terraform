# azion-sg-terraform

Este projeto permite obter automaticamente endereços IP's da Azion para poder
configurar security groups na AWS.

## Como funciona?

O programa em Python `azion_border.py` irá utilizar suas credenciais na Azion
para fazer uma chamada HTTPS na API da mesma, criando como resultado o arquivo
`terraform.tfvars.json`. Este é um exemplo de conteúdo do arquivo:

```json
{
  "items_values": [
    "10.0.0.0/16",
    "172.16.0.0/24",
    "192.168.0.0/19",
    "192.168.1.10/32"
  ]
}
```

Ao executar o módulo Terraform via `terraform apply`, a configuração do
*security group* com os endereços IP da Azion será automática.

## Requisitos

- Python versão 3.6.13 ou maior
- `pip` versão 21.3.1 ou maior
- Terraform versão 0.15 ou maior

## Como utilizar

1 - Criar usuário API e NetworkLists

1.1 - Criar usario token seguindo as orientações da Documentação:
 - https://www.azion.com/pt-br/documentacao/produtos/api/v3/authentication/

1.2 - Listar as Networklists e coletar o ID
 - https://www.azion.com/pt-br/documentacao/produtos/api/v3/network-lists/

2 - Python

2.1 - Alterar as variáveis `authorization` e `id` no arquivo `azion_border.py`

* preencher o valor de `authorization` com a instruções 1.1;
* preencher o `id` com as instruções 1.2;

2.2 - Instalar módulos Python requeridos:

```
pip install -r requirements.txt
```

3 - Aplicar o módulo Terraform

```
terraform init
terraform plan
terra apply
```
