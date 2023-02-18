#include <iostream>


int main(){
    /*
    // Assignment 4: Is it even? Or could it be odd?
    int num;

    std::cout << "Please type in an integral value : " << std::endl;
    std::cin >> num;

    if (num%2 == 0)
    {
        std::cout << num << " is even" << std::endl;
    }
    else
    {
        std::cout << num << " is odd" << std::endl;
    }
    */


    /*
    // Assignment 5: Will you get the treatment?
    int age;

    std::cout << "Please type in your age: " << std::endl;
    std::cin >> age;

    if ((age >= 21) && (age <= 39))
    {
        std::cout << "You are eligible for the treatment" << std::endl;
    }
    else if ((age < 21) && (age >= 0))
    {
        std::cout << "Sorry, you are too young for the treatment" << std::endl;
    }
    else if (age > 39)
    {
        std::cout << "Sorry, you are too old for the treatment" << std::endl;
        std::cout << age;
    }
    else
    {
        std::cout << "Sorry, invalid input" << std::endl;
    }
    */

   /*
   // Assignement 6: Is the day valid?

   
   */

    int day;

    std::cout << "Which day is today [1 : Monday,....., 7 : Sunday] : " << std::endl;
    std::cin >> day;

    switch (day)
    {
    case 1:
        std::cout << "Today is Monday. Let's have some fun" << std:: endl; 
        break;
    
    case 2:
        std::cout << "Today is Tuesday. Let's have some fun" << std:: endl; 
        break;
    
    case 3:
        std::cout << "Today is Wednesday. Let's have some fun" << std:: endl; 
        break;
    
    case 4:
        std::cout << "Today is Thursday. Let's have some fun" << std:: endl; 
        break;
    
    case 5:
        std::cout << "Today is Friday. Let's have some fun" << std:: endl; 
        break;
    
    case 6:
        std::cout << "Today is Saturday. Let's have some fun" << std:: endl; 
        break;

    case 7:
        std::cout << "Today is Sunday. Let's have some fun" << std:: endl; 
        break;
    
    default:
        std::cout << day << " is not a valid day. Bye!" << std:: endl;
        break;
    } 

    return 0;
}