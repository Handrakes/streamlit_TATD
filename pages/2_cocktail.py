import io
import streamlit as st


st.markdown(
    """
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    """,
    unsafe_allow_html=True
)


st.markdown(
    """
    <style>
    .left-corner {
        text-align: left;
        float: left;
        font-size : 1.3em;
        margin-top: 1em;
    }
    <style>
    body {
    color: #fff;
    background-color: #4f8bf9;
    }
    .right-corner {
        text-align: right;
        float: right;
        font-size : 1.3em;
        margin-top : 1em;
    }
    .space{
        font-size : 0.8em;
        margin-top : 0em;
        margin-bottom : 0.5em;
        line-height : 0em;
    }
    .clearfix::after {
        content: "";
        display: table;
        clear: both;
    }
    .cocktail-left{
        text-align: left;
        float: left;
        font-size : 1.0em;
        margin-top: 0.5em;
    }
    .cocktail-right {
        text-align: right;
        float : right;
        font-size : 1.0em;
        margin-top : 0.5em;
    }
    .body{
        backrground-color : black;
    }
    .content{
        text-align : justify;
        font-size : 0.6em;
        margin-top : 0.5em;
    }
    .category{
        text-align : justify;
        font-size : 1.8em;
        font-weight : bold;
        margin-bottom : 1em;
        margin-top : 0.5em;
    }
    </style>
    """,
    unsafe_allow_html=True
)


st.title('SIGNATURE')
#st.markdown('</div></p>', unsafe_allow_html=True)
st.markdown('<div class="left-corner">가디언즈 오브 갤럭시</div><div class="right-corner">1.5</div>', unsafe_allow_html=True)
st.markdown('<div class="space">달콤판 파인애플과 코코넛 크림의 조합 2%</div>', unsafe_allow_html=True)
st.image('images/guardians.jpg')
#st.markdown('</div>', unsafe_allow_html=True)
st.markdown('<div class="left-corner">사랑과 전쟁</div><div class="right-corner">1.5</div>', unsafe_allow_html=True)
st.markdown('<div class="space">패션 후르츠, 리치맛 칵테일 15%</div>', unsafe_allow_html=True)
st.image('images/love_war.jpg')
#st.markdown('</div>', unsafe_alow_html=True)
st.markdown('<div class="left-corner">데 킬러</div><div class="right-corner">1.6</div>', unsafe_allow_html=True)
st.markdown('<div class="space">데킬라 베이스의 생라임과 허브 리큐르가 들어간 칵테일 25%</div>', unsafe_allow_html=True)
st.image('images/the_killer.jpg')
#st.markdown('</div>', unsafe_allow_html=True)
st.markdown('<div class="left-corner">드리머스</div><div class="right-corner">2.5</div>', unsafe_allow_html=True)
st.markdown('<div class="space">깔끔 + 오묘 + 체리 28%</div>', unsafe_allow_html=True)
st.image('images/lemon_drop.jpg')
#st.markdown('</div>', unsafe_alow_html=True)
st.markdown('<div class="left-corner">레몬드랍 * 6</div><div class="right-corner">2.5</div>', unsafe_allow_html=True)
st.markdown('<div class="space">달달하고 상큼한 원샷 칵테일 5%</div>', unsafe_allow_html=True)
st.image('images/lemon_drop.jpg')
#st.markdown('</div>', unsafe_alow_html=True)




st.title('Cocktails')
#1.0
st.markdown('<div class="cocktail-left">gin & tonic 진토닉 8%</div><div class="cocktail-right">1.0</div>', unsafe_allow_html=True)
st.markdown('<div class="cocktail-left">malibu orange 말리부 오렌지 5%<span class = "content"> 코코넛 오렌지 </span></div>', unsafe_allow_html=True)
st.markdown('<div class="cocktail-left">kahula milk 깔루아 밀크 4%</div>', unsafe_allow_html=True)
#1.1
st.markdown('<div class="cocktail-left">tequila sunrise 데킬라 선라이즈 8%</div><div class="cocktail-right">1.1</div>', unsafe_allow_html=True)
st.markdown('<div class="cocktail-left">valencia 발렌시아 8%<span class = "content"> 살구 오렌지 </span></div>', unsafe_allow_html=True)
st.markdown('<div class="cocktail-left">screwdriver 스크류 드라이버 8%<span class = "content"> 보드카 오렌지 </span></div>', unsafe_allow_html=True)
st.markdown('<div class="cocktail-left">cuba libre 쿠바리브레 7%<span class = "content"> 럼 라임 콜라</span></div>', unsafe_allow_html=True)
#1.3
st.markdown('<div class="cocktail-left">jack coke 잭콕 5%</div><div class = "cocktail-right">1.3</div>', unsafe_allow_html=True)
st.markdown('<div class="cocktail-left">daiquiri 다이키리 26% <span class = "content"> 럼, 라임, 설탕 조합의 숏드링크 </span></div>', unsafe_allow_html=True)
st.markdown('<div class="cocktail-left">gimlet 김렛 25%<span class = "content"> 진, 라임, 설탕 조합의 숏드링크</span></div>', unsafe_allow_html=True)
st.markdown('<div class="cocktail-left">tokyo iced tea 도쿄 아이스티 15%</div>', unsafe_allow_html=True)
st.markdown('<div class="cocktail-left">long island iced tea 롱아일랜드 아이스티 15%</div>', unsafe_allow_html=True)
st.markdown('<div class="cocktail-left">martini 마티니 38%<span class = "content"> 진 올리브 </span></div>', unsafe_allow_html=True)
st.markdown('<div class="cocktail-left">apple martini 애플 마티니 18%</div>', unsafe_allow_html=True)
st.markdown('<div class="cocktail-left">dark n stormy 다크 앤 스토미 10%<span class = "content"> 럼, 라임, 진저에일의 조합</span></div>', unsafe_allow_html=True)
st.markdown('<div class="cocktail-left">black russian 블랙 러시안 32%<span class = "content"> 보드카 커피 </span></div>', unsafe_allow_html=True)
st.markdown('<div class="cocktail-left">bailey''s milk 베일리스 밀크 4%<span class = "content"> 달콤 쵸콜렛 </span></div>', unsafe_allow_html=True)
st.markdown('<div class="cocktail-left">spumoni 스푸모니 4%<span class = "content"> 자몽 </span></div>', unsafe_allow_html=True)
st.markdown('<div class="cocktail-left">midori sour 미도리 사워 4%<span class = "content"> 멜론과 레몬이 들어간 칵테일</span></div>', unsafe_allow_html=True)
st.markdown('<div class="cocktail-left">china blue 차이나 블루 7%<span class = "content"> 리치 자몽</span></div>', unsafe_allow_html=True)
st.markdown('<div class="cocktail-left">cassis soda 카시스 소다 3% <span class = "content"> 블랙커런트 탄산 롱 드링크</span></div>', unsafe_allow_html=True)
st.markdown('<div class="cocktail-left">peach crush 피치 크러쉬 6%<span class = "content"> 복숭아 레몬 </span></div>', unsafe_allow_html=True)
#1.4
st.markdown('<div class="cocktail-left">hendrick''s tonic 핸드릭스 토닉 10%<span class = "content"> 오이 장미 진</span></div><div class="cocktail-right">1.4</div>', unsafe_allow_html=True)
st.markdown('<div class="cocktail-left">litchi coconut 리치 코코넛 10%</div>', unsafe_allow_html=True)
st.markdown('<div class="cocktail-left">god-mother 갓마더 36%<span class = "content">체리 보드카</span></div>', unsafe_allow_html=True)
st.markdown('<div class="cocktail-left">margarita 마가리타 32%<span class = "content"> 데킬라 라임 소금 </span></div>', unsafe_allow_html=True)
st.markdown('<div class="cocktail-left">mojito 모히또 8%</div>', unsafe_allow_html=True)
st.markdown('<div class="cocktail-left">pinacolada 피나콜라다 7%<span class = "content"> 럼 파인애플 코코넛 </span></div>', unsafe_allow_html=True)
st.markdown('<div class="cocktail-left">blue hawaii 블루하와이 8%<span class = "content"> 럼 파인애플 코코넛 </span></div>', unsafe_allow_html=True)
st.markdown('<div class="cocktail-left">june bug 준벅 7%<span class = "content"> 멜론 파인애플 </span></div>', unsafe_allow_html=True)
#1.5
st.markdown('<div class="cocktail-left">god-father 갓파더 36% <span class = "content"> 위스키 베이스 칵테일 </span></div><div class="cocktail-right">1.5</div>', unsafe_allow_html=True)
st.markdown('<div class="cocktail-left">negroni 네그로니 30%<span class = "content"> 진과 캄파리의 달콤 쌉사름함</span></div>', unsafe_allow_html=True)
st.markdown('<div class="cocktail-left">cosmopolitan 코스모폴리탄 20%</div>', unsafe_allow_html = True)
st.markdown('<div class="cocktail-left">moscow mule 모스코 뮬 10%<span class = "content"> 라임 진저비어 </span></div>', unsafe_allow_html=True)
#1.6
st.markdown('<div class="cocktail-left">electric lemonade 일렉트릭 레몬에이드 10%</div><div class="cocktail-right">1.6</div>', unsafe_allow_html=True)
st.markdown('<div class="cocktail-left">rusty nail 러스티네일 40%<span class = "content"> 꿀 리큐르와 위스키의 조합</span></div>', unsafe_allow_html=True)
st.markdown('<div class="cocktail-left">white russian 화이트 러시안 20%<span class = "content"> 커피 생크림 </span></div>', unsafe_allow_html=True)
st.markdown('<div class="cocktail-left">old fashioned 올드패션드 30%<span class = "content"> 버번 위스키 베이스 </span></div>', unsafe_allow_html=True)
#1.7
st.markdown('<div class="cocktail-left">faust 파우스트 45% <span class = "content">론디아즈 블랙커런트 </span></div><div class="cocktail-right">1.7</div>', unsafe_allow_html=True)
st.markdown('<div class="cocktail-left">jungle bird 정글버드 18%<span class = "content"> 다크럼 파인애플</span></div>', unsafe_allow_html=True)
st.markdown('<div class="cocktail-left">katarsis 카타르시스 50%<span class = "content">론디아즈 라임 </span></div>', unsafe_allow_html=True)
#1.8
st.markdown('<div class="cocktail-left">french connection 프렌치커넥션 36%</div><div class="cocktail-right">1.8</div>', unsafe_allow_html=True)
st.markdown('<div class="cocktail-left">side car 사이드 카 30% <span class = "content"> 꼬냑과 레몬의 조합 </span></div>', unsafe_allow_html=True)

##highball
st.markdown('<div class ="category"> Highball </div>', unsafe_allow_html = True)
st.markdown('<div class="cocktail-left">Suntory highball 산토리 하이볼</div><div class = "cocktail-right">1.2 </div>', unsafe_allow_html = True)
st.markdown('<div class="cocktail-left">Jameson highball 제임슨 하이볼</div><div class = "cocktail-right">1.2 </div>', unsafe_allow_html = True)
st.markdown('<div class="cocktail-left">Jimbeam highball 짐빔 하이볼</div><div class = "cocktail-right">1.2 </div>', unsafe_allow_html = True)
st.markdown('<div class="cocktail-left">Jonnie highball 조니 하이볼</div><div class = "cocktail-right">1.2 </div>', unsafe_allow_html = True)
st.markdown('<div class="cocktail-left">Fireball highball 파이어볼 하이볼 </div><div class = "cocktail-right">1.3 </div>', unsafe_allow_html = True)
st.markdown('<div class="cocktail-left">Monkey Shoulder highball 몽키숄더 하이볼</div><div class = "cocktail-right">1.6 </div>', unsafe_allow_html = True)
st.markdown('<div class="cocktail-left">Talisker highball 탈리스커 하이볼 </div><div class = "cocktail-right">1.8 </div>', unsafe_allow_html = True)
st.markdown('<div class="cocktail-left">Laphroaig highball 라프로익 하이볼 </div><div class = "cocktail-right">2.0 </div>', unsafe_allow_html = True)


st.markdown('<div class ="category"> Non-alcholic </div>', unsafe_allow_html = True)
st.markdown('<div class="cocktail-left">Coke 코카콜라 </div><div class="cocktail-right">0.4</div>', unsafe_allow_html=True)
st.markdown('<div class="cocktail-left">Coke-Zero 코카콜라 제로</div>', unsafe_allow_html=True)
st.markdown('<div class="cocktail-left">Sprite 스프라이트</div>', unsafe_allow_html=True)
st.markdown('<div class="cocktail-left">Ginger Ale 진저에일</div>', unsafe_allow_html=True)
st.markdown('<div class="cocktail-left">Tonic Water 토닉 워터</div>', unsafe_allow_html=True)
st.markdown('<div class="cocktail-left">Club Soda 클럽 소다</div>', unsafe_allow_html=True)
st.markdown('<div class="cocktail-left">Grapefruit Sparkling 자몽 스파클링 </div><div class="cocktail-right">0.9</div>', unsafe_allow_html=True)
st.markdown('<div class="cocktail-left">Cinderella 신데렐라 </div><div class="cocktail-right">1.0</div>', unsafe_allow_html=True)
st.markdown('<div class="cocktail-left">Lemon Squash 레몬 스쿼시</div><div class="cocktail-right">1.0</div>', unsafe_allow_html=True)
st.markdown('<div class="cocktail-left">Virgin Mojito 버진 모히또 </div><div class="cocktail-right">1.2</div>', unsafe_allow_html=True)