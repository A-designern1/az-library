import  requests

req = requests.get("https://img.redbull.com/images/c_crop,x_575,y_0,h_1080,w_810/c_fill,w_400,h_540/q_auto:low,f_auto/redbullcom/2020/3/5/zdul8ghfo1hogo5jkn1e/brawl-stars")
print(req.content)
file = open('img.jpg', 'wb')
file.write(req.content)
file.close()
