import streamlit as st

st.set_page_config(
    page_title="Ben's Menu",
    page_icon="./images/kimchi_fried.jpg"
)

st.markdown("""  

<style>

h1 {
color : black;
}
.data-testid=stExpanderDetails div{
    display:flex;
    justify-content:center;
    font-size:16px;

}
.stText st-emotion-cache-y4bq5x.ewgb6651 div.st-emotion-cache-mptgkq.exotz4b0 {
   display:flex;
    justify-content:center;
    font-size:26px;
}
# [data-testid="stExpanderToggleIcon"]{
# visibility: hidden;
# }
# .streamlit-expanderHeader{
# pointer-events: none;
# }
# [data-testid="StyledFullScreenButton"]{
# visibility: hidden;
# }
</style>

""",unsafe_allow_html=True )



st.title("Ben's Menu")
# st.text(" bens menu gallery")
# st.subheader(" 요리 Gallery")
# st.markdown(" bens **menu** gallery")

cook_type ={

}

bensmenus =[
    {
    "name": "김치 볶음밥",
    "type": "한식",
    "image_url":".\static\images\kimchi_fried.jpg"
},
{
    "name": "파스타",
    "type": "양식",
    "image_url":".\static\images\menu_12.jpg"
},
{
    "name": "열무국수",
    "type": "한식",
    "image_url":".\static\images\menu_14.jpg"
},
{
    "name": "제육볶음",
    "type": "한식",
    "image_url":".\static\images\menu_10.jpg"
},
{
    "name": "파스타",
    "type": "양식",
    "image_url":".\static\images\menu_13.jpg"
},
{
    "name": "스파게티",
    "type": "양식",
    "image_url":".\static\images\menu_15.jpg"
},
{
    "name": "칼국수",
    "type": "한식",
    "image_url":".\static\images\Knif-cut_noodle.jpg"
},
{
    "name": "우동",
    "type": "중식",
    "image_url":".\static\images\menu_03.jpg"
},
{
    "name": "계란말이",
    "type": "일식",
    "image_url":".\static\images\menu_04.jpg"
},
{
    "name": "짜장면",
    "type": "중식",
    "image_url":".\static\images\menu_05.jpg"
},
{
    "name": "파스타",
    "type": "양식",
    "image_url":".\static\images\menu_06.jpg"
},
{
    "name": "냉콩국수",
    "type": "한식",
    "image_url":".\static\images\menu_07.jpg"
},
{
    "name": "수박국수",
    "type": "한식",
    "image_url":".\static\images\menu_08.jpg"
},
{
    "name": "파스타",
    "type": "양식",
    "image_url":".\static\images\menu_11.jpg"
},

{
    "name": "김치 볶음밥",
    "type": "한식",
    "image_url":".\static\images\Kimchi_Fried_Rice .jpg"
},
]


for i in range(0,len(bensmenus),3):  #0 부타 길이까지 간격 3
    row_bensmenus=bensmenus[i:i+3]   #0,1,2  , 3,4,5
    cols = st.columns(3)
    for j in range(len(row_bensmenus)):
        with cols[j]:
            bensmenu = row_bensmenus[j]
            with st.expander(label=f"**{i+j+1}.{bensmenu['name']}**",expanded=True):
                st.image(bensmenu["image_url"])
                st.text(bensmenu['type'])
                st.write('''요리재료:...''')

