import thulac

thu1 = thulac.thulac(seg_only=True, filt=True)  #默认模式
text = thu1.cut("我爱北京天安门，天安门上太阳升，卧槽泥马勒戈壁，我到底是谁", text=True)  #进行一句话分词
print(text)