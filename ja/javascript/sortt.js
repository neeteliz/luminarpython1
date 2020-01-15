so=[20,10,5,70,50]

l=so.length
for(var i=0;i<l;i++)
{
    for(var j=i+1;j<l;j++)
    {
        if(so[i]>so[j])
        {
        var temp;
        temp=so[i];
        so[i]=so[j];
        so[j]=temp;
        }
    }
}
for(i of so)
{
console.log(i);
}