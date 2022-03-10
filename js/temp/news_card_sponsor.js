// 후원 카테고리 렌더링 JS
const newsCard = document.querySelector('main .news-card-list');

async function getSponsorData() {
  const data = await (
    await fetch('/crawlingData/kr_HistoryNewsData.json')
  ).json();
  console.log(data);

  for (let i = 0; i < data.length; i++) {
    const title = data[i].title;
    const content = data[i].content;
    const link = data[i].link;
    const time = data[i].time;
    const source = data[i].source;
    if (i === data.length - 1 && data[i].category !== 'sponsor') {
      alert('해당 카테고리에 뉴스가 없습니다');
    } else if (data[i].category === 'sponsor') {
      newsCard.innerHTML += `
        <li>
        <article class="news-card">
          <a href="${link}" class="news-card-link">
            <div class="card-img-frame">
              <img src="" alt="" class="card-img" />
            </div>
            <div class="card-cont">
              <h3 class="card-tit">
                ${title}
              </h3>
              <p class="card-desc">
                ${content}
              </p>
              <span class="card-date">${time}</span>
              <span class="card-source">${source}</span>
            </div>
          </a>
        </article>
      </li>`;
    }
  }
}

getSponsorData();
