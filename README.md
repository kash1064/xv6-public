
## ビルド

1. 必要なモジュールのインストール

``` bash
sudo apt-get update
sudo apt-get install build-essential gcc-multilib qemu 
```

2. ソースファイルのダウンロード

``` bash
git clone https://github.com/kash1064/xv6-public
cd xv6-public/src
```

3. ビルド

``` bash
make
make qemu
```

参考：[xv6をインストール - 技術メモ](https://shuntavista.jimdofree.com/2017/11/29/xv6%E3%82%92%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB/)