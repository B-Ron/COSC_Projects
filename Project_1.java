import java.util.Scanner;


public class Project_1 {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		 Scanner r =new Scanner (System.in);
			    int side1; 
				int side2;
				int side3;
				System.out.print("Enter the length first side of the triangle:");
				side1=r.nextInt();
				System.out.print("Enter the length of the second side of the triangle:");
				side2=r.nextInt();
				System.out.print("Enter the length of the third side of the triangle:");
				side3=r.nextInt();
				if (side1==side2&&side1==side3&&side2==side3){
					System.out.print("This is an Equilateral Triangle");
			}
				else if((side1==side2&&side2!=side3)||(side1==side3&&side3!=side2)){
					System.out.print("This is an Isosceles Triangle");
				}
				
				else{
					System.out.print("This is an Scalene Triangle");
				}

			}
}


