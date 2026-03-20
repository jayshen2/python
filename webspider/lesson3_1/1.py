from lxml import etree
html = etree.parse(r"C:\Users\29433\Desktop\实例文件\test.html")
zhiwei =html.xpath("//div/span/a/text()")
print(zhiwei)