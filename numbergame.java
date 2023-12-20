import java.util.Random;
import java.util.Scanner;

public class NumberGame {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Random random = new Random();

        int lowerBound = 1;
        int upperBound = 100;
        int numberToGuess = random.nextInt(upperBound - lowerBound + 1) + lowerBound;

        int numberOfAttempts = 0;
        boolean hasGuessedCorrectly = false;

        System.out.println("Welcome to the Number Guessing Game!");
        System.out.println("I have selected a number between " + lowerBound + " and " + upperBound + ". Try to guess it!");

        while (!hasGuessedCorrectly) {
            System.out.print("Enter your guess: ");
            int userGuess = getUserInput(scanner);

            numberOfAttempts++;

            if (userGuess < lowerBound || userGuess > upperBound) {
                System.out.println("Please enter a number within the specified range.");
            } else if (userGuess == numberToGuess) {
                hasGuessedCorrectly = true;
                System.out.println("Congratulations! You've guessed the correct number in " + numberOfAttempts + " attempts.");
            } else {
                String hint = (userGuess < numberToGuess) ? "higher" : "lower";
                System.out.println("Incorrect! Try a " + hint + " number.");
            }
        }

        scanner.close();
    }

    private static int getUserInput(Scanner scanner) {
        while (!scanner.hasNextInt()) {
            System.out.println("Invalid input. Please enter a valid number.");
            scanner.next(); // Consume invalid input
        }
        return scanner.nextInt();
    }
}
