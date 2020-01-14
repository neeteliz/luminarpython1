var range= Number(prompt("enter the range"));
var flag=0;
for(var i=2;i<range;i++)
{
    for(var j=2;j<i;j++)
    {
      if(i%j==0)
        {
         flag++;
         break;
        }
    else
        {
         flag=0;
        }


 if(flag==0);
  {
     console.log(i);
  }

}
}