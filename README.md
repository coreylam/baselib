# 使用 sphinx + git pages 构建代码文档说明网站


- [sphinx-doc](https://www.sphinx-doc.org/en/master/index.html): 相关的所有内容和指引, 都可以在这个网站找到
- [Sphinx简明教程](https://iridescent.ink/HowToMakeDocs/Basic/Sphinx.html): 中文文档, 更简明易懂, 也很全面

## 安装 sphinx 
参考本分支下的 requirements.txt,
```shell
pip install -r requirements.txt
```

## 创建 makefile, conf 等项目基础文档

```shell
sphinx-quickstart
```

## 配置 conf
参考本分支下的配置, 自行设置主题等

## 建立软连接(用于Github Pages)
在 github 页面的 settings 中, 选择本分支, 目录选择 docs, 在项目中创建软连接

```shell
ln -s ./build/html docs
```

## 编译并提交
在项目根目录下, 用 make 将 rst 文件编译成 html 静态文件, 并提交
```shell
make html
```
## rstSyntax 语法 

语法说明： https://3vshej.cn/rstSyntax/tips.html#id2