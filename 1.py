import re
html_text = """ 
<div class="poem"> 
<h2>静夜思</h2><p class="author">李白</p> 
<div class="content">床前明月光<br/>疑是地上霜</div> 
</div> 
"""

bt = re.findall(r"<h2>(.*?)</h2>",html_text)
zz = re.findall(r"<p.*?>(.*?)</p>",html_text)
zw = re.findall(r'<div class="content">(.*?)</div>',html_text)[0]
zw_new = re.sub(r'<br/>',"\n",zw)
print(bt)
print(zz)
print(zw_new)