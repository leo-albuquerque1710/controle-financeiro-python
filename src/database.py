
"""Camada de acesso ao banco de dados SQLite."""

from pathlib import Path
import sqlite3
from datetime import date
from contextlib import contextmanager

DB_PATH = Path(__file__).resolve().parent.parent / "data" / "financeiro.db"


@contextmanager
def get_connection():
    """Abre uma conexão e garante que ela seja fechada ao final."""
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)

    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row

    try:
        with connection:
            yield connection
    finally:
        connection.close()


def initialize_database():
    """Cria a tabela de movimentações caso ela ainda não exista."""
    with get_connection() as connection:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                description TEXT NOT NULL,
                amount REAL NOT NULL CHECK (amount > 0),
                kind TEXT NOT NULL CHECK (kind IN ('receita', 'despesa')),
                category TEXT NOT NULL,
                transaction_date TEXT NOT NULL
            )
            """
        )


def add_transaction(description, amount, kind, category, transaction_date):
    """Insere uma movimentação e retorna seu identificador."""
    with get_connection() as connection:
        cursor = connection.execute(
            """
            INSERT INTO transactions
                (description, amount, kind, category, transaction_date)
            VALUES (?, ?, ?, ?, ?)
            """,
            (description, amount, kind, category, transaction_date),
        )
        return cursor.lastrowid


def list_transactions(kind=None):
    """Retorna movimentações, opcionalmente filtradas por tipo."""
    with get_connection() as connection:
        if kind:
            rows = connection.execute(
                """
                SELECT * FROM transactions
                WHERE kind = ?
                ORDER BY transaction_date DESC, id DESC
                """,
                (kind,),
            ).fetchall()
        else:
            rows = connection.execute(
                """
                SELECT * FROM transactions
                ORDER BY transaction_date DESC, id DESC
                """
            ).fetchall()

        return rows


def delete_transaction(transaction_id):
    """Exclui uma movimentação. Retorna True se encontrou o ID."""
    with get_connection() as connection:
        cursor = connection.execute(
            "DELETE FROM transactions WHERE id = ?",
            (transaction_id,),
        )
        return cursor.rowcount > 0


def get_summary():
    """Calcula receitas, despesas e saldo diretamente no SQLite."""
    with get_connection() as connection:
        row = connection.execute(
            """
            SELECT
                COALESCE(SUM(CASE WHEN kind = 'receita' THEN amount ELSE 0 END), 0) AS income,
                COALESCE(SUM(CASE WHEN kind = 'despesa' THEN amount ELSE 0 END), 0) AS expenses
            FROM transactions
            """
        ).fetchone()

    income = float(row["income"])
    expenses = float(row["expenses"])

    return {
        "income": income,
        "expenses": expenses,
        "balance": income - expenses,
    }


def is_valid_date(value):
    """Valida uma data no formato AAAA-MM-DD."""
    try:
        date.fromisoformat(value)
        return True
    except ValueError:
        return False
