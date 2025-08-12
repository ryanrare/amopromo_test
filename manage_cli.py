import subprocess
import requests

API_URL = "http://web:8000/api/flights/"


def run_command(cmd_list):
    """Roda comando no shell e retorna output"""
    result = subprocess.run(cmd_list, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Erro ao executar {' '.join(cmd_list)}:")
        print(result.stderr)
        return None
    return result.stdout.strip()


def export_airports():
    print("Exportando aeroportos...")
    output = run_command(["python", "manage.py", "export_airport"])
    if output:
        print(output)


def create_user():
    print("Criando super usuário:")
    subprocess.run(["python", "manage.py", "createsuperuser"])


def generate_token(username):
    print(f"Gerando token para {username}...")
    token = run_command(["python", "manage.py", "drf_create_token", username])
    if token:
        print(f"Token: {token}")
    else:
        print("Não foi possível gerar token.")


def main():
    while True:
        print("\nO que deseja fazer?")
        print("1 - Exportar aeroportos")
        print("2 - Criar superusuário")
        print("3 - Gerar token para o usuario")
        print("0 - Sair")

        choice = input("Escolha uma opção: ").strip()

        if choice == "1":
            export_airports()
        elif choice == "2":
            create_user()
        elif choice == "3":
            username = input("Digite o nome do usuário para gerar token: ").strip()
            generate_token(username)
        elif choice == "0":
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
