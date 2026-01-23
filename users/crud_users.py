from koneksi import create_connection
from pymysql.err import IntegrityError


def load_data():
    try:
        db = create_connection()
        cursor = db.cursor()
        query = "SELECT id, username, password, email, created_at FROM users"
        cursor.execute(query)
        result = cursor.fetchall()
        db.close()
        return True, result
    except Exception as e:
        return False, f"Error load data: {e}"


def simpan_data(id_user, username, password, email, created_at):
    try:
        db = create_connection()
        cursor = db.cursor()
        query = "INSERT INTO users (id, username, password, email, created_at) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(query, (id_user, username, password, email, created_at))
        db.commit()
        db.close()
        return True, "User berhasil disimpan."
    except IntegrityError:
        return False, f"ID {id_user} sudah ada."
    except Exception as e:
        return False, f"Gagal simpan: {e}"


def ubah_data(old_id, new_id, username, password, email, created_at):
    try:
        db = create_connection()
        cursor = db.cursor()
        query = "UPDATE users SET id=%s, username=%s, password=%s, email=%s, created_at=%s WHERE id=%s"
        cursor.execute(query, (new_id, username, password, email, created_at, old_id))
        db.commit()
        db.close()
        return True, "User berhasil diubah."
    except Exception as e:
        return False, f"Gagal ubah: {e}"


def hapus_data(id_user):
    try:
        db = create_connection()
        cursor = db.cursor()
        query = "DELETE FROM users WHERE id = %s"
        cursor.execute(query, (id_user,))
        db.commit()
        db.close()
        return True, "User berhasil dihapus."
    except Exception as e:
        return False, f"Gagal hapus: {e}"
