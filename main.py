
import json
from datetime import datetime

# ==========================================
#              CUIDAR+
#   Seu cuidado, organizado em um só lugar
# ==========================================

print("=" * 40)
print("             CUIDAR+")
print(" Seu cuidado, organizado em um só lugar")
print("=" * 40)


# ==========================================
# FUNÇÃO PARA SALVAR OS DADOS
# ==========================================


# ==========================================
# FUNÇÃO PARA SALVAR OS DADOS
# ==========================================

def salvar_dados():
    # Abre o arquivo de medicamentos no modo de escrita.
    # Se o arquivo não existir, o Python cria um novo.
    # Se já existir, seu conteúdo será substituído.
    with open("medicamentos.json", "w", encoding="utf-8") as arquivo:

        # Converte a lista de medicamentos para o formato JSON
        # e grava os dados no arquivo.
        json.dump(
            medicamentos,
            arquivo,
            ensure_ascii=False,  # Mantém acentos e caracteres especiais.
            indent=4             # Organiza o JSON com quatro espaços.
        )

    # Abre o arquivo de consultas para salvar os dados
    # cadastrados nessa outra lista.
    with open("consultas.json", "w", encoding="utf-8") as arquivo:

        # Converte a lista de consultas para JSON e grava no arquivo.
        json.dump(
            consultas,
            arquivo,
            ensure_ascii=False,
            indent=4
        )



# ==========================================
# CARREGAR OS DADOS SALVOS
# ==========================================

# Tenta abrir o arquivo que contém os medicamentos cadastrados.
try:
    # Abre o arquivo no modo de leitura ("r").
    # O comando with fecha o arquivo automaticamente ao terminar.
    with open("medicamentos.json", "r", encoding="utf-8") as arquivo:

        # Lê o conteúdo JSON e transforma os dados
        # em uma estrutura que o Python consegue utilizar.
        medicamentos = json.load(arquivo)

# Se o arquivo ainda não existir, trata essa situação.
except FileNotFoundError:

    # Cria uma lista vazia para armazenar medicamentos.
    # Assim, o programa pode iniciar sem cadastros anteriores.
    medicamentos = []


# Tenta abrir o arquivo que contém as consultas cadastradas.
try:
    # Abre o arquivo de consultas no modo de leitura.
    with open("consultas.json", "r", encoding="utf-8") as arquivo:

        # Carrega as consultas do JSON para a variável consultas.
        consultas = json.load(arquivo)

# Se o arquivo ainda não existir, trata essa situação.
except FileNotFoundError:

    # Inicia uma lista vazia de consultas.
    consultas = []


# ==========================================
# MENU PRINCIPAL
# ==========================================

while True:
    print("\n" + "=" * 30)
    print("          MENU PRINCIPAL")
    print("=" * 30)

    print("1 - Cadastrar medicamento")
    print("2 - Listar medicamentos")
    print("3 - Registrar dose tomada")
    print("4 - Cadastrar consulta")
    print("5 - Ver próximas consultas")
    print("6 - Ver histórico de doses")
    print("7 - Editar medicamento")
    print("8 - Excluir medicamento")
    print("0 - Sair")

    opcao = input("\nEscolha uma opção: ").strip()

    # ======================================
    # OPÇÃO 1: CADASTRAR MEDICAMENTO
    # ======================================

    if opcao == "1":
        print("\n--- CADASTRO DE MEDICAMENTOS ---")

        nome = input("Nome do medicamento: ").strip()
        intervalo = input(
            "Intervalo entre doses (em horas): "
        ).strip()
        horario = input(
            "Horário da primeira dose (HH:MM): "
        ).strip()
        inicio = input(
            "Data de início (DD/MM/AAAA): "
        ).strip()
        fim = input(
            "Data de término (DD/MM/AAAA): "
        ).strip()

        medicamento = {
            "nome": nome,
            "intervalo": intervalo,
            "horario": horario,
            "inicio": inicio,
            "fim": fim,
            "historico_doses": []
        }

        medicamentos.append(medicamento)

        salvar_dados()

        print("\nMedicamento cadastrado com sucesso!")

    # ======================================
    # OPÇÃO 2: LISTAR MEDICAMENTOS
    # ======================================

    elif opcao == "2":
        print("\n--- SEUS MEDICAMENTOS ---")

        if len(medicamentos) == 0:
            print("Nenhum medicamento cadastrado.")

        else:
            for numero, medicamento in enumerate(medicamentos, 1):
                print(f"\n{numero}. {medicamento['nome']}")
                print(
                    f"Intervalo: {medicamento['intervalo']} horas"
                )
                print(
                    f"Primeira dose: {medicamento['horario']}"
                )
                print(f"Início: {medicamento['inicio']}")
                print(f"Término: {medicamento['fim']}")

                historico = medicamento.get("historico_doses", [])

                print(f"Doses registradas: {len(historico)}")

    # ======================================
    # OPÇÃO 3: REGISTRAR DOSE TOMADA
    # ======================================

    elif opcao == "3":
        print("\n--- REGISTRAR DOSE TOMADA ---")

        if len(medicamentos) == 0:
            print("Cadastre um medicamento primeiro.")

        else:
            for numero, medicamento in enumerate(medicamentos, 1):
                print(f"{numero} - {medicamento['nome']}")

            try:
                numero = int(
                    input("\nQual medicamento você tomou? ")
                )

                if 1 <= numero <= len(medicamentos):
                    medicamento = medicamentos[numero - 1]

                    registro = {
                        "data": datetime.now().strftime("%d/%m/%Y"),
                        "horario": datetime.now().strftime("%H:%M")
                    }

                    if "historico_doses" not in medicamento:
                        medicamento["historico_doses"] = []

                    medicamento["historico_doses"].append(registro)

                    salvar_dados()

                    print(
                        f"\nRegistro da dose de "
                        f"{medicamento['nome']} salvo!"
                    )
                    print(f"Data: {registro['data']}")
                    print(f"Horário: {registro['horario']}")

                else:
                    print("Número inválido.")

            except ValueError:
                print("Digite um número válido.")

    # ======================================
    # OPÇÃO 4: CADASTRAR CONSULTA
    # ======================================

    elif opcao == "4":
        print("\n--- CADASTRAR CONSULTA ---")

        nome = input("Nome da consulta: ").strip()
        data = input(
            "Data da consulta (DD/MM/AAAA): "
        ).strip()
        horario = input("Horário (HH:MM): ").strip()
        local = input("Local da consulta: ").strip()

        try:
            datetime.strptime(data, "%d/%m/%Y")
            datetime.strptime(horario, "%H:%M")

            consulta = {
                "nome": nome,
                "data": data,
                "horario": horario,
                "local": local
            }

            consultas.append(consulta)

            salvar_dados()

            print("\nConsulta cadastrada com sucesso!")

        except ValueError:
            print(
                "\nData ou horário inválido. "
                "Use DD/MM/AAAA e HH:MM."
            )

    # ======================================
    # OPÇÃO 5: VER PRÓXIMAS CONSULTAS
    # ======================================

    elif opcao == "5":
        print("\n--- PRÓXIMAS CONSULTAS ---")

        if len(consultas) == 0:
            print("Nenhuma consulta cadastrada.")

        else:
            try:
                consultas_ordenadas = sorted(
                    consultas,
                    key=lambda consulta: datetime.strptime(
                        consulta["data"],
                        "%d/%m/%Y"
                    )
                )

                for consulta in consultas_ordenadas:
                    print(f"\nConsulta: {consulta['nome']}")
                    print(f"Data: {consulta['data']}")
                    print(f"Horário: {consulta['horario']}")
                    print(f"Local: {consulta['local']}")

            except ValueError:
                print(
                    "Existe uma consulta com data inválida. "
                    "Confira os dados cadastrados."
                )

    # ======================================
    # OPÇÃO 6: HISTÓRICO DE DOSES
    # ======================================

    elif opcao == "6":
        print("\n--- HISTÓRICO DE DOSES ---")

        if len(medicamentos) == 0:
            print("Nenhum medicamento cadastrado.")

        else:
            for numero, medicamento in enumerate(medicamentos, 1):
                print(f"\n{numero} - {medicamento['nome']}")

            try:
                numero = int(
                    input("\nDe qual medicamento deseja ver o histórico? ")
                )

                if 1 <= numero <= len(medicamentos):
                    medicamento = medicamentos[numero - 1]

                    historico = medicamento.get("historico_doses", [])

                    if len(historico) == 0:
                        print(
                            "Ainda não existem doses registradas "
                            "para esse medicamento."
                        )

                    else:
                        print(
                            f"\nHistórico de {medicamento['nome']}:"
                        )

                        for registro in historico:
                            print(
                                f"Data: {registro['data']} | "
                                f"Horário: {registro['horario']}"
                            )

                else:
                    print("Número inválido.")

            except ValueError:
                print("Digite um número válido.")


    # ======================================
    # OPÇÃO 7: EDITAR MEDICAMENTO
    # ======================================

    elif opcao == "7":
        print("\n--- EDITAR MEDICAMENTO ---")

        if len(medicamentos) == 0:
            print("Nenhum medicamento cadastrado.")

        else:
            for numero, medicamento in enumerate(medicamentos, 1):
                print(f"{numero} - {medicamento['nome']}")

            try:
                numero = int(
                    input("\nQual medicamento deseja editar? ")
                )

                if 1 <= numero <= len(medicamentos):
                    medicamento = medicamentos[numero - 1]

                    print("\nPressione Enter para manter o valor atual.")

                    nome = input(
                        f"Nome [{medicamento['nome']}]: "
                    ).strip()

                    intervalo = input(
                        f"Intervalo em horas [{medicamento['intervalo']}]: "
                    ).strip()

                    horario = input(
                        f"Primeira dose [{medicamento['horario']}]: "
                    ).strip()

                    inicio = input(
                        f"Data de início [{medicamento['inicio']}]: "
                    ).strip()

                    fim = input(
                        f"Data de término [{medicamento['fim']}]: "
                    ).strip()

                    if nome:
                        medicamento["nome"] = nome

                    if intervalo:
                        medicamento["intervalo"] = intervalo

                    if horario:
                        medicamento["horario"] = horario

                    if inicio:
                        medicamento["inicio"] = inicio

                    if fim:
                        medicamento["fim"] = fim

                    salvar_dados()

                    print("\nMedicamento atualizado com sucesso!")

                else:
                    print("Número inválido.")

            except ValueError:
                print("Digite um número válido.")


    # ======================================
    # OPÇÃO 8: EXCLUIR MEDICAMENTO
    # ======================================

    elif opcao == "8":
        print("\n--- EXCLUIR MEDICAMENTO ---")

        if len(medicamentos) == 0:
            print("Nenhum medicamento cadastrado.")

        else:
            for numero, medicamento in enumerate(medicamentos, 1):
                print(f"{numero} - {medicamento['nome']}")

            try:
                numero = int(
                    input("\nQual medicamento deseja excluir? ")
                )

                if 1 <= numero <= len(medicamentos):
                    medicamento = medicamentos[numero - 1]

                    print(
                        f"\nMedicamento selecionado: "
                        f"{medicamento['nome']}"
                    )

                    confirmar = input(
                        "Tem certeza que deseja excluir? (s/n): "
                    ).strip().lower()

                    if confirmar == "s":
                        medicamentos.pop(numero - 1)
                        salvar_dados()

                        print("Medicamento excluído com sucesso!")

                    else:
                        print("Exclusão cancelada.")

                else:
                    print("Número inválido.")

            except ValueError:
                print("Digite um número válido.")


    # ======================================
    # OPÇÃO 0: SAIR
    # ======================================

    elif opcao == "0":
        print("\nObrigada por utilizar o CUIDAR+!")
        print("Se cuida! Até a próxima.")
        break

    # ======================================
    # OPÇÃO INVÁLIDA
    # ======================================

    else:
        print("\nOpção inválida. Tente novamente.")