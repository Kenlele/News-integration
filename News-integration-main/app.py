from flask import Flask, render_template, jsonify, request
import requests

app = Flask(__name__)

# 模擬新聞來源資料
NEWS_SOURCES = {
    "sanli": "https://api.example.com/sanli",
    "ctv": "https://api.example.com/ctv",
    "ftv": "https://api.example.com/ftv"
}

# 首頁：渲染主頁面
@app.route("/")
def index():
    return render_template("index.html")

# API：取得新聞資料
@app.route("/api/get_news", methods=["GET"])
def get_news():
    platform = request.args.get("platform")  # 從 query string 取得平台參數
    if platform in NEWS_SOURCES:
        try:
            response = requests.get(NEWS_SOURCES[platform])
            data = response.json()
            return jsonify(data)
        except Exception as e:
            return jsonify({"error": str(e)})
    return jsonify({"error": "Invalid platform"}), 400

if __name__ == "__main__":
    app.run(debug=True)
