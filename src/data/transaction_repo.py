import uuid
from database import get_connection
from models.transaction import Transaction


#create transaction
def create_transaction(transaction: Transaction):
    amount = transaction.amount
    date = str(transaction.date)
    description = transaction.description
    type = transaction.type.value
    account_id = transaction.account_id.hex
    category_id = transaction.category_id.hex if transaction.category_id else None
    transaction_id = transaction.transaction_id
    with get_connection() as conn:
        conn.execute("""
            INSERT INTO transactions (
                amount,
                date,
                description,
                type,
                account_id,
                category_id,
                transaction_id
            ) VALUES (?,?,?,?,?,?,?)
        """, (amount, date, description, type, account_id, category_id, transaction_id.hex,))

#get all transactions
def get_all_transactions():
    with get_connection() as conn:
        cursor = conn.execute("""SELECT * from transactions""")
        return cursor.fetchall()

#get select transaction
def get_transaction(transaction_id: uuid.UUID):
    with get_connection() as conn:
        cursor = conn.execute("""SELECT * from transactions WHERE transaction_id = ?""", (transaction_id.hex,))
        return cursor.fetchone()

#update select transaction
def update_transaction(transaction: Transaction):
    amount = transaction.amount
    date = str(transaction.date)
    description = transaction.description
    type = transaction.type.value
    account_id = transaction.account_id.hex
    category_id = transaction.category_id.hex if transaction.category_id else None
    transaction_id = transaction.transaction_id
    with get_connection() as conn:
        conn.execute("""UPDATE transactions SET
            amount = ?,
            date = ?,
            description = ?,
            type = ?,
            account_id = ?,
            category_id = ?,
            WHERE transaction_id = ?
        """, (amount, date, description, type, account_id, category_id, transaction_id.hex,))

#delete select transaction
def delete_transaction(transaction_id: uuid.UUID):
    with get_connection() as conn:
        conn.execute("""DELETE FROM transactions WHERE transaction_id = ?""", (transaction_id.hex,))