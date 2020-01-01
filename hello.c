int is_pal(char s[], int first,int last)
{
	if (first>=last)
		return TRUE;

	return (s[first] == s[last])  && 
	      is_pal(s, first+1,last-1);
}