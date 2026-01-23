from koneksi import create_connection
from pymysql.err import IntegrityError


def load_data():
    try:
        db = create_connection()
        cursor = db.cursor()
        query = "SELECT id, title, status, task_id FROM sub_tasks"
        cursor.execute(query)
        result = cursor.fetchall()
        db.close()
        return True, result
    except Exception as e:
        return False, f"Error load data: {e}"


def simpan_data(title, status, task_id):
    try:
        db = create_connection()
        cursor = db.cursor()
        query = "INSERT INTO sub_tasks (title, status, task_id) VALUES (%s, %s, %s)"

        cursor.execute(query, (title, status, task_id))
        db.commit()
        db.close()
        return True, "Sub Task berhasil disimpan."
    except IntegrityError as e:
        return False, f"Error Database: {e}"
    except Exception as e:
        return False, f"Gagal simpan: {e}"


def ubah_data(old_id, new_id, title, status, task_id):
    try:
        db = create_connection()
        cursor = db.cursor()
        query = (
            "UPDATE sub_tasks SET id=%s, title=%s, status=%s, task_id=%s WHERE id=%s"
        )
        cursor.execute(query, (new_id, title, status, task_id, old_id))
        db.commit()
        db.close()
        return True, "Sub Tasks berhasil diubah."
    except Exception as e:
        return False, f"Gagal ubah: {e}"


def hapus_data(id):
    try:
        db = create_connection()
        cursor = db.cursor()
        query = "DELETE FROM sub_tasks WHERE id = %s"
        cursor.execute(query, (id,))
        db.commit()
        db.close()
        return True, "Sub Tasks berhasil dihapus."
    except Exception as e:
        return False, f"Gagal hapus: {e}"
