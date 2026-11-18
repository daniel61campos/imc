print("-------Auditoria Forense Digital e Custódia de Evidências.-------")

for tentativa in range(5):
    nome_do_perito = input("Digite nome do perito: ").strip().title()
    especialidade_forense = input("Digite especialidade forense: ").strip().title()
    departamento_policial = input("Digite departamento policial: ").strip().upper()
    cidade_da_ocorrencia = input("Digite cidade da ocorrência: ").strip().title()
    codigo_da_evidencia = input("Digite código da evidência: ").strip()
    hash_sha_256_da_imagem = input("Digite hash sha-256 da imagem: ").strip()
    tamanho_em_megabytes = input("Digite tamanho em megabytes: ").strip()
    numero_do_lacre = input("Digite número do lacre: ").strip()
    data_da_apreensao = input("Digite data da apreensão: ").strip()
    e_mail_do_instituto_de_pericia = input("Digite e-mail do instituto de perícia: ").strip().lower()
    senha_do_cofre_digital = input("Digite senha do cofre digital: ").strip()
    parecer_forense = input("Digite parecer forense: ").strip().upper()

    data_formatada = data_da_apreensao.replace("-", "/")

    if nome_do_perito.isalpha() and \
       especialidade_forense.isalpha() and \
       cidade_da_ocorrencia.isalpha() and \
       hash_sha_256_da_imagem.isalnum() and \
       codigo_da_evidencia.startswith('EVID-') and \
       codigo_da_evidencia[len('EVID-'):].isalnum() and \
       tamanho_em_megabytes.isdigit() and \
       numero_do_lacre.isdigit() and \
       data_formatada.count('/') == 2 and \
       len(data_formatada) == 10 and \
       e_mail_do_instituto_de_pericia.endswith('.policia.gov.br') and \
       len(senha_do_cofre_digital) > 0 and \
       parecer_forense == 'INTEGRO':
        senha_do_cofre_digital_oculto = "*" * len(senha_do_cofre_digital)
        print("Registro validado com sucesso!")
        print(f"Data: {data_formatada} | Código protegido: {senha_do_cofre_digital_oculto}")
        break
    else:
        print(f"Tentativa inválida ({tentativa + 1} de 5). Verifique os dados.")
        print("-" * 50)
else:
    print("BLOQUEADO: 5 tentativas esgotadas.")
