import java.util.Scanner;

public class Ch8Ex13 {
	 public static void main(String[] args) {

	        Scanner input = new Scanner(System.in);
	        System.out.printf("Enter the number of rows and columns of the array: ");
	        int row = input.nextInt();
	        int column = input.nextInt();
	        double[][] m = new double[row][column];

	        System.out.println("Enter the array below: ");
	        for (int i = 0; i < row; i++)
	            for (int k = 0; k < column; k++)
	                m[i][k] = input.nextDouble();


	        int[] location = locateLargest(m);
	        System.out.printf("The location of the largest element is at (%d, %d)\n", location[0], location[1]);
	    }

	    public static int[] locateLargest(double[][] a) {

	        int[] location = new int[] { 0, 0 };
	        double largest = a[0][0];
	        for (int i = 0; i < a.length; i++) {

	            for (int k = 0; k < a[i].length; k++) {

	                if (a[i][k] > largest) {
	                    location[0] = i; // row
	                    location[1] = k; // column
	                    largest = a[i][k];
	                }

	            }
	        }

	        return location;
	    }
	}
