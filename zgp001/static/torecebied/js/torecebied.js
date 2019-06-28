function queren(co_id) {
    fetch('/queren'+'?co_id='+co_id).then(res =>res.json()).then(data =>{
        var a =data['data']
        window.location.href="http://127.0.0.1:8000/toreceived/"
    })

}
