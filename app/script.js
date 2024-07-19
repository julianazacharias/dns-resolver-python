function resolveDNS() {
	var domain = document.getElementById("domainInput").value.trim();
	if (domain === "") {
		alert("Please enter a domain name.");
		return;
	}

	var xhr = new XMLHttpRequest();
	xhr.open(
		"GET",
		"http://localhost:8000/resolve?domain=" + encodeURIComponent(domain),
		true
	);
	xhr.onload = function () {
		if (xhr.status === 200) {
			var response = JSON.parse(xhr.responseText);
			displayResults(response);
		} else {
			alert("Failed to resolve DNS. Please try again.");
		}
	};
	xhr.onerror = function () {
		alert("Failed to make the request. Please try again later.");
	};
	xhr.send();
}

function displayResults(data) {
	var resultsDiv = document.getElementById("results");
	resultsDiv.innerHTML = ""; // Clear previous results

	for (var type in data) {
		if (data.hasOwnProperty(type)) {
			var servers = data[type];
			var header = document.createElement("h3");
			header.textContent = type + ": " + servers.length + " items";
			resultsDiv.appendChild(header);

			var ul = document.createElement("ul");
			servers.forEach(function (server) {
				var li = document.createElement("li");
				li.textContent = server;
				ul.appendChild(li);
			});
			resultsDiv.appendChild(ul);
		}
	}
}
