1. GIT 의 개념
	- 버전 관리 프로그램
	사람이 관리 할 때 발생하는 여러 가지 문제	
	1. 어떤 게 진짜 최종인지 모르는 문제	
		- 파일에 날짜와 시간을 기록
	-- 레포트 하나가 1,000장 이라면 ?
		-> 어떤 걸 수정했더라 ?
	2. 변경사항을 기록하는 파일을 따로 작성
	-- 레포트가 너무 많다면 ? ( 10억장 )
		-> 용량이 너무 큰 문제 발생
	3. 맨 나중 파일과 이전 변경사항만 남김
	-- 사람이 어떻게 변경사항을 다 돌이켜보냐 ?
	4. 나는 소프트웨어니까 빠르고 정확함

* 버전 관리 파일 작성 시
	- 작성자, 수정 위치, 수정 내용, 이유

이것을 코드로 대입
	버전 관리 프로그램이란 ?
	1. 코드의 히스토리(버전)을 관리하는 도구
	2. 개발되어온 과정 파악 가능
	3. 이전 버전과의 변경 사항 비교 및 분석

2. 분산 버전 관리
	* 중앙 집중식 버전 관리
		: 하나의 컴퓨터에 파일을 모두 저장
		- 변경된 파일을 포함하여
	- 서버 컴퓨터를 관리하는 곳에 문제가 생기면
		큰일난다
	이를 해결 하기위해
	* 분산 버전 관리
		: 사용자의 컴퓨터에도
			파일을 모두 복사하여 저장

* gitlab, github, bitbucket 등 많은 버전 관리 프로그램
	- 그 중 github 를 배우는 이유는
		가장 많이 쓰기 때문
	* git 과 github 는 다르다
		git : 분산 버전 관리 !!프로그램
		github : git 기반의 저장소 서비스-

3. CLI
	GUI 란 ?
		Graphic User Interface
		그래픽을 통해 사용자와 컴퓨터가 상호 작용하는 방식
	CLI 란 ?
		Command line interface
		명령어를 통해 사용자와 컴퓨터가 상호 작용하는 방식
	그래픽이 더 편한 것 같은데 왜 CLI 를 사용하나요 ?
		GUI 가 CLI 에 비해 사용하기 쉽지만, 단계가 많고 컴퓨터의 성능을 더 소모
		수 많은 서버/개발 시스템이 CLI 를 통한 조직 환경을 제공
	기본적인 명령어
		touch : 파일 생성
		mkdir(make directory) : 새 폴더 생성
		ls(list) : 현재 작업 중인 디렉토리의 폴더/파일 목록 출력
		cd(change directory) : 현재 작업 중인 디렉토리 변경
		start : 폴더, 파일을 여는 명령어 ( Mac 은 open )
		rm : 파일 삭제 ( -r 옵션으로 폴더 삭제 가능 )
		rmdir : 폴더 삭제
		pwd : 현재 작업 중인 디렉토리의 절대 경로 출력
	cli 팁
		- tab 을 누르면 자동완성된다
		- 방향키 위를 통해 이전 명령어 사용 가능
		- end / home 키 활용하자
	절대경로 vs 상대경로
		절대 경로 : 루트 디렉토리부터 목적 지점까지 거치는 모든 경로를 작성한 것
		상대 경로 : 현재 작업하고 있는 디렉토리를 기준으로 계산된 상대적 위치

4. 마크다운
	텍스트 기반의 가벼운 마크업(Markup) 언어
	문서의 구조와 내용을 쉽고 빠르게 적고자 탄생
	
	#
		헤딩(Heading)
		문서의 제목이나 소제목 작성
	1. 2. 3. * - 
		리스트
		- 순서가 있는 리스트와 순서가 없는 리스트로 구분
	- ```block code``` / `inline code`
		코드 블럭(code block)
		일반 텍스트와 다르게 코드를 이쁘게 출력하는 기능
	- [문자](URL)
		링크(link)
		문자는 보여지는 부분, URL 은 연결할 주소
	- ![문자](IMG_URL)
		이미지(image)
		링크와 비슷하며, 이미지를 삽입
	- **굵게** *기울임* ~~취소선~~
		텍스트 강조(Text Emphasis)
		위를 통해 텍스를 강조
	- --- *** ___
		수평선(horizontal line)
		가로로 긴 수평선을 작성. 대게 단락을 구분할 때 사용

5. git 기본기
	Working Directory : 내가 작업하고 있는 실제 디렉토리
	Staging Area : 커밋(commit) 으로 남기고 싶은 파일들이 대기 하는 곳
	Repository : 커밋(commit) 들이 저장되는 곳. 즉, 변경 사항들이 반영되는 곳

6. git 명령어 ( local )
	git init
		현재 내 디렉토리(폴더)를 git 이 관리하는 폴더로 초기화
	git add
		untracked 파일 or 변경된 파일을 Staging area 에 적용
	git commit
		Staging area 의 파일들을 repository 에 반영
	git status
		git 으로 관리되고 있는 파일들의 상태 출력

7. git 파일 상태
	untracked : git 이 관리하지 않는 파일
	tracked : git 이 관리(추적) 하는 파일
	staged : staging area 에 올라온 파일 == commit 을 대기하는 파일
	committed : commit 이 완료된 상태 ( repository )
	modified : commit 이 완료된 최신 상태 ( Working Directory ). 즉, repository 와 비교하여 최신 상태

8. git Remote
	git remote add
		현재 git 이 관리하고 있는 local repository 를 remote repository 와 연동
		remote 의 파일과 이름이 겹치는 등에서 많은 문제 발생
		!!! 꼭 스스로 한 번 해보기
	git clone
		remote repository 를 local 폴더로 복사
		clone 명령어는 init + remote add 와 동일한 동작을 수행한다
	git pull
		remote repository -> local repository
		remote repository 의 내용을 local 폴더로 복사
		clone 은 최초 실행하여 repository 를 연동하는 것이고,
			안의 내용을 가져오기 위해 pull 명령어를 사용한다.
	git push
		local repository -> remote repository
		수정한 내용을 remote repository 에 반영

고생하셨습니다 !!!
	