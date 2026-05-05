import uuid
from database import get_connection
from models.account import Account

#create account
def create_account(account: Account):
    name = account.name
    balance = account.balance
    account_type = account.account_type.value
    account_id = account.account_id.hex

    with get_connection() as conn:
        conn.execute("""
            INSERT INTO account (
                name,
                balance,
                account_type,
                account_id
            ) VALUES (?,?,?,?)
        """, (name, balance, account_type, account_id,))

#fetch one account from ID
def get_account(account_id: uuid.UUID):
    with get_connection() as conn:
        cursor = conn.execute("""
            SELECT * FROM account WHERE account_id = ?
        """, (account_id.hex,))
        return cursor.fetchone()

#fetch all accounts
def get_all_accounts():
    with get_connection() as conn:
        cursor = conn.execute("""SELECT * FROM account""")
        return cursor.fetchall()

#update select account from ID
def update_account(account: Account):
    name = account.name
    balance = account.balance
    account_type = account.account_type.value
    account_id = account.account_id.hex
    with get_connection() as conn:
        conn.execute("""
            UPDATE account SET 
                name = ?,
                balance = ?,
                account_type = ?
                WHERE account_id = ?
            """, (name, balance, account_type, account_id,))

#delete the account
def delete_account(account_id: uuid.UUID):
    with get_connection() as conn:
        conn.execute("""
            DELETE FROM account
            WHERE account_id = ? """, (account_id.hex,))
