import requests
import tldextract
import whois
from datetime import datetime
from urllib.parse import urlparse, unquote
import re

class PhishShield:
    def __init__(self):
        self.SUSPICIOUS_KEYWORDS = ["login", "verify", "secure", "account"]
        self.HOMOGLYPH_DOMAINS = self._load_homoglyphs()
    
    def analyze_url(self, url):
        """Analiza una URL y devuelve un reporte detallado."""
        report = {
            "url": url,
            "domain": self._extract_domain(url),
            "is_safe": True,
            "alerts": [],
            "risk_score": 0  # 0-100
        }

        # Análisis de capas
        self._check_domain_age(report)
        self._check_homoglyphs(report)
        self._check_url_parameters(report)
        self._check_redirects(report)
        
        # Calcula puntuación de riesgo
        report["risk_score"] = min(len(report["alerts"]) * 20, 100)
        report["is_safe"] = report["risk_score"] < 40

        return report

    def _extract_domain(self, url):
        ext = tldextract.extract(url)
        return f"{ext.domain}.{ext.suffix}"

    def _check_homoglyphs(self, report):
        domain = report["domain"]
        for legit_domain in self.HOMOGLYPH_DOMAINS:
            if legit_domain in domain and domain != legit_domain:
                report["alerts"].append(f"⚠️ Homoglifo detectado: parece '{legit_domain}' pero es '{domain}'")
                break

    def _check_domain_age(self, report):
        try:
            domain_info = whois.whois(report["domain"])
            if domain_info.creation_date:
                age = (datetime.now() - domain_info.creation_date[0]).days
                if age < 180:
                    report["alerts"].append(f"🕒 Dominio reciente ({age} días)")
        except Exception as e:
            report["alerts"].append(f"❌ Error WHOIS: {str(e)}")

    def _check_url_parameters(self, report):
        parsed = urlparse(report["url"])
        if any(key in unquote(parsed.query).lower() for key in self.SUSPICIOUS_KEYWORDS):
            report["alerts"].append("🔍 Parámetros sospechosos en URL")

    def _check_redirects(self, report):
        try:
            response = requests.head(report["url"], allow_redirects=True, timeout=5)
            if response.url != report["url"]:
                report["alerts"].append(f"↪️ Redirige a: {response.url}")
        except:
            report["alerts"].append("⏳ No se pudo verificar redirecciones")

    def _load_homoglyphs(self):
        return ["paypal", "amazon", "google", "microsoft"]

# Ejemplo de uso
if __name__ == "__main__":
    analyzer = PhishShield()
    report = analyzer.analyze_url("https://paypål.com/login?user=test")
    print("🔎 Reporte de Phishing:")
    for alert in report["alerts"]:
        print(f"- {alert}")
    print(f"📊 Puntuación de riesgo: {report['risk_score']}/100")
