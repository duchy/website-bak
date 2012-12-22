#!/usr/bin/env python
#coding=utf-8

print "Content-Type: text/html"
print "charset: utf-8"
print
print """\
<!--meta http-equiv="Content-Type" content="text/html; charset=utf-8"/-->
<html>

<head>

<style type="text/css">
#floater	{float:left; height:50%; margin-bottom:-120px;}
#top		{float:right; width:100%; text-align:center;}
#content	{clear:both; height:240px; position:relative; text-align:center}

.textbox {overflow:auto; }

</style>

<!--
<Script Language="JavaScript">
function borderColor()
{
    if(self['oText'].style.borderColor=='red')
    {
        self['oText'].style.borderColor = 'yellow';
    }
    else
    {
        self['oText'].style.borderColor = 'red';
    }

    oTime = setTimeout('borderColor()',400);
}
</Script>
-->
</head>

<body>

<div id="top">
<h1>Text2PNG 将文字转成图片</h1>
</div>
<div id="content">
    请在下面输入要转换的文本(Input the text below)
    <form method="POST" action="process_form.py" enctype="multipart/form-data">
        <!--input type="text" name="name"-->

        <!--textarea name="name" rows="40" cols="100" onpropertychange="if(this.scrollHeight>80) this.style.posHeight=this.scrollHeight+5"></textarea-->
        <textarea name="name" rows="30" cols="100" class="textboox"></textarea>

        <!--input type="text" id="oText" name="name" style="border:5px dotted red;color:red" onfocus="borderColor(this);" onblur="clearTimeout(oTime);"-->

	<div><input type="submit" value="转成图片"></div>
	<div><P>Copyright ©2012 <a href="http://www.eqbaobei.com"><B>eqbaobei.com<B></a></div>
    </form>
</div>
</body></html>
"""
