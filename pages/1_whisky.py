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
    .w-left{
        text-align: left;
        float: left;
        font-size : 0.9em;
        margin-top: 0.5em;
    }
    .w-right{
        text-align: right;
        float : right;
        font-size : 0.9em;
        margin-top : 0.5em;
    }
    .left-corner {
        text-align: left;
        float: left;
        font-size : 1.3em;
        margin-top: 1em;
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
        font-size : 1.1em;
        margin-top: 0.5em;
    }
    .cocktail-right {
        text-align: right;
        float : right;
        font-size : 1.1em;
        margin-top : 0.5em;
    }
    .body{
        backrground-color : black;
    }
    .content{
        text-align : justify;
        font-size : 0.7em;
        margin-top : 0.5em;
    }
    .category{
        text-align : justify;
        font-size : 1.8em;
        font-weight : bold;
        margin-bottom : 0em;
        margin-top : 0.5em;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("WHISKY")
st.markdown('<div class = "category"> Highland </div>', unsafe_allow_html = True)
st.markdown('<div class ="cocktail-right"> G &nbsp; B </div>', unsafe_allow_html = True)
st.markdown('<div class="w-left">Dalwhinnie 15Y 달위니 15Y</div><div class = "w-right"> 1.8 / - </div>', unsafe_allow_html = True)
st.markdown('<div class="w-left">Dalmore 12Y 달모어 12Y</div><div class = "w-right"> 1.8 / 32.0 </div>', unsafe_allow_html = True)
st.markdown('<div class="w-left">Dalmore 12Y sherry cask 달모어 12Y 셰리 캐스크</div><div class = "w-right"> 2.2 / - </div>', unsafe_allow_html = True)
st.markdown('<div class="w-left">Dalmore 15Y 달모어 15Y </div><div class = "w-right"> 2.6 / 41.0 </div>', unsafe_allow_html = True)
st.markdown('<div class="w-left">Glenmorangie 10Y 글렌모렌지 10Y</div><div class = "w-right"> 1.4 / 23.0 </div>', unsafe_allow_html = True)
st.markdown('<div class="w-left">Glenmorangie lasanta 12Y 글렌모렌지 라산타 12Y</div><div class = "w-right"> 1.6 / 26.0 </div>', unsafe_allow_html = True)
st.markdown('<div class="w-left">Glenmorangie quintaruban 14Y 글렌모렌지 퀸타루반 14Y</div><div class = "w-right"> 1.8 / 32.0 </div>', unsafe_allow_html = True)
st.markdown('<div class="w-left">Glenmorangie necta d''or 글렌모렌지 넥타도르</div><div class = "w-right"> 2.0 / 34.0 </div>', unsafe_allow_html = True)
st.markdown('<div class="w-left">Glenmorangie 18Y 글렌모렌지 18Y</div><div class = "w-right"> 2.7 / - </div>', unsafe_allow_html = True)
st.markdown('<div class="w-left">Glenmorangie Signet 글렌모렌지 시그넷</div><div class = "w-right"> 3.6 / - </div>', unsafe_allow_html = True)
st.markdown('<div class="w-left">Glengoyne 12Y 글렌고인 12Y</div><div class = "w-right"> 1.7 / - </div>', unsafe_allow_html = True)
st.markdown('<div class="w-left">Glengoyne 18Y 글렌고인 18Y</div><div class = "w-right"> 3.7 / -</div>', unsafe_allow_html = True)
st.markdown('<div class="w-left">Glendronach 12Y 글렌드로낙 12Y</div><div class = "w-right"> 1.6 / 28.0 </div>', unsafe_allow_html = True)
st.markdown('<div class="w-left">Glendronach Port wood 글렌드로낙 포트우드</div><div class = "w-right"> 1.9 / 34.0 </div>', unsafe_allow_html = True)
st.markdown('<div class="w-left">Oban 14Y 오반 14Y</div><div class = "w-right"> 2.0 / 32.0 </div>', unsafe_allow_html = True)


#st.title("Speyside")
st.markdown('<div class = "category"> Speyside </div>', unsafe_allow_html = True)
st.markdown('<div class ="cocktail-right"> G &nbsp; B </div>', unsafe_allow_html = True)
st.markdown('<div class="w-left"> Aberlour A''Bunadh 아벨라워 아부나흐</div><div class = "w-right"> 2.8 / - </div>', unsafe_allow_html = True)
st.markdown('<div class="w-left"> Benromach 10Y 벤로막 10Y</div><div class = "w-right"> 1.5 / - </div>', unsafe_allow_html = True)
st.markdown('<div class="w-left"> Benromach 15Y 벤로막 15Y</div><div class = "w-right"> 2.5 / - </div>', unsafe_allow_html = True)
st.markdown('<div class="w-left"> Glenlivet 12Y 글렌리벳 12Y</div><div class = "w-right"> 1.5 / 23.0 </div>', unsafe_allow_html = True)
st.markdown('<div class="w-left"> Glenlivet 15Y 글렌리벳 15Y</div><div class = "w-right"> 1.8 / 29.0 </div>', unsafe_allow_html = True)
st.markdown('<div class="w-left"> Glenlivet 18Y 글렌리벳 18Y</div><div class = "w-right"> 2.7 / 38.0 </div>', unsafe_allow_html = True)
st.markdown('<div class="w-left"> Glenfiddich 12Y 글렌피딕 12Y</div><div class = "w-right"> 1.5 / 26.0 </div>', unsafe_allow_html = True)
st.markdown('<div class="w-left"> Glenfiddich 15Y 글렌피딕 15Y</div><div class = "w-right"> 1.8 / 32.0 </div>', unsafe_allow_html = True)
st.markdown('<div class="w-left"> Glenfiddich 18Y 글렌피딕 18Y</div><div class = "w-right"> 2.5 / 40.0 </div>', unsafe_allow_html = True)
st.markdown('<div class="w-left"> Glenallachie 10CS 글렌알라키 10CS 배치 8</div><div class = "w-right"> 2.2 / - </div>', unsafe_allow_html = True)
st.markdown('<div class="w-left"> Glenallachie 12Y 글렌알라키 12Y</div><div class = "w-right"> 1.7 / 29.0 </div>', unsafe_allow_html = True)
st.markdown('<div class="w-left"> Glenallachie 15Y 글렌알라키 15Y</div><div class = "w-right"> 2.4 / 41.0 </div>', unsafe_allow_html = True)
st.markdown('<div class="w-left"> Glenallachie Cuvee cask 글렌알라키 뀌베 캐스크 피니시</div><div class = "w-right"> 2.2 / - </div>', unsafe_allow_html = True)
st.markdown('<div class="w-left"> Glenallachie 2007 single cask 글렌알라키 2007 싱글 캐스크</div><div class = "w-right"> 4.0 / - </div>', unsafe_allow_html = True)
st.markdown('<div class="w-left"> Macallan 12Y double 맥켈란 12Y 더블</div><div class = "w-right"> 1.6 / 28.0 </div>', unsafe_allow_html = True)
st.markdown('<div class="w-left"> Macallan 12Y sherry 맥켈란 12Y 셰리</div><div class = "w-right"> 1.7 / 29.0 </div>', unsafe_allow_html = True)
st.markdown('<div class="w-left"> Macallan 12Y sherry 맥켈란 18Y 셰리</div><div class = "w-right"> 4.5 / - </div>', unsafe_allow_html = True)
st.markdown('<div class="w-left"> Macallan night on earth 맥켈란 나이트 온 어스</div><div class = "w-right"> 2.8 / - </div>', unsafe_allow_html = True)
st.markdown('<div class="w-left"> Glengrant 15Y 글렌그란트 15Y</div><div class = "w-right"> 1.8 / - </div>', unsafe_allow_html = True)
st.markdown('<div class="w-left"> Balvenie 12Y double wood 발베니 12Y 더블우드</div><div class = "w-right"> 1.7 / 29.0 </div>', unsafe_allow_html = True)
st.markdown('<div class="w-left"> Balvenie 14Y caribbean cask 발베니 14Y 캐러비안 캐스크</div><div class = "w-right"> 2.2 / 38.0 </div>', unsafe_allow_html = True)
st.markdown('<div class="w-left"> Balvenie 14Y week of peat 발베니 14Y 위크 오브 피트</div><div class = "w-right"> 2.3 / - </div>', unsafe_allow_html = True)
st.markdown('<div class="w-left"> Balvenie 15Y single barrel 발베니 15Y 싱글베럴</div><div class = "w-right"> 2.7 / - </div>', unsafe_allow_html = True)
#st.markdown('<div class="w-left"> </div><div class = "w-right"> / </div>', unsafe_allow_html = True)
#st.markdown('<div class="w-left"> </div><div class = "w-right"> / </div>', unsafe_allow_html = True)
#st.markdown('<div class="w-left"> </div><div class = "w-right"> / </div>', unsafe_allow_html = True)




#st.title("Campbeltown")
st.markdown('<div class = "category"> Campbeltown </div>', unsafe_allow_html = True)
st.markdown('<div class ="cocktail-right"> G &nbsp; B </div>', unsafe_allow_html = True)
st.markdown('<div class="w-left">Springbank 10 스프링뱅크 10</div><div class="w-right">1.9 / - </div>', unsafe_allow_html=True)
st.markdown('<div class="w-left">Springbank 15 스프링뱅크 15</div><div class="w-right">2.7 / - </div>', unsafe_allow_html=True)
st.markdown('<div class="w-left">Longrow peated 롱로우 피티드</div><div class="w-right">1.9 / - </div>', unsafe_allow_html=True)
st.markdown('<div class="w-left">Kilkerran 12 킬커란 12</div><div class="w-right">1.8 / - </div>', unsafe_allow_html=True)
st.markdown('<div class="w-left">Kilkerran 16 킬커란 16</div><div class="w-right">2.5 / - </div>', unsafe_allow_html=True)
st.markdown('<div class="w-left">Kilkerran heavily peated 킬커란 헤빌리 피티드</div><div class="w-right">2.0 / - </div>', unsafe_allow_html=True)
st.markdown('<div class="w-left">Kilkerran 8CS Bourbon cask 킬커란 8CS 버번</div><div class="w-right">2.2 / - </div>', unsafe_allow_html=True)
st.markdown('<div class="w-left">Kilkerran 8CS Sherry cask 킬커란 8CS 셰리</div><div class="w-right">2.2 / - </div>', unsafe_allow_html=True)
st.markdown('<div class="w-left">Glenscotia double cask 글렌스코시아 더블 캐스크</div><div class="w-right">1.8 / - </div>', unsafe_allow_html=True)
st.markdown('<div class="w-left">Glenscotia 10Y 글렌스코시아 10Y</div><div class="w-right">1.9 / - </div>', unsafe_allow_html=True)
st.markdown('<div class="w-left">Glenscotia 15Y 글렌스코시아 15Y</div><div class="w-right">2.2 / - </div>', unsafe_allow_html=True)

#st.title("Islay")
st.markdown('<div class = "category"> Islay </div>', unsafe_allow_html = True)
st.markdown('<div class ="cocktail-right"> G &nbsp; B </div>', unsafe_allow_html = True)
st.markdown('<div class="w-left">Bowmore 12Y 보모어 12Y</div><div class="w-right"> 1.5 / 26.0 </div>', unsafe_allow_html=True)
st.markdown('<div class="w-left">Bowmore 15Y 보모어 15Y</div><div class="w-right"> 2.1 / - </div>', unsafe_allow_html=True)
st.markdown('<div class="w-left">Bowmore 18Y 보모어 18Y</div><div class="w-right"> 2.8 / - </div>', unsafe_allow_html=True)
st.markdown('<div class="w-left">Ardbeg 10Y 아드벡 10Y</div><div class="w-right"> 1.7 / 27.0 </div>', unsafe_allow_html=True)
st.markdown('<div class="w-left">Ardbeg An oa 아드벡 언 오</div><div class="w-right"> 1.9 / 32.0 </div>', unsafe_allow_html=True)
st.markdown('<div class="w-left">Ardbeg uigeadail 아드벡 우거다일</div><div class="w-right"> 2.2 / 36.0 </div>', unsafe_allow_html=True)
st.markdown('<div class="w-left">Ardbeg corryvreckan 아드벡 코리브레칸</div><div class="w-right"> 2.6 / 42.0 </div>', unsafe_allow_html=True)
st.markdown('<div class="w-left">Laphroaig 10Y 라프로익 10Y </div><div class="w-right"> 1.6 / 27.0 </div>', unsafe_allow_html=True)
st.markdown('<div class="w-left">Laphroaig quarter cask 라프로익 쿼터캐스크</div><div class="w-right"> 1.7 / 29.0 </div>', unsafe_allow_html=True)
st.markdown('<div class="w-left">Bunnahabhain 12Y 부나하벤 12Y</div><div class="w-right"> 1.7 / 29.0 </div>', unsafe_allow_html=True)
st.markdown('<div class="w-left">Lagavulin 8Y 라가불린 8Y</div><div class="w-right"> 1.8 / 32.0 </div>', unsafe_allow_html=True)
st.markdown('<div class="w-left">Lagavulin 16Y 라가불린 16Y</div><div class="w-right"> 2.5 / - </div>', unsafe_allow_html=True)
st.markdown('<div class="w-left">Kilchoman machir bay 킬호만 마키어 베이</div><div class="w-right"> 1.7 / 27.0 </div>', unsafe_allow_html=True)
st.markdown('<div class="w-left">Kilchoman sanig 킬호만 사닉</div><div class="w-right"> 1.9 / 34.0 </div>', unsafe_allow_html=True)
st.markdown('<div class="w-left">Kilchoman machir bay CS 킬호만 마키어 베이 CS</div><div class="w-right"> 2.2 / - </div>', unsafe_allow_html=True)
st.markdown('<div class="w-left">Bruichladdich classic ladie 브룩라디 클래식 라디</div><div class="w-right"> 1.8 / - </div>', unsafe_allow_html=True)

#st.title("Islands")
st.markdown('<div class = "category"> Islands </div>', unsafe_allow_html = True)
st.markdown('<div class ="cocktail-right"> G &nbsp; B </div>', unsafe_allow_html = True)
st.markdown('<div class="w-left">Talisker 10Y 탈리스커 10Y</div><div class = "w-right"> 1.4 / 22.0 </div>', unsafe_allow_html = True)
st.markdown('<div class="w-left">Highland Park 12Y 하이랜드 파크 12Y</div><div class = "w-right"> 1.5 / - </div>', unsafe_allow_html = True)
st.markdown('<div class="w-left">Arran 10Y 아란 10Y </div><div class = "w-right"> 1.6 / - </div>', unsafe_allow_html = True)
st.markdown('<div class="w-left">Arran Sherry cask 아란 셰리 캐스크</div><div class = "w-right"> 2.2 / - </div>', unsafe_allow_html = True)



#st.title("Blended")
st.markdown('<div class = "category"> Blended </div>', unsafe_allow_html = True)
st.markdown('<div class ="cocktail-right"> G &nbsp; B </div>', unsafe_allow_html = True)
st.markdown('<div class="w-left">Jonnie Walker Red 조니워커 레드</div><div class = "w-right"> 0.9 / 12.0 </div>', unsafe_allow_html = True)
st.markdown('<div class="w-left">Jonnie Walker Black 조니워커 블랙 </div><div class = "w-right"> 1.2 / 17.0 </div>', unsafe_allow_html = True)
st.markdown('<div class="w-left">Jonnie Walker Green 조니워커 그린 </div><div class = "w-right"> 1.4 / 24.0 </div>', unsafe_allow_html = True)
st.markdown('<div class="w-left">Jonnie Walker Blue 조니워커 블루 </div><div class = "w-right"> 3.0 / 55.0 </div>', unsafe_allow_html = True)
st.markdown('<div class="w-left">Monkey Shoulder 몽키 숄더</div><div class = "w-right"> 1.1 / 17.0 </div>', unsafe_allow_html = True)
st.markdown('<div class="w-left">Rumreek 10Y CS 럼릭 10Y CS</div><div class = "w-right"> 2.2 / 37.0 </div>', unsafe_allow_html = True)
st.markdown('<div class="w-left">Royal Salute 21Y 로얄 살루트 21Y </div><div class = "w-right"> 3.2 / - </div>', unsafe_allow_html = True)
#st.markdown('<div class="w-left"> </div><div class = "w-right"> / </div>', unsafe_allow_html = True)
#st.markdown('<div class="w-left"> </div><div class = "w-right"> / </div>', unsafe_allow_html = True)
#st.markdown('<div class="w-left"> </div><div class = "w-right"> / </div>', unsafe_allow_html = True)


st.markdown('<div class = "category"> American </div>', unsafe_allow_html = True)
st.markdown('<div class ="cocktail-right"> G &nbsp; B </div>', unsafe_allow_html = True)
st.markdown('<div class="w-left">Jim Beam 짐 빔</div><div class = "w-right"> 0.8 / 11.0 </div>', unsafe_allow_html = True)
st.markdown('<div class="w-left">Jack Daniel''s black 잭다니엘 블랙 </div><div class = "w-right"> 1.2 / 17.0</div>', unsafe_allow_html = True)
st.markdown('<div class="w-left">Jack Daniel''s Honey 잭다니엘 허니 </div><div class = "w-right"> 1.2 / 17.0</div>', unsafe_allow_html = True)
st.markdown('<div class="w-left">Buffalo Trace 버팔로 트레이스</div><div class = "w-right"> 1.1 / 17.0</div>', unsafe_allow_html = True)
st.markdown('<div class="w-left">Knob Creek 납크릭</div><div class = "w-right"> 1.3 / -</div>', unsafe_allow_html = True)
st.markdown('<div class="w-left">Whistle Pig 10Y 휘슬피그 10Y </div><div class = "w-right"> 1.5 / -</div>', unsafe_allow_html = True)
st.markdown('<div class="w-left">Micter''s Small batch 믹터스 스몰 배치</div><div class = "w-right"> 1.7 / -</div>', unsafe_allow_html = True)
st.markdown('<div class="w-left">Micter''s Single barrel Rye 믹터스 싱글베럴 라이</div><div class = "w-right"> 1.7 / -</div>', unsafe_allow_html = True)
st.markdown('<div class="w-left">Woodford Reserve 우드포드 리저브</div><div class = "w-right"> 1.7/ 27.0</div>', unsafe_allow_html = True)
st.markdown('<div class="w-left">Wild Turkey 8Y 와일드 터키 8Y</div><div class = "w-right"> 1.2 / 19.0</div>', unsafe_allow_html = True)
st.markdown('<div class="w-left">Wild Turkey Rarebreed 와일드 터키 레어브리드</div><div class = "w-right"> 1.6 / 25.0</div>', unsafe_allow_html = True)
st.markdown('<div class="w-left">Yellow Rose American 옐로우 로즈 아메리칸</div><div class = "w-right"> 1.1 / 17.0 </div>', unsafe_allow_html = True)
st.markdown('<div class="w-left">Yellow Rose Harris County 옐로우 로즈 해리스 카운티</div><div class = "w-right"> 1.3 / 21.0</div>', unsafe_allow_html = True)
st.markdown('<div class="w-left">Yellow Rose Rye 옐로우 로즈 라이</div><div class = "w-right"> 1.4 / 24.0 </div>', unsafe_allow_html = True)
st.markdown('<div class="w-left">Redemptions Bourbon 리뎀션 버번</div><div class = "w-right"> 1.3 / 21.0 </div>', unsafe_allow_html = True)
st.markdown('<div class="w-left">Redemptions Rye 리뎀션 라이</div><div class = "w-right"> 1.3 / 21.0 </div>', unsafe_allow_html = True)
st.markdown('<div class="w-left">James E.Pepper bourbon 제임스 E.페퍼 버번</div><div class = "w-right"> 1.5 / 23.0</div>', unsafe_allow_html = True)
st.markdown('<div class="w-left">James E.Pepper Rye 제임스 E.페퍼 라이</div><div class = "w-right"> 1.5 / 23.0</div>', unsafe_allow_html = True)
st.markdown('<div class="w-left">Basil Hayden 바질 헤이든</div><div class = "w-right"> 1.4/ 23.0</div>', unsafe_allow_html = True)
st.markdown('<div class="w-left">Russell''s 10Y 러셀 10Y</div><div class = "w-right"> 1.5 / -</div>', unsafe_allow_html = True)
st.markdown('<div class="w-left">Russell''s Single barrel 러셀 싱글베럴</div><div class = "w-right"> 1.7 / -</div>', unsafe_allow_html = True)
st.markdown('<div class="w-left">Blanton''s Single barrel 블랑톤 싱글베럴</div><div class = "w-right"> 2.8 / -</div>', unsafe_allow_html = True)
st.markdown('<div class="w-left">Rowan''s Creek 로완스 크릭</div><div class = "w-right"> 1.7 / -</div>', unsafe_allow_html = True)
st.markdown('<div class="w-left">Noah''s Mill 노아스 밀</div><div class = "w-right"> 2.2 / 39.0</div>', unsafe_allow_html = True)
st.markdown('<div class="w-left">Elijah Craig small batch 엘라이저 크레이그 스몰배치</div><div class = "w-right"> 1.1 / -</div>', unsafe_allow_html = True)
st.markdown('<div class="w-left">1792 small batch 1792 스몰배치 </div><div class = "w-right"> 1.3 / -</div>', unsafe_allow_html = True)
st.markdown('<div class="w-left">Four Roses small batch 포 로지스 스몰배치</div><div class = "w-right"> 1.3 / - </div>', unsafe_allow_html = True)
st.markdown('<div class="w-left">Four Roses single barrel 포 로지스 싱글베럴</div><div class = "w-right"> 1.6 / -</div>', unsafe_allow_html = True)
#st.markdown('<div class="w-left"> </div><div class = "w-right"> / </div>', unsafe_allow_html = True)
#st.markdown('<div class="w-left"> </div><div class = "w-right"> / </div>', unsafe_allow_html = True)
#st.markdown('<div class="w-left"> </div><div class = "w-right"> / </div>', unsafe_allow_html = True)
#st.markdown('<div class="w-left"> </div><div class = "w-right"> / </div>', unsafe_allow_html = True)
#st.markdown('<div class="w-left"> </div><div class = "w-right"> / </div>', unsafe_allow_html = True)

st.markdown('<div class = "category"> Irish </div>', unsafe_allow_html = True)
st.markdown('<div class ="cocktail-right"> G &nbsp; B </div>', unsafe_allow_html = True)
st.markdown('<div class="w-left">Jameson 제임슨 </div><div class = "w-right"> 0.9 / 12.0 </div>', unsafe_allow_html = True)

st.markdown('<div class = "category"> Japanese </div>', unsafe_allow_html = True)
st.markdown('<div class ="cocktail-right"> G &nbsp; B </div>', unsafe_allow_html = True)
st.markdown('<div class="w-left">Suntory Kakubin 가쿠빈 </div><div class = "w-right"> 1.0 / - </div>', unsafe_allow_html = True)
st.markdown('<div class="w-left">Yamazaki 12Y 야마자키 12Y </div><div class = "w-right"> 3.2 / - </div>', unsafe_allow_html = True)

st.markdown('<div class = "category"> Taiwanese </div>', unsafe_allow_html = True)
st.markdown('<div class ="cocktail-right"> G &nbsp; B </div>', unsafe_allow_html = True)
st.markdown('<div class="w-left">Kavalan Classic 카발란 클래식</div><div class = "w-right"> 2.3 / - </div>', unsafe_allow_html = True)

st.markdown('<div class = "category"> Indian </div>', unsafe_allow_html = True)
st.markdown('<div class ="cocktail-right"> G &nbsp; B </div>', unsafe_allow_html = True)
st.markdown('<div class="w-left">Amrut Fusion 암룻 퓨전</div><div class = "w-right"> 1.9 / - </div>', unsafe_allow_html = True)


st.markdown('<div class = "category"> Independent Bottle </div>', unsafe_allow_html = True)
st.markdown('<div class ="cocktail-right"> G &nbsp; B </div>', unsafe_allow_html = True)
st.markdown('<div class="w-left">Ochard House 오차드 하우스 </div><div class = "w-right"> 1.7 / 25.0 </div>', unsafe_allow_html = True)
st.markdown('<div class="w-left">Hedonism 헤도니즘 </div><div class = "w-right"> 2.5 / 42.0 </div>', unsafe_allow_html = True)

st.markdown('<div class = "category"> Cognac </div>', unsafe_allow_html = True)
st.markdown('<div class ="cocktail-right"> G &nbsp; B </div>', unsafe_allow_html = True)
st.markdown('<div class="w-left">Remmy Martin V.S.O.P 레미마틴 VSOP</div><div class = "w-right"> 1.5 / 24.0</div>', unsafe_allow_html = True)
st.markdown('<div class="w-left">Hennessy V.S.O.P 헤네시 VSOP</div><div class = "w-right"> 1.5 / 24.0</div>', unsafe_allow_html = True)