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

# Uses of `memcpy` in C++
---

## Common Uses of `memcpy`

### 1. Copying Raw Data Buffers

- **Explanation:** Copy a block of bytes, typically arrays or buffers.
- **Example:**

```cpp
#include <iostream>
#include <cstring>

int main() {
    char src[5] = {'H', 'e', 'l', 'l', 'o'};
    char dest[5];
    memcpy(dest, src, 5);  // Copy 5 bytes

    // Check the results
    for (int i = 0; i < 5; ++i) {
        std::cout << dest[i];
    }
    std::cout << std::endl;  // Output: Hello
    return 0;
}
```
### 2. Implementing Custom Memory Management

- **Explanation:** Used in dynamic array resizing or custom allocators to move blocks of memory efficiently.

- **Example:**

```cpp
#include <iostream>
#include <cstring>

int main() {
    int* oldArr = new int[5]{1, 2, 3, 4, 5};
    int* newArr = new int[10];

    // Copy old data into new array during resizing
    memcpy(newArr, oldArr, 5 * sizeof(int));

    // Check the results
    for (int i = 0; i < 5; ++i) {
        std::cout << newArr[i] << " ";
    }
    std::cout << std::endl;  // Output: 1 2 3 4 5

    delete[] oldArr;
    delete[] newArr;
    return 0;
}
```
### 3. Fast Copying of Large Blocks of Data

- **Explanation:** Efficient copying of large multimedia or data buffers.

- **Example:**

```cpp
#include <iostream>
#include <cstring>

int main() {
    const int size = 1024 * 1024;  // 1 MB
    char* buffer1 = new char[size];
    char* buffer2 = new char[size];

    // Fill buffer1 with a pattern
    for (int i = 0; i < size; ++i) {
        buffer1[i] = 'A';
    }

    // Copy large block of data
    memcpy(buffer2, buffer1, size);

    // Check the results
    std::cout << "First byte: " << buffer2[0] << ", Last byte: " << buffer2[size - 1] << std::endl;
    // Output: First byte: A, Last byte: A

    delete[] buffer1;
    delete[] buffer2;
    return 0;
}
```
### 4. Copying Between Non-overlapping Memory Areas

- **Explanation:** Safe copying when source and destination don’t overlap.

- **Example:**

```cpp
#include <iostream>
#include <cstring>

int main() {
    char buffer[10] = "123456789";
    memcpy(buffer + 5, buffer, 4);  // Safe: non-overlapping regions

    // Check the results
    std::cout << buffer << std::endl;  // Output: 123451234
    return 0;
}
```
### 5. Bitwise Copying for Serialization or Networking

- **Explanation:** Copy raw bytes of a struct for sending over network or writing to file.

- **Example:**

```cpp
#include <iostream>
#include <cstring>

struct Data {
    int id;
    float value;
};

int main() {
    Data d = {42, 3.14f};
    char networkBuffer[sizeof(Data)];

    memcpy(networkBuffer, &d, sizeof(Data));

    // Check the results by copying back
    Data d_copy;
    memcpy(&d_copy, networkBuffer, sizeof(Data));
    std::cout << "id = " << d_copy.id << ", value = " << d_copy.value << std::endl;
    // Output: id = 42, value = 3.14
    return 0;
}
```
### 6. Setting up Data for Hardware or APIs

- **Explanation:** Copy data into hardware or API buffers expecting raw memory.

- **Example:**

```cpp
#include <iostream>
#include <cstring>

int main() {
    char audioData[256];
    // Fill audioData with samples (simulate with 'S')
    memset(audioData, 'S', 256);

    char hardwareBuffer[256];
    memcpy(hardwareBuffer, audioData, 256);

    // Check the results
    std::cout << "hardwareBuffer[0] = " << hardwareBuffer[0] << ", hardwareBuffer[255] = " << hardwareBuffer[255] << std::endl;
    // Output: hardwareBuffer[0] = S, hardwareBuffer[255] = S
    return 0;
}


