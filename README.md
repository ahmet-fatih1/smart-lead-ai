# Mihenk SmartLead AI

## Proje Hakkında

**Mihenk** kiralama sektöründeki işletmeler için yapay zeka destekli müşteri iletişimi ve lead toplama sistemidir.

## Özellikler

- AI asistan ile sohbet
- Müşteri adaylarının isim ve telefon bilgilerinin alınması
- Lead'lerin SQLite veritabanında saklanması
- Yönetim panelinde lead'lerin görüntülenmesi
- Flask REST API
- Wix Velo frontend entegrasyonu

## Kullanılan Teknolojiler

- Python
- Flask
- SQLite
- Groq API
- Wix Velo
- Render
- GitHub

## Proje Yapısı

smartlead_ai/
└── app/
    └── services/
        |── ai_service.py
        ├── __init__.py
    ├── templates/
    │   ├── index.html
    │   └── dashboard.html
    ├── database.py
    ├── routes.py
    ├── __init__.py
├── run.py
├── config.py
├── requirements.txt
├── .env
├── README.md


## Kurulum

Projeyi klonladıktan sonra proje klasörüne girin:
`git clone <GITHUB_REPO_URL>`
`cd smarlead_ai`

daha sonrasında sanal ortam oluşturun:

`python -m venv venv`

sanal ortamı aktif edin (Windows):

`venv\Scripts\activate`

gerekli bağımlılıkları yükleyin:

`pip install -r requirements.txt`

.env dosyasını oluşturun ve gerekli ortam değişkenlerini ekleyin.

Uygulamayı çalıştırın:

`python run.py`



## Environment Variables

Aşağıdaki ortam değişkenleri kullanılmaktadır.

AI_PROVIDER=groq
GROQ_API_KEY=api_key
SECRET_KEY=secret_key
DATABASE_URL=sqlite:///smartlead.db
BUSINESS_CONTEXT=business_context
CORS_ORIGIN=*

## Çalıştırma

Uygulamayı çalıştırdıktan sonra 

(http://127.0.0.1:5000) adresinden karşılama sayfasına gidilebilir.

### Yönetim Paneli

(http://127.0.0.1:5000/dashboard)

### Backend sağlık kontrolü

(http://127.0.0.1:5000/health)

## Canlı Sistem

[Render](https://smart-lead-ai.onrender.com)

[Wix](https://afcaliskan1.wixstudio.com/mihenk)
