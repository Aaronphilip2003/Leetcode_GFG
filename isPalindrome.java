class Solution
{
    public boolean isPalindrome(int x) 
    {
        int copy=x;
        int rev=0;
        while(x!=0)
        {
            int r=x%10;
            rev=rev*10+r;
            x=x/10;
        }
        if(rev==copy && copy>0 || copy==0)
        {
            return true;
        }
        else
        {
            return false;
        }
    }
}
