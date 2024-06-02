#include <iostream>

int add(int number1,int number2){
	return number1 + number2
}
int main(){
	std::cout << add(3,5) << std::endl;
	std::cout << add(0,0) << std::endl;
	std::cout << add(-7,-3) << std::endl;
	std::cout << add(-1,5) << std::endl;
	std::cout << add(14,-11) << std::endl;
}