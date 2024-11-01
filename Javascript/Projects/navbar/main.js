let navbar = document.querySelector('.container')
let close_btn = document.querySelector('#close_btn')
let open_btn = document.querySelector('#open_btn')

var close_nav = function(){
    navbar.classList.add('hide');
    this.classList.add('hide');
    open_btn.classList.remove('hide');
}

var open_nav = function(){
    navbar.classList.remove('hide');
    close_btn.classList.remove('hide');
    this.classList.add('hide');
}

close_btn.onclick = close_nav
open_btn.onclick = open_nav