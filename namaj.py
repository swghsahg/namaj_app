import streamlit as st
from streamlit_autorefresh import st_autorefresh
from datetime import datetime

st_autorefresh(interval=60000, key = "time_checker")

N_t = "7:00"
current_t = datetime.now().strftime("%H:%M")

if current_t == N_t:
    st.toast("Sokol amol korsos to ----- from Zarin", icon = "?")

option = st.radio("select koro",["Aytul Kursi","bismillah-alif lam mim-(7)", "mukh dos muktir dua", "soytan palanor dua","duscinta muktir dua"])

if st.button("namaj somoy Narsingdi"):
    st.text("https://salat.habibur.com/districts/narsingdi")
if st.button("namaj somoy Chattogram"):
    st.text("https://salat.habibur.com/world/bd/1205733")
if st.button("Kajol deeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee"):
    st.text("mukhdos duai zothesto naa")

if option == "Aytul Kursi":
    st.image(
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQlFOjW6UGAomiRZMW3mp-hwg5sv2Q311JA9_dxMSY_sutGAVtDf-RY5bXt&s=10",
        use_container_width = True
        )

elif option == "duscinta muktir dua":
    st.image(
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTFV9y1IsNZ7fgYAiiJ2dc2ed868VUY3Eiodj1KjPUNGXsu6PbSoNTBQVA&s=10", 
        use_container_width = True
        )
    st.image(
        "https://authentic-dua.com/wp-content/uploads/2015/08/allaahumma-innee-aoothu-bika-minal-hammi-walhazani.jpg",
        use_container_width = True

        )
elif option == "soytan palanor dua":
    st.image(
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ8Jdrx8I9evsLUR3K5XoHZIoULcYZoe6YWzU7lbJl58wUg_K4xeyeFLKc&s=10",
        use_container_width = True
    )

elif option == "mukh dos muktir dua":
    st.image(
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRDFoLlOPngs86v3Woa2d7FGeKkobnsaylpndPqY28iAM1Hg05se61723te&s=10",
        use_container_width = True
    )

elif option == "bismillah-alif lam mim-(7)":
    st.image(
        "https://as1.ftcdn.net/jpg/18/61/14/34/1000_F_1861143433_W3NEpQrej1fhS9lZztWaRtuzGMVo3RRH.jpg",
        use_container_width = True
    )

