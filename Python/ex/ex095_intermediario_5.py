"""
Descrição do exercício:

   Produto           Código     Preço
Cachorro Quente      100        R$ 1,20
Bauru Simples        101        R$ 1,30
Bauru com Ovo        102        R$ 1,50
Hambúrguer           103        R$ 1,20
Cheeseburguer        104        R$ 1,30
Refrigerante         105        R$ 1,00

Faça um programa que leia o código dos itens
pedidos e as quantidades desejadas (valide as entradas).
Calcule e mostre o valor a ser pago por item
(preço * quantidade) e o total geral do pedido.
Considere que o cliente deve informar quando o pedido deve ser encerrado.
"""

products = [
    {"name": 'Cachorro Quente', "code": 100, "price": 1.20},
    {"name": "Bauru Simples ", "code": 101, "price": 1.30},
    {"name": "Bauru com Ovo ", "code": 102, "price": 1.50},
    {"name": "Hambúrguer", "code": 103, "price": 1.20},
    {"name": "Cheeseburguer", "code": 104, "price": 1.30},
    {"name": "Refrigerante", "code": 105, "price": 1.00},
]

number_of_pedidos = int(input("Enter the number of products: "))
total_price = 0
for i in range(number_of_pedidos):
    code_product = int(input("Send the product code:"))
    for items in products:
        if code_product == items.get("code"):
            amount = int(input("Sent the amount of products with this code: "))
            price = items.get("price")
            total_price += amount * price
            

print(f"The total value is {total_price}!")