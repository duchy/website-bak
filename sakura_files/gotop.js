var $win = $(window);
var $top = $("#gotop");
$win.scroll(function(){
 setInterval(showTop,100); 

})

//Can we show this button?
function showTop() {

    if (!window.XMLHttpRequest) {
        $top .css("top", $win.scrollTop()+$win.height()-45);
    }
    if($win.scrollTop() > 400) {

        $top .show()
    }
    else {
        $top .hide()
    };
}