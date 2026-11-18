print("-------Controle de Imigração e Passaportes.-------")

for tentativa in range(5):
    nome_do_passageiro = input("Digite nome do passageiro: ").strip().title()
    sobrenome = input("Digite sobrenome: ").strip().title()
    pais_de_origem = input("Digite país de origem: ").strip().title()
    cidade_de_destino = input("Digite cidade de destino: ").strip().title()
    numero_do_passaporte = input("Digite número do passaporte: ").strip()
    codigo_do_voo = input("Digite código do voo: ").strip()
    quantidade_de_bagagens = input("Digite quantidade de bagagens: ").strip()
    tempo_de_estadia_em_dias = input("Digite tempo de estadia em dias: ").strip()
    data_de_entrada = input("Digite data de entrada: ").strip()
    e_mail_da_companhia_aerea = input("Digite e-mail da companhia aérea: ").strip().lower()
    codigo_de_visto = input("Digite código de visto: ").strip()
    entrada_no_pais = input("Digite entrada no país: ").strip().upper()

    data_formatada = data_de_entrada.replace("-", "/")

    if nome_do_passageiro.isalpha() and \
       sobrenome.isalpha() and \
       pais_de_origem.isalpha() and \
       cidade_de_destino.isalpha() and \
       numero_do_passaporte.isalnum() and \
       codigo_do_voo.startswith('FLIGHT-') and \
       codigo_do_voo[len('FLIGHT-'):].isalnum() and \
       len(numero_do_passaporte) == 8 and \
       quantidade_de_bagagens.isdigit() and \
       tempo_de_estadia_em_dias.isdigit() and \
       data_formatada.count('/') == 2 and \
       len(data_formatada) == 10 and \
       e_mail_da_companhia_aerea.endswith('.air.com') and \
       len(codigo_de_visto) > 0 and \
       entrada_no_pais == 'AUTORIZADO':
        codigo_de_visto_oculto = "*" * len(codigo_de_visto)
        print("Registro validado com sucesso!")
        print(f"Data: {data_formatada} | Código protegido: {codigo_de_visto_oculto}")
        break
    else:
        print(f"Tentativa inválida ({tentativa + 1} de 5). Verifique os dados.")
        print("-" * 50)
else:
    print("BLOQUEADO: 5 tentativas esgotadas.")
