# 마크다운(MarkDown)


## 0. 특징
- 작성된 Markdown 문서는 다른 프로그램에 의해 변환되어 출력됨


## 1. 문법 및 활용

### 0) 마크다운 미리보기 켜는 법
1. 마크다운 파일 마우스 우측 클릭 (파일의 확장자는 **.md**)
2. Open Preview(미리 보기 열기) 클릭

### 1) Heading
- 문서의 단계별 제목으로 사용
- #의 개수에 따라 제목의 수준을 구별
+ 사용법 <br> 
\# 제목 <br> ## 제목 <br> ### 제목

### 2) 리스트
- 목록을 표시하기 위해 사용
- 순서가 있는 리스트와 순서가 없는 리스트 제공
+ 사용법 <br>
\- 내용 <br> + 내용 <br> * 내용

### 3) Code block & Inline code block
- 일반 텍스트와 달리 해당 프로그래밍 언어에 맞춰서 텍스트 스타일을 변환
- **<u>개발에서 마크다운을 사용하는 가장 큰 이유</u>**
- `(Backtick, *Esc밑, Tap위*) 사용
+ 사용법 <br> 
\``` <br> '코드' <br> ```
```
print('Hello World!')
```

### 4) 링크(link) & 이미지(image)
- 특정 주소를 사용해 다른 페이지로 이동하는 링크 혹은 이미지 출력
- **이미지의 너비와 높이는 마크 다운으로 조절할 수 없음(HTML 문법 필요)**
+ 사용법 <br>
\[링크](링크 주소) <br> 
\![이미지](이미지 주소)

### 5) 텍스트 관련 문법
- 굵게 :       ** 굵게 **
- 기울임 :     * 기울임 *
- 취소선 :     ~~ 취소선 ~~

### 6) 수평선
- 단락을 구분할 때 사용하는 수평선
- '-(hypen)'을 3개 이상 적으면 작동
+ 사용법 <br>
본문 <br> --- <br> 내용

## 2. [기본 가이드](https://www.markdownguide.org/basic-syntax/)
이 외 기타 문법은 가이드 문서를 활용하기

## 3. 마크다운 작성을 도와주는 마크다운 에디터
- Typora(유료, 무료버전은 구글에 검색) <br> https://typora.io

- MarkText(무료) <br> https://github.com/marktext/marktext#download-and-installation

- Markdown All in One (VSCode 확장프로그램) <br> https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one
