let dollar = document.getElementById('dollar');
let pound = document.getElementById('pound');

dollar.onkeyup = function(){
    pound.value = this.value * 15.6;
}

pound.onkeyup = function(){
    dollar.value = this.value / 15.6;
}