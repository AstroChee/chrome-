document.getElementById('buttonProcess').onclick = bt;
var n = 0;
function bt(){
    document.getElementById("yx").firstChild.data = "测试的结果"+n;
    n = n + 1;
}
