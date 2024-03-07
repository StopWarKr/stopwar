# 🖐StopWar
- 우크라이나 전쟁관련 소식 제공 비영리 서비스
- 서비스 링크 : www.stopwar.co.kr

## 목적
- 플랫폼 별 **다양한 전쟁 관련 뉴스** 를 항목별 아카이빙하여 전쟁 상황을 한 눈에 파악
- 우크라이나에 **금전적으로 후원할 수 있는 수단**을 아카이빙하여 후원에 대한 접근성 향상
 
## 멤버
- PM
    - [이호준](https://github.com/paullabkorea)
- 기획
    - 현재국, [이한나](https://github.com/yeeehannah)
- 디자인
    - [강혜진](https://github.com/dreamfulbud), [조미진](https://github.com/mmcho122), [장서령](https://github.com/beurmuz)
- 프론트엔드
    - 파트별 PL: [강혜진](https://github.com/dreamfulbud), [김창현](https://github.com/kimtothechang), [이예슬](https://github.com/Leemainsw), [윤수영](https://github.com/ddooyn)
    - 권혁, [장서령](https://github.com/beurmuz), [지다혜](https://github.com/daaahailey), [박지윤](https://github.com/junep16), [윤우상](https://github.com/yws1502), [심채영](https://github.com/chaengs), [조미진](https://github.com/mmcho122), [조혜미](https://github.com/JoHyemi), [김경민](https://github.com/View-Studio), [김유경](https://github.com/kimyou1102), [김초연](https://github.com/vnfdusdl), [최성이](https://github.com/choisung2), [이수빈](https://github.com/Stephanie9349), [양아름](https://github.com/areumsheep), [이지아](https://github.com/zeroto99), [정기수](https://github.com/Jeong-ki), [유현세](https://github.com/Mangopapa1), [주혜린](https://github.com/HyeRrin), [정시찬](https://github.com/sichan1301), [주현호](https://github.com/hyjoo1226), [박유진](https://github.com/yoojin-park19), [김상돈](https://github.com/Sangdon1029), [강지승](https://github.com/jiseung-kang), [조민성](https://github.com/kkumtree)
- 크롤링
    - 이호준, [윤수영](https://github.com/ddooyn), [오가빈](https://github.com/gabiiiiiiii), [장성원](https://github.com/jjangsungwon), [김미경](https://github.com/rmfosem613), [진윤재](https://github.com/jinyun3075), [윤우상](https://github.com/yws1502), [장병길](https://github.com/krgil), [현진호](https://github.com/neverlish), [유순상](https://github.com/yooss2006), [박준](https://github.com/Penguin-God), [조찬민](https://github.com/jochanmin), [Hakeoung Hannah Lee](https://github.com/HakeoungLee), [이지영](https://github.com/gygy7151), [장익준](https://github.com/jangjo123)

## 폴더 트리
* crawler : 뉴스 크롤링
* crawlingData : 크롤링된 데이터셋
* css, font, html, image, js : 정적 파일

## 데이터 구조
```javascript
[
    {
        "name": "Opinion | Will Sanctions on Russia Help Ukraine?",
        "description": "The sanctions are raising the price of Russia's belligerence and can \ndegrade its capacity to pursue this campaign of terror, or others,...",
        "link": "https://www.nytimes.com/2022/03/11/opinion/russia-sanctions.html",
        "date": "2일 전",
        "image_path": "",
        "catagory": "교전 최신 상황"
    } ...
]
``` 
* forktest