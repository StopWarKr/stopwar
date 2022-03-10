import { IMG_URL, BASE_URL, AllCategory } from '../common/constants.js';
import { getAPI } from '../utils/fetcher.js';

// img 태그 alret, src 넣어주기
// Card 렌더링 함수
const renderCard = (news, inputValue) => {

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
  if (news.image_path){
    img.setAttribute('src', IMG_URL + news.image_path);
  } else {
    img.setAttribute('src', './image/no-image.jpg');
  }
  img.setAttribute('alt', news.category);
  link.appendChild(contentsBox);
  link.setAttribute('href', news.link);
  link.setAttribute('target', '_blink');
  // contentsBox.appendChild(title).textContent = news.name;
  contentsBox.appendChild(time).textContent = news.date;
  contentsBox.appendChild(source).textContent = ' 출처 : ' + news.link.split('/')[2];
  
  // 기본 데이터 설정
  const newsName = news.name ? news.name : '제목없음';
  let output = newsName;
  
  // 검색어가 있을 경우
  if(inputValue && inputValue.length !== 0) {
    // 검색어 배열을 forEach로 돌려 keyword를 하나씩 가져온다.
    inputValue.forEach((keyword) => {
      // newsName keyword 시작 위치를 가져온다.
      const find = output.toLowerCase().indexOf(keyword.toLowerCase());
      const startIndex = find; // keyword 시작 위치
      const endIndex = find + (keyword.length); // keyword 끝나는 위치
      const addMarkElement = ' <mark>' + output.slice(startIndex, endIndex) + '</mark> ' // marker 추가한 keyword
      
      // 원래 있던 문장을 잘라 재결합 한다.
      output = [output.slice(0, startIndex), addMarkElement, output.slice(endIndex, newsName.length)].join('');
    });
  } 
  
  contentsBox.appendChild(title).innerHTML = output;
  contentsBox.appendChild(content).textContent = news.description;

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
      } else {
        console.log('데이터 없음!');
      }
    }
  } else {
    const url = BASE_URL + AllCategory[category];
    const datas = await getAPI(url);
    if (!!datas) {
      response.push(...datas);
    } else {
      console.log('데이터 없음!');
    }
  }

  removeElement();
  response.forEach((news) => {
    console.log(news);
    newsCardList.appendChild(renderCard(news));
  });
};

export { getNews, removeElement, renderCard };
