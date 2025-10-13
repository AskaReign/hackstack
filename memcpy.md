# memcpy in c++
## simple use of memcpy
memcpy() is a function that copies bytes from one place in memory to another.
```c++
#include <iostream>
#include <cstring>  // for memcpy

int main() {
    int src[3] = {1, 2, 3};
    int dest[3] = {0};  // initialize to 0s

    memcpy(dest, src, sizeof(src));

    // Check the result:
    for (int i = 0; i < 3; i++) {
        std::cout << "dest[" << i << "] = " << dest[i] << std::endl;
    }

    return 0;
}
```
## memcpy in char arrays
```c++
#include <iostream>
#include <cstring>

int main() {
    char _last_code[20] = {};     // destination buffer
    char codeArr[20] = "HelloWorld123456";

    int chnum = 5;  // start copying into _last_code at index 5
    int i = 0;      // start copying from codeArr at index 0
    int _sz_codeDataStr = 10; // copy 10 bytes

    memcpy(&_last_code[chnum], &codeArr[i], _sz_codeDataStr);

    // Print _last_code as a string
    std::cout << "_last_code: ";
    for(int j = 0; j < 20; j++) {
        std::cout << _last_code[j];
    }
    std::cout << std::endl;

    return 0;
}
```
## memcpy in int arrays
```c++
#include <iostream>
#include <cstring>

int main() {
    int _last_code[10] = {0};     
    int codeArr[10] = {100, 200, 300, 400, 500, 600, 700};

    int chnum = 2;  // start copying into _last_code at index 2
    int i = 3;      // start copying from codeArr at index 3
    int _sz_codeDataStr = 3 * sizeof(int); // copy 3 ints worth of bytes

    memcpy(&_last_code[chnum], &codeArr[i], _sz_codeDataStr);

    // Print _last_code
    std::cout << "_last_code: ";
    for(int j = 0; j < 10; j++) {
        std::cout << _last_code[j] << " ";
    }
    std::cout << std::endl;

    return 0;
}
```
