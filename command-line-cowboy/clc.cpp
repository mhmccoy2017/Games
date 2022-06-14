#include <iostream>
#include <iomanip>
#include <cctype>

using namespace std;

void displayBanner(){
    cout << R"(
	 ____  ____  _      _      ____  _      ____    _     _  _      _____   ____  ____  _      ____  ____ ___  _
	/   _\/  _ \/ \__/|/ \__/|/  _ \/ \  /|/  _ \  / \   / \/ \  /|/  __/  /   _\/  _ \/ \  /|/  _ \/  _ \\  \//
	|  /  | / \|| |\/||| |\/||| / \|| |\ ||| | \|  | |   | || |\ |||  \    |  /  | / \|| |  ||| | //| / \| \  / 
	|  \__| \_/|| |  ||| |  ||| |-||| | \||| |_/|  | |_/\| || | \|||  /_   |  \__| \_/|| |/\||| |_\\| \_/| / /  
	\____/\____/\_/  \|\_/  \|\_/ \|\_/  \|\____/  \____/\_/\_/  \|\____\  \____/\____/\_/  \|\____/\____//_/   
*
*
* Start
* Quit
*
*
																											 )";
    cout << "\n";
}

int main(){
	displayBanner();
	char a;
	bool gamePlayLoop = true;
	while(gamePlayLoop){
		cin >> a;
		//input is quit game
		if(a == 'q'){
			gamePlayLoop = false;
		}
	}
	return 0;
}