public class Prob14{


	static long TOTAL_MAX = 0;
	public static void main(String [] args){
	
	
	
	
	
	
		long number = 0;
		int numOfChains = 0;
		
		for(int i = 999999 ; i > 1; i--){
			if(i % 1000 == 0)
				System.out.println("num " + i);		
			int num = rec(i);
			if(num >numOfChains){
				numOfChains = num;
				number = i;
				
			}
			
		}
		
		System.out.println(number + "    Count " + numOfChains + "\nBiggestNumber - " + 
TOTAL_MAX);
	}
	
	public static int rec(long x){
	
	int y = 1;
	while(x != 1){
		if(x % 2 == 0)
			x = x/2;
		else
			x = (3*x)+1;
		if(x > TOTAL_MAX){
			TOTAL_MAX = x;
		}
		//System.out.println("CHANGING " + x);
		y++;
	}
	
	return y;
	
		
		
		
	}

	public static int recu(long x, int count){
	if(x == 1)
		return count;
	if(x%2 ==0)
		return recu(x/2,++count);
	return recu((3*x)+1,++count);	
	}	

}
