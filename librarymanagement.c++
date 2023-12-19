#include <iostream>
#include <vector>
#include <string>
#include <chrono>

class Book {
public:
    std::string title;
    std::string author;
    int bookId;
    bool available;
    std::chrono::system_clock::time_point dueDate;

    Book(const std::string& title, const std::string& author, int bookId)
        : title(title), author(author), bookId(bookId), available(true) {}

    void checkOutBook(int days) {
        available = false;
        dueDate = std::chrono::system_clock::now() + std::chrono::hours(24 * days);
    }

    void returnBook() {
        available = true;
    }

    bool isOverdue() const {
        return !available && std::chrono::system_clock::now() > dueDate;
    }
};

class Borrower {
public:
    std::string name;
    int borrowerId;

    Borrower(const std::string& name, int borrowerId)
        : name(name), borrowerId(borrowerId) {}
};

class Library {
private:
    std::vector<Book> books;
    std::vector<Borrower> borrowers;
    int nextBookId;
    int nextBorrowerId;

public:
    Library() : nextBookId(1), nextBorrowerId(1) {}

    void addBook(const std::string& title, const std::string& author) {
        books.emplace_back(title, author, nextBookId++);
    }

    void addBorrower(const std::string& name) {
        borrowers.emplace_back(name, nextBorrowerId++);
    }

    bool borrowBook(int bookId, int borrowerId, int days) {
        auto book = findBookById(bookId);
        if (book != nullptr && book->available) {
            book->checkOutBook(days);
            std::cout << "Book '" << book->title << "' borrowed by Borrower " << borrowerId << ".\n";
            return true;
        } else {
            std::cout << "Book not available for borrowing or does not exist.\n";
            return false;
        }
    }

    bool returnBook(int bookId, int borrowerId) {
        auto book = findBookById(bookId);
        if (book != nullptr && !book->available) {
            book->returnBook();
            std::cout << "Book '" << book->title << "' returned by Borrower " << borrowerId << ".\n";
            return true;
        } else {
            std::cout << "Book cannot be returned. Either it is not checked out or does not exist.\n";
            return false;
        }
    }

    void displayBooks() const {
        std::cout << "Books in the library:\n";
        for (const auto& book : books) {
            std::cout << "ID: " << book.bookId << ", Title: " << book.title
                      << ", Author: " << book.author << ", Available: " << (book.available ? "Yes" : "No")
                      << ", Due Date: " << (book.available ? "N/A" : formatTimePoint(book.dueDate)) << "\n";
        }
    }

    void displayBorrowers() const {
        std::cout << "Borrowers in the library:\n";
        for (const auto& borrower : borrowers) {
            std::cout << "ID: " << borrower.borrowerId << ", Name: " << borrower.name << "\n";
        }
    }

    void calculateFines() const {
        std::cout << "Calculating fines:\n";
        for (const auto& book : books) {
            if (book.isOverdue()) {
                auto overdueDays = std::chrono::duration_cast<std::chrono::hours>(std::chrono::system_clock::now() - book.dueDate).count() / 24;
                std::cout << "Book '" << book.title << "' is overdue by " << overdueDays << " days.\n";
                // Basic fines calculation (customize based on your needs)
                double fine = overdueDays * 0.5;
                std::cout << "Fine for this book: $" << fine << "\n";
            }
        }
    }

private:
    Book* findBookById(int bookId) {
        for (auto& book : books) {
            if (book.bookId == bookId) {
                return &book;
            }
        }
        return nullptr;
    }

    std::string formatTimePoint(const std::chrono::system_clock::time_point& timePoint) const {
        auto time = std::chrono::system_clock::to_time_t(timePoint);
        std::string formattedTime = std::ctime(&time);
        formattedTime.pop_back();  // Remove the newline character from ctime result
        return formattedTime;
    }
};

int main() {
    Library library;

    library.addBook("The Catcher in the Rye", "J.D. Salinger");
    library.addBook("To Kill a Mockingbird", "Harper Lee");
    library.addBook("1984", "George Orwell");

    library.addBorrower("Alice");
    library.addBorrower("Bob");

    library.displayBooks();
    library.displayBorrowers();

    library.borrowBook(1, 1, 14);  // Borrow for 14 days

    library.displayBooks();

    library.returnBook(1, 1);

    library.calculateFines();

    return 0;
}
