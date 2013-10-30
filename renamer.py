#! /usr/bin/python
#! -*- coding: utf-8 -*-

#ディレクトリ内の任意のファイルを別のファイル名に変更する。
#引数：テキストファイル。1列目に元ファイル名、2列目に新しいファイル名
#元ファイル名が存在しなければ警告表示してスキップ。
#新ファイル名が存在すれば警告表示してスキップ
import sys
import os
import re
from StringIO import StringIO
import csv
import argparse

def conv_table_from_tabfile(filename):
	table = []
	for line in open(filename, 'r'):
		itemList = line[:-1].split('\t')
		table.append(itemList)
	return table

# tableのcol列をファイル名として存在をしらべ、全て存在すればTrueを返す
def check_exists_by_column(table, col):
	is_exist_all = True
	for line in table:
		fname = line[col]
		if (not os.path.exists(fname)):
			print "このファイルは存在しません: "+fname
			is_exist_all = False
	return is_exist_all


if __name__ == "__main__":
	#引数の解析
	parser = argparse.ArgumentParser(description="FILEの1列目のファイル名を2列目のファイル名に変換します。FILEはTab区切りです。")
	parser.add_argument('FILE', help="ファイル名変換表のファイル名")	# 引数TABLEを追加
	parser.add_argument('-icol', '--input_column', type=int, help="変換元ファイル名の列番号")
	parser.add_argument('-ocol', '--output_column', type=int, help="変換元ファイル名の列番号")
	parser.add_argument('-r', '--reverse', action='store_true', help="2列目:元ファイル名,1列目:新ファイル名")
	parser.add_argument('--version', action='version', version='renamer.py 0.1')
	args = parser.parse_args()

	# 1列目と2列目の反転フラグを確認
	f_reverse = args.reverse

	icol = args.input_column
	if (icol == None): icol = 1
	ocol = args.output_column
	if (ocol == None): ocol = 2

	if (f_reverse):
		icol, ocol = ocol, icol

	# 列番号を配列の添字にあわせる
	icol-=1;
	ocol-=1;

	
	# ファイルの指定
	filename = args.FILE
	if (None == filename):
		print "ファイル名が指定されていません。"
		sys.exit()

	print "ファイル名：" +  filename
	print "入力ファイル列:"+ str(icol)+"  出力ファイル列:"+ str(ocol)
	print "------------------------------"
	
	# ファイルから変換テーブルを作成
	convtable = conv_table_from_tabfile(filename)

	
	# リネーム元ファイルが存在するかチェック。
	is_exist_all = check_exists_by_column(convtable, icol)	
	if (not is_exist_all):
		print "存在しないファイルがあったため、処理を中止します。"
		sys.exit()
	print "元ファイル名はすべて存在しました。"
	
	# 変換テーブルにあわせてリネームを実行
	print "処理を開始します。"
	for line in convtable:
		fname_old = line[icol]
		fname_new = line[ocol]
		if (os.path.exists(fname_new)):
			print "i:o="+str(icol)+":"+str(ocol)
			print "リネーム後のファイル名が存在します！: "+fname_new+"  スキップします。"
			continue
		os.rename(fname_old, fname_new)
		print "OK: "+fname_old+" --> "+fname_new

