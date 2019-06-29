function ajaxre(name){
    fetch('/aaa'+'?aa='+name).then(res => res.json()).then(data =>{
        var a =data['data']
        $('#mainmain').empty()
        for (var j=0;j<a.length;j++ )
        {
            $('#mainmain').append('<div id="mainmainleft" class=" col-xs-5 col-sm-5 col-md-5"><a href="" class="thumbnail"><img src="/'+a[j][0]+'"/></a></div><div id="mainmainright" class=" col-xs-7 col-sm-7 col-md-7"><a href="">'+a[j][2]+'</a><div id="mainmainleftprice" class=" col-xs-6 col-sm-6 col-md-6"><a href=""><span style="font-size: 0.3rem;">￥'+a[j][1]+'</span><br /><span style="font-size: 0.2rem;">11万好评</span></a></div><div id="change" class=" col-xs-6 col-sm-6 col-md-6"><input type="button" onclick="jianchange('+a[j][3]+')" class="jianchange" value="-" /><span id = "'+a[j][3]+'">'+a[j][4]+'</span><input type="button"  onclick="addchange('+a[j][3]+')"  class="addchange"  value="+" /></div></div>')
        }
    })
 }
function addchange(idis){
    fetch('/addchange'+'?car_id='+idis).then(res => res.json()).then(data =>{
        var a = data['data']
        if(a == 'err')
        {

        }
        else if(a == 'error')
        {
            window.location.href ='/sign'
        }
        else
        {
            $("#" + idis).text(a)
        }
   })
 }
function jianchange(idis){
    document.getElementById(idis).innerHTML=1
    fetch('/jianchange'+'?car_id='+idis).then(res => res.json()).then(data => {
       var a=data['data']
       if(a == 'err')
        {
            $("#" + idis).text(0)
        }
        else if(a == 'error')
        {
            window.location.href ='/sign'
        }
        else
        {
            $("#" + idis).text(a)
        }
   })
 }






















