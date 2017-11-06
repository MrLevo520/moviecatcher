#!/usr/bin/env python
# -*- coding: utf-8 -*-
import Tkinter
import tkMessageBox
import webbrowser
import MenuBarView
from Lib import Tools
from Bl import Search
from Da import AppBase
from Da import Config

class GUI :

	def __init__ (self) :
		self.Tools = Tools.Tools()
		self.winTitle = AppBase.info['title']
		self.__mainWindow()  # 这个初始化的时候就有很多操作

	def __mainWindow (self) :
		# master是TK框架的一个主线索，GUI的配置项都是从master着手
		self.master = Tkinter.Tk()

		self.master.title(self.winTitle)
		self.master.resizable(width = 'false', height = 'false')
		if self.Tools.isWin() :  # 避免因为系统的原因导致获取不到图标
			self.master.iconbitmap(self.Tools.getRes('biticon.ico'))

		self.__topBox()  

		self.Cfg = Config.Config()
		if self.Cfg.connStat :
			menuBar = MenuBarView.GUI(self.master)
			menuBar.show()
		else :
			tkMessageBox.showinfo('Error', '创建配置文件失败。\r\n请检查「~/Library/Application Support」文件夹是否有操作权限！')

	def __topBox (self) :
		# TK框架里面的内容安排
		self.mainTop = Tkinter.Frame(self.master, bd = 0, bg="#444")
		self.mainTop.pack(expand = True, fill = 'both', ipady = 5)

		self.searchKey = Tkinter.Entry(self.mainTop, 
										width = 40, 
										bd = 0, 
										bg = "#222", 
										fg = "#ddd",
										highlightthickness = 1, 
										highlightcolor="#111", 
										highlightbackground = '#111', 
										selectbackground = '#116cd6', 
										justify='center')
		self.searchKey.grid(row = 0, column = 1, padx = '10', pady = '20')
		self.searchKey.insert('end', '电影名/电视剧名')
		self.searchKey.bind('<FocusIn>', self.__cleanSearchKey)  # 事件监听绑定

		Searcher = Search.Search(self.master)  # 实例化search类
		self.sBtn = Tkinter.Button(self.mainTop, 
								text = '观看/下载', 
								width = 10, 
								fg = '#222', 
								highlightbackground = '#444', 
								command = lambda key = self.searchKey : 
								tkMessageBox.showinfo('Error', '请输入想要查询的电视剧/电影名再进行查询') if self.searchKey.get() == u'电影名/电视剧名' or self.searchKey.get() == '' 
								else Searcher.showResult(key))
		self.sBtn.grid(row = 1, column = 1, sticky='W',padx='10',columnspan=2)

		# 豆瓣影评栏
		self.sBtn_douban = Tkinter.Button(self.mainTop, 
								text = '豆瓣影评', 
								width = 10, 
								fg = '#222', 
								highlightbackground = '#444', 
								command = lambda key = self.searchKey : 
								webbrowser.open_new('https://movie.douban.com/') if self.searchKey.get() == u'电影名/电视剧名' or self.searchKey.get() == '' 
								else Searcher.showDBResult(key))
								# 这里传递打破search的类里面，会用到enter的get方法获取值
		self.sBtn_douban.grid(row = 1, column = 1,padx='10')

		# 豆瓣影评栏
		self.sBtn_zhihu = Tkinter.Button(self.mainTop, 
								text = '知乎话题', 
								width = 10, 
								fg = '#222', 
								highlightbackground = '#444', 
								command = lambda key = self.searchKey : 
								webbrowser.open_new('https://www.zhihu.com/search?type=content&q=%E6%9C%89%E5%93%AA%E4%BA%9B%E5%A5%BD%E7%9C%8B%E7%9A%84%E5%BD%B1%E8%A7%86') if self.searchKey.get() == u'电影名/电视剧名' or self.searchKey.get() == '' 
								else Searcher.showZHResult(key))
								# 这里传递打破search的类里面，会用到enter的get方法获取值
		self.sBtn_zhihu.grid(row = 1, column = 1, sticky='E',padx='10')


		self.mainTop.grid_columnconfigure(0, weight=1)
		self.mainTop.grid_columnconfigure(2, weight=1)

	def __cleanSearchKey(self, e) : 
		key = self.searchKey.get() # 获取文件框的值

		if key == u'电影名/电视剧名' :
			self.searchKey.delete('0', 'end') # 删除所有值

	def run (self) :
		self.master.mainloop()  # tk的基本格式，启动

# 入口在BI的App.py里