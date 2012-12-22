#!/usr/bin/env python
#coding=utf-8

import cgi
import time
from txt2png import picChecker

form = cgi.FieldStorage()
name = form.getfirst('name', 'empty')
# Avoid script injection escaping the user input
name = cgi.escape(name)

c = picChecker(foregroundColor=(12, 54, 108)) 
res = c.createChecker(name)
pngurl = "http://eqbaobei.com/" + res['imgaddr']
pngtitle = res['title'] + "by txt2png"

print "Content-Type: text/html"
print "charset: utf-8"
print
print """\
<!--meta http-equiv="Content-Type" content="text/html; charset=utf-8"/-->
<html>
<head>
    <title>%s</title>

    <style type="text/css">
    #content	{clear:both; height:240px; position:relative; text-align:center}
    </style>

</head>
<body>
    <div id="content">
        <script type="text/javascript" charset="utf-8">
        (function(){
            var _w = 142 , _h = 66;
            var param = {
                url:'', //'http://eqbaobei.com/cgi-bin/txt2pic.py', /**location.href,*/
                type:'4',
                count:'1', /**是否显示分享数，1显示(可选)*/
                appkey:'3505588903', /**您申请的应用appkey,显示分享来源(可选)*/
                title:'', /**分享的文字内容(可选，默认为所在页面的title)*/
                pic:'%s', /**分享图片的路径(可选)*/
                ralateUid:'2957048762', /**关联用户的UID，分享微博会@该用户(可选)*/
	        language:'zh_cn', /**设置语言，zh_cn|zh_tw(可选)*/
                rnd:new Date().valueOf()
            }
            var temp = [];
            for( var p in param ){
                temp.push(p + '=' + encodeURIComponent( param[p] || '' ) )
            }
            document.write('<iframe allowTransparency="true" frameborder="0" scrolling="no" src="http://hits.sinajs.cn/A1/weiboshare.html?' + temp.join('&') + '" width="'+ _w+'" height="'+_h+'"></iframe>')
        })()
        </script>
        <p>转换完成 (共计 %s 字符)</p>
        <img src="%s"></img>
    </div>
</body>
</html>
""" % (res['title'], pngurl, res['length'], pngurl)
#""" % (res['summary'], res['length'], pngurl)
