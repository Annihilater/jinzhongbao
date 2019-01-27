# jinzhongbao
 爬取金中宝公众号的交易数据



启动文件为`jinzhongbao_requests.py`文件，抓取到的数据会存放到 `data.py`文件，最后处理好的数据会写入`trading_record.xls`文件中。



启动文件内所需的变量都放在了 `config.py`内，内含敏感数据，未传至 `github`，需要时请自行配置。主要变量包括：

`url`、`User_Agent`、`language`、`Content_Type`、`transaction_date_list`、`requests_data`、`requests_cookies`

