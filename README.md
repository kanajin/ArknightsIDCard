# ArknightsIDCard

本项目fork自[Eumenides0305/ArknightsIDCard](https://github.com/Eumenides0305/ArknightsIDCard)，为明日方舟个人名片生成器，样例如下图：

this project is a fork with [Eumenides0305/ArknightsIDCard](https://github.com/Eumenides0305/ArknightsIDCard), for generating arknights' ID card. the sample is below:

![output](https://github.com/kanajin/ArknightsIDCard/blob/master/%E8%BE%93%E5%87%BA%E6%A0%B7%E5%9B%BE.png)
![caption](https://github.com/kanajin/ArknightsIDCard/blob/master/%E5%9B%BE%E7%89%87%E5%8F%82%E6%95%B0%E8%AF%B4%E6%98%8E.png)

## 运行环境

python3

## 使用方式

1. clone 本项目
2. 下载release中的资源包(名称为`Source/`)，并放进项目根目录中
3. 根据模板填写`Source`中的`DoctorInfo.csv`和`arkD.csv`
4. 执行以下命令：

```bash
pip install -r requirements.txt
python main.py
```

之后会在项目根目录下生成`OutPut`文件夹，输出图片将以`<博士名称><日期>`命名并输出

注：*Doctorinfo.csv中的可填Source/TTF路径下的文件名，推荐BenderBold或BenderRegular*

## 施工中

准备重写`Draw.py`，增加可读性与逻辑性

## environment

python3

## usage

1. clone this repository
2. download `Source/` in release and put it into the root of repository
3. fill `Source/DoctorInfo.csv` and `Source/arkD.csv`
4. command:

```bash
pip install -r requirements.txt
python main.py
```

the output image will be generated in `/OutPut/`, rule of name is `<doctor_name><draw_date>`
