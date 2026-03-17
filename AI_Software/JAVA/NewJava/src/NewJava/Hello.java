package NewJava;

public class Hello {

	public static int sum(int n, int m)
	{
		return n+m;
	}
	public static void main(String[] args)
	{
		int i = 20;
		int j = 10;
		char c = ' ';
		
		j = sum(i,10);
		c = '?';
		
		System.out.println(i);
		System.out.println(j);
		System.out.println(c);
	}

}
