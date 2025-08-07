import pandas as pd
import streamlit as st
import altair as alt

# CSV 파일 불러오기 (Streamlit Cloud에 업로드 필요 또는 기본 경로 지정)
@st.cache_data
def load_data():
    return pd.read_csv("countriesMBTI_16types.csv")

df = load_data()

# 국가별 가장 높은 MBTI 유형 컬럼 생성
df["Top_MBType"] = df.drop(columns=["Country"]).idxmax(axis=1)

# 가장 많이 등장한 MBTI 유형 집계
top_counts = df["Top_MBType"].value_counts().reset_index()
top_counts.columns = ["MBTI", "Country Count"]

# 스트림릿 앱 UI
st.title("🌍 국가별 주요 MBTI 유형 분석")
st.markdown("각 국가에서 **가장 비율이 높은 MBTI 유형**을 집계한 결과입니다.")

# 표 출력
st.dataframe(top_counts)

# Altair 그래프 출력
chart = alt.Chart(top_counts).mark_bar().encode(
    x=alt.X("MBTI:N", sort="-y", title="최상위 MBTI 유형"),
    y=alt.Y("Country Count:Q", title="해당 MBTI가 가장 높은 국가 수"),
    tooltip=["MBTI", "Country Count"]
).properties(
    width=700,
    height=400,
    title="국가별 최상위 MBTI 유형 분포"
)

st.altair_chart(chart, use_container_width=True)
