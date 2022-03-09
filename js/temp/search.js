import { removeData } from './locallive.js';

export const search = () => {
  const searchInput = document.querySelector('.search-input');
  const searchBtn = document.querySelector('.search-button');

  searchBtn.addEventListener('click', (e) => {
    e.preventDefault();
    const arr = [];
    const inputValue = searchInput.value.split(' ');

    (async function () {
      const res = await (
        await fetch(
          'https://stopwarkr.github.io/stopwar_frontend/crawlingData/kr_HistoryNewsData.json',
        )
      ).json();

      res.forEach((news) => {
        inputValue.forEach((keyword) => {
          if (news.title.indexOf(keyword) > -1) {
            arr.push(news);
          }
        });
      });

      const newsCardList = document.querySelector('.news-card-list');

      removeData();
      if (arr.length > 0) {
        arr.forEach((news) => {
          const newsCard = document.createElement('li');
          const article = document.createElement('article');
          const link = document.createElement('a');
          const imgBox = document.createElement('div');
          const img = document.createElement('img');
          const contentsBox = document.createElement('div');
          const title = document.createElement('strong');
          const content = document.createElement('p');
          const time = document.createElement('span');
          const source = document.createElement('span');

          article.classList.add('news-card');
          link.classList.add('news-card-link');
          imgBox.classList.add('card-img-frame');
          img.classList.add('card-img');
          contentsBox.classList.add('card-cont');
          title.classList.add('card-tit');
          content.classList.add('card-desc');
          time.classList.add('card-date');
          source.classList.add('card-source');

          newsCardList.appendChild(newsCard);
          newsCard.appendChild(article);
          article.appendChild(link);
          link.appendChild(imgBox);
          imgBox.appendChild(img);
          link.appendChild(contentsBox);
          contentsBox.appendChild(title).textContent = news.title;
          contentsBox.appendChild(content).textContent = `${news.content.slice(
            0,
            100,
          )}...`;
          contentsBox.appendChild(time).textContent = news.time;
          contentsBox.appendChild(source).textContent = news.source;
        });
      } else {
        const newsCardList = document.querySelector('.news-card-list');

        newsCardList.innerHTML = '검색 결과가 없습니다.';
      }
    })();
  });

  // 1. input
  // 2. 띄어쓰기 기준 배열
  // 3. 호출 시 title 기준
};
