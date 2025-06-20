import requests
import tldextract
import whois
from datetime import datetime
from urllib.parse import urlparse, unquote

class PhishShield:
    def __init__(self):
        self.SUSPICIOUS_KEYWORDS = ["login", "verify", "bank", "secure"]
        self.HOMOGLYPHS = ["paypal", "amazon", "google", "microsoft"]

    def analyze_url(self, url):
        report = {
            "url": url,
            "domain": self._extract_domain(url),
            "is_safe": True,
            "alerts": [],
            "risk_score": 0
        }
        self._check_homoglyphs(report)
        self._check_domain_age(report)
        self._check_url_keywords(report)
        report["risk_score"] = min(len(report["alerts"]) * 25, 100)
        report["is_safe"] = report["risk_score"] < 50
        return report

    def _extract_domain(self, url):
        ext = tldextract.extract(url)
        return f"{ext.domain}.{ext.suffix}"

    def _check_homoglyphs(self, report):
        domain = report["domain"]
        for legit in self.HOMOGLYPHS:
            if legit in domain and domain != legit:
                report["alerts"].append(f"⚠️ Homoglifo: parece '{legit}' pero es '{domain}'")

    def _check_domain_age(self, report):
        try:
            info = whois.whois(report["domain"])
            if info.creation_date:
                age = (datetime.now() - info.creation_date[0]).days
                if age < 180:
                    report["alerts"].append(f"🕒 Dominio reciente ({age} días)")
        except Exception as e:
            report["alerts"].append(f"❌ Error WHOIS: {str(e)}")

    def _check_url_keywords(self, report):
        if any(kw in report["url"].lower() for kw in self.SUSPICIOUS_KEYWORDS):
            report["alerts"].append("🔍 URL contiene términos sospechosos")

if __name__ == "__main__":
    analyzer = PhishShield()
    print(analyzer.analyze_url("https://paypål.com/login"))
