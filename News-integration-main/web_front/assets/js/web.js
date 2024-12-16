// 從後端 API 獲取新聞內容
document.addEventListener("DOMContentLoaded", () => {
    fetchNews("sanli", "sanli-news");
    fetchNews("ctv", "ctv-news");
    fetchNews("ftv", "ftv-news");
});

// 動態更新新聞內容
function fetchNews(platform, containerId) {
    const apiUrl = `/api/get_news?platform=${platform}`; // 修改此 API URL 至後端設定
    const container = document.getElementById(containerId).querySelector('.news-content');

    fetch(apiUrl)
        .then(response => response.json())
        .then(newsData => {
            container.innerHTML = "";
            newsData.forEach(news => {
                const newsItem = `
                    <div class="news-item">
                        <h3>${news.title}</h3>
                        <p>${news.summary}</p>
                        <a href="${news.url}" target="_blank">閱讀更多</a>
                    </div>
                `;
                container.innerHTML += newsItem;
            });
        })
        .catch(error => {
            console.error(`Error fetching ${platform} news:`, error);
            container.innerHTML = "<p>無法載入新聞，請稍後再試。</p>";
        });
}
