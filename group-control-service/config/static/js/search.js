//  일정 수정과 삭제 모달에 관한 코드
  function search() {
    var head = document.getElementById("searchModal_head");
    var search = document.getElementById('search_text').value;
    var smb = document.querySelector('.search-message-box');
    var spb = document.querySelector('.search-post-box');

    head.innerHTML = search + " 검색결과";

    if(search == ""){
    alert("입력이 없습니다.");
    return
    }

    var searchPost = [];
    var searchChat = [];
    for(var i=0;i<postData.length;i++){
        if(postData[i]["title"].indexOf(search) != -1){
            searchPost.push(postData[i]);
        }
    }
    for(var i=0;i<chatData.length;i++){
        if(chatData[i]["message"].indexOf(search) != -1){
            searchChat.push(chatData[i]);
        }
    }

    if(searchPost.length==0) {
    spb.innerHTML = `<li class="list-group-item">검색된 내용이 없습니다.</li>`;
    } else {
        spb.innerHTML = "";
        for(var i=0;i<searchPost.length;i++) {
            spb.innerHTML += `<li class="list-group-item">${searchPost[i]["title"]}<ul><li> 작성자 : ${searchPost[i]["author"]}</li><li> 파일 : <a href=${searchPost[i]["photo-url"]} download>${searchPost[i]["photo"]}</a></li></ul></li>`;
        }
    }

    if(searchChat.length==0) {
    smb.innerHTML = `<li class="list-group-item">검색된 내용이 없습니다.</li>`;
    } else {
        smb.innerHTML = "";
        for(var i=0;i<searchChat.length;i++) {
            smb.innerHTML += `<li class="list-group-item"><a href=${searchChat[i]["url"]}>${searchChat[i]["message"]}</a><ul><li> 작성자 : ${searchChat[i]["author"]}</li><li> 대화방 : ${searchChat[i]["room"]}</li></ul></li>`;
        }
    }

    $('#searchModal').modal('show');

  }