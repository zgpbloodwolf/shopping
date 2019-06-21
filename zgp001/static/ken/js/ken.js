function ajaxre(name){
    fetch('/aaa'+'?aa='+name).then(res => res.json()).then(data => {
        var a=data['data']
        $('#mainmain').empty()
        for (var j=0;j<a.length;j++ )
        {
              $('#mainmain').append('<div id="mainmainleft" class=" col-xs-5 col-sm-5 col-md-5"><a href="" class="thumbnail"><img src="/'+a[j][0]+'"/></a></div><div id="mainmainright" class=" col-xs-7 col-sm-7 col-md-7"><a href=""><!--<div id="mainmainleftname">-->'+a[j][2]+'<!--</div></a>--></a><div id="mainmainleftprice" class=" col-xs-6 col-sm-6 col-md-6"><a href=""><span style="font-size: 0.3rem;">￥'+a[j][1]+'</span><br /><span style="font-size: 0.2rem;">11万好评</span></a></div><div id="change" class=" col-xs-6 col-sm-6 col-md-6"><input type="button" onclick="jianchange('+a[j][3]+')" class="jianchange" value="-" /><span id = "'+a[j][3]+'">0</span><input type="button"  onclick="addchange('+a[j][3]+')"  class="addchange"  value="+" /></div></div>')
        }
    })
 }
function addchange(idis){
    console.log(idis)
    document.getElementById(idis).innerHTML=2
//    fetch('/aaa'+'?aa='+name).then(res => res.json()).then(data => {
//        var a=data['data']
//        $('#mainmain').empty()
//        for (var j=0;j<a.length;j++ )
//        {
//              $('#mainmain').append()
//        }
//    })
 }
function jianchange(idis){
    console.log(idis)
    document.getElementById(idis).innerHTML=1
//    fetch('/aaa'+'?aa='+name).then(res => res.json()).then(data => {
//        var a=data['data']
//        $('#mainmain').empty()
//        for (var j=0;j<a.length;j++ )
//        {
//              $('#mainmain').append()
//        }
//    })
 }






















