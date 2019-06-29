$(document).ready(function(){
    var usname = document.getElementById('name')
    var nameerr = document.getElementById('nameerr')
    var pass = document.getElementById('pass')
    var passerr = document.getElementById('passerr')
    var sign = document.getElementById('sign')
    usname.addEventListener('focus',function (ev) {
        nameerr.style.display='none'
        sign.disabled = true
    },false)
    usname.addEventListener('blur',function (ev) {
        ins = this.value
        $.post('/verusername/',{'usrname':ins},function (data) {
            if (data.sta == 'error'){
                sign.disabled = true
                instr = pass.value
                if (instr.length > 5 ){
                    sign.disabled=false}}
            else if(data.sta == 'success'){
                nameerr.style.display = 'inline'
            }})
    },false)
    pass.addEventListener('focus',function (ev) {
        passerr.style.display='none'
    },false)
    pass.addEventListener('blur',function (ev) {
        ins = this.value
        if (ins.length > 5 ){
            sign.disabled=false
        }
        else {
            passerr.style.display='inline'
            sign.disabled=true
        }
    },false)


})