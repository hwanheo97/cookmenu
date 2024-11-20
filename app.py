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

# import os

# current_dir = os.getcwd()
# st.write(f"Current working directory: {current_dir}")

bensmenus =[
    {
    "name": "김치 볶음밥",
    "type": "한식",
    "image_url":"./images/kimchi_fried.jpg",
    "recipe":"재료:마늘,파,신김치,찬밥,고추장,계란"
},
{
    "name": "파스타",
    "type": "양식",
    "image_url":"./images/menu_12.jpg",
    "recipe":"재료:마늘,양파,해산물,토마토소스,파스타면,식용유"
},
{
    "name": "열무국수",
    "type": "한식",
    "image_url":"./images/menu_14.jpg",
    "recipe":"재료:열무육수,열무,면사리,오이,깨"
},
{
    "name": "제육볶음",
    "type": "한식",
    "image_url":"./images/menu_10.jpg",
    "recipe":"마늘,파,양파,돼지고기,고추장"
},
{
    "name": "파스타",
    "type": "양식",
    "image_url":"./images/menu_13.jpg",
    "recipe":"재료:마늘,양파,새우,오징어,토마토소스,파스타면,식용유"
},
{
    "name": "스파게티",
    "type": "양식",
    "image_url":"./images/menu_15.jpg",
    "recipe":"재료:마늘,양파,피마으토마토소스,스파게티면 ,식용유"
},
{
    "name": "칼국수",
    "type": "한식",
    "image_url":"./images/Knif-cut_noodle.jpg",
    "recipe":"재료:마늘,양파,청양고추,육수,칼국수면"
},
{
    "name": "우동",
    "type": "중식",
    "image_url":"./images/menu_03.jpg",
    "recipe":"재료:마늘,양파,새우,오징어,육수,면,게란"
},
{
    "name": "계란말이",
    "type": "일식",
    "image_url":"./images/menu_04.jpg",
    "recipe":"재료: 파,당근,계란"
},
{
    "name": "짜장면",
    "type": "중식",
    "image_url":"./images/menu_05.jpg",
    "recipe":"춘장,감자,양파,돼지고기,오이,꺠"
},
{
    "name": "파스타",
    "type": "양식",
    "image_url":"./images/menu_06.jpg",
    "recipe":"재료:마늘,양파,새우,오징어,토마토소스,파스타,식용유"
},
{
    "name": "냉콩국수",
    "type": "한식",
    "image_url":"./images/menu_07.jpg",
    "recipe":"육수,김치,김,면,깨"
},
{
    "name": "수박국수",
    "type": "한식",
    "image_url":"./images/menu_08.jpg",
    "recipe":"수박,블루베리,오인,면사리,깨"
},
{
    "name": "파스타",
    "type": "양식",
    "image_url":"./images/menu_11.jpg",
    "recipe":"재료:마늘,양파,새우,오징어,토마토소스,파스타,식용유"
},

{
    "name": "김치 볶음밥",
    "type": "한식",
    "image_url":"./images/Kimchi_Fried_Rice .jpg",
    "recipe":"재료:마늘,파,신김치,찬밥,고추장,계란"
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
                st.markdown(bensmenu['recipe'])

