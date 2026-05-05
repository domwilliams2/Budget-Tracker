import uuid
from database import get_connection
from models.category import Category

#create category
def create_category(category: Category):
    name = category.name
    color = category.color
    category_id = category.category_id.hex
    with get_connection() as conn:
        conn.execute("""
            INSERT INTO category (
                name,
                color,
                category_id
            ) VALUES (?,?,?)
        """, (name, color, category_id,))

#get all categories
def get_all_categories():
    with get_connection() as conn:
        cursor = conn.execute("""
            SELECT * FROM category
        """)
        return cursor.fetchall()

#get select category
def get_category(category_id: uuid.UUID):
    with get_connection() as conn:
        cursor = conn.execute("""
            SELECT * FROM category where category_id = ?
        """, (category_id.hex,))
        return cursor.fetchone()

#update select category
def update_category(category: Category):
    name = category.name
    color = category.color
    category_id = category.category_id.hex
    with get_connection() as conn:
        conn.execute("""
            UPDATE category SET
                name = ?,
                color = ?
                WHERE category_id = ?
        """, (name, color, category_id,))

#delete select category from list
def delete_category(category_id: uuid.UUID):
    with get_connection() as conn:
        conn.execute("""
            DELETE FROM category
            where category_id = ?
        """, (category_id.hex,))