#include <iostream>

int main(){

    //Overflow 

    unsigned char data {250};

    ++data;
    std::cout << "data : " << static_cast<int>(data) << std::endl;

    ++data;
    std::cout << "data : " << static_cast<int>(data) << std::endl;

    ++data;
    std::cout << "data : " << static_cast<int>(data) << std::endl;

    ++data;
    std::cout << "data : " << static_cast<int>(data) << std::endl;

    ++data; 
    // std::hex --> data will be shown in hexadecimal
    std::cout << "data : " << std::hex <<  static_cast<int>(data) << std::endl; // 255

    ++data;  // Overflow
    std::cout << "data : " << static_cast<int>(data) << std::endl; // 256

    // std::dec --> data will be shown in decimal
    std::cout << std::dec ;


    data = 1;

    --data;
    std::cout << "data : " << static_cast<int>(data) << std::endl;

    --data;
    std::cout << "data : " << static_cast<int>(data) << std::endl;

   
    return 0;
}