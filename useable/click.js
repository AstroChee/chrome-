chrome.contextMenus.create({
    "type": 'normal',
    "title": '摘要',
    "id": 'menuDemo',
    "contexts": ['selection'],
    "onclick": genericOnClick
});

function genericOnClick(info, tab) {
  var text  = info.selectionText;
  var data = {
      data: JSON.stringify({"value":text})
   };
    $.ajax({
        type: 'post',
        async : false,
        url: 'http://127.0.0.1:8989/text',
        data: data,
        success: function (data) {
            alert(data);
        }
    });
}
