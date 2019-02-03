# jinzhongbao

 爬取金中宝公众号的交易数据



启动文件为`jinzhongbao_requests.py`文件，抓取到的数据会存放到 `data.py`文件，最后处理好的数据会写入`trading_record.xls`文件中。



启动文件内所需的变量都放在了 `config.py`内，内含敏感数据，未传至 `github`，需要时请自行配置。主要变量包括：

`url`、`User_Agent`、`language`、`Content_Type`、`transaction_date_list`、`requests_data`、`requests_cookies`



## 问题场景

使用金中保每次交易之后都需要保存小票，比较烦，实际上公众号提供了小票下载功能，但是需要点进每条记录手动点击下载然后保存图片，大量批量交易的话就会比较繁琐，有没有什么办法可以一键保存所有交易的小票呢？



## 主要功能

抓取金中保公众号所有交易记录的小票



## 思路

1. 通过抓包分析得出，小票图片的的 url 不需要 cookie，就可以访问；
2. 所以只要得的小票的 url 就可以了；
3. 用 chrome 模拟微信登录金中保公众号，进入小票页面，发现小票的 url 是由 JavaScript 生成的；
4. 进入 chrome 的控制台的 Sources，交叉分析所有 js 文件发现，小票的 url 是由前缀 + THUUID 生成的，THUUID 为交易记录的一项内容；
5. 所以只需要得到所有交易记录的 JSON 对象就行了，这正是服务器返回回来的数据。



> 实际上之前走了弯路，之前是这么想的：
>
> 1. 模拟登陆进入到交易记录列表页面；
>
> 2. 从交易记录列表页面得到交易记录详情页面的 url；
>
>    （其实交易记录详情页面的 url 并没有什么用，只是得到而已，后面并没有用上，但是奈何获得整个花了好几天的时间，删掉可惜啊，就留下了。）
>
> 3. 再从交易记录详情页面得到小票的 url。
>
> 但是**交易记录详情页面**和**小票的 url**都是由 JavaScript 生成，所以 request 没办法获取，只能另想别的办法。
>
> 之前没有分析 js 文件，也强行将交易记录详情页面的 url 生成出来了，使用`libs.generate_trade_url`方法，不过该方法太繁琐，但是好在是用 Python 实现的，比 Python 内调用 JavaScript 函数性能好。



## 效果图

![image-20190203201212073](https://ws3.sinaimg.cn/large/006tNc79gy1fzthvu4qr0j30m20imae7.jpg)