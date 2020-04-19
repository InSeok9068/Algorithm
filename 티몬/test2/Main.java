package 티몬.test2;

import java.util.Scanner;

public class Main {
	public static void main(String[] args) throws Exception{
    Scanner scanner = new Scanner(System.in);
    int number = scanner.nextInt();

    System.out.println(countBits(number));
  }

  public static int countBits(int number){
    int count = 0;
    int []b = new int[32];
    int i = 0;

    while(number != 1)
    {
     b[i++] = number%2;
     number = number/2;
    }

    b[i] = number;

    for(int j = 0; j <= i; j++){
      if(b[j] == 1){
        count+=1;
      }
    }  

    return count;

  }
}