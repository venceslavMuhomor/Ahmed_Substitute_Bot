# Ahmed substitute bot

Telegram bot for sending naughty photos of girls daily.

### How to send girl photo
```sh
$ git clone https://github.com/venceslavMuhomor/Ahmed_Substitute_Bot
$ docker build -t ahmed-bot .
$ docker run -e TOKEN=<token> -e CHAT_IDS=<chat ids> 
 -e reddit_clientid=<reddit_clientid> -e reddit_secret=<reddit_secret> 
 -e subs_list=<subs_list> --name bot ahmed-bot
```

### Environment variables bot

| Key               | Description                          | Example value                                  |
|:------------------|:-------------------------------------|:-----------------------------------------------|
| `TOKEN`           | Telegram bot token                   | 239843023:ABFGC11nC7C6IF3le29yl9u4fJJeV2Ts4z19 |
| `CHAT_IDS`        | Telegram chat id list                | -209572499,-10438139                           |
| `reddit_clientid` | clientid from reddit app             | applicationid                                  |
| `reddit_secret`   | secret from reddit app               | some secret                                    |
| `subs_list`       | names of reddit subreddits for parse | sub1, sub2, sub3                               |


