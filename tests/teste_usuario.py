from src.models.recebedor import Recebedor
from src.models.doador import Doador


def main():
    print("=== TESTE ===\n")

    # 1. Criando um Recebedor
    print("-> Criando Recebedor...")
    recebedor = Recebedor(10, "Ana Aluna", "ana@escola.com", "123", "Rua Escola, 1", 9999, 500)

    print(f"   Recebedor criado: {recebedor.nome} (ID: {recebedor.id_recebedor})")

    # 2. Criando um Doador
    print("\n-> Criando Doador...")
    doador = Doador(11, "Gohan", "dragon@ball.com", "321", "Rua 2", 88982183456, 499)
    print(f"   Doador criado: {doador.nome} (ID: {doador.id_doador})")

    print("\n=== VERIFICANDO ESTADO ===")
    print("Recebedor:", vars(recebedor))
    print("Doador:", vars(doador))

    print("\n=== TESTE DE MÉTODOS ===")

    # Teste de Login
    print(f"1. Testando Login para {recebedor.nome}...")
    if recebedor.verificar_login("ana@escola.com", "123"):
        print("   -> RESULTADO: SUCESSO (Login aprovado)")
    else:
        print("   -> RESULTADO: FALHA (Senha ou email incorretos)")

    # Teste de Atualização
    print(f"\n2. Atualizando contato...")
    print(f"   Endereço antigo: {recebedor.endereco}")

    mensagem = recebedor.atualizar_contato('Rua Colégio Nova', 35621874)
    print(f"   -> Retorno do sistema: {mensagem}")

    # Verificamos se mudou mesmo usando o Getter
    print(f"   Endereço novo: {recebedor.endereco}")


if __name__ == "__main__":
    main()