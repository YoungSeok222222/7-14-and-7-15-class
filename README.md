

## GUI (graphic user interface)

- 그래픽을 통해 사용자와 컴퓨터가 상호 작용하는 방식	

### CLI (command Line interface)

- 명령어를 통해 사용자와 컴퓨터가 상호 작요하는 방식



### Why CLI 

- GUI는 CLI에 비해 사용하기 쉽지만 단계가 많고 컴퓨터의 성능을 더 많이 소모
- 수 많은 서버/ 개발 시스템이 CLI를 통한 조작 환경을 제공



#### CLI 기본적인 명령어



- touch 파일 생성
- mkdir(소문자로): 새 폴더를 생성
- rm 파일 삭제 / -r 폴더 삭제 가능  / rmdir   디렉토리 삭제(파일 삭제)
- ls(엘에스)  현재 작업중인 디렉토리의 폴더/파일 목록을 보여주는 명령어
- cd 현재 작업 중인 디렉토리를 변경하는 명령어
- start,open 
- \ 백슬래시는 공백이 아닌 문자로 인식(띄어쓰기 되어있는 곳에)

__Tab을 누르면 자동완성 된다. 방향키 위를 통해 이전 명령어 사용 가능__

맨앞은 home / 맨 뒤는 end

---------



### 절대 경로 vs 상대 경로



### 절대 경로  pwd

- 루트 디렉토리부터 목표지점까지 거치는 모든 경로를 전부 작성한 것
- 윈도우 바탕 화면의 절대 경로 -C:/Users/ssafy/Desktop

### 상대 경로

- 현재 작업하고 있는 디렉토리를 기준으로 계산된 상대적 위치를 작성한것
- 현재 작업하고 있는 디렉토리가 C:/Users일 때
- 윈도우 바탕 화면으로의 상대 경로는  ssafy/Desktop

- ./:현재 작업하고 있는 폴더		../:현재 작업하고 있는 폴더의 부모 폴더

# Markdown 기본 문법

- 텍스트 기반의 가벼운 마크업(markup\) 언어
- 문서의 구조와 내용을 같이  __쉽고 빠르게__ 적고자 탄생
- Typora 실시간 마크다운 변환(미리보기)제공
- 이미지 또는 표 삽입시 매우 편한 UI 제공



## 1. 헤딩

-  #의 개수에 따라 제목의 수준을 구별(h1~h6)
- 문서 구조의 기본
- 글자 크기를 키우기 위해서 사용하면 안 돼요.



## 2. 리스트

- 순서가 있는 리스트와 순서가 없는 리스트(+,-)
- 리스트 안의 리스트 만들려면 TAB
- 바깥쪽으로 들여쓰려면 shift TAB
- 목록을 표시하기 위해 사용
- 많이 사용하는 태그 중 하나



## 3. 코드블럭 ```

- 일반 텍스트와 다르게 예쁘게 출력
- 개발자가 마크다운을 사랑하는 이유 중 하나
- 사용하는 프로그램에 따라 특정 언어를 명시하면 구문 강조(syntax highlighting) 지원



## 4. 링크 [string] (url)

- string은 보여지는 부분. url은 연결할 곳
- 다른 페이지로 이동하는 링크를 삽입
- 필요하다면 파일의 경로를 넣어 다운로드가 가능한 링크를 만들 수 있음



## 5. 이미지  ! [string] (img_url)

- 링크와 비슷하지만 이미지를 삽입



## 6. 텍스트 강조

- 순서대로 굵게,기울임, 취소선을 이용해 텍스트를 강조합니다.
- *를  _(underbar)로 대체 할 수 있어요._
  - _ 언더바 _1개_  기울임
  - _언더바 __2개__ 굵은 글씨
  - 취소선은 ~~우~~  ~2개씩



## 7. 수평선

- 가로로 긴 수평선을 작성합니다.
- *** 혹은 ---
------
# Git
1. 파일 생성
  1. untracked: git이 관리하지 않는 파일
  - git add
2. tracked: git이 관리하는 파일 (변경사항을 추적 상태)
3. staged: staging area에 올라간 상태 
  - staging area: commit을 원하는 파일들이 대기하는 곳
4.  git commit
5. committed: commit이 완료된 상태
- repository에 반영된(올라간)상태
6. 


working directory: 내가 작업하고 있는 실제 디렉토리
staging area: 커밋(commit)으로 남기고 싶은, 특정 버전으로 관리하고 싶은 파일이 있는 곳


repository: 커밋(commit)들이 저장되는 곳

----
### git 명령어
#### 뭘 모르면 add-commit-push만 알면 된다.
- __git init 명령어로 로컬 저장소를 생성__
- .git  
- git status는 현재 상태 
- __git add . 추적되지 않는 모든 파일과 추적하고 있는 파일 중 수정된 파일을 모두 staging area에 올려 (한 번에 올리고 싶으면 "git add .")__ 
- __git commit -m "commit message"__ :
- git config --global user.name " "
- git config --global user.email " "
- git log 지금까지 변경에 대한 히스토리
- git remote add origin https://github.com/YoungSeok222222/main
- git push -u origin master
- git clone {remote_repo} remote repo를 local로
- __git push__ 
---- 
1. git init
2. git commit -m "message"
3. git remote add origin remote_repo
4. git push -u origin master
5. git add .
6. git push