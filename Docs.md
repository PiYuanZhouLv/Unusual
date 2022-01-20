# 中文文档
> You can find an English copy at [here](Docs_En.md)

>如果你还没有下载或不知道如何导入，请先阅读[使用方法](README.md#usage-使用方法)

## 快速跳转

[`img.py`](#imgpy)
[`language.py`](#languagepy)
[`others.py`](#otherspy)
***
## img.py
快速跳转:
[`返回`](#快速跳转)
***
## language.py
快速跳转:
[`FakeChatAI, fake_chat_ai`](#fakechatai)
[`be_civilized`](#be_civilized)
[`返回`](#快速跳转)
***
### FakeChatAI
[`返回`](#languagepy)

**FakeChatAI(sentences, level)**
> 注意：该类对中文不友好

#### 参数

`sentences`:初始语料库

`level`:语言的相似程度

#### 内置实例
`fake_chat_ai`

#### 方法
`update(sentences)`添加语料库内容

`get()`获取当前语料库

`reset()`清空语料库

`chat(input)`模拟聊天

#### 例子
```pycon
>>> fake_chat_ai = FakeChatAI([
        ('Hello', ('Hello!', 'Hi~')),
        ('What\'s you name?', ('Fake', 'My name is Fake.')),
        ('F*ck', ('be civilized, please.', 'F*ck')),
        ('What\'s the weather like today?', 'It\'s Ok.')
    ])
>>> fake_chat_ai.chat('Hello')
# Hello!
>>> fake_chat_ai.chat('Hello!')
# Hi~
>>> fake_chat_ai.chat('Hi')
# F*ck
>>> fake_chat_ai.get()
#[
#    ('Hello', ('Hello!', 'Hi~')),
#    ('What\'s you name?', ('Fake', 'My name is Fake.')),
#    ('F*ck', ('be civilized, please.', 'F*ck')),
#    ('What\'s the weather like today?', 'It\'s Ok.')
#]
>>> fake_chat_ai.update([('Hi', 'Hello!')])
>>> fake_chat_ai.get()
#[
#    ('Hello', ('Hello!', 'Hi~')),
#    ('What\'s you name?', ('Fake', 'My name is Fake.')),
#    ('F*ck', ('be civilized, please.', 'F*ck')),
#    ('What\'s the weather like today?', 'It\'s Ok.'),
#    ('Hi', 'Hello!')
#]
>>> fake_chat_ai.reset()
>>> fake_chat_ai.get()
# []
```
[`返回`](#languagepy)
***
### be_civilized
[`返回`](#languagepy)

将语言“文明化”

**be_civilized(sentence, words, level)**
> 注意：该函数对中文不友好
> 
> 解决方案：在调用该函数之前使用`jieba`库[_(我是链接)_](https://github.com/fxsjy/jieba )分词，在词语间加上空格
#### 参数
`sentence`:需要“文明化”的原句

`words`:一些十分“文明”的单词

`level`:“文明”程度(0 _(不"文明")_ 到1 _(完全"文明")_ 之间)

#### 示例
```pycon
>>> uuu.language.be_civilized("I give your mother foods")
# I f*ck your mother b*tch
>>> uuu.language.be_civilized("I give your mother foods", level=0.3)
# I give your d*mmit foods
>>> uuu.language.be_civilized("I give your mother foods", words=['?', '(oxo)', '@_@?', '(ovo)?'], level=1)
# ? @_@? @_@? (ovo)? (oxo)
```
***
## others.py
快速跳转:
[`返回`](#快速跳转)