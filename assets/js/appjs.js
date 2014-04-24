$(document).ready(function() {
	$('#submit').prop('disabled',true);
	$('#captchaverify').click(function() {
		$('#responsestring').load('/verify/'+$('#captchacode').val()+'/', function( response, status, xhr ) {
			if ( response == "Verified Human!!!" )
				$('#submit').prop('disabled',false);						
		});
	});
	$('#sametemp').click(function() {
		$('#permanent').slideToggle(1000);
		if($(this).prop('checked')) {
			$('#line1perm').val($('#line1').val());
			$('#line2perm').val($('#line2').val());
			$('#stateperm').val($('#state').val());
			var state_name = $('#stateperm').val().replace(' ','%20');
			$('#cityperm').load('/data/'+state_name+"/")
			$('#cityperm').val($('#city').val());
			$('#pinperm').val($('#pin').val());
		}
	});
	$('#state').on('change',function() {
		var state_name = $(this).val().replace(/ /g,'%20');
		console.log(state_name);
		$('#city').load('/data/'+state_name+"/");
	});
	$('#stateperm').on('change',function() {
		var state_name = $(this).val().replace(/ /g,'%20');
		$('#cityperm').load('/data/'+state_name+"/");
	});
	$('.textcomponent').each(function(index, element) {
		var $element = $(element);
		var defaultValue = $element.val();
		$element.focus(function() {
			var actualValue = $element.val();
			if (actualValue == defaultValue) {
				$element.val('');
			}
		});
		$element.blur(function() {
			var actualValue = $element.val();
				if (!actualValue) {
					$element.val(defaultValue);
				}
		});
	});
});
