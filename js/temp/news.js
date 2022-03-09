const ALL = {
  역사: 'kr_HistoryNewsData.json',
  규제: 'kr_RegulationNewsData.json',
  '협상 진행 과정': 'kr_NegoNewsData.json',
  '지역 라이브 상황': 'kr_LocalNewsData.json',
  '피해 상황': 'kr_DamageNewsData.json',
  '교전 최신 상황': 'kr_BattleNewsData.json',
  후원: 'kr_SponsorNewsData.json',
};

// Card 렌더링 함수
const renderCard = (news) => {
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

  //  newsCardList.appendChild(newsCard);
  newsCard.appendChild(article);
  article.appendChild(link);
  link.appendChild(imgBox);
  imgBox.appendChild(img);
  link.appendChild(contentsBox);
  contentsBox.appendChild(title).textContent = news.title;
  contentsBox.appendChild(content).textContent = news.content;
  contentsBox.appendChild(time).textContent = news.time;
  contentsBox.appendChild(source).textContent = news.source;

  return newsCard;
};

// 카테고리 클릭 이벤트(이벤트 캡쳐링)
const buttonWrapper = document.querySelector('.news-category');

buttonWrapper.addEventListener('click', (e) => {
  const currentNode = e.target;
  if (currentNode.nodeName === 'BUTTON') {
    removeElement();
    getNews(currentNode.textContent);
  }
});

// 현재 렌더링된 뉴스 지우기
const removeElement = () => {
  const newsCardList = document.querySelector('.news-card-list');

  while (newsCardList.hasChildNodes()) {
    newsCardList.removeChild(newsCardList.firstChild);
  }
};

const getNews = async (category) => {
  const newsCardList = document.querySelector('.news-card-list');
  const response = [];

  console.log(category);

  if (category === 'ALL') {
    for (ele in ALL) {
      const res = await fetch(
        `https://stopwarkr.github.io/stopwar_frontend/crawlingData/${ALL[ele]}`,
      );
      const data = await res.json();
      response.push(...data);

      console.log('in all');
    }
  } else {
    const res = await fetch(
      `https://stopwarkr.github.io/stopwar_frontend/crawlingData/${ALL[category]}`,
    );
    const data = await res.json();
    response.push(...data);
    console.log('in other');
  }

  removeElement();
  response.forEach((news) => {
    newsCardList.appendChild(renderCard(news));
    console.log('card render');
  });
};
