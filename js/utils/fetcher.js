// 크롤링 데이터가 없을 경우 예외 처리 고도화 필요

export const getAPI = async (url) => {
  try {
    // loading 화면 표시 추가
    const loading = document.createElement('p');
    const newsCardList = document.querySelector('.news-card-list');
    loading.textContent = 'Loading...';
    newsCardList.appendChild(loading);

    const res = await fetch(url);
    const datas = await res.json();

    console.log(url + 'json파일이 있습니다.');

    newsCardList.removeChild(loading);
    return datas;
  } catch (error) {
    console.log(url + 'json파일이 없습니다.');
    console.log(error);
  }
};
