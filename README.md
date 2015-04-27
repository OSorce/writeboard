# WriteBoard

---

## 项目地址

* [Github][]: http://github.com/yufeiminds/writeboard
* [Coding][]: http://wb.thxminds.com/write

---

## 创作目的

书写板的创作起源说来话长，小组正在写的一门生成DSL的解释器，用于生成各种标记语言的Parser，
需要一个简洁易用的前端，这个书写板即组合开源社区现有的工具，形成一个简洁通用的文档编辑工具。

现在我们自己用得很Happy，同步分享，临时暂存，so easy，:) 。

因为自家使用，目前只对Chrome浏览器做了兼容测试，其它比如Safari浏览器自动保存等功能无法使用。

---

## Feature

* 同步到云端
* 无跳转刷新( HTML5新特性, pushState )
* 本地存储( HTML5新特性, localStorage )
* 支持预览、分享
* 支持转换幻灯片

---

## Markdown

感谢两个开源项目的作者，lepture和hakimel

他们分别创作了[editor][]和[reveal.js][]两个开源JS项目，[editor][]提供了一个清新的编辑环境，
[reveal.js][]提供了Markdown转换为PPT的快捷方法，没有他们在开源社区的贡献，我们的项目会变得十分复杂。

Markdown语法请参考：

* [English](http://lab.lepture.com/editor/markdown)
* [繁體中文](http://markdown.tw)
* [简体中文](http://www.appinn.com/markdown/)

如果需要幻灯片，请将每一页用三个中划线``---``隔开。

---

## Quickstart

1. Open Writeboard
2. 书写内容
3. 点击同步，获取分享key
4. 预览发布版本或者幻灯片
5. 下次使用key再次获取内容

---

## HTML5特性

---

### pushState

无跳转对浏览器状态进行刷新，可以改变浏览器地址栏的内容和历史浏览记录，比如：

```javascript
	var refresh_state = function(tid) {
			var state = ({
					url: '/write/'+tid,
					title: document.title
			});
			
			window.history.pushState(state, state.title, state.url);
	}
```

这段代码会将浏览器的地址栏更新为url所指定的地址，并且设置浏览器状态，每当我们新建一个writeboard时会将当前页面的URL修改分享时所发布的正确链接。

---

### localStorage

HTML5提供了高达5M的本地存储空间，用来解决使用Cookie作为本地存储所导致的客户端-服务器端通讯压力。

```javascript
	localStorage.setItem(key, value);
	localStorage.getItem(key);
```

我们每隔十秒会自动保存书写内容到localStorage里，下次会优先读取localStorage里的内容。

---

## 关于我们

Writeboard由OSorce Team的两名成员，Yufei Li 和 Aisling Bai编写，我们都是CS大三本科生。程序是我们思想的延伸，同时也是智慧的桥梁。

---

### Yufei Li

![Yufei Li](https://avatars1.githubusercontent.com/u/9150374?v=3&s=120)

Python爱好者，思维方法，知识计算

### Aisling Bai

![Aisling Bai](http://ohoo.thxminds.com/static/image/1.png)

萌萌哒小菇凉，充满艺术细菌，逻辑控，GPA杀手

---

## Contact us

1. yufei@thxminds.com
2. [Github][] 上提交issue.

---

Thank you~!

[editor]: https://github.com/lepture/editor
[reveal.js]: https://github.com/hakimel/reveal.js
[Github]: http://github.com/yufeiminds/writeboard
[Coding]: http://coding.net/aisling/WriteBoard
