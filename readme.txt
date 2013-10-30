*** renamer.pyの使い方 ***
* ファイル名を一括変更するコマンド
*
*   date: 2013/10/30
* author: Fujiruki(http://suntree.orsp.net/)
* * * * * *

【主な使い方】
次のようなテキストファイル'name.txt'を準備します。
これはTab区切りです。
Excelからの貼り付けで作ることができます。
+---( name.txt )----------------------
|oldname.txt	newname.txt
|old.txt	new.txt
|

	python renamer.py name.txt
このコマンドで、同じフォルダに存在するファイルは、
	'oldname.txt' --> 'newname.txt'
	'old.txt'     --> 'new.txt'
のようにリネームされます。

【例外のときの動作】
・変換前のファイル名のいずれかが存在しない
	なにも処理をせず終了します。
・変換後のファイルがすでに存在する
	すでに存在したファイル以外をすべてリネームします。

【オプション】
・'-r'
	デフォルトではテキストの1列目を元ファイル名、2列目を新ファイル名とします。
	しかしこのオプションをつけると、それが逆転します。
		    (1列目:元ファイル名, 2列目:新ファイル名)
		==> (2列目:元ファイル名, 1列目:新ファイル名)

	例) python renamer.py name.txt -r

・'-icol', '--input_column'
	元ファイル名の列番号を数字で指定します。
	デフォルト: 1

	例) python renamer.py name.txt -icol 2 -ocol 3

・'-ocol', '--output_column'
	新ファイル名の列番号を数字で指定します。
	デフォルト: 2

	例) python renamer.py name.txt -icol 2 -ocol 3

・'-r' & '-icol', '-ocol'
	-rオプションは、-icol, -ocolオプション適用後に適用されます。
	つまり、次の２つの例は同じ動作になります。
	例) python renamer.py name.txt -icol 2 -ocol 3
	例) python renamer.py name.txt -icol 3 -ocol 2	-r
