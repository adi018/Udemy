#include <iostream>
#include <cmath>
#include <vector>
#include <algorithm>


// Calculate the distance between two points
float distance_points (float x1, float x2, float y1, float y2)
{
    return pow(((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)), 0.5);
}

int main(){
    // Declare the variables
    std::vector<float> co_ordinates {1,4,4,4,3,2,5,1};
    float min_value = 99999;
    float max_value = -9999;
    // For indexes of minimum distances
    int x1_co {};
    int y1_co {};
    int x2_co {};
    int y2_co {};

    // For indexes of maximum distances
    int m_x1_co {};
    int m_y1_co {};
    int m_x2_co {};
    int m_y2_co {};

    // Looping through all co-orinates : O(n^2/2)
    for (int i=0; i<=co_ordinates.size()/2; ++i)
    {
        for (int j=0; j<=co_ordinates.size()/2; ++j)
        {
            float value = distance_points(co_ordinates[i*2], co_ordinates[i*2 + 1], co_ordinates[j*2], co_ordinates[j*2 + 1]);
            // Check if minimum value is less than obtained distance and not 0 i.e. distance of point from itself then assign new value to min_value and record the indexes
            if (value < min_value && value != 0)
            {
                min_value = value;
                x1_co = i*2;
                y1_co = i*2 + 1;
                x2_co = j*2;
                y2_co = j*2 + 1;
            }
            // Check if maximum value is greater than obtained distance then assign new value to max_value and record the indexes
            if (abs(value) > max_value && abs(value) != 0)
            {
                max_value = value;
                m_x1_co = i*2;
                m_y1_co = i*2 + 1;
                m_x2_co = j*2;
                m_y2_co = j*2 + 1;
            }
        }
    }

    std::cout << "Sortest distance is between : [" << co_ordinates[x1_co] << ", " << co_ordinates[y1_co] << "] and [" << co_ordinates[x2_co] << ", " << co_ordinates[y2_co] << "]." << std::endl;
    std::cout << "Highest distance is between : [" << co_ordinates[m_x1_co] << ", " << co_ordinates[m_y1_co] << "] and [" << co_ordinates[m_x2_co] << ", " << co_ordinates[m_y2_co] << "]." << std::endl;
    return 0;
}