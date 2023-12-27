import urllib.request

# 下载一个网页
url_page = 'http://www.baidu.com'
urllib.request.urlretrieve(url_page, 'baidu.html')
# 方法内容url代表下载的路径，filename代表文件名字

# 下载图片
url_img = 'https://tse2-mm.cn.bing.net/th/id/OIP-C.DEDs56Wojg6GrMPs9Bhx7AHaEK?w=310&h=180&c=7&r=0&o=5&dpr=1.3&pid=1.7'
urllib.request.urlretrieve(url_img, 'ylnx.jpg')

# 下载视频
url_video = 'http://flv4mp4.people.com.cn/videofile2/FLV/2015/4/29/57298B65-A05B-4D18-A40F-C3D070EAA469_android_c.mp4'
urllib.request.urlretrieve(url_video, 'ylnx.mp4')