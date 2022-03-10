const getData = async function () {
  const res = await fetch('../crawlingData/kr_HistoryNewsData.json');
  const datas = await res.json();
  datas.forEach((data) => {
    drawData(data);
  });
};

getData();

const drawData = function (data) {
  const cardWrapper = document.querySelector('.news-card-list');

  const li = document.createElement('li');

  const article = document.createElement('article');
  article.setAttribute('class', 'news-card');

  const a = document.createElement('a');
  a.setAttribute('href', data.link);
  a.setAttribute('class', 'news-card-link');

  const thumbnailDiv = document.createElement('div');
  thumbnailDiv.setAttribute('class', 'card-img-frame');

  const thumbnailImg = document.createElement('img');
  thumbnailImg.setAttribute('class', 'card-img');
  thumbnailImg.setAttribute('alt', data.title);

  thumbnailDiv.appendChild(thumbnailImg);
  a.appendChild(thumbnailDiv);

  const contentDiv = document.createElement('div');
  contentDiv.setAttribute('class', 'card-cont');

  const titleH3 = document.createElement('h3');
  titleH3.setAttribute('class', 'card-tit');
  titleH3.textContent = data.title;

  const contentP = document.createElement('p');
  contentP.setAttribute('class', 'card-desc');
  contentP.textContent = data.content;

  const dateSpan = document.createElement('span');
  dateSpan.setAttribute('class', 'card-date');
  dateSpan.textContent = data.time;

  const sourceSpan = document.createElement('span');
  sourceSpan.setAttribute('class', 'card-source');
  sourceSpan.textContent = data.source;

  contentDiv.appendChild(titleH3);
  contentDiv.appendChild(contentP);
  contentDiv.appendChild(dateSpan);
  contentDiv.appendChild(sourceSpan);

  a.appendChild(contentDiv);
  article.appendChild(a);
  li.appendChild(article);

  cardWrapper.appendChild(li);
};
