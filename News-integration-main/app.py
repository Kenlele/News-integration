import flask
from flask import Flask, render_template, jsonify, request
from get_news.get_news_api import get_news_data

app = Flask(__name__)

# 首頁路由：渲染首頁模板
@app.route('/')
def index():
    return render_template('index.html')

# 新聞頁面路由：渲染新聞頁面
@app.route('/news')
def news():
    return render_template('news.html')

# API 路由：提供新聞資料
@app.route('/api/get_news', methods=['GET'])
def api_get_news():
    platform = request.args.get('platform', 'all')  # 接收前端的參數
    news_data = get_news_data(platform)
    return jsonify(news_data)

if __name__ == '__main__':
    app.run(debug=True)
