print("-------Plataforma de Leilões e Rastreamento de Gado.-------")

for tentativa in range(5):
    nome_do_pecuarista = input("Digite nome do pecuarista: ").strip().title()
    nome_da_fazenda = input("Digite nome da fazenda: ").strip().title()
    raca_do_animal = input("Digite raça do animal: ").strip().title()
    municipio_do_registro = input("Digite município do registro: ").strip().title()
    codigo_do_brinco_eletronico = input("Digite código do brinco eletrônico: ").strip()
    registro_genealogico = input("Digite registro genealógico: ").strip()
    peso_em_arrobas = input("Digite peso em arrobas: ").strip()
    idade_em_meses = input("Digite idade em meses: ").strip()
    data_da_pesagem = input("Digite data da pesagem: ").strip()
    e_mail_da_associacao_agropecuaria = input("Digite e-mail da associação agropecuária: ").strip().lower()
    pin_do_produtor = input("Digite pin do produtor: ").strip()
    certificacao_sanitaria = input("Digite certificação sanitária: ").strip().upper()

    data_formatada = data_da_pesagem.replace("-", "/")

    if nome_do_pecuarista.replace(' ', '').isalpha() and \
       nome_da_fazenda.replace(' ', '').isalpha() and \
       raca_do_animal.replace(' ', '').isalpha() and \
       municipio_do_registro.replace(' ', '').isalpha() and \
       registro_genealogico.isalnum() and \
       codigo_do_brinco_eletronico.startswith('BOV-') and \
       codigo_do_brinco_eletronico[len('BOV-'):].isalnum() and \
       peso_em_arrobas.isdigit() and \
       idade_em_meses.isdigit() and \
       data_formatada.count('/') == 2 and \
       len(data_formatada) == 10 and \
       e_mail_da_associacao_agropecuaria.endswith('.agro.org.br') and \
       len(pin_do_produtor) > 0 and \
       certificacao_sanitaria == 'APROVADO':
        pin_do_produtor_oculto = "*" * len(pin_do_produtor)
        print("Registro validado com sucesso!")
        print(f"Data: {data_formatada} | Código protegido: {pin_do_produtor_oculto}")
        break
    else:
        print(f"Tentativa inválida ({tentativa + 1} de 5). Verifique os dados.")
        print("-" * 50)
else:
    print("BLOQUEADO: 5 tentativas esgotadas.")
