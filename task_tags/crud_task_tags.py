from koneksi import create_connection
from pymysql.err import IntegrityError


def load_data():
    try:
        db = create_connection()
        cursor = db.cursor()
        query = "SELECT task_id, tag_id FROM task_tags"
        cursor.execute(query)
        result = cursor.fetchall()
        db.close()
        return True, result
    except Exception as e:
        return False, f"Error load data: {e}"


def simpan_data(task_id, tag_id):
    try:
        db = create_connection()
        cursor = db.cursor()
        query = "INSERT INTO task_tags (task_id, tag_id) VALUES (%s, %s)"
        cursor.execute(query, (task_id, tag_id))
        db.commit()
        db.close()
        return True, "Task Tags berhasil disimpan."
    except IntegrityError:
        return False, f"Task ID {task_id} sudah ada atau ID tidak valid."
    except Exception as e:
        return False, f"Gagal simpan: {e}"


def ubah_data(old_task_id, new_task_id, new_tag_id):
    try:
        db = create_connection()
        cursor = db.cursor()
        query = "UPDATE task_tags SET task_id=%s, tag_id=%s WHERE task_id=%s"
        cursor.execute(query, (new_task_id, new_tag_id, old_task_id))
        db.commit()
        db.close()
        return True, "Task Tags berhasil diubah."
    except Exception as e:
        return False, f"Gagal ubah: {e}"


def hapus_data(task_id):
    try:
        db = create_connection()
        cursor = db.cursor()
        query = "DELETE FROM task_tags WHERE task_id = %s"
        cursor.execute(query, (task_id,))
        db.commit()
        db.close()
        return True, "Task Tags berhasil dihapus."
    except Exception as e:
        return False, f"Gagal hapus: {e}"
