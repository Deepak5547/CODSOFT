import java.util.Scanner;

public class StudentGradeCalculator {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Input student details
        System.out.print("Enter student name: ");
        String studentName = scanner.nextLine();

        System.out.print("Enter number of subjects: ");
        int numSubjects = scanner.nextInt();

        // Input marks for each subject
        int[] marks = new int[numSubjects];
        inputMarks(scanner, marks);

        // Display student details and results
        displayStudentDetails(studentName, marks);
    }

    // Function to input marks for each subject
    private static void inputMarks(Scanner scanner, int[] marks) {
        for (int i = 0; i < marks.length; i++) {
            System.out.print("Enter marks for Subject " + (i + 1) + ": ");
            marks[i] = scanner.nextInt();
        }
    }

    // Function to calculate average
    private static double calculateAverage(int[] marks) {
        int sum = 0;
        for (int mark : marks) {
            sum += mark;
        }
        return (double) sum / marks.length;
    }

    // Function to calculate grade
    private static char calculateGrade(double average) {
        if (average >= 90) {
            return 'A';
        } else if (average >= 80) {
            return 'B';
        } else if (average >= 70) {
            return 'C';
        } else if (average >= 60) {
            return 'D';
        } else {
            return 'F';
        }
    }

    // Function to display student details and results
    private static void displayStudentDetails(String studentName, int[] marks) {
        System.out.println("\nStudent Details:");
        System.out.println("Name: " + studentName);
        System.out.println("Number of Subjects: " + marks.length);
        System.out.println("Marks:");
        for (int i = 0; i < marks.length; i++) {
            System.out.println("Subject " + (i + 1) + ": " + marks[i]);
        }

        // Calculate average and determine grade
        double average = calculateAverage(marks);
        char grade = calculateGrade(average);

        System.out.println("Average: " + average);
        System.out.println("Grade: " + grade);
    }
}
