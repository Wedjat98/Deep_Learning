# Deep_Learning


```c++
#define ENABLE 5
#define DIRA 3
#define DIRB 4
#define BUTTON_PIN 2
#define LED_PIN 10
volatile bool flag = LOW;//ボタンフラグ変数
bool highend = LOW, high_begin = LOW;//高速モードフラグ変数
int i = 0;//for文
const int bounce = 100;//ms判断条件変数
unsigned long msTime;
void switchON();//割り込み関数
```
