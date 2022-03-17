// 크롤링 데이터가 없을 경우 예외 처리 고도화 필요

export const getAPI = async (url) => {
  try {
    const res = await fetch(url);
    const datas = await res.json();
    
    console.log(url + ' json파일이 있습니다.');
    
    // loading 화면 지우고 뉴스 기사들 보여주기
    document.querySelector(".news-card-list").style.display = 'block';
    document.querySelector(".button-more").style.display = 'block';
    document.querySelector(".loader").style.display = "none";
    return datas;
  } catch (error) {
    console.log(url + ' json파일을 불러오는데 실패했습니다.');
    console.log(error);
  }
};
