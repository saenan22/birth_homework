import json

# 큰 JSON 파일 열기
with open('C:/Users/김새난/data/BND_SIGUNGU_PG.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 나누어 저장할 파일 수 설정
chunk_size = 1000  # 예시로 1000개의 항목씩 나누기

# 데이터를 나누어 저장하기
for i in range(0, len(data), chunk_size):
    chunk = data[i:i+chunk_size]
    with open(f'chunk_{i//chunk_size + 1}.json', 'w', encoding='utf-8') as f:
        json.dump(chunk, f, ensure_ascii=False, indent=4)
