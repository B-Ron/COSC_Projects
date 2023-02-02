import java.util.Scanner;
public class Menu {
	public static void main(String[]args){		
		Scanner r =new Scanner(System.in);
		double number = 0.0;
		String doItAgain="y";
		String menuOption = null;
		String m1="1) Enter the number you're finding the squre root of ";
		String m2="2) Enter the number you're finding the cube root of";
		String m3="3) Exit Loop";
		while(doItAgain=="y"||doItAgain=="y"){
			if(menuOption==m1){
				System.out.print("1)Enter the number you're finding the square root of ");
				number = r.nextDouble()*Math.pow(0,2.0)/number;
				System.out.print("Do it Again? (Yes or No?): ");
			}
			else if(menuOption==m2){
				System.out.print("2) Enter the number you're finding the cube root of");
				number = r.nextDouble()*Math.pow(0,3.0)/number;
				System.out.print("Do it Again? (Yes or No?): ");
			}
			else System.out.print("Invalid");
		}
	}
}
