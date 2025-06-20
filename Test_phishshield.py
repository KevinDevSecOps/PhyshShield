<!DOCTYPE html>
<html>
<head>
    <title>PhishShield</title>
    <style>
        body { font-family: Arial; text-align: center; margin-top: 50px; }
        input { padding: 10px; width: 300px; }
        button { padding: 10px 20px; background: #4CAF50; color: white; border: none; }
    </style>
</head>
<body>
    <h1>🔍 PhishShield</h1>
    <form onsubmit="analyze(); return false;">
        <input type="text" id="url" placeholder="https://example.com" required>
        <button type="submit">Analizar</button>
    </form>
    <div id="result" style="margin-top: 20px;"></div>
    <script>
        async function analyze() {
            const url = document.getElementById('url').value;
            const response = await fetch('/analyze', {
                method: 'POST',
                headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
                body: `url=${encodeURIComponent(url)}`
            });
            const data = await response.json();
            document.getElementById('result').innerHTML = `
                <h3>Resultado:</h3>
                <p>Dominio: <strong>${data.domain}</strong></p>
                <p>Riesgo: <strong>${data.risk_score}/100</strong></p>
                <ul>${data.alerts.map(a => `<li>${a}</li>`).join('')}</ul>
            `;
        }
    </script>
</body>
</html>
