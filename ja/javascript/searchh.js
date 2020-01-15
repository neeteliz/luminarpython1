so=[20,10,5,70,50];
input=Number(prompt("enter the input"));
flag=0
for(var i=0;i<so.length;i++)
{
    if(input==so[i])
    {
        flag=1
        break;
    }

}
if(flag!=0)
{
alert("element is found");
}
else
{
alert("element not found");
}