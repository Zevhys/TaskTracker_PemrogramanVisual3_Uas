from koneksi import create_connection
from pymysql.err import IntegrityError


def load_data():
    try:
        db = create_connection()
        cursor = db.cursor()
        query = "SELECT id, title, description, status, due_date, user_id, project_id FROM tasks"
        cursor.execute(query)
        result = cursor.fetchall()
        db.close()
        return True, result
    except Exception as e:
        return False, f"Error load data: {e}"


def simpan_data(id, title, description, status, due_date, user_id, project_id):
    try:
        db = create_connection()
        cursor = db.cursor()
        query = "INSERT INTO tasks (id, title, description, status, due_date, user_id, project_id) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(
            query, (id, title, description, status, due_date, user_id, project_id)
        )
        db.commit()
        db.close()
        return True, "Tasks berhasil disimpan."
    except IntegrityError:
        return False, f"ID {id} sudah ada."
    except Exception as e:
        return False, f"Gagal simpan: {e}"


def ubah_data(
    old_id, new_id, title, description, status, due_date, user_id, project_id
):
    try:
        db = create_connection()
        cursor = db.cursor()
        query = "UPDATE tasks SET id=%s, title=%s, description=%s, status=%s, due_date=%s, user_id=%s, project_id=%s WHERE id=%s"
        cursor.execute(
            query,
            (new_id, title, description, status, due_date, user_id, project_id, old_id),
        )
        db.commit()
        db.close()
        return True, "Tasks berhasil diubah."
    except Exception as e:
        return False, f"Gagal ubah: {e}"


def hapus_data(id):
    try:
        db = create_connection()
        cursor = db.cursor()
        query = "DELETE FROM tasks WHERE id = %s"
        cursor.execute(query, (id,))
        db.commit()
        db.close()
        return True, "Tasks berhasil dihapus."
    except Exception as e:
        return False, f"Gagal hapus: {e}"
