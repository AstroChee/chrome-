document.getElementById('buttonProcess').onclick = bt;

function bt(){
    var text  = document.getElementById("zh").value;
    var data = {
      data: JSON.stringify({
                        "value":text
                    })
   };
    $.ajax({
        type: 'post',
        async : false,
        url: 'http://127.0.0.1:8989/text',
        data: data,
        success: function (data) {
            document.getElementById("yx").firstChild.data = data;
        }
    });
}
