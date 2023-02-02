import ch.aplu.turtle.*;
public class Series1 {
	public static void problem1(){
		//create a turtle
		Turtle amanda=new Turtle();
		//write the commands to draw a triangle
		for(int i=0; i< 3; i++){
		amanda.forward(100);
		amanda.right(120);
			}
		
	}
public static void problem2(){
		//create a turtle
	   Turtle robert=new Turtle();
		//write the commands to draw a hexagon
 	   for(int i=0; i<6; i++){
	   robert.forward(100);
	   robert.right(60);
	   }
	   
	}
public static void problem3(){
		//create a turtle
		Turtle trump= new Turtle();
		//write the commands to draw a house
		
		trump.forward(100);
		trump.right(60);
		trump.forward(100);
		trump.right(60);
		trump.forward(100);
		trump.right(60);
		trump.forward(100);
		trump.right(90);
		trump.forward(174);
		trump.right(90);
		trump.forward(100);
		trump.right(90);
		trump.forward(174);
	}
public static void problem4(){
		//create a turtle
		Turtle harper= new Turtle();
	  // write commands to draw a box with a x in the middle
		for(int i=0; i<=4; i++){
			 harper.forward(150);
				harper.right(90);
			}
		harper.right(45);
		harper.forward(213);
		harper.right(135);
		harper.forward(150);
		harper.right(135);
		harper.forward(215);
	}
	public static void main(String[] args) {
		//call the triangle function
		 problem1();
		//call the hexagon function
		 problem2();
		 //call the house function
		 problem3();
		//call the box with a x function
		 problem4();

	}

}
