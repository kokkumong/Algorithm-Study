import java.util.Scanner;

public class Main {
   public static void main(String[] args) {
       Scanner sc = new Scanner(System.in);
       int count = sc.nextInt();
       int [] answer = new int[count];
       for (int i = 0; i < count; i++) {
           int a = sc.nextInt();
           int b = sc.nextInt();
           answer[i] = a + b;
       }
       for (int i = 0; i < count; i++) {
           System.out.println(answer[i]);
       }
   }
}
