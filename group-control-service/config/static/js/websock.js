// WebSocket 객체 생성
var chatSocket = new WebSocket(
  "ws://" + window.location.host + "/ws/chat/" + room + "/"
);

// Socket에서 message 수신
chatSocket.onmessage = function (e) {
  var data = JSON.parse(e.data);
  var author = data["author"];
  var message = data["message"];
  if (user === author) {
  document.querySelector("#chat-log").innerHTML += `
    <div style="width: 100%; display: inline-block;">
        <div class="col-4 mt-3 mb-1" style="background-color: rgba(0, 0, 0, 0); float: right;">
            <div class="card" style="background-color: rgba(0, 0, 0, 0); border-color: rgba(0, 0, 0, 0);">
                <div style="padding-top: 1.25rem; background-image: url(${myChatTopUrl}); background-size: 100%, 100%; background-repeat: no-repeat;">
                </div>
          <div style="flex: 1 1 auto; background-image: url(${myChatMidUrl}); background-size: 100%, 100%; padding: 0 1.25rem 1rem 1.25rem;">
            <h5 class="card-title">${author}</h5>
            ${message}
          </div>
          <div class="card-body" style="background-image: url(${myChatBotUrl});background-size: 100%, 100%;background-repeat: no-repeat;">
          </div>
        </div>
      </div>
    </div>`;
  } else {
  document.querySelector("#chat-log").innerHTML += `
        <div class="col-4 mt-3 mb-1" style="background-color: rgba(0, 0, 0, 0);">
            <div class="card" style="background-color: rgba(0, 0, 0, 0); border-color: rgba(0, 0, 0, 0);">
                <div style="padding-top: 1.25rem; background-image: url(${otherChatTopUrl}); background-size: 100%, 100%; background-repeat: no-repeat;">
                </div>
          <div style="flex: 1 1 auto; background-image: url(${otherChatMidUrl}); background-size: 100%, 100%; padding: 0 1.25rem 1rem 1.25rem;">
            <h5 class="card-title">${author}</h5>
            ${message}
          </div>
          <div class="card-body" style="background-image: url(${otherChatBotUrl});background-size: 100%, 100%;background-repeat: no-repeat;">
          </div>
        </div>
      </div>`;
  }
  autoScroll();
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
