#include <iostream>


int main(){

    /*
    // Celcius into Fahrenheit
    -----------------------

    float celcius;
    float farenheit;
    
    std::cout << "Please enter a degree value in Celcius :" << std::endl;
    std::cin >> celcius;

    farenheit = (9.0 /5)*celcius + 32;
    std::cout << celcius << " Celcius is " << farenheit << " Fahrenheit" << std::endl;
    */

    // Area and Volume of a Box
    //-------------------------

    float length;
    float width;
    float height;

    std::cout << "Welcome to box calculator. Please type in length, width and height information : " << std::endl;
    std::cout << "length : ";
    std::cin >> length;
    std::cout << std::endl;

    std::cout << "width : ";
    std::cin >> width;
    std::cout << std::endl;

    std::cout << "height : ";
    std::cin >> height;
    std::cout << std::endl;

    float area = width*length;
    float volume = area*height;

    std::cout << "The base area is : " << area << std::endl;
    std::cout <<"The volume is : " << volume << std::endl;

    return 0;
}