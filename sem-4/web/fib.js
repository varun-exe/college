var n = Number(prompt("Enter a number:"))
var a = 0
var b = 1
var c = 0
document.write("Fibonacci Series: "+"<br>")
if(n==1){
    document.write(a+"\n")
}
else if(n==2){
    document.write(a+"<br>")
    document.write(b+"<br>")
}
else if(n>2){
    document.write(a+"<br>")
    document.write(b+"<br>")
    for(i=3;i<= n;i++){
        c = a + b
        a = b
        b = c
        document.write(c+"<br>")
    }
}
else{
    document.write("Wrong input")
}
