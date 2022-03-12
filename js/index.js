import { getNews, initialRenderCard, renderTen } from './modules/category.js';
import { search } from './modules/search.js';

let data = await getNews('ALL');

// 최초 ALL 카테고리 렌더링
// window.onload = getNews('ALL');

// 카테고리 클릭 이벤트(이벤트 캡쳐링)
const buttonWrapper = document.querySelector('.news-category');

buttonWrapper.addEventListener('click', async (e) => {
  const btnNodes = [...buttonWrapper.children];

  btnNodes.forEach((node) => {
    node.classList.remove('on');
  });

  const currentNode = e.target;
  if (currentNode.nodeName === 'BUTTON') {
    currentNode.parentElement.classList.add('on');
    initialRenderCard();
    btnMore.style.display = 'block';
    data = await getNews(currentNode.textContent);
  }
});

const searchBtn = document.querySelector('.search-button');

searchBtn.addEventListener('click', search);

// 모달창
const supportModal = document.querySelector('.modal-background');

const openBtn = document.querySelector('.sponsor-info-btn');
export const openModal = () => {
  supportModal.style.display = 'flex';
};

const closeBtn = document.querySelector('.btn-close');
export const closeModal = () => {
  supportModal.style.display = 'none';
};

// openBtn.addEventListener('click', openModal);
// closeBtn.addEventListener('click', closeModal);

// // [이예슬] modal background click -> modal close
// document.addEventListener('mousemove', (e) => {
//   const element = document.elementFromPoint(e.pageX, e.pageY);
//   const isBg = element.className == 'modal-background';

//   if (isBg) closeBtn();
// });

// 더보기 클릭 시 10가 카드 추가 렌더링
const btnMore = document.querySelector('.button-more');

btnMore.addEventListener('click', (e) => {
  renderTen(data);
});
