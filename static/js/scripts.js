if (window.pspmizzou === undefined) {
	pspmizzou = (function() {
		return {
		}
	})(); // Initialize pspmizzou namespace if not defined
}

$(function() {
	
	$("#login").delegate("input[name=user], input[name=pass]", "focus", function(e) {
		if (this.name == "user" && this.value == "Username") this.value = "";
		if (this.name == "pass" && this.value == "Password") this.value = "";
	});
	
	$("#login").delegate("input[name=user], input[name=pass]", "blur", function(e) {
		if (this.name == "user" && this.value == "") this.value = "Username";
		if (this.name == "pass" && this.value == "") this.value = "Password";
	});
	
	$("#menu_links").delegate("a.quickview", "click", function(e) {
		var link = this.innerHTML;
		var url = this.href;
		//$("#menu_preview").show("normal");
		$.ajax({
			url: "/" + link.toLowerCase() + "/quickview",
			success: function(data) {
				$("#menu_preview_loader").hide();
				$("#menu_preview").html(data);
				$("#menu_preview").show("normal");
			},
			error: function() {
				// If the quickview can't be loaded via ajax, follow the link
				document.location.href = url;
			}
		});
		return false; // Progressive enhancement -- prevent link
	});
});
