+ 函数结构

```c++
#include<iostream>
using namespace std;
int main（参数）
{
	//body代码
    return 0;
}
/* 一个函数由四部分组成：
	返回数据类型：int
	函数名：main
	参数：放在（）内
	函数主体：放在{}内，对于main函数要返回0，即return 0 未写会自动加上
#include <iostream>代表使用的iostream库,cout << 和cin>> 代表输入输出
namespace代表申请名为std的内存空间
*/
```

+ 数据类型与变量类型

| 数据类型 | 关键字  |
| :------- | :------ |
| 布尔型   | bool    |
| 字符型   | char    |
| 整型     | int     |
| 浮点型   | float   |
| 双浮点型 | double  |
| 无类型   | void    |
| 宽字符型 | wchar_t |

​	一些基本变量类型可以用类型修饰符修饰，如signed、unsigned、short、long。

​	变量类型指变量的属性，决定变量支持的方法，例如数字就不是变量类型，但数组、列表是。

+ 运算符优先级（由上到下逐渐增大）
  + 逻辑运算符NOT
  + 算术运算符 * / % 
  + 算数运算符 + -
  + 关联运算符 >  <  =  >=  <=
  + 相关联运算法 ==  !=
  + 逻辑运算符 and
  + 逻辑运算法 or
  + 赋值运算符
  
+ 基础语句
  + 条件语句
  
    ```C++
    //if-else if -else 条件
    if(conditionA)
    {
        //执行A；
    }
    else if(conditionB)
    {
        //执行B；
    }
    else
    {
        //执行c
    }
    //switch条件
    #include <iostream>
    using namespace std;
     
    int main ()
    {
       // 局部变量声明
       int a = 100;
       int b = 200;
     
       switch(a) {
          case 100:
             cout << "这是外部 switch 的一部分" << endl;
             switch(b) {
                case 200:
                   cout << "这是内部 switch 的一部分" << endl;
             }
       }
       cout << "a 的准确值是 " << a << endl;
       cout << "b 的准确值是 " << b << endl;
     
       return 0;
    }
    ```
  
    
  
  + 循环语句
  
  ```C++
  //while循环
  #include <iostream>
  using namespace std;
  int main()
  {
    while(condition) 
    {
        //执行；
    }
     return 0;
  }
  //for循环
  #include <iostream>
  using namespace std;
   
  int main ()
  {
     // for 循环执行
     for( int a = 10; a < 20; a = a + 1 )
     {
         cout << "a 的值：" << a << endl;
     }
   
     return 0;
  }
  //do...while循环
  #include <iostream>
  using namespace std;
  int main ()
  {
     // 局部变量声明
     int a = 10;
  
     // do 循环执行
     do
     {
         cout << "a 的值：" << a << endl;
         a = a + 1;
     }while( a < 20 );
   
     return 0;
  }
  //循环控制 continue、break、goto
  #include <iostream>
  using namespace std;
   
  int main ()
  {
     // 局部变量声明
     int a = 10;
  
     // do 循环执行
     LOOP:do
     {
         if( a == 15)
         {
            // 跳过迭代
            a = a + 1;
            goto LOOP;
         }
         cout << "a 的值：" << a << endl;
         a = a + 1;
     }while( a < 20 );
   
     return 0;
  }
  ```



+ 变量操作

  + 数字与字符串以及string库

    ```c++
    //数字类型，操作同python
    short  s = 10;
    int    i = -1000;
    long   l = 100000;
    float  f = 230.47;
    double d = 200.374;
    //字符串实际上是使用 null 字符 \0 终止的一维字符数组
    //char site[7] = {'R', 'U', 'N', 'O', 'O', 'B', '\0'};
    //char site[] = "RUNOOB";
    #include <iostream>
    #include <cstring>
     
    using namespace std;
     
    int main ()
    {
       char str1[13] = "runoob";
       char str2[13] = "google";
       char str3[13];
       int  len ;
     
       // 复制 str1 到 str3
       strcpy( str3, str1);
       cout << "strcpy( str3, str1) : " << str3 << endl;
     
       // 连接 str1 和 str2
       strcat( str1, str2);
       cout << "strcat( str1, str2): " << str1 << endl;
     
       // 连接后，str1 的总长度
       len = strlen(str1);
       cout << "strlen(str1) : " << len << endl;
     
       return 0;
    }
    //标准库string类，可用于字符串操作，操作类似python
    #include <iostream>
    #include <string>
     
    using namespace std;
     
    int main ()
    {
       string str1 = "runoob";
       string str2 = "google";
       string str3;
       int  len ;
     
       // 复制 str1 到 str3
       str3 = str1;
       cout << "str3 : " << str3 << endl;
     
       // 连接 str1 和 str2
       str3 = str1 + str2;
       cout << "str1 + str2 : " << str3 << endl;
     
       // 连接后，str3 的总长度
       len = str3.size();
       cout << "str3.size() :  " << len << endl;
     
       return 0;
    }
    ```

  + 数组和向量（vector库）

    ```C++
    //数组使用
    double arry[10]; //声明数组arry的元素为double类型，有10个元素
    double balance[5] = {1000.0, 2.0, 3.4, 7.0, 50.0};
    arry[4] = 50.0; //根据下标对数组元素进行赋值
    //vetor向量使用
    #include <vector>
    int main()
    {
        vector<int> seq(size);
        
    }
    ```
    

+ 函数操作

  + 函数结构

  ```c++
  return_type function_name( parameter list )
  {
     body of the function
  }
  /*一个函数由四部分组成：
  	返回数据类型：return_type
  	函数名：function_name
  	参数：parameter list 放在（）内
  	函数主体：body of the function放在{}内，对于main函数要返回0，即return 0 未写会自动加上
  */
  ```

  + 定义函数，声明与引用

  ```c++
  //函数定义
  int max(int b,int a);//定义函数可以单独进行声明，函数体放在后面操作
  int max(int,int);//函数声明数据类型是必须的，可以只声明类型
  //函数引用
  //在一个源文件中定义函数且在另一个文件中调用函数时，函数声明是必需的。在这种情况下，您应该在调用函数的文件顶部声明函数
  #include <iostream>
  using namespace std;
   
  // 函数声明
  int max(int num1, int num2);
   
  int main ()
  {
     // 局部变量声明
     int a = 100;
     int b = 200;
     int ret;
   
     // 调用函数来获取最大值
     ret = max(a, b);
   
     cout << "Max value is : " << ret << endl;
   
     return 0;
  }
   
  // 函数返回两个数中较大的那个数
  int max(int num1, int num2) 
  {
     // 局部变量声明
     int result;
   
     if (num1 > num2)
        result = num1;
     else
        result = num2;
   
     return result; 
  }
  ```

  

+ 指针与引用

  ​	**指针**是一个变量，其值为另一个变量的地址，使用&访问一个变量的地址，指针的变量名名已*开头

  ```C++
  //指针
  int    *ip;    /* 一个整型的指针 */
  double *dp;    /* 一个 double 型的指针 */
  float  *fp;    /* 一个浮点型的指针 */
  char   *ch;    /* 一个字符型的指针 */
  //指针使用
  int ival = 20;
  int *ip = &ival;//*ip对应的就是ival的值，ip对应的时ival的内存地址。当ival为数组时可以不加&
  int *ip;//当未对*ip赋值时其值为null，对应ip内存地址为0
  //引用
  int a = 20;
  int& d = a; // &声明了d引用了a，当a发生改变，d也会改变
  ```
