# 온라인 스터디 그룹
- 프로젝트 실행하는 방법
    
    - `Pycharm`으로 프로젝트 실행 후, 터미널에 다음 코드 순서대로 입력
    
    - ```
      .\myvenv\Script\activate.bat
      python manage.py runserver
      ```



## Front html문서 배치

- 전체적으로 중복되는 코드는 한 곳으로 따로 저장하였음

  

- ##### 상단 부분과 왼쪽 부분과 맨 아랫 부분 코드



- `group-control-service` - `config` - `templates` - `main_base.html` 에서 코드 관리



- ##### 왼쪽 구역에서 그룹에 관한 부분에 대한 코드



- `group-control-service` - `config` - `templates` - `group_base.html` 에서 코드 관리



- ##### 콘텐츠 부분 코드



- 메인 화면
  - `group-control-service` - `main` - `templates` - `main`- `main.html` 에서 코드 관리
- 그룹 화면
  - `group-control-service` - `group-control` -`templates` - `group-control` 에서 코드 관리
  - 그룹 메인 화면 - `index.html`
  - 대화방 - `chat.html`
  - 공지사항 - `notice.html`



이거대로 해서 코드 수정하는 부분은 저 경로로 찾아가서 코드 수정하면돼

만약에 저게 이해안가면 나한테 말하면 내가 그 부분 코드 수정해줌



