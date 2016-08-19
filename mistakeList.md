# Mistake List  

- 输入字符串，没有添加后引号`"`or `'`  

 解决方法: 先输入前后引号，再往里添加文本

	```
	wrong:  
	months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug
	
	correct:  
	months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"
	```
- 在字符串内输入 formatter , 没有在字符串外添加 `%`  

  ```
  wrong：
  print "So, you're %r old, %r tall and %r heavy."  (
	age, height, weight)	
	
	correct：
	print "So, you're %r old, %r tall and %r heavy." % (
	age, height, weight)