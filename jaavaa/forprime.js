var range= Number(prompt("enter the range"));
var flag=0;
var i;
for( i=2;i<range;i++)
{
    for(j=2;j<i;j++)
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
    }

   if(flag!=1)
    {
        console.log(i);
    }



}