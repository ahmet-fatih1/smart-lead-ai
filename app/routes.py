from flask import Blueprint, request, jsonify, render_template
from app.services.ai_service import ai_service, AIServiceError
from app import database

# Pages Blueprint ve API Blueprint ayrı tutulacak.

# Blueprint Controller'ı organize eden yapı

#request ise body erişimidir.

pages_bp = Blueprint("pages", __name__) 
api_bp = Blueprint("api", __name__, url_prefix="/api")

# Ana sayfa
@pages_bp.route("/", methods=["GET"])
def home():
    return render_template("index.html")

# Dashboard sayfası
@pages_bp.route("/dashboard", methods=["GET"])
def dashboard():
    return render_template("dashboard.html")

# Yapay zekayla konuşmayı yönetir.
@api_bp.route("/sohbet", methods=["POST"])
def sohbet():
    try:
        istek = request.get_json()
        
        if not istek or not istek.get("mesaj"):
            return jsonify({
                "basari": False,
                "hata": "Mesaj alanı zorunludur."
            }), 400 # Eksik veri

        mesaj = istek.get("mesaj")
        gecmis = istek.get("gecmis", [])

        cevap = ai_service.yanit_uret(mesaj, gecmis)
        
        return jsonify({
            "basari": True,
            "cevap": cevap
        })

    except AIServiceError:
        return jsonify({
            "basari": False,
            "hata": "Yapay zeka servisine şu anda ulaşılamıyor"
        }),503 # AI hatası

# Kayıtlı tüm leadleri getirir.
@api_bp.route("/leads", methods=["GET"])
def get_leads():
    leadler = database.tum_leadler()

    return jsonify({
        "basari": True,
        "leadler": leadler
    })

# Yeni bir lead kaydeder.
@api_bp.route("/leads", methods=["POST"])
def save_leads():
    veri = request.get_json()
    
    if not veri or not veri.get("isim") or not veri.get("telefon"):
        return jsonify({
            "basari": False,
            "hata": "İsim ve telefon alanları zorunludur."
        }), 400 # Eksik veri

    database.lead_ekle(
        veri["isim"],
        veri["telefon"],
        veri.get("mesaj")
    )

    return jsonify({
        "basari": True,
        "mesaj": "Lead başarıyla kaydedildi."
        }), 201 # 201 = created