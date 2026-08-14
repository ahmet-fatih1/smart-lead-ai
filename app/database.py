import sqlite3

# Veritabanına bağlanır, satırlara sütun adıyla erişim sağlar
def get_db():
    connection = sqlite3.connect("smartlead.db")
    connection.row_factory = sqlite3.Row
    return connection


# 'leads' tablosunu oluşturur (yoksa)
def init_db(app):
    with app.app_context():
        db = get_db()

        db.execute("""
            CREATE TABLE IF NOT EXISTS leads (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                isim TEXT NOT NULL,
                telefon TEXT NOT NULL,
                mesaj TEXT,
                tarih TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

    db.commit()
    db.close()


# Yeni kayıt ekler
def lead_ekle(isim, telefon, mesaj):
    db = get_db()
    
    db.execute(
        """
        INSERT INTO leads (isim, telefon, mesaj)
        VALUES (?, ?, ?)
        """,
        (
            isim, 
            telefon,
            mesaj
        )
    )

    db.commit()
    
    
# Tüm kayıtlar en yeniden eskiye getirir
def tum_leadler():
    db = get_db()
    
    cursor = db.execute(
        """
        SELECT id, isim, telefon, mesaj, tarih
        FROM leads
        ORDER BY id DESC
        """
    )
    
    satirlar = cursor.fetchall()
    
    leadler = []
    
    for satir in satirlar:
        leadler.append({
            "id": satir[0],
            "isim": satir[1],
            "telefon": satir[2],
            "mesaj": satir[3],
            "tarih": satir[4],
        })
        
    return leadler


