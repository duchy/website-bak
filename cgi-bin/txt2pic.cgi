#!/usr/bin/env python
#coding=utf-8

print "Content-Type: text/html"
print
print """\
<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
<html xmlns:wb="http://open.weibo.com/wb">

<head>
<meta property="wb:webmaster" content="0aa89f898b09d188" />
<title>Text2Pic 文本转图片</title>
<style type="text/css">
#floater	{text-align:center}
#top		{float:right; width:100%; text-align:center}
#content	{clear:both; height:240px; position:relative; text-align:center}
.textbox {overflow:auto; }
</style>
<script src="http://tjs.sjs.sinajs.cn/open/api/js/wb.js?appkey=3505588903" type="text/javascript" charset="utf-8"></script>
</head>

<body>
    <div id="top">
        <h1>Text2Pic 将文字转成图片<wb:share-button size="middle" appkey="3505588903" relateuid="2957048762" ></wb:share-button></h1>
    </div>
    <div id="content">
        请在下面输入要转换的文本(Input the text below)
        <form method="POST" action="process.cgi" enctype="multipart/form-data">
            <textarea name="name" rows="30" cols="100" class="textboox"></textarea>
	    <div><input type="reset" value="重置">&nbsp;&nbsp<input type="submit" value="转成图片"></div>
            <div><P>Copyright ©2012 <a href="http://www.eqbaobei.com"><B>eqbaobei.com<B></a></div>
        </form>
    </div>
</body>
</html>
"""
