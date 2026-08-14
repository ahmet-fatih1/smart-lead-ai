import requests
import os
from dotenv import load_dotenv

load_dotenv()

class AIServiceError(Exception):
    pass

class AIService:

    def yanit_uret(self, mesaj, gecmis):

        try:
            # AI'ye istek atacağımız kodlar buraya gelecek
            # 1. AI istemcisini oluştur 
            # 2. AI'ye mesajı + geçmişi gönder 
            # 3. Gelen cevabı al 
            # 4. cevabı return et 

            messages = [
                {
                    "role": "system",
                    "content": os.getenv("BUSINESS_CONTEXT", "")
                }
            ]

            messages.extend(gecmis)
            
            messages.append({
                "role": "user",
                "content": mesaj
            })

            api_key = os.getenv("GROQ_API_KEY")
            
            if not api_key:
                return "Demo modu: Şu anda yapay zeka servisi aktif değil."
            
            response = requests.post(
                "https://api.groq.com/openai/v1/chat/completions",
                headers={
                    "Authorization": f"Bearer {api_key}",
                    "Content-Type": "application/json"
                },
                json={
                    "model": "llama-3.1-8b-instant",
                    "messages": messages
                }
            )

            if response.status_code != 200:
                raise AIServiceError("AI servisi hata verdi.")
            
            data = response.json()
            
            cevap = data["choices"][0]["message"]["content"]
            
            return cevap

        except AIServiceError:
            raise
        
        except Exception as e:
            raise AIServiceError(f"AI servisiyle iletişim kurulamadı: {e}") from e # from e = Yeni hatayı önceki hatanın sbebiyle birlikte fırlat
    
ai_service = AIService() 
        

        

        

    