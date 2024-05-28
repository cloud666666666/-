#后台启服务器
echo "server staring..."
nohup python  -u ../app.py > server.log 2>&1 & 
sleep 3
echo "server started!"

sleep 1 
#后台启爬虫
echo "spider staring..."
nohup python  -u spider.py > spider.log 2>&1 & 
sleep 2 
echo "spider started!"
sleep 1
#启面板
echo "loading page..."
python control_page_by_shell.py 
