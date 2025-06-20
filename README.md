# PhyshShield
# 🔍 **PhishShield** - Detector Avanzado de Phishing  
*por [KevinDevSecOps](https://github.com/KevinDevSecOps)*  

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)  
![Flask](https://img.shields.io/badge/Flask-2.0-green)  
![License](https://img.shields.io/badge/License-MIT-red)  
![VirusTotal](https://img.shields.io/badge/Integración-VirusTotal-yellow)  

---

## 📌 **Descripción**  
**PhishShield** es una herramienta multifuncional para combatir el phishing, que incluye:  
✅ **Análisis de URLs** en tiempo real (homoglifos, dominios sospechosos, parámetros maliciosos).  
✅ **Integración con VirusTotal** para detectar amenazas conocidas.  
✅ **Bot de Telegram** para escanear URLs desde cualquier chat.  
✅ **Interfaz Web** con Flask para análisis detallados.  

---

## 🚀 **Instalación**  
1. Clona el repositorio:  
   ```bash
   git clone https://github.com/KevinDevSecOps/PhishShield.git
   cd PhishShield
   ```  
2. Instala dependencias:  
   ```bash
   pip install -r requirements.txt
   ```  
3. Configura las APIs en `config.ini` (crea una copia de `config.ini.example`):  
   ```ini
   [virustotal]
   api_key = tu_api_key_virustotal

   [telegram]
   bot_token = tu_token_de_telegram
   ```  

---

## 🛠 **Uso**  

### 🤖 **Bot de Telegram**  
1. Ejecuta el bot:  
   ```bash
   python src/bot/telegram_bot.py
   ```  
2. Envía cualquier URL al bot para analizarla.  

### 🌐 **Interfaz Web**  
1. Inicia el servidor Flask:  
   ```bash
   python src/web/app.py
   ```  
2. Abre `http://localhost:5000` en tu navegador.  

### 🖥 **CLI (Línea de Comandos)**  
```bash
python src/phishshield.py --url "https://example.com/login"
```  

---

## 📂 **Estructura del Proyecto**  
```
PhishShield/
├── src/
│   ├── phishshield.py       # Lógica principal
│   ├── api/                 # Integración VirusTotal
│   ├── bot/                 # Bot de Telegram
│   └── web/                 # Interfaz Flask
├── tests/                   # Pruebas unitarias
├── config.ini.example       # Plantilla de configuración
└── requirements.txt         # Dependencias
```

---

## 📸 **Demo**  
### Interfaz Web  
![Demo Web](assets/web_demo.gif)  

### Bot de Telegram  
![Demo Bot](assets/bot_demo.gif)  

*(Nota: Añade tus propios GIFs grabados con [ScreenToGif](https://www.screentogif.com/))*  

---

## 🤝 **Contribuciones**  
¡Se aceptan PRs! Sigue estos pasos:  
1. Haz un **Fork** del proyecto.  
2. Crea una rama: `git checkout -b feature/nueva-funcion`.  
3. Haz commit: `git commit -m "Añade nueva función"`.  
4. Haz Push: `git push origin feature/nueva-funcion`.  
5. Abre un **Pull Request**.  

---

## 📜 **Licencia**  
MIT License - Copyright © 2024 [KevinDevSecOps](https://github.com/KevinDevSecOps).  

---

## 🔑 Obtención de APIs  
- [VirusTotal](https://www.virustotal.com/gui/join-us): Registro gratuito (500 peticiones/día).  
- [BotFather](https://t.me/BotFather): Crea un bot y copia el token.
## 🔗 **Enlaces Útiles**  
- [Documentación de VirusTotal API](https://developers.virustotal.com/reference)  
- [Guía de Bots en Telegram](https://core.telegram.org/bots)  

---

Hecho con ❤️ por [KevinDevSecOps](https://github.com/KevinDevSecOps).  
```
