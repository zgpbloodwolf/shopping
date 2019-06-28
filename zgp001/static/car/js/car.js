function addchange(idis){
    fetch('/addchange'+'?car_id='+idis).then(function (response){return response.json()}).then(function (data) {
        var a = data['data']
        var b = data['danjia']
        var c = data["zj"]
        if(a == 'err')
        {
        }
        else
        {
            $('#'+idis).text(a)
            $('#'+idis+'jiage').text('￥'+b)
            $('#jiesuanmoney').text('￥'+c)
        }
   })
 }
function jianchange(idis){
    fetch('/jianchange'+'?car_id='+idis).then(function (response){return response.json()}).then(function (data) {
        var a=data['data']
        var b = data['danjia']
        var c = data["zj"]
        if( a == 0)
        {
            window.location.href="http://127.0.0.1:8000/car/"

        }
        else
        {
            $('#'+idis).text(a)
            $('#'+idis+'jiage').text('￥'+b)
            $('#jiesuanmoney').text('￥'+c)
        }
   })
 }
 function chosenco(coid) {
     fetch('/chosenchange'+'?co_id='+coid).then(function (response){return response.json()}).then(function (data) {
         var a = data['data']
         window.location.href="http://127.0.0.1:8000/car/"
            })
 }
 function jiesuan() {
    var f = confirm('是否确认下单')
     if(f){
         fetch('/jiesuan').then(response => response.json()).then(data => {
             window.location.href="http://127.0.0.1:8000/car/"
     })
     }

 }
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 