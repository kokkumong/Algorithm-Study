import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int a = scanner.nextInt();
        int b = scanner.nextInt();
        for(int i = 0; i<a; i++){
            int c = scanner.nextInt();
            if(c < b) System.out.print(c + " ");
        }
    }
}