import { getNews, initialRenderCard, renderTen } from './modules/category.js';
import { search } from './modules/search.js';

let data = await getNews('all-btn');

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
    data = await getNews(currentNode.className.split(' ')[1]);
  }
});

const searchBtn = document.querySelector('.search-button');

searchBtn.addEventListener('click', search);

// 모달창
const supportModal = document.querySelector('.modal-background');
// 메인화면 영역
const mainElement = document.querySelector('.main');

const openBtn = document.querySelector('.sponsor-info-btn');
export const openModal = () => {
  // modal open 시 뒷 배경 스크롤 및 커서 클릭 막기
  mainElement.style['pointer-events'] = 'none';
  mainElement.style['position'] = 'fixed';

  supportModal.style.display = 'flex';
};

const closeBtn = document.querySelector('.btn-close');
export const closeModal = () => {
  // modal close 시 뒷 배경 스크롤 및 커서 클릭 원래대로 돌려놓기
  supportModal.style.display = 'none';
  mainElement.style['position'] = 'relative';

  setTimeout(() => {
    mainElement.style['pointer-events'] = 'auto';
  }, 100);
};

openBtn.addEventListener('click', openModal);
closeBtn.addEventListener('click', closeModal);

closeModal();

// [이예슬] modal background click -> modal close
document.addEventListener('mousemove', (e) => {
  const element = document.elementFromPoint(e.pageX, e.pageY);

  const modal = document.querySelector('.modal-background');
  const isModalFlex = modal.style.display;

  // error 방지
  if (!isModalFlex || !element) return false;

  const isBg = element.className == 'modal-background';
  if (isBg) closeModal();
});

// 더보기 클릭 시 10가 카드 추가 렌더링
const btnMore = document.querySelector('.button-more');

btnMore.addEventListener('click', (e) => {
  renderTen(data);
});

// 구글 번역 API 스타일링 => css로 할 경우 가끔씩 안되는 문제, 시간차 때문인가..
/*
const translateBox = document.querySelector('#google_translate_element');
const translateIcon = document.querySelector('.goog-te-gadget-icon');
const translateBoxStyle = document.querySelector('.goog-te-gadget-simple');
const translateKorea = document.querySelector('.goog-te-menu-value');

translateBox.style.overflow = 'hidden';
translateBoxStyle.style.padding = '4px';
translateBoxStyle.style.width = '75px';

translateKorea.textContent = '한국어';

translateIcon.style.backgroundImage = 'url("./image/icon-lang.svg")';
translateIcon.style.backgroundPosition = 'center';
translateIcon.style.backgroundRepeat = 'no-repeat';
*/
