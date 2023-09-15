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
    </style>
    """,
    unsafe_allow_html=True
)


st.title('SIGNATURE')
st.markdown('<div class="left-corner">레몬드랍 * 6</div><div class="right-corner">2.5</div>', unsafe_allow_html=True)
st.markdown('<div class="space">달달하고 상큼한 원샷 칵테일 5%</div>', unsafe_allow_html=True)
st.image('images/manhattan.jpg')
#st.markdown('</div></p>', unsafe_allow_html=True)
st.markdown('<div class="left-corner">가디언즈 오브 갤럭시</div><div class="right-corner">1.5</div>', unsafe_allow_html=True)
st.markdown('<div class="space">피나콜라다 베이스의 밀키스 맛 칵테일 (3%)</div>', unsafe_allow_html=True)
st.image('images/guardians.jpg')
#st.markdown('</div>', unsafe_allow_html=True)
st.markdown('<div class="left-corner">데 킬러</div><div class="right-corner">1.6</div>', unsafe_allow_html=True)
st.markdown('<div class="space">데킬라 베이스의 생라임과 허브가 들어간 칵테일 24%</div>', unsafe_allow_html=True)
st.image('images/jungle-bird.jpg')
#st.markdown('</div>', unsafe_allow_html=True)
st.markdown('<div class="left-corner">PASSAT</div><div class="right-corner">1.5</div>', unsafe_allow_html=True)
st.markdown('<div class="space">패션 후르츠, 리치맛 칵테일 10%</div>', unsafe_allow_html=True)
st.image('images/passats.jpg')

st.title('Cocktails')
st.markdown('<div class="cocktail-left">gin & tonic 진토닉 8%</div><div class="cocktail-right">1.0</div>', unsafe_allow_html=True)
st.markdown('<div class="cocktail-left">malibu orange 말리부 오렌지 5%</div>', unsafe_allow_html=True)
st.markdown('<div class="cocktail-left">kahula milk 깔루아 밀크 4%</div>', unsafe_allow_html=True)
st.markdown('<div class="cocktail-left">tequila sunrise 데킬라 선라이즈 8%</div><div class="cocktail-right">1.1</div>', unsafe_allow_html=True)
st.markdown('<div class="cocktail-left">valencia 발렌시아 8%<span class = "content">    살구와 오렌지가 들어간 숏 칵테일</span></div>', unsafe_allow_html=True)
st.markdown('<div class="cocktail-left">screwdriver 스크류 드라이버 8%</div>', unsafe_allow_html=True)
st.markdown('<div class="cocktail-left">cuba libre 쿠바리브레 7%</div>', unsafe_allow_html=True)
st.markdown('<div class="cocktail-left">dark n stormy 다크 앤 스토미 10%</div><div class = "cocktail-right">1.3</div>', unsafe_allow_html=True)
st.markdown('<div class="cocktail-left">daiquiri 다이키리 26%</div>', unsafe_allow_html=True)
st.markdown('<div class="cocktail-left">gimlet 김렛 25%</div>', unsafe_allow_html=True)
st.markdown('<div class="cocktail-left">tokyo iced tea 도쿄 아이스티 15%</div>', unsafe_allow_html=True)
st.markdown('<div class="cocktail-left">long island iced tea 롱아일랜드 아이스티 15%</div>', unsafe_allow_html=True)
st.markdown('<div class="cocktail-left">martini 마티니 38%</div>', unsafe_allow_html=True)
st.markdown('<div class="cocktail-left">apple martini 애플 마티니 18%</div>', unsafe_allow_html=True)
st.markdown('<div class="cocktail-left">midori sour 미도리 사워 4%</div>', unsafe_allow_html=True)
st.markdown('<div class="cocktail-left">black russian 블랙 러시안 32%</div>', unsafe_allow_html=True)
st.markdown('<div class="cocktail-left">bailey''s milk 베일리스 밀크 4%</div>', unsafe_allow_html=True)
st.markdown('<div class="cocktail-left">spumoni 스푸모니 4%</div>', unsafe_allow_html=True)
st.markdown('<div class="cocktail-left">jack coke 잭콕 5%</div>', unsafe_allow_html=True)
st.markdown('<div class="cocktail-left">china blue 차이나 블루 7%</div>', unsafe_allow_html=True)
st.markdown('<div class="cocktail-left">cassis soda 카시스 소다 3%</div>', unsafe_allow_html=True)
st.markdown('<div class="cocktail-left">peach crush 피치 크러쉬 6%</div>', unsafe_allow_html=True)
st.markdown('<div class="cocktail-left">hendrick''s tonic 핸드릭스 토닉 10%</div><div class="cocktail-right">1.4</div>', unsafe_allow_html=True)
st.markdown('<div class="cocktail-left">litchi coconut 리치 코코넛 10%</div>', unsafe_allow_html=True)
st.markdown('<div class="cocktail-left">god-mother 갓마더 36%</div>', unsafe_allow_html=True)
st.markdown('<div class="cocktail-left">margarita 마가리타 32%</div>', unsafe_allow_html=True)
st.markdown('<div class="cocktail-left">mojito 모히또 8%</div>', unsafe_allow_html=True)
st.markdown('<div class="cocktail-left">pinacolada 피나콜라다 7%</div>', unsafe_allow_html=True)
st.markdown('<div class="cocktail-left">blue hawaii 블루하와이 8%</div>', unsafe_allow_html=True)
st.markdown('<div class="cocktail-left">june bug 준벅 7%</div>', unsafe_allow_html=True)
st.markdown('<div class="cocktail-left">god-father 갓파더 36%</div><div class="cocktail-right">1.5</div>', unsafe_allow_html=True)
st.markdown('<div class="cocktail-left">negroni 네그로니 30%</div>', unsafe_allow_html=True)
st.markdown('<div class="cocktail-left">electric lemonade 일렉트릭 레몬에이드 10%</div><div class="cocktail-right">1.6</div>', unsafe_allow_html=True)
st.markdown('<div class="cocktail-left">moscow mule 모스코 뮬 10%</div>', unsafe_allow_html=True)
st.markdown('<div class="cocktail-left">white russian 화이트 러시안 20%</div>', unsafe_allow_html=True)
st.markdown('<div class="cocktail-left">katarsis 카타르시스 50%</div>', unsafe_allow_html=True)
st.markdown('<div class="cocktail-left">old fashioned 올드패션드 30%</div>', unsafe_allow_html=True)
st.markdown('<div class="cocktail-left">rusty nail 러스티네일 40%</div><div class="cocktail-right">1.7</div>', unsafe_allow_html=True)
st.markdown('<div class="cocktail-left">jungle bird 정글버드 18%</div>', unsafe_allow_html=True)
st.markdown('<div class="cocktail-left">faust 파우스트 45%</div>', unsafe_allow_html=True)
st.markdown('<div class="cocktail-left">french connection 프렌치커넥션 36%</div><div class="cocktail-right">1.8</div>', unsafe_allow_html=True)
st.markdown('<div class="cocktail-left">side car 사이드 카 30%</div>', unsafe_allow_html=True)