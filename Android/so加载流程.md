### 安卓so加载流程深入分析

一个app是如何加载so以及调用so中的函数的。

其实分2部分，java层的分析比较简单system.loadLibrary,更值得了解的是在底层的源码，是如何查找并且映射到内存中的.

调用栈就是**system.loadLibrary->Runtime.loadLibrary->BaseDexClassLoader.findLibrary->Runtime.doLoad->LoadNativeLibrary**

Native层分4个阶段

1. find_libraries()第一部分：初始化
2. find_libraries()第二部分：载入so到内存
   1. load_library()第一部分：打开so文件
   2. load_library()第二部分：映射so文件
   3. load_library()第三部分：解析dynamic section
3. find_libraries()第二部分：链接阶段



soinfo_link_image 建立so链接