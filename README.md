# Ahmed substitute bot

Telegram bot for sending naughty photos of girls daily.

### How to send girl photo
```sh
$ git clone https://github.com/venceslavMuhomor/Ahmed_Substitute_Bot
$ docker build -t ahmed-bot .
$ docker run --env TOKEN=<token> --env CHAT_IDS=<chat ids> --name bot ahmed-bot
```

### Environment variables bot

| Key    | Description   |    Example value  |
| :---         |     :---      |          :--- |
| `TOKEN`  | Telegram bot token | 239842023:BBFGC10nC7C6IF3le59yl9u4fJJeV2Ts4z19              |
| `CHAT_IDS`  | Telegram chat id list  | -209572499,-10438139              |
