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
        margin-bottom : 0.5em;
        margin-top : 0.5em;
    }
    .wine_category{
        text-align : justify;
        font-size : 1.2em;
        font-weight : lighter;
        margin-bottom : 0.5em;
        margin-top : 0em;
    }
    </style>
    """,
    unsafe_allow_html=True
)


#st.title("Wine")
#st.markdown('<div class ="category"> Red </div>', unsafe_allow_html = True)
#st.markdown('<div class ="category"> White </div>', unsafe_allow_html = True)
#st.markdown('<div class ="category"> Porto </div>', unsafe_allow_html = True)

st.title('Tequila')
st.markdown('<div class ="cocktail-right"> G &nbsp; B </div>', unsafe_allow_html = True)
st.markdown('<div class="cocktail-left">Tequila SHOT / SHOT*6</div><div class="cocktail-right">0.5 / 2.5</div>', unsafe_allow_html=True)
st.markdown('<div class="cocktail-left">Jose Cuervo</div><div class="cocktail-right">0.9 / 15.0</div>', unsafe_allow_html=True)
st.markdown('<div class="cocktail-left">Cenote Reposado</div><div class="cocktail-right">1.6 / 26.0</div>', unsafe_allow_html=True)
st.markdown('<div class="cocktail-left">Patron Silver</div><div class="cocktail-right">1.8 / 30.0</div>', unsafe_allow_html=True)

st.title('Rum')
st.markdown('<div class ="cocktail-right"> G &nbsp; B </div>', unsafe_allow_html = True)
st.markdown('<div class="cocktail-left">Barcadi</div><div class="cocktail-right">0.7 / 10.0</div>', unsafe_allow_html=True)
st.markdown('<div class="cocktail-left">Havana Club</div><div class="cocktail-right">0.7 / 10.0</div>', unsafe_allow_html=True)
st.markdown('<div class="cocktail-left">Diplomatico</div><div class="cocktail-right">1.6 / 26.0</div>', unsafe_allow_html=True)

st.title('Vodka')
st.markdown('<div class ="cocktail-right"> G &nbsp; B </div>', unsafe_allow_html = True)
st.markdown('<div class="cocktail-left">Absoult</div><div class="cocktail-right">0.7 / 10.0</div>', unsafe_allow_html=True)
st.markdown('<div class="cocktail-left">Sminoff Red</div><div class="cocktail-right">0.7 / 10.0</div>', unsafe_allow_html=True)
st.markdown('<div class="cocktail-left">Grey Goose</div><div class="cocktail-right">1.1 / 17.0</div>', unsafe_allow_html=True)

st.title('Gin')
st.markdown('<div class ="cocktail-right"> G &nbsp; B </div>', unsafe_allow_html = True)
st.markdown('<div class="cocktail-left">Bombay Sapphire</div><div class="cocktail-right">0.8 / 12.0</div>', unsafe_allow_html=True)
st.markdown('<div class="cocktail-left">Gordon&rsquo;s</div><div class="cocktail-right">0.7 / 10.0</div>', unsafe_allow_html=True)
st.markdown('<div class="cocktail-left">Hendric&rsquo;s</div><div class="cocktail-right">1.0 / 16.0</div>', unsafe_allow_html=True)
st.markdown('<div class="cocktail-left">Four Pillars</div><div class="cocktail-right">1.3 / 18.0</div>', unsafe_allow_html=True)
st.markdown('<div class="cocktail-left">Tanqueray</div><div class="cocktail-right">0.8 / 12.0</div>', unsafe_allow_html=True)
st.markdown('<div class="cocktail-left">Tanqueray No.10</div><div class="cocktail-right">0.9 / 15.0</div>', unsafe_allow_html=True)
st.markdown('<div class="cocktail-left">Martin Miller</div><div class="cocktail-right">1.4 / -</div>', unsafe_allow_html=True)
st.markdown('<div class="cocktail-left">Monkey 47</div><div class="cocktail-right">1.7 / 22.0</div>', unsafe_allow_html=True)


st.title('Bomb')
st.markdown('<div class="cocktail-left">JAGER-BOMB</div><div class="cocktail-right">1.0</div>', unsafe_allow_html=True)
st.markdown('<div class="cocktail-left">FIRE-BOM</div><div class="cocktail-right">1.0</div>', unsafe_allow_html=True)
st.markdown('<div class="cocktail-left">AGWA-BOMB</div><div class="cocktail-right">1.1</div>', unsafe_allow_html=True)


st.title('Beer')
st.markdown('<div class="cocktail-left">Budweiser</div><div class="cocktail-right">0.8</div>', unsafe_allow_html=True)
st.markdown('<div class="cocktail-left">Red Stripe</div><div class="cocktail-right">1.0</div>', unsafe_allow_html=True)
st.markdown('<div class="cocktail-left">Heineken</div><div class="cocktail-right">1.0</div>', unsafe_allow_html=True)
st.markdown('<div class="cocktail-left">Guinness</div><div class="cocktail-right">1.0</div>', unsafe_allow_html=True)




st.title('Wine')
st.markdown('<div class = "category"> RED </div>', unsafe_allow_html = True)
st.markdown('<div class = "wine_category"> &nbsp;&nbsp;<i>by the glass</i> </div>', unsafe_allow_html = True)
st.markdown('<div class="cocktail-left">2019chile 카베르네 소비뇽</div><div class="cocktail-right">0.8</div>', unsafe_allow_html=True)

st.markdown('<div class = "wine_category"> &nbsp;&nbsp;<i>bottle</i> </div>', unsafe_allow_html = True)
st.markdown('<div class="cocktail-left">2020France 카베르네-쉬라즈</div><div class="cocktail-right">5.9</div>', unsafe_allow_html=True)
st.markdown('<div class="cocktail-left">2018France 비뉴롱 부르고뉴 피노누아</div><div class="cocktail-right">7.9</div>', unsafe_allow_html=True)
#st.markdown('<div class="cocktail-left">2020 프랑스 피노누아</div><div class="cocktail-right">7.9</div>', unsafe_allow_html=True)

st.markdown('<div class = "category"> WHITE </div>', unsafe_allow_html = True)
st.markdown('<div class = "wine_category"> &nbsp;&nbsp;<i>only bottle</i> </div>', unsafe_allow_html = True)
st.markdown('<div class="cocktail-left">2020France 레어빈야드 사르도네</div><div class="cocktail-right">7.9</div>', unsafe_allow_html=True)
st.markdown('<div class="cocktail-left">2018France 비뉴롱 부르고뉴 사르도네</div><div class="cocktail-right">7.9</div>', unsafe_allow_html=True)

st.markdown('<div class = "category"> PORTO </div>', unsafe_allow_html = True)
st.markdown('<div class = "wine_category"> &nbsp;&nbsp;<i>by the glass</i> </div>', unsafe_allow_html = True)
st.markdown('<div class="cocktail-left">루비</div><div class="cocktail-right">1.0</div>', unsafe_allow_html=True)

st.markdown('<div class = "wine_category"> &nbsp;&nbsp;<i>bottle</i> </div>', unsafe_allow_html = True)
st.markdown('<div class="cocktail-left">루비</div><div class="cocktail-right">5.9</div>', unsafe_allow_html=True)
st.markdown('<div class="cocktail-left">10Y</div><div class="cocktail-right">14.0</div>', unsafe_allow_html=True)

