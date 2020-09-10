document.getElementById('buttonProcess').onclick = bt;
function bt(){
    var text  = document.getElementById('zh').innerText;
    $.ajax({
        type: "POST",
        dataType:"text",
        url: "pmain.py",
        data: {param: text},
        success: function (data) {
            document.getElementById("yx").firstChild.data = data;
        }
    });
}
