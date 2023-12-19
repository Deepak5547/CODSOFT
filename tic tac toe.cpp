#include <iostream>
#include <vector>
#include <limits>

class TicTacToe {
private:
    int boardSize;
    int currentPlayer;
    std::vector<std::vector<int>> board;

public:
    TicTacToe(int size, int players) : boardSize(size), currentPlayer(1) {
        initializeBoard();
        playGame(players);
    }

private:
    void initializeBoard() {
        board.resize(boardSize, std::vector<int>(boardSize, 0));
    }

    void printBoard() const {
        for (int i = 0; i < boardSize; ++i) {
            for (int j = 0; j < boardSize; ++j) {
                if (board[i][j] == 0) {
                    std::cout << "   ";
                } else {
                    std::cout << " " << static_cast<char>(board[i][j] + '0') << " ";
                }

                if (j < boardSize - 1) {
                    std::cout << "|";
                }
            }

            std::cout << "\n";

            if (i < boardSize - 1) {
                for (int j = 0; j < boardSize * 4 - 1; ++j) {
                    std::cout << "-";
                }
                std::cout << "\n";
            }
        }
        std::cout << "\n";
    }

    bool makeMove(int row, int col) {
        if (row < 0 || row >= boardSize || col < 0 || col >= boardSize || board[row][col] != 0) {
            std::cout << "Invalid move! Try again.\n";
            return false;
        }

        board[row][col] = currentPlayer;
        return true;
    }

    bool checkWin(int row, int col) const {
        // Check row
        for (int i = 0; i < boardSize; ++i) {
            if (board[row][i] != currentPlayer) {
                break;
            }
            if (i == boardSize - 1) {
                return true;
            }
        }

        // Check column
        for (int i = 0; i < boardSize; ++i) {
            if (board[i][col] != currentPlayer) {
                break;
            }
            if (i == boardSize - 1) {
                return true;
            }
        }

        // Check diagonals
        if (row == col) {
            for (int i = 0; i < boardSize; ++i) {
                if (board[i][i] != currentPlayer) {
                    break;
                }
                if (i == boardSize - 1) {
                    return true;
                }
            }
        }

        if (row + col == boardSize - 1) {
            for (int i = 0; i < boardSize; ++i) {
                if (board[i][boardSize - 1 - i] != currentPlayer) {
                    break;
                }
                if (i == boardSize - 1) {
                    return true;
                }
            }
        }

        return false;
    }

    bool isBoardFull() const {
        for (const auto& row : board) {
            for (int cell : row) {
                if (cell == 0) {
                    return false;
                }
            }
        }
        return true;
    }

    void switchPlayer() {
        currentPlayer = (currentPlayer % 2) + 1;
    }

    void playGame(int players) {
        std::cout << "Tic-Tac-Toe Game\n";
        printBoard();

        while (true) {
            int row, col;

            do {
                std::cout << "Player " << currentPlayer << "'s turn. Enter your move (row and column): ";
                std::cin >> row >> col;

                // Handle non-integer input
                if (std::cin.fail()) {
                    std::cin.clear();
                    std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
                    std::cout << "Invalid input! Please enter integers.\n";
                    continue;
                }

                // Handle out-of-bounds input
                if (row < 0 || row >= boardSize || col < 0 || col >= boardSize) {
                    std::cout << "Invalid input! Row and column must be within the board.\n";
                    continue;
                }

            } while (!makeMove(row, col));

            if (checkWin(row, col)) {
                std::cout << "Player " << currentPlayer << " wins!\n";
                break;
            } else if (isBoardFull()) {
                std::cout << "It's a draw! The board is full.\n";
                break;
            }

            switchPlayer();
            printBoard();
        }

        std::cout << "Game over!\n";
    }
};

int main() {
    int size, players;

    // Get board size and number of players
    std::cout << "Enter the size of the Tic-Tac-Toe board: ";
    std::cin >> size;

    std::cout << "Enter the number of players (2 or more): ";
    std::cin >> players;

    if (size < 3 || players < 2) {
        std::cout << "Invalid input! Board size must be 3 or more, and there must be at least 2 players.\n";
        return 1;
    }

    TicTacToe game(size, players);

    return 0;
}
