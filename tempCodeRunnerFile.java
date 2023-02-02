import java.util.*;
import java.util.Arrays;
public class main{
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        int n;
        n = 10;
        int arr[]= new int[n];
        System.out.println("Enter 10 integer number: ");
        for(int i=0;i<n;i++){
            arr[i]=sc.nextInt();
        }
        System.out.println("Enter the element whose frequency you want to check: ");
        int ele = sc.nextInt();
        int occ = 0;
        for(int i =0;i<n;i++){
            if(ele == arr[i]){
                occ++;  
            }
            System.out.println("The number " +ele+" occurs "+occ+" times");
    }
    }
}