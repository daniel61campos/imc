print("-------Centro de Comando e Telemetria de Drones de Resgate.-------")

for tentativa in range(5):
    nome_do_piloto_remoto = input("Digite nome do piloto remoto: ").strip().title()
    regiao_de_busca = input("Digite região de busca: ").strip().title()
    cidade_base = input("Digite cidade base: ").strip().title()
    tipo_de_missao = input("Digite tipo de missão: ").strip().title()
    prefixo_do_drone = input("Digite prefixo do drone: ").strip()
    canal_do_transmissor = input("Digite canal do transmissor: ").strip()
    altitude_de_voo = input("Digite altitude de voo: ").strip()
    nivel_da_bateria_em_porcentagem = input("Digite nível da bateria em porcentagem: ").strip()
    data_da_decolagem = input("Digite data da decolagem: ").strip()
    e_mail_do_corpo_de_bombeiros = input("Digite e-mail do corpo de bombeiros: ").strip().lower()
    chave_de_arme_dos_motores = input("Digite chave de arme dos motores: ").strip()
    status_do_link = input("Digite status do link: ").strip().upper()

    data_formatada = data_da_decolagem.replace("-", "/")

    if nome_do_piloto_remoto.replace(' ', '').isalpha() and \
       regiao_de_busca.replace(' ', '').isalpha() and \
       cidade_base.replace(' ', '').isalpha() and \
       tipo_de_missao.replace(' ', '').isalpha() and \
       canal_do_transmissor.isalnum() and \
       prefixo_do_drone.startswith('DRONE-') and \
       prefixo_do_drone[len('DRONE-'):].isalnum() and \
       altitude_de_voo.isdigit() and \
       nivel_da_bateria_em_porcentagem.isdigit() and \
       data_formatada.count('/') == 2 and \
       len(data_formatada) == 10 and \
       e_mail_do_corpo_de_bombeiros.endswith('.bombeiros.gov.br') and \
       len(chave_de_arme_dos_motores) > 0 and \
       status_do_link == 'CONECTADO':
        chave_de_arme_dos_motores_oculto = "*" * len(chave_de_arme_dos_motores)
        print("Registro validado com sucesso!")
        print(f"Data: {data_formatada} | Código protegido: {chave_de_arme_dos_motores_oculto}")
        break
    else:
        print(f"Tentativa inválida ({tentativa + 1} de 5). Verifique os dados.")
        print("-" * 50)
else:
    print("BLOQUEADO: 5 tentativas esgotadas.")
