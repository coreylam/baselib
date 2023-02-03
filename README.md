# 使用 sphinx + git pages 构建代码文档说明网站


- [sphinx-doc](https://www.sphinx-doc.org/en/master/index.html): 相关的所有内容和指引, 都可以在这个网站找到
- [sphinx-dic中文](https://www.sphinx-doc.org/zh_CN/master/index.html): 上面链接的中文版
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

## 编译并提交
在项目根目录下, 用 make 将 rst 文件编译成 html 静态文件, 并提交
```shell
make html
```

## 将 build/html 下的文件拷贝到 docs 目录(用于Github Pages)
在 github 页面的 settings 中, 选择本分支, 目录选择 docs, 在项目中创建软连接

```shell
mv ./build/html docs
```
## Jekyll 配置
- [about-github-pages-and-jekyll](https://docs.github.com/zh/pages/setting-up-a-github-pages-site-with-jekyll/about-github-pages-and-jekyll)

由于 Github 使用 Jekyll 进行静态网站生成, 且默认情况下，Jekyll 不会构建以下文件或文件夹：

- 位于名为 /node_modules 或 /vendor 的文件夹中
- 以 _、. 或 # 开头
- 以 ~ 结尾
- 被配置文件中的 exclude 设置排除
- 如果想要 Jekyll 处理其中任何文件，可以使用配置文件中的 include 设置。

由于 sphinx 编译出来的静态网站文件, 默认是在 html/_static 目录, 会导致该资源无法打包, 因此需要在 include 中配置, 具体操作如下:

在 docs 目录下创建配置文件 _config.yml, 在文件中编写 include
```shell
include: ['_static']
```

由于每次 make 后, 需要刷新 docs 文件, 所以可以将 _config.yml 文件创建到 根目录下, 每次重新 make 后, 将文件复制到 docs 目录
```shell
cp _config.yml docs/
```


## rstSyntax 语法 

语法说明： https://3vshej.cn/rstSyntax/tips.html#id2