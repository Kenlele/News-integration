document.addEventListener("DOMContentLoaded", () => {
    fetchNews("sanli", "sanli-news");
    fetchNews("ctv", "ctv-news");
    fetchNews("ftv", "ftv-news");
});

// 動態抓取 API 資料並更新內容
function fetchNews(platform, containerId) {
    const apiUrl = `/api/get_news?platform=${platform}`;
    const container = document.getElementById(containerId).querySelector('.news-content');

    fetch(apiUrl)
        .then(response => response.json())
        .then(newsData => {
            container.innerHTML = "";
            newsData.forEach(news => {
                const newsItem = `
                    <div class="news-item">
                        <h4>${news.title}</h4>
                        <p>${news.summary}</p>
                        <a href="${news.url}" target="_blank">閱讀更多</a>
                    </div>
                `;
                container.innerHTML += newsItem;
            });
        })
        .catch(error => {
            console.error("Error fetching news:", error);
            container.innerHTML = "<p>無法加載新聞，請稍後再試。</p>";
        });
}
