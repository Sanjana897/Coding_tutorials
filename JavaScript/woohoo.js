alert( "Hello World! I'm some external code!" );
//creates an alert with this text each time the page is loaded.

var foo = "hello";
var bar = "world"
console.log( foo + " to the " + bar ); 
//this will output "hello world" to the console! Won't be visible on the page.

var i = 1;
i = ++i;
console.log(i)
//this will output "2" to the console!

var i = 6;
i = ++i;
console.log(i)
//this will output "7" to the console! ++ is a short form for add 1, since incrementing numbers are very common in programming languages.

var num1 = 5;
var num2 = 6;
console.log(num1 + num2);
//this will output "11" to the console!

var bim = true;
var bam = false;

if (bam)
{console.log("If bam was true this would print, but it's not");}
else {console.log("Bam isn't true");}

var zim = false;
var zam = false;

if (zam)
{console.log("If zam was true this would print, but it's not");}
else if (zim) {console.log("Zim is true");}
else {console.log("Neither of them is true");}

var zoom = 4;
var boom = 5;

if (zoom > boom)
{console.log("Zoom is bigger");}
else if (zoom < boom) {console.log("Boom is bigger");}
else {console.log("Neither is bigger");}

greet = function( person, greeting ) {
    var text = greeting + ", " + person + " what's up?";
    console.log( text );
}



