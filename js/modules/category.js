import { IMG_URL, BASE_URL, AllCategory } from '../common/constants.js';
import { getAPI } from '../utils/fetcher.js';

// img 태그 alret, src 넣어주기
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

  newsCard.appendChild(article);
  article.appendChild(link);
  link.appendChild(imgBox);
  imgBox.appendChild(img);
  img.setAttribute('src', IMG_URL + news.image_path);
  img.setAttribute('alt', news.category);
  link.appendChild(contentsBox);
  link.setAttribute('href', news.link);
  link.setAttribute('target', '_blink');
  contentsBox.appendChild(title).textContent = news.name;
  contentsBox.appendChild(content).textContent = news.description;
  contentsBox.appendChild(time).textContent = news.date;
  contentsBox.appendChild(source).textContent = '출처';

  return newsCard;
};

// 현재 렌더링된 뉴스 지우기
const removeElement = () => {
  const newsCardList = document.querySelector('.news-card-list');

  while (newsCardList.hasChildNodes()) {
    newsCardList.removeChild(newsCardList.firstChild);
  }
};

// 뉴스 불러오기
const getNews = async (category) => {
  const newsCardList = document.querySelector('.news-card-list');
  const response = [];

  if (category === 'ALL') {
    for (let ele in AllCategory) {
      console.log(ele);
      const url = BASE_URL + AllCategory[ele];
      const datas = await getAPI(url);
      if (!!datas) {
        response.push(...datas);
      }
    }
  } else {
    const url = BASE_URL + AllCategory[category];
    const datas = await getAPI(url);
    response.push(...datas);
  }

  removeElement();
  response.forEach((news) => {
    newsCardList.appendChild(renderCard(news));
  });
};

export { getNews, removeElement, renderCard };
