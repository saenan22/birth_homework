import requests
import geopandas as gpd
from io import BytesIO

# Google Drive 파일 ID로 다운로드 URL 생성
file_id = "164ypqgBqDYRChtcmTCI1daGQXZeNBw4d"
download_url = f"https://drive.google.com/uc?export=download&id={file_id}&confirm=t"

# 파일 다운로드
response = requests.get(download_url)
file_content = BytesIO(response.content)

# GeoPandas로 파일 읽기
gdf = gpd.read_file(file_content)

# 데이터 출력 (선택 사항)
print(gdf.head())
