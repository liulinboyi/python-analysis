# Python Analysis
## 进入虚拟环境

## [虚拟环境Python官网相关文章](https://docs.python.org/zh-cn/3/tutorial/venv.html#creating-virtual-environments)

![img.png](./images/img.png)

## IDEA创建虚拟环境

![img_1.png](./images/img_1.png)
![img_2.png](./images/img_2.png)

## powershell激活虚拟环境
```powershell
./Scripts/Active.ps1
```
## 运行notebook
```cmd
jupyter notebook
```
## 运行jupyter lab - 推荐
```cmd
jupyter lab
```
### [Jupyterlab安装中文语言包失败](https://cyfeng.science/2021/01/15/jupyterlab-error-when-install-chinses-language-pack/)

### [JupyterLab 3.0 正式发布，同时解决中文语言包下载不成功，汉化不成功的问题，jupyterlab-language-pack-zh-CN 安装失败解决方案](http://zsduo.com/archives/244.html)

### [jupyter lab汉化包](jupyterlab_language_pack_zh_CN-0.0.1.dev0-py2.py3-none-any.whl)

## 汉化包安装
```cmd
pip install jupyterlab_language_pack_zh_CN-0.0.1.dev0-py2.py3-none-any.whl
```

## 切换中文

![img.png](./images/img_3.png)

## Pandas介绍

![img.png](./images/img_4.png)

其中Series是一维的，而DataFrame是二维的！

![img_1.png](./images/img_5.png)

### 仓库用来学习，数据来源于网络


    当更新安装Python时, 卸载之前的安装, 会连带pip之前安装的库文件一同卸载, 可以使用命令导出已安装的库的列表到文件, 等安装完新的Python后, 在通过文件批量安装库文件

### 1.导出安装列表到文件
```powershell
pip freeze > requirements.txt
```

### 2.通过文件批量安装Python依赖(使用清华的源)
```powershell
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

```
### 3.通过pip生成批量离线安装包(whl文件)
```powershell
pip wheel --wheel-dir=./tmp/packages -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

```
### 4.通过离线安装包安装Python依赖
```powershell
pip install --no-index --find-links=./tmp/packages -r requirements.txt

```
### 5.检查安装
```powershell
pip freeze
```
