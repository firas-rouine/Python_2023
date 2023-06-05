var x1 = document.querySelector(".pirate").innerHTML
var y1 = document.querySelector(".pirate")
var x2 = document.querySelector(".ninja").innerHTML
var y2 = document.querySelector(".ninja")
function Increase1(){
    x1++
    y1.innerHTML=x1
}
function Increase2(){
    x2++
    y2.innerHTML=x2
}
function Remove(elm){
    elm.remove()
}

setTimeout(function(){alert("The Ninja have won !")},13000);