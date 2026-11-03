"""Interface de terminal do Controle Financeiro Pessoal."""

from datetime import date
from database import (
    initialize_database,
    add_transaction,
    list_transactions,
    delete_transaction,
    get_summary,
    is_valid_date,
)


def read_amount():
    while True:
        raw_value = input("Valor (ex.: 125,50): R$ ").strip().replace(",", ".")
        try:
            amount = float(raw_value)
            if amount <= 0:
                print("O valor precisa ser maior que zero.")
                continue
            return amount
        except ValueError:
            print("Digite um número válido. Exemplo: 125,50.")


def register_transaction():
    print("\n--- Nova movimentação ---")
    description = input("Descrição: ").strip()
    if not description:
        print("A descrição não pode ficar vazia.")
        return

    print("1. Receita")
    print("2. Despesa")
    option = input("Tipo: ").strip()
    if option not in ("1", "2"):
        print("Opção inválida.")
        return
    kind = "receita" if option == "1" else "despesa"

    amount = read_amount()
    category = input("Categoria (ex.: salário, alimentação): ").strip()
    if not category:
        print("A categoria não pode ficar vazia.")
        return

    transaction_date = input(
        f"Data (AAAA-MM-DD) [padrão: {date.today().isoformat()}]: "
    ).strip()
    if not transaction_date:
        transaction_date = date.today().isoformat()
    if not is_valid_date(transaction_date):
        print("Data inválida. Use o formato AAAA-MM-DD.")
        return

    transaction_id = add_transaction(
        description, amount, kind, category, transaction_date
    )
    print(f"Movimentação cadastrada com sucesso! ID: {transaction_id}")


def show_transactions():
    print("\n--- Movimentações ---")
    print("1. Todas")
    print("2. Apenas receitas")
    print("3. Apenas despesas")
    option = input("Filtro: ").strip()

    filters = {"1": None, "2": "receita", "3": "despesa"}
    if option not in filters:
        print("Opção inválida.")
        return

    transactions = list_transactions(filters[option])
    if not transactions:
        print("Nenhuma movimentação encontrada.")
        return

    print("-" * 78)
    print(f"{'ID':<5} {'DATA':<12} {'TIPO':<9} {'VALOR':>12}  DESCRIÇÃO / CATEGORIA")
    print("-" * 78)
    for item in transactions:
        print(
            f"{item['id']:<5} {item['transaction_date']:<12} "
            f"{item['kind']:<9} R$ {item['amount']:>9.2f}  "
            f"{item['description']} / {item['category']}"
        )


def show_summary():
    summary = get_summary()
    print("\n--- Resumo financeiro ---")
    print(f"Total de receitas: R$ {summary['income']:.2f}")
    print(f"Total de despesas: R$ {summary['expenses']:.2f}")
    print(f"Saldo atual:       R$ {summary['balance']:.2f}")


def remove_transaction():
    print("\n--- Excluir movimentação ---")
    raw_id = input("ID da movimentação: ").strip()
    try:
        transaction_id = int(raw_id)
        if transaction_id <= 0:
            raise ValueError
    except ValueError:
        print("Informe um ID inteiro positivo.")
        return

    if delete_transaction(transaction_id):
        print("Movimentação excluída.")
    else:
        print("Não foi encontrada uma movimentação com esse ID.")


def main():
    initialize_database()
    while True:
        print("\n" + "=" * 38)
        print("       CONTROLE FINANCEIRO")
        print("=" * 38)
        print("1. Cadastrar movimentação")
        print("2. Listar movimentações")
        print("3. Ver resumo financeiro")
        print("4. Excluir movimentação")
        print("0. Sair")

        option = input("Escolha uma opção: ").strip()
        if option == "1":
            register_transaction()
        elif option == "2":
            show_transactions()
        elif option == "3":
            show_summary()
        elif option == "4":
            remove_transaction()
        elif option == "0":
            print("Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
