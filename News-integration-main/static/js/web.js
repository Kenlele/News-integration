document.addEventListener("DOMContentLoaded", () => {
    // 動態獲取各平台的新聞
    fetchNews("sanli", "sanli-news");
    fetchNews("ctv", "ctv-news");
    fetchNews("ftv", "ftv-news");
});

// 函式：抓取新聞資料並顯示
function fetchNews(platform, containerId) {
    const apiUrl = `/api/get_news?platform=${platform}`;
    const container = document.getElementById(containerId);

    fetch(apiUrl)
        .then(response => response.json())
        .then(newsData => {
            container.innerHTML = "";  // 清空內容
            if (newsData.error) {
                container.innerHTML = `<p>${newsData.error}</p>`;
            } else {
                newsData.forEach(news => {
                    container.innerHTML += `
                        <div class="news-item">
                            <h3>${news.title}</h3>
                            <p>${news.summary || '無摘要'}</p>
                            <a href="${news.url}" target="_blank">閱讀更多</a>
                        </div>
                    `;
                });
            }
        })
        .catch(error => {
            container.innerHTML = `<p>無法載入新聞資料</p>`;
            console.error("Error fetching news:", error);
        });
}
