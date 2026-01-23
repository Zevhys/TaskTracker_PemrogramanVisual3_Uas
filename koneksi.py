import pymysql


def create_connection():
    connection = pymysql.connect(
        host="localhost",
        user="root",
        password="",
        database="task_tracker",
        cursorclass=pymysql.cursors.DictCursor,
    )
    return connection


if __name__ == "__main__":
    try:
        db = create_connection()
        print("Koneksi ke database BERHASIL!")
        db.close()
    except Exception as e:
        print("Koneksi GAGAL:", e)
