export const removeData = () => {
  const newsCardList = document.querySelector('.news-card-list');

  while (newsCardList.hasChildNodes()) {
    newsCardList.removeChild(newsCardList.firstChild);
  }
};

export const getLocalLive = async () => {
  const newsCardList = document.querySelector('.news-card-list');

  const res = await (
    await fetch('../crawlingData/kr_HistoryNewsData.json')
  ).json();

  res.forEach((news) => {
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
};
