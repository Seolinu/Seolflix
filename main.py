from flask import Flask, render_template
import requests

app = Flask(__name__)

# GAS 웹 앱 URL (1-3에서 복사한 URL)
GAS_WEB_APP_URL = "https://script.google.com/macros/s/AKfycbxZlibPGGO52FVhALwrnhRX4okcAxX5F-6Dlz6Xqbepi_Yd1D-5CUBLNx-sg6qUHbNW/exec"

@app.route('/')
def index():
    # GAS API에서 최신 메일 5개 요청
    response = requests.get(GAS_WEB_APP_URL, params={'count': 1})
    emails = []
    if response.status_code == 200:
        emails = response.json()

    return render_template('index.html', emails=emails)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
