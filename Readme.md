# Font Sika

[Cica](https://github.com/miiton/Cica)から生成したビットマップフォントで置き換えます。

Cica は SIL Open Font License の Reserved Font Name なので Cica の名称は使えず、便宜的に Sika と名乗っています。
尚、配布物にはオリジナルの Cica は含んでいません。
生成には[Bitmap font generator](https://www.angelcode.com/products/bmfont/)を使用しました。

# Tips

別のフォントを使いたい方や、自分用の忘備録としてメモを残しておきます。

## 落とし穴

1. テクスチャサイズに応じて連番で png ファイルが作られるが、starsector が対応していない。
    - 1 つのファイルに収まるようにサイズを指定する必要がある。
    - Export Options -> Texture -> Width / Height
2. 文字の高さが可変だと文字がずれる。
    - Export Options -> Equalize the cell heights をチェックする。
3. Noto Sans Jp, Noto CJK Jp は starsector が謎落ちして起動しない。
    - 何かが足りない？

## 必須の設定まとめ

-   Font settings
    -   Charset: Unicode
    -   Autofit pages: 0
    -   他はお好みで
-   Export Options
    -   Equalize the cell heights: True
    -   Texture Width/Height: 1 ファイルに収まるように調整(2^n)
    -   Bit depth: 32
    -   Pack chars in multiple channels: False
    -   Chnl Value は以下の通り。Invert は全て False。
        -   A: outline
        -   R: glyph
        -   G: glyph
        -   B: glyph
    -   File Format
        -   Font descriptor: Text
        -   Textures: png

# Reference

以下を参考にしました。

-   [Alex の投稿](https://fractalsoftworks.com/forum/index.php?topic=17921.msg281079#msg281079)
-   [How to change the font used in game](https://fractalsoftworks.com/forum/index.php?topic=5481.0)

# ソース

https://github.com/hirmiura/starsector-mod-Font_Sika
