$(document).ready(function(){
    var account = document.getElementById('username')
    var accountlenerr = document.getElementById('namelenerr')
    var accounterr = document.getElementById('nameerr')
    var password = document.getElementById('pass')
    var passerr = document.getElementById('passerr')
    var phton = document.getElementById('phton')
    var phoneerr = document.getElementById('phoneerr')
    var button = document.getElementById("sign")
    account.addEventListener('focus',function(){
        accountlenerr.style.display = 'none'
        accounterr.style.display = 'none'
    },false)
    account.addEventListener('blur',function(){
        instr = this.value
        if (instr.length<2){
            accountlenerr.style.display = 'inline'
            button.disabled=true
            return
        }
        $.post('/verusername/',{'usrname':instr},function (data) {
            if (data.sta == 'error'){
                accounterr.style.display = 'inline'
            }
            if(data.sta == 'success'){
                if (instr.length > 6 && instr.length != 11 ){
                    button.disabled=false
                }

            }
        })
    },false)
    password.addEventListener('focus',function(){
        passerr.style.display = 'none'
    },false)
    password.addEventListener('blur',function(){
        instr = this.value
        if (instr.length<6){
            button.disabled=true
            passerr.style.display = 'inline'
            return
        }
        else {
            button.disabled=false
        }
    },false)
    phton.addEventListener('focus',function(){
        phoneerr.style.display = 'none'
    },false)
    phton.addEventListener('blur',function(){
        instr = this.value
        if (instr.length != 11){
            phoneerr.style.display = 'inline'
            button.disabled=true
            return
        }
        else {
            button.disabled=false
        }
    },false)



})

// function reg() {
//     fetch('/register',{method:'POST',
//         username:
//     }).then(res)
//
// }