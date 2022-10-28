# Git Advanced

## 0. **사전 준비**
1. Github에 원격 Repository를 생성한다.
2. git clone을 통해 Local Repository로 복사한다.

---
## 1. **복습**

Git은 파일 관리를 크게 2가지(총 5가지)로 구분한다.

1. **Untracked**
    - git이 추적하지 않은 파일
    - 윈도우 기준으로 폴더 내부에 '.git' 폴더가 존재하면 자동으로 추적된다.
    - '.gitignore' 사용을 통해 폴더나 파일을 untracked 상태로 만들 수 있다.

2. **Tracked**
    - git이 변화를 감지하고 있는 상태
    - Tracked 상태는 아래 **3가지**로 나눌 수 있다.
        - **Unmodified**
            - 수정하지 않은 파일(==최신파일)
            - Local Git에 올라간 파일가 비교하였을 때, 수정되지 않은 상태
        - **Modified(vscode: Changes)**
            - 수정한 파일
        - __Staged(vscode: Staged Changes)__
            - commit을 하기 위해 기다리는 상태
            - 이 영역을 __Staging Area__ 라고 부름

---
## **명령어 정리: Local Git Repository**
```
현재 디렉토리를 Git 작업 디렉토리로 초기화  git init

Unmodified  ->  Modified                 파일 수정

Modified    ->  Staged                   git add

Staged      ->  Local Repository         git commit

현재 Git 파일 상태 확인                   git status

Git 작업(commit) 내역 확인                git log
    
    - commit id, 작성자, 날짜, commit message 확인 가능
    - 종료 명령어: q
```
---
## **명령어 정리: Remote Git Repository**
```
1. 최초 작업시 

Local Repo   ->  Remote Repo             git remote add
Remote Repo  ->  Local Repo              git clone

2. 진행 중일 때

Local Repo   ->  Remote Repo             git push
Remote Repo  ->  Local Repo              git pull
```
---
## **Working Directory 작업 단계 되돌리기(작업 취소)**

취소는 크게 2가지로 뉜다.

> ## 1. 직전 작업 취소
<br>

### Working Directory 작업 취소
    - Modified 상태의 파일을 직전 Commit으로 되돌림(수정한 파일을 수정전으로)
    - '$ git restore <파일명>'
    - 이미 버전 관리가 되고 있는 파일만 되돌리기 가능
    - 되돌린 내용은 복원할 수 없으니 주의해야 함
> ### git restore
- Working Directory에서 수정한 파일을 수정전(직전 커밋)으로 되돌리기
- 이미 저번 관리가 되고 있는 파일만 되돌리기 가능
- git restore를 통해 되돌리면, 해당 내용을 복원할 수 없으니 주의할 것!
- git resotre {파일 이름}
- [참고] git 2.23.0 버전 이전에는 git checkout --{파일이름}


### Staging Area 작업 취소
    - staged 상태의 파일을 Modified 상태로 되돌림(add 취소)
    - root -commit 여부에 따라 두 가지로 나뉨
        - root -commit: 이전에 commit을 한 적이 있는 파일이면 True
        - root -commit이 없는 경우: '$git rm --cached <파일명>'
        - root -commit이 있는 경우: '$git restore --staged <파일명>'

### Repositroy 작업 취소 
    - commit을 완료한 파일을 staging area로 되돌리기 (commit 취소)
    - 명령어: '$ git commit --amend'
    - staging area에 다른 파일이 올라와 있는가에 따라서 두 가지로 나뉨
        - Staging Area에 새로 올라온 내용이 없다면: 직전 Commit의 메세지만 수정
        - Staging Area에 새로 올라온 내용이 있다면: 직전 Commit을 새로운 Commit으로 덮어쓰기
            - 이때, Staging Area의 모든 내용이 Commit에 포함된다.

    - Commit 메세지 수정을 위해 Vim 편집기가 열림
        - 입력 모드(i): 문서 편집 가능
        - 명령 모드(esc):
            - 명령 모드는 ':'과 함께 사용한다.
            - 저장 후 종료 (:wq)
            - 강제 종료 (:q!)
                - 리눅스에서 특정 동작을 강제로 수행하게 하는 것: '!'
<br>


<br>

> ## 2. 과거 작업으로 돌아가기
<br>

### 1. Git Reset
- 프로젝트를 특정 Commit(버전) 상태로 되돌림
- 특정 Commit으로 되돌아 갔을 때, **해당 Commit 이후 쌓았던 Commit들은 전부 사라짐**
- 명령어: '$ git reset [옵션] <Commit_id>'

> ### git reset 의 세가지 옵션

--soft 
- 해당 Commit으로 되돌아가고
- 되돌아간 Commit 이후의 파일들은 Staging Area로 돌려놓음

--mixed
- 해당 커밋으로 되돌아가고
- 되돌아간 커밋 이후의 파일들은 Working Directory로 돌려놓음
- git reset 옵션의 기본값

-- hard
- 해당 커밋으로 되돌아가고
- 되돌아간 커밋 이후의 파일들은 모두 Working Directory에서 삭제 -> 따라서 사용시 주의할 것!
- 기존의 Untracked 파일은 사라지지 않고 Untracked로 남아있음

<br>

> ### git reflog

- git reset의 hard 옵션은 Working Directory 내용까지 삭제하므로 위험할 수 있음

<br>

> ### git revet

git reset과의 차이점
- 개념적 차이
    - reset은 커밋 내역을 삭제하는 반면, revert는 새로운 커밋을 생성함
    - revert는 Github를 이용해 협업할 때, 커밋 내역의 차이로 인한 충돌 방지 가능

- 문법적 차이
    - git reset 5sd2f42라고 작성하면 5sd2f42라는 커밋으로 되돌린다는 뜻
    - git revert 5sd2f42라고 작성하면 5sd2f42라는 커밋 한 개를 취소한다는 뜻 (5sd2f42라는 커밋이 취소되었다는 내용의 새로운 커밋을 생성함)
- 명령어: '$ git revert <Commit_id>'
    - '$ git reset <Commit_id>': Commit_id로 프로젝트를 되돌린다는 뜻
    - '$ git revert <Commit_id>': Commit_id에 반영된 내용을 취소한다라는 뜻

    - 여러 내역 revert: '$ git revert <start_id>..<end_id> 
        - 역순으로 하나씩 Commit revert 가능
---
<br>

## 3. Git branch

- 브랜치의 조회, 생성 삭제와 관련된 명령어

> 조회

    - '$ git branch': Local Repo의 브랜치 목록을 확인
    - '$ git branch -r': Remote Repo의 브랜치 목록 확인

> 생성

    - '$ git branch <브랜치명>': 새로운 브랜치 생성
    - '$ git branch <브랜치명> <commit_id>': 특정 Commit 기준으로 브랜치 생성

> 삭제

    - '$ git branch -d <브랜치명>': 병합된 브랜치를 삭제 가능
    - '$ git branch -D <브랜치명>':강제로 브랜치 삭제

<br>

## git switch
 - 현재 브랜치에서 다른 브랜치로 **HEAD**를 이동하는 명령어
 - 'HEAD': 현재 브랜치의 최신 Commit을 가리킴


 - '$ git switch <브랜치명>': 다른 브랜치로 이동
 - '$ git switch -c <브랜치명>': 브랜치 새로 생성 후 이동
 - '$ git switch -c <브랜치명>': 특정 commit 기준으로 브랜치 생성 후 이동

<br>

## git merge





