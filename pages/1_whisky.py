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

st.title("Campbelbown")
st.markdown('<div class="left-corner">Springbank 10 스프링뱅크 10</div><div class="right-corner">1.9</div>', unsafe_allow_html=True)
st.markdown('<div class="left-corner">Springbank 15 스프링뱅크 15</div><div class="right-corner">2.7</div>', unsafe_allow_html=True)
st.markdown('<div class="left-corner">Longrow peated 롱로우 피티드</div><div class="right-corner">1.9</div>', unsafe_allow_html=True)
st.markdown('<div class="left-corner">kilkerran 12 킬커란 12</div><div class="right-corner">1.9</div>', unsafe_allow_html=True)