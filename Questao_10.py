print("-------Plataforma de E-commerce e Despacho de Pedidos.-------")

for tentativa in range(5):
    nome_do_comprador = input("Digite nome do comprador: ").strip().title()
    sobrenome = input("Digite sobrenome: ").strip().title()
    cidade_de_entrega = input("Digite cidade de entrega: ").strip().title()
    estado_federativo = input("Digite estado federativo: ").strip().upper()
    codigo_de_rastreamento = input("Digite código de rastreamento: ").strip()
    sku_do_produto = input("Digite sku do produto: ").strip()
    quantidade_comprada = input("Digite quantidade comprada: ").strip()
    valor_total_em_reais = input("Digite valor total em reais: ").strip()
    data_da_postagem = input("Digite data da postagem: ").strip()
    e_mail_do_cliente = input("Digite e-mail do cliente: ").strip().lower()
    codigo_de_validacao_do_cartao = input("Digite código de validação do cartão: ").strip()
    status_da_entrega = input("Digite status da entrega: ").strip().upper()

    data_formatada = data_da_postagem.replace("-", "/")

    if nome_do_comprador.replace(' ', '').isalpha() and \
       sobrenome.replace(' ', '').isalpha() and \
       cidade_de_entrega.replace(' ', '').isalpha() and \
       sku_do_produto.isalnum() and \
       codigo_de_rastreamento.startswith('LOG-') and \
       codigo_de_rastreamento[len('LOG-'):].isalnum() and \
       quantidade_comprada.isdigit() and \
       valor_total_em_reais.isdigit() and \
       data_formatada.count('/') == 2 and \
       len(data_formatada) == 10 and \
       e_mail_do_cliente.endswith('.com.br') and \
       len(codigo_de_validacao_do_cartao) > 0 and \
       status_da_entrega == 'DESPACHADO':
        codigo_de_validacao_do_cartao_oculto = "*" * len(codigo_de_validacao_do_cartao)
        print("Registro validado com sucesso!")
        print(f"Data: {data_formatada} | Código protegido: {codigo_de_validacao_do_cartao_oculto}")
        break
    else:
        print(f"Tentativa inválida ({tentativa + 1} de 5). Verifique os dados.")
        print("-" * 50)
else:
    print("BLOQUEADO: 5 tentativas esgotadas.")
