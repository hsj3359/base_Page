function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}


// message를 socket으로 전송
// 동시에 django 서버에도 message 전송
document.querySelector("#chat-submit").onclick = function (e) {
  var messageInputDom = document.querySelector("#chat-message-input");
  var author = user;
  var message = messageInputDom.value;
  var created_at = new Date();
  chatSocket.send(
    JSON.stringify({
      author: author,
      message: message,
      created_at: created_at,
    })
  );

  messageInputDom.value = "";

  $.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
    });

  $.ajax({
    type: "post",
    url: chat_url,
    data: {
      author: author,
      message: message,
      photo: "undefined",
      created_at: created_at,
    },
    dataType: "json",
    success: console.log("Send message to server!"),
  });
};

// 대화방에 이미지 업로드
document.querySelector("#image-upload").onclick = function (e) {
  var imageUploadDom = document.querySelector("#image-upload-url");
  var author = user;
  var message = imageUploadDom.value;
  var photo = imageUploadDom;
  console.log(message);
  console.log(photo.files[0]);
  var created_at = new Date();
//  chatSocket.send(
//    JSON.stringify({
//      author: author,
//      message: message,
//      created_at: created_at,
//    })
//  );

  var formData = new FormData();
  formData.append('photo', photo.files[0])

  $.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
  });

  $.ajax({
    type: "post",
    url: upload_url,
    data: formData,
    processData: false,
    contentType: false,
    dataType: "json",
    success: console.log("Send image to server!"),
  });
};