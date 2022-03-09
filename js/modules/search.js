import { renderCard, removeElement } from '../modules/category.js';
import { getAPI } from '../utils/fetcher.js';
import { AllCategory, BASE_URL } from '../common/constants.js';

export const search = async (event) => {
  event.preventDefault();
  const searchInput = document.querySelector('.search-input');
  const filteredArr = [];
  const AllNews = [];
  const inputValue = searchInput.value.split(' ');

  for (let ele in AllCategory) {
    const url = BASE_URL + AllCategory[ele];
    const data = await getAPI(url);
    if (!!data) {
      AllNews.push(...data);
    }
  }

  const newsCardList = document.querySelector('.news-card-list');

  // 검사
  AllNews.forEach((news) => {
    inputValue.forEach((keyword) => {
      if (news.hasOwnProperty('title')) {
      } else if (news.name.toLowerCase().indexOf(keyword.toLowerCase()) > -1) {
        filteredArr.push(news);
      }
    });

    removeElement();
    if (filteredArr.length > 0) {
      filteredArr.forEach((news) => {
        newsCardList.appendChild(renderCard(news));
      });
    } else {
      newsCardList.innerHTML = '검색 결과가 없습니다.';
    }
  });
};
