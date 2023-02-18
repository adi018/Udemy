#include <iostream>
#include <ctime>

int main(){
    // Setting the seed for randomization
    std::srand(std::time(0));

    const int NUM {200};
    const int OP_NUM {4};
    char operation [][2] {"+", "-", "*", "/"};
    int rand_1 {}, rand_2 {}, rand_3 {};
    bool b_end {false};
    double result {}, u_input {};
    char u_try;

    std::cout << "Welcome to the greatest calculator on Earth!" << std::endl;

    while(!b_end)
    {
        rand_1 = (std::rand() % NUM);
        rand_2 = (std::rand() % NUM);
        rand_3 = (std::rand() % std::size(operation));

        if (rand_3 == 0)
        {
            result = rand_1 + rand_2;
        }
        else if (rand_3 == 1)
        {
            result = rand_1 - rand_2;
        }
        else if (rand_3 == 2)
        {
            result = rand_1 * rand_2;
        }
        else if (rand_3 == 3)
        {
            result = rand_1 / rand_2;
        }
        else
        {
            std::cout << "INVALID!" << std::endl;
            break;
        }

        std::cout << "What's the result of " << rand_1 << " " << operation[rand_3] << " " << rand_2 <<" : ";
        std::cin>> u_input;

        if (result == u_input)
        {
            std::cout << "Congratulations! You got te result " << result << " right!" << std::endl;
        }
        else
        {
            std::cout << "Naah! the correct result is : " << result << std::endl;
        }
        
        std::cout << "Do you want to try again ? (Y | N ) : " ;
        std::cin>>u_try;

        b_end = ((u_try == 'Y') || (u_try == 'y')) ? false : true;


    }
    return 0;
}