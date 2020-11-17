# Pwidget for Testing

> This repo is for the final assignment in Software Testing. I hope it will be useful in my future Software Development

## Structure

* File Folder
   - data: storing orthogonal table.
   - doc: Documents for this software.
   - gui_utils: tools for constructing the GUI.
   - utils: tools for achieving searching oithogonal table.
   - test: tools for testing this widget.
   - output: generate the searching result.

* File
   - main.py: run this widget.
   - requirements.txt: install environment what this software needed.
   - README.md: YOU ARE WATCHING NOW.

## Schedule 

### GUI

> 子页面：主页、生成测试用例界面、正交表查询界面、显示历史记录

- [ ] PyQT GUI设计
- [ ] 输入水平数和因素数框
- [ ] 输入测试用例需要的类别框
- [ ] 生成出来的测试用例框
- [ ] 在线查询页面
- [ ] 查询已生成的测试用例
- [ ] 查询文件夹

### 查询正交表

- [ ] 查询一般正交表
- [ ] 查询混合正交表
- [ ] 读取正交表并找到对应水平数和因素数的区间
- [ ] 在线查询

### 生成测试用例

- [ ] 根据获取到的正交表以及测试用例类别进行映射
- [ ] 输出到GUI中
- [ ] 可以切换模式，是出现完整的正交表还是映射过后的测试用例
- [ ] 根据测试用例输入到代码中
- [ ] 记录历史记录
- [ ] 输出到csv文件中
- [ ] 记录生成的测试用例的名字

### 从网上获取正交表

- [ ] 不依赖本地的文件，读取网页上的
- [ ] 网络连接测试

### 根据代码自动生成测试用例并运行

- [ ] 提供代码输入框和运行框
- [ ] 可选择编译环境
- [ ] 提供多种语言的接口
- [ ] 