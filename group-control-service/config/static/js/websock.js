// WebSocket 객체 생성
var chatSocket = new WebSocket(
  "ws://" + window.location.host + "/ws/chat/" + room + "/"
);

// Socket에서 message 수신
chatSocket.onmessage = function (e) {
  var data = JSON.parse(e.data);
  var author = data["author"];
  var message = data["message"];
  document.querySelector("#chat-log").value += author + " : " + message + "\n";
};

// WebSocket 연결
chatSocket.onopen = function (e) {
  console.log("connection success!");
};

// WebSocket 닫힘
chatSocket.onclose = function (e) {
  console.log("Chat socket closed unexpectedly");
};

// enter를 누를 시 채팅 내용이 입력
document.querySelector("#chat-message-input").focus();
document.querySelector("#chat-message-input").onkeyup = function (e) {
  if (e.keyCode === 13) {
    // enter를 입력한 경우
    document.querySelector("#chat-submit").click();
  }
};
