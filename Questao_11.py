print("-------Controle de Acesso ao Datacenter.-------")

for tentativa in range(5):
    nome_do_especialista = input("Digite nome do especialista: ").strip().title()
    area_de_atuacao = input("Digite área de atuação: ").strip().title()
    empresa_contratada = input("Digite empresa contratada: ").strip().upper()
    cidade_da_sede = input("Digite cidade da sede: ").strip().title()
    codigo_do_rack = input("Digite código do rack: ").strip()
    id_do_gabinete = input("Digite id do gabinete: ").strip()
    temperatura_do_corredor_frio = input("Digite temperatura do corredor frio: ").strip()
    umidade_relativa_do_ar = input("Digite umidade relativa do ar: ").strip()
    data_do_acesso = input("Digite data do acesso: ").strip()
    e_mail_corporativo = input("Digite e-mail corporativo: ").strip().lower()
    senha_biometrica = input("Digite senha biométrica: ").strip()
    liberacao_da_porta = input("Digite liberação da porta: ").strip().upper()

    data_formatada = data_do_acesso.replace("-", "/")

    if nome_do_especialista.isalpha() and \
       area_de_atuacao.isalpha() and \
       cidade_da_sede.isalpha() and \
       id_do_gabinete.isalnum() and \
       codigo_do_rack.startswith('RACK-') and \
       codigo_do_rack[len('RACK-'):].isalnum() and \
       temperatura_do_corredor_frio.isdigit() and \
       umidade_relativa_do_ar.isdigit() and \
       data_formatada.count('/') == 2 and \
       len(data_formatada) == 10 and \
       e_mail_corporativo.endswith('.datacenter.com') and \
       len(senha_biometrica) > 0 and \
       liberacao_da_porta == 'ABERTO':
        senha_biometrica_oculto = "*" * len(senha_biometrica)
        print("Registro validado com sucesso!")
        print(f"Data: {data_formatada} | Código protegido: {senha_biometrica_oculto}")
        break
    else:
        print(f"Tentativa inválida ({tentativa + 1} de 5). Verifique os dados.")
        print("-" * 50)
else:
    print("BLOQUEADO: 5 tentativas esgotadas.")
