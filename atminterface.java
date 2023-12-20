import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

class Account {
    private String accountNumber;
    private String pin;
    private double balance;

    public Account(String accountNumber, String pin, double initialBalance) {
        this.accountNumber = accountNumber;
        this.pin = pin;
        this.balance = initialBalance;
    }

    public String getAccountNumber() {
        return accountNumber;
    }

    public boolean verifyPin(String enteredPin) {
        return pin.equals(enteredPin);
    }

    public double getBalance() {
        return balance;
    }

    public void deposit(double amount) {
        balance += amount;
    }

    public boolean withdraw(double amount) {
        if (amount > balance) {
            System.out.println("Insufficient funds");
            return false;
        } else {
            balance -= amount;
            System.out.println("Withdrawal successful. Remaining balance: " + balance);
            return true;
        }
    }
}

class Bank {
    private Map<String, Account> accounts;

    public Bank() {
        this.accounts = new HashMap<>();
        // Add sample accounts
        accounts.put("123456", new Account("123456", "1234", 1000.0));
        accounts.put("789012", new Account("789012", "5678", 2000.0));
    }

    public Account getAccount(String accountNumber) {
        return accounts.get(accountNumber);
    }
}

class ATM {
    private Bank bank;
    private Scanner scanner;

    public ATM(Bank bank) {
        this.bank = bank;
        this.scanner = new Scanner(System.in);
    }

    public void start() {
        System.out.println("Welcome to the ATM!");

        // Simulate user login (in a real scenario, this would involve authentication)
        System.out.print("Enter your account number: ");
        String accountNumber = scanner.nextLine();
        Account currentAccount = bank.getAccount(accountNumber);

        if (currentAccount == null) {
            System.out.println("Account not found. Exiting.");
            return;
        }

        System.out.print("Enter your PIN: ");
        String enteredPin = scanner.nextLine();

        if (!currentAccount.verifyPin(enteredPin)) {
            System.out.println("Invalid PIN. Exiting.");
            return;
        }

        // Display account information and options
        displayAccountInfo(currentAccount);

        while (true) {
            displayOptions();
            int choice = getUserChoice();

            switch (choice) {
                case 1:
                    System.out.println("Balance: " + currentAccount.getBalance());
                    break;
                case 2:
                    performWithdrawal(currentAccount);
                    break;
                case 3:
                    performDeposit(currentAccount);
                    break;
                case 4:
                    System.out.println("Exiting. Thank you!");
                    return;
                default:
                    System.out.println("Invalid choice. Please enter a number between 1 and 4.");
            }

            // Display updated account information
            displayAccountInfo(currentAccount);
        }
    }

    private void displayAccountInfo(Account account) {
        System.out.println("\nAccount Information:");
        System.out.println("Account Number: " + account.getAccountNumber());
        System.out.println("Balance: " + account.getBalance());
    }

    private void displayOptions() {
        System.out.println("\nOptions:");
        System.out.println("1. Check Balance");
        System.out.println("2. Withdraw Money");
        System.out.println("3. Deposit Money");
        System.out.println("4. Exit");
    }

    private int getUserChoice() {
        System.out.print("Enter your choice (1-4): ");
        while (!scanner.hasNextInt()) {
            System.out.println("Invalid input. Please enter a number between 1 and 4.");
            scanner.next(); // Consume invalid input
        }
        return scanner.nextInt();
    }

    private void performWithdrawal(Account account) {
        System.out.print("Enter withdrawal amount: ");
        while (!scanner.hasNextDouble()) {
            System.out.println("Invalid input. Please enter a valid amount.");
            scanner.next(); // Consume invalid input
        }
        double withdrawalAmount = scanner.nextDouble();
        account.withdraw(withdrawalAmount);
    }

    private void performDeposit(Account account) {
        System.out.print("Enter deposit amount: ");
        while (!scanner.hasNextDouble()) {
            System.out.println("Invalid input. Please enter a valid amount.");
            scanner.next(); // Consume invalid input
        }
        double depositAmount = scanner.nextDouble();
        account.deposit(depositAmount);
    }
}

public class Main {
    public static void main(String[] args) {
        Bank bank = new Bank();
        ATM atm = new ATM(bank);
        atm.start();
    }
}
