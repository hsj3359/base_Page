  // 달력에 관한 코드

  function build() {
    var today = new Date(); // 오늘 날짜
    var date = new Date();



    var nMonth = new Date(today.getFullYear(), today.getMonth(), 1); //현재달의 첫째 날
    var lastDate = new Date(today.getFullYear(), today.getMonth() + 1, 0); //현재 달의 마지막 날
    var tbcal = document.getElementById("calendar"); // 테이블 달력을 만들 테이블
    var yearmonth = document.getElementById("today"); //  년도와 월 출력할곳
    yearmonth.innerHTML = today.getFullYear() + "년 " + (today.getMonth() + 1) + "월"; //년도와 월 출력

    // 남은 테이블 줄 삭제
    while (tbcal.rows.length > 2) {
      tbcal.deleteRow(tbcal.rows.length - 1);
    }

    var row = null;
    row = tbcal.insertRow();
    var cnt = 0;

    // 1일 시작칸 찾기
    for (i = 0; i < nMonth.getDay(); i++) {
      cell = row.insertCell();
      cnt = cnt + 1;
    }

    // 달력 출력
    for (i = 1; i <= lastDate.getDate(); i++) { // 1일부터 마지막 일까지
      cell = row.insertCell();
      cell.setAttribute('onclick', 'clickCal(' + i + ')');
      cell.setAttribute('style', 'cursor: pointer;');
      cell.innerHTML = i;
      cnt = cnt + 1;

      if (cnt % 7 == 1) {//일요일 계산
        cell.innerHTML = "<font color=#FF9090>" + i//일요일에 색
      }

      if (cnt % 7 == 0) { // 1주일이 7일 이므로 토요일 계산
        cell.innerHTML = "<font color=#7ED5E4>" + i//토요일에 색
        row = calendar.insertRow();// 줄 추가
      }

      for (var j = 0; j < sche.length; j++) {
        if (sche[j].getFullYear() == date.getFullYear() && sche[j].getMonth() == date.getMonth() && i == sche[j].getDate()) {
          cell.bgColor = "#ffffce"; //오늘날짜배경색
        }
      }

      if (today.getFullYear() == date.getFullYear() && today.getMonth() == date.getMonth() && i == date.getDate()) {
        cell.bgColor = "#BCF1B1"; //오늘날짜배경색
      }
    }

    while (cnt % 7 != 0) {
      cell = row.insertCell();
      cell.innerHTML = "";
      cnt = cnt + 1;

      if (cnt % 7 == 1) {//일요일 계산
        cell.innerHTML = "";//일요일에 색
      }

      if (cnt % 7 == 0) { // 1주일이 7일 이므로 토요일 계산
        cell.innerHTML = "";//토요일에 색
        row = calendar.insertRow();// 줄 추가
      }

      if (today.getFullYear() == date.getFullYear() && today.getMonth() == date.getMonth() && i == date.getDate()) {
        cell.bgColor = "#BCF1B1"; //오늘날짜배경색
      }

      for (var j = 0; j < sche.length; j++) {
        if (sche[j].getFullYear() == date.getFullYear() && sche[j].getMonth() == date.getMonth() && i == date.getDate()) {
          cell.bgColor = "#BCF1B1"; //오늘날짜배경색
        }
      }
    }
  }

  build();