if (window.pspmizzou === undefined) {
	pspmizzou = (function() {
		return {
		}
	})(); // Initialize pspmizzou namespace if not defined
}

$(function() {
	$("#menu_links").delegate("a", "click", function(e) {
		var link = this.innerHTML;
		if (link == "Home") {
			return true;
		}
		$("#menu_preview").show("normal");
		return false; // Progressive enhancement -- prevent link
	});
});
