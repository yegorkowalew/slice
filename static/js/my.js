var aj_href = '/index-jq/';

aj_reload(aj_href);

var timerId = setInterval(function() {
  aj_reload(aj_href);
}, 3000);

function aj_reload(aj_href) {
  $.ajax({url: aj_href, success: function(html){ $("#header-page").html(html);}}); 
}

$(".menu-aj").click(function() {
	aj_href = this.href;
	aj_reload(aj_href)
	return false;});	