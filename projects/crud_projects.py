from koneksi import create_connection
from pymysql.err import IntegrityError


def load_data():
    try:
        db = create_connection()
        cursor = db.cursor()
        query = "SELECT id, name, user_id FROM projects"
        cursor.execute(query)
        result = cursor.fetchall()
        db.close()
        return True, result
    except Exception as e:
        return False, f"Error load data: {e}"


def simpan_data(id, name, user_id):
    try:
        db = create_connection()
        cursor = db.cursor()
        query = "INSERT INTO projects (id, name, user_id) VALUES (%s, %s, %s)"
        cursor.execute(query, (id, name, user_id))
        db.commit()
        db.close()
        return True, "Project berhasil disimpan."
    except IntegrityError:
        return False, f"ID {id} sudah ada."
    except Exception as e:
        return False, f"Gagal simpan: {e}"


def ubah_data(old_id, new_id, name, user_id):
    try:
        db = create_connection()
        cursor = db.cursor()
        query = "UPDATE projects SET id=%s, name=%s, user_id=%s WHERE id=%s"
        cursor.execute(query, (new_id, name, user_id, old_id))
        db.commit()
        db.close()
        return True, "Project berhasil diubah."
    except Exception as e:
        return False, f"Gagal ubah: {e}"


def hapus_data(id):
    try:
        db = create_connection()
        cursor = db.cursor()
        query = "DELETE FROM projects WHERE id = %s"
        cursor.execute(query, (id,))
        db.commit()
        db.close()
        return True, "Project berhasil dihapus."
    except Exception as e:
        return False, f"Gagal hapus: {e}"
