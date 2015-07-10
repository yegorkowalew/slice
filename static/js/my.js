$.ajax({
	url: "/index-jq/",
	success: function(html){
    $("#header-page").append(html);
  }
});

$("#acces_log").click(function() {
	$.ajax({
		url: "/index-jq/",
		success: function(html){
    	$("#header-page").html(html);

  								}
			}); return false;
							});