$(document).ready(function() {
	$('#submit').click(function() {
		var height = $('#height').val();
		var weight = $('#weight').val();
		if(height<=149 || weight<=50)
			$('#output').text("Sorry you cannot donate the blood");
		else if(height>=168 || weight>=64)
			$('#output').text("Congratulations you are eligible to donate blood");
		else if(data[$('#height').val()]['values'][$('#weight').val()]>3500)
			$('#output').text("Congratulations you are eligible to donate blood");
		else
			$('#output').text("Sorry you cannot donate the blood");
	});
});
