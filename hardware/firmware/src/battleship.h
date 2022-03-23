
typedef struct board_t{
	char cells[10][10];
} board_t;


typedef enum battleship_err_t{
	OK,
	BOARD_INIT_FAILED,
} battleship_err_t;

battleship_err_t init_board(board_t* board);
