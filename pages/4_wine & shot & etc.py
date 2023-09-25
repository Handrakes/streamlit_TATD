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


#st.title("Wine")
#st.markdown('<div class ="category"> Red </div>', unsafe_allow_html = True)
#st.markdown('<div class ="category"> White </div>', unsafe_allow_html = True)
#st.markdown('<div class ="category"> Porto </div>', unsafe_allow_html = True)

st.title('Tequila')
st.markdown('<div class ="cocktail-right"> G &nbsp; B </div>', unsafe_allow_html = True)


st.title('Rum')
st.markdown('<div class ="cocktail-right"> G &nbsp; B </div>', unsafe_allow_html = True)

st.title('Vodka')
st.markdown('<div class ="cocktail-right"> G &nbsp; B </div>', unsafe_allow_html = True)

st.title('Gin')
st.markdown('<div class ="cocktail-right"> G &nbsp; B </div>', unsafe_allow_html = True)

st.title('Bomb')

st.title('Beer')

st.title('Liqueur')
st.markdown('<div class ="cocktail-right"> G &nbsp; B </div>', unsafe_allow_html = True)

