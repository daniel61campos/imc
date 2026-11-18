print("-------Gestão de Cargas e Tráfego Ferroviário.-------")

for tentativa in range(5):
    nome_do_maquinista = input("Digite nome do maquinista: ").strip().title()
    terminal_de_partida = input("Digite terminal de partida: ").strip().title()
    terminal_de_chegada = input("Digite terminal de chegada: ").strip().title()
    tipo_de_minerio = input("Digite tipo de minério: ").strip().title()
    codigo_do_vagao = input("Digite código do vagão: ").strip()
    numero_do_trem = input("Digite número do trem: ").strip()
    peso_em_toneladas = input("Digite peso em toneladas: ").strip()
    quilometros_a_percorrer = input("Digite quilômetros a percorrer: ").strip()
    data_da_viagem = input("Digite data da viagem: ").strip()
    e_mail_da_ferrovia = input("Digite e-mail da ferrovia: ").strip().lower()
    chave_do_bloqueio_de_freio = input("Digite chave do bloqueio de freio: ").strip()
    sinalizacao_da_linha = input("Digite sinalização da linha: ").strip().upper()

    data_formatada = data_da_viagem.replace("-", "/")

    if nome_do_maquinista.isalpha() and \
       terminal_de_partida.isalpha() and \
       terminal_de_chegada.isalpha() and \
       tipo_de_minerio.isalpha() and \
       numero_do_trem.isalnum() and \
       codigo_do_vagao.startswith('CARGA-') and \
       codigo_do_vagao[len('CARGA-'):].isalnum() and \
       peso_em_toneladas.isdigit() and \
       quilometros_a_percorrer.isdigit() and \
       data_formatada.count('/') == 2 and \
       len(data_formatada) == 10 and \
       e_mail_da_ferrovia.endswith('.ferrovia.log.br') and \
       len(chave_do_bloqueio_de_freio) > 0 and \
       sinalizacao_da_linha == 'VERDE':
        chave_do_bloqueio_de_freio_oculto = "*" * len(chave_do_bloqueio_de_freio)
        print("Registro validado com sucesso!")
        print(f"Data: {data_formatada} | Código protegido: {chave_do_bloqueio_de_freio_oculto}")
        break
    else:
        print(f"Tentativa inválida ({tentativa + 1} de 5). Verifique os dados.")
        print("-" * 50)
else:
    print("BLOQUEADO: 5 tentativas esgotadas.")
