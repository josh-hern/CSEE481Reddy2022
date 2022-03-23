#include <stdio.h>
#include "../src/battleship.h"

void assert_ok(battleship_err_t err){
	if(err == OK){
		printf("OK\n");
	} else {
		printf("TEST FAILED");
	}
}

void main(int argc, char **argv){

	board_t board;
	assert_ok(init_board(&board));
}
