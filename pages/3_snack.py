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

st.title('Snack')
st.markdown('<div class="cocktail-left">크래커 크림치즈</div><div class="cocktail-right">0.5</div>', unsafe_allow_html=True)
st.markdown('<div class="cocktail-left">나초 치즈</div><div class="cocktail-right">0.8</div>', unsafe_allow_html=True)
st.markdown('<div class="cocktail-left">크림브륄레</div><div class="cocktail-right">1.1</div>', unsafe_allow_html=True)
st.markdown('<div class="cocktail-left">하겐다즈 바나나</div><div class="cocktail-right">1.4</div>', unsafe_allow_html=True)
st.markdown('<div class="cocktail-left">부라타 치즈 토마토</div><div class="cocktail-right">1.4</div>', unsafe_allow_html=True)
st.markdown('<div class="cocktail-left">소세지 모짜렐라 3P</div><div class="cocktail-right">1.5</div>', unsafe_allow_html=True)
st.markdown('<div class="cocktail-left">소세지 모짜렐라 5P</div><div class="cocktail-right">1.7</div>', unsafe_allow_html=True)
st.markdown('<div class="cocktail-left">치즈 플레이트</div><div class="cocktail-right">2.0</div>', unsafe_allow_html=True)
st.markdown('<div class="cocktail-left">슬라이스 레몬</div><div class="cocktail-right">0.2</div>', unsafe_allow_html=True)
st.markdown('<div class="cocktail-left">슬라이스 라임</div><div class="cocktail-right">0.2</div>', unsafe_allow_html=True)
st.markdown('<div class="cocktail-left">올리브 10PS</div><div class="cocktail-right">0.5</div>', unsafe_allow_html=True)