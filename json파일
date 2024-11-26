import requests
import geopandas as gpd
import streamlit as st
from io import BytesIO

# Google Drive 파일 ID
file_id = "164ypqgBqDYRChtcmTCI1daGQXZeNBw4d"  # 사용자가 제공한 파일 ID

# Google Drive 공유 링크 다운로드 URL 생성
url = f"https://drive.google.com/uc?id={file_id}"

# 파일 다운로드
@st.cache_data  # Streamlit 캐시를 사용하여 효율적으로 다운로드
def download_file(url):
    response = requests.get(url)
    response.raise_for_status()  # 오류가 있을 경우 예외 발생
    return BytesIO(response.content)

# JSON 파일 읽기 및 GeoPandas로 변환
try:
    file_data = download_file(url)
    gdf = gpd.read_file(file_data)
    st.success("JSON 파일을 성공적으로 불러왔습니다!")
except Exception as e:
    st.error(f"파일을 불러오는 중 오류가 발생했습니다: {e}")

# GeoDataFrame 내용 확인
if 'gdf' in locals():
    st.write("GeoDataFrame 미리보기:")
    st.write(gdf.head())

    # 지도 시각화 (예시로 Folium 사용)
    import folium
    from streamlit_folium import st_folium

    m = folium.Map(location=[36.5, 127.5], zoom_start=7)  # 한국 중심 좌표
    for _, row in gdf.iterrows():
        folium.Marker(
            location=[row.geometry.centroid.y, row.geometry.centroid.x],
            popup=row['NAME'],  # 적절한 열 이름으로 변경
        ).add_to(m)

    st_folium(m, width=700, height=500)
