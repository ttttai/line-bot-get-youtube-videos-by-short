# line-bot-get-youtube-video-by-short
## 概要
2023年8月31日よりYoutubeのshortのコメントのリンクが効かない仕様になった。（[Googleより](https://support.google.com/youtube/thread/229722002)）  
そのため、Shortの固定コメントなどに貼ってある動画本編へのURLを踏むことができず、本編を見るのを断念してしまうようになってしまった。  (ブラウザ版ではURLのコピーができるがアプリ版ではできないためベタ打ちをしなければならない)  
この問題を解決し、Youtubeを使いやすくするために以下のLINEボットを作成した。

## 使い方
1. 以下のQRコードのアカウントと友達登録を行う
2. 本編のURLが固定コメントに記載されているShort動画を1のアカウントに共有する
3. 本編のURLが返信されるためそのURLから動画本編を視聴する

![QR](image/line-bot-qr.png)
