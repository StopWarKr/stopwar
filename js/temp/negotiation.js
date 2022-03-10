const negoBtn = document.querySelector('.nego-btn');
const newsBox = document.querySelector('.news-card-list');

export const getNegotiation = async () => {
  const res = await (
    await fetch('../crawlingData/kr_HistoryNewsData.json')
  ).json();

  res.forEach((el) => {
    const title = el.title;
    const content = el.content;
    const link = el.link;
    const time = el.time;
    const source = el.source;

    newsBox.innerHTML += `
      <li>
        <article class="news-card">
           <a href="${link}" class="news-card-link">
             <div class="card-img-frame">
               <img src="" alt="" class="card-img" />
             </div>
             <div class="card-cont">
               <h3 class="card-tit">
                 ${title}
               </h3>
               <p class="card-desc">
                 ${content}
               </p>
               <span class="card-date">${time}</span>
               <span class="card-source">${source}</span>
             </div>
           </a>
         </article>
      </li>`;
  });
};

// getNegotiation()
