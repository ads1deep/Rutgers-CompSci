import java.util.Scanner;
public class Ch7Ex19 {
	static int size = 100;

    public static void main(String[] args) {


        Scanner input = new Scanner(System.in);
        System.out.println("First number is size of list...");
        System.out.print("Enter list: ");
        size = input.nextInt();
        int[] numbers = new int[size];
        for (int i = 0; i < size; i++) {
            numbers[i] = input.nextInt();
        }
        if (isSorted(numbers)) System.out.print("The list is already sorted.\n");
        else System.out.print("The list is not sorted.\n");

    }

    public static boolean isSorted(int[] numbers) {

        for (int i = 0; i < numbers.length - 1; i++) {

            if (numbers[i] > numbers[i + 1]) return false;

        }
        return true;
    }
    public static void printArray(int[] array, int numberPerLine) {

                for (int i = 0; i < array.length; i++) {

                    System.out.printf("%4d ", array[i]);
                    if ((i + 1) % numberPerLine == 0) System.out.println("");
                }
    }
}
