Python：Relative import 相对路径 ValueError: Attempted relative import in non-package


使用相对的的 import 方式，只能在包里面；这样 “.” 就会按照name 找路径；

如果主main运行的话`__name__ = "__main__"`  就找不到路径了。


> **包含相对路径import 的python脚本不能直接运行，只能作为module被引用。原因正如手册中描述的，所谓相对路径其实就是相对于当前module的路径，但如果直接执行脚本，这个module的name就是“__main__”, 而不是module原来的name， 这样相对路径也就不是原来的相对路径了，导入就会失败，出现错误“ValueError: Attempted relative import in non-package”**
>
> Note that both explicit and implicit relative imports are based on the name of the current module. Since the name of the main module is always`"__main__"`, modules intended for use as the main module of a Python application should always use absolute imports.
>
> [refer]: http://blog.csdn.net/chinaren0001/article/details/7338041



只能 从包外面 触发里面的相对路径调用；

eg：执行外面的 z.py  触发里面 top/sub1/m1.py  使用相对路径

​	[<u>GitHub</u>](https://github.com/willowj/python_exercise/package_/relative_import)     示例文件下载 [<u>rar_down</u>](https://github.com/willowj/python_exercise/package_/relative_import.rar)

<div align=center><img src="http://images2017.cnblogs.com/blog/1083549/201712/1083549-20171221233317365-2134773654.png"  /> </div>


```python
#\relative_import\top\sub1\m1.py
print 'i am m1 \nfrom . import m2 \n...from ..sub2 import sub2_sub'
from . import m2  
from ..sub2 import sub2_sub
```

from . import m2   #同级目录

from ..sub2 import sub2_sub  # 上级目录

```python
#\relative_import\z.py  
from top.sub1 import m1
```