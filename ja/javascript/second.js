var a=10;
var b=7;
var c=5;
var max,min,tot,second;
if((a>c) and (a>b))
{
    console.log(b);
    max=b;
}
else if((a<b) and (b>c))
{
    console.log(a);
    max=a;
}
else
{
    console.log(c);
    max=c;
}
if ((a <= b) and (a <= c))
{
    console.log(a)
    min=a;
}
else if ((b <= a) and (b <= c))
{
    console.log(b);
    min=b;
}
else
{
    console.log(c)
    min=c;
}
tot=a+b+c
second=tot-(min+max)
console.log("second largest is",second)