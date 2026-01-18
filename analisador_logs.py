print("=== ANALISADOR DE LOGS - V1 ===")

caminho = input("Digite o caminho do arquivo log: ")

print("Você digitou: ", caminho)

try:
    # Abre o arquivo para modo leitura ("r")
    with open(caminho, "r") as arquivo:

        # Contador de linhas
        linhas = 0
        acessos_por_ip = {}  # dicionário: ip -> quantidade
        acessos_por_status = {}
        erros_401_por_ip = {}

        for linha in arquivo:
            linhas += 1  # mesmo que linhas = linhas + 1

            conteudo = linha.strip()  # tira o (\n) do final

            partes = conteudo.split()  # Quebrar a linha em partes separadas por espaço

            ip = partes[0]

            status = partes[-1]

            if status == "401":
                if ip not in erros_401_por_ip:
                    erros_401_por_ip[ip] = 0
                erros_401_por_ip[ip] += 1

            if (
                ip not in acessos_por_ip
            ):  # Se o IP ainda não existe no dicionário, começa em 0
                acessos_por_ip[ip] = 0

            acessos_por_ip[ip] += 1

            if (
                status not in acessos_por_status
            ):  # Se o Status ainda não existe no dicionário, começa em 0
                acessos_por_status[status] = 0

            acessos_por_status[status] += 1

            print(f"LINHA {linhas} : IP = {ip} : STATUS = {status} ")

    print("\nTotal de linhas do arquivo: ", linhas)
    print("\n=== RESUMO POR IP ===")
    for ip, quantidade in acessos_por_ip.items():
        print(f"{ip} -> {quantidade} acessos")

    print("\n=== RESUMO POR STATUS ===")
    for status, quantidade in acessos_por_status.items():
        print(f"{status} -> {quantidade} acessos")

    print("=== IPs com muitos 401 ===")
    for ip, quantidade in erros_401_por_ip.items():
        if quantidade >= 2:
            print(f"ALERTA: {ip} teve {quantidade} erros 401")

except FileNotFoundError:
    print("Arquivo não encontrado, Verifique o caminho.")
