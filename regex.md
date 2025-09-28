# Regex hacks

## Case 1:
I want to extract the variable names to use them somewhere.
there are two methods for that:
1. use regular expressions search
2. use multiple line selection

In other words i wanna go from this:
```cpp
static constexpr uint16_t PAKCET_ID_THRESHOLD = 0x1022;
static constexpr uint16_t PAKCET_ID_AMPLITUDE = 0x1023;
static constexpr uint16_t PAKCET_ID_INFO1 = 0x1024;
static constexpr uint16_t PAKCET_ID_INFO2 = 0x1025;
static constexpr uint16_t PAKCET_ID_INFO3 = 0x1026;
```
to this:
```cpp
PAKCET_ID_THRESHOLD
PAKCET_ID_AMPLITUDE
PAKCET_ID_INFO1
PAKCET_ID_INFO2
PAKCET_ID_INFO3
```

do the following steps in Qt framework.
(It's almost the same in other environments)
1. hit ctrl + shift + f to enter advanced search
2. check "use regular expressions".
3. add this regex in the search field
```regex
static constexpr uint16_t (\w+) =
```
4. replace with:
```
$1
```
now this is what you get:
```cpp
PAKCET_ID_THRESHOLD 0x1022;
PAKCET_ID_AMPLITUDE 0x1022;
PAKCET_ID_INFO1 0x1022;
PAKCET_ID_INFO2 0x1022;
PAKCET_ID_INFO3 0x1022;
```
what you should have searched for is:
```regex
static constexpr uint16_t (\w+) =.*
```
then you replace the results with
```
$1
```
then what you get is
```cpp
PAKCET_ID_THRESHOLD
PAKCET_ID_AMPLITUDE
PAKCET_ID_INFO1
PAKCET_ID_INFO2
PAKCET_ID_INFO3
```
