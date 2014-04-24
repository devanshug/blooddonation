$(document).ready(function() {
	$('#fillform').submit(function(event) {
		//State validation
		if($('#state').length) {
			if($('#state').val()=='') {
				$('#error').text('Please select your state');
				return false;
			}
		}

		//Name Validations
		if($('#username').length) {
			var username = $('#username').val();
			if( username.length < 2) {
				$('#error').text('Doesn\'t sound like a valid username, please check!!!');
				return false;
			}
			if(!username.match(/^[a-zA-Z]+$/)) {
				$('#error').text('Invalid UserName must match ^[a-zA-Z]+$');
				return false;
			}
			
			//Check if username exists
			function doSomethingWithData(data) {
				if ( data == "Username Exists" ) {
					$('#error').text(data);
					return false;
				}
			}

			$.get('/exists/'+$('#username').val()+'/', doSomethingWithData);
		}

		if($('#name').length) {
			var name = $('#name').val();
			if( name.length < 2) {
				$('#error').text('Doesn\'t sound like a valid name, please check!!!');
				return false;
			}
			if(!name.match(/^[a-zA-Z ]+$/)) {
				$('#error').text('Invalid Name must match ^[a-zA-Z ]+$');
				return false;
			}
		}
		
		if($('#firstname').length) {
			var firstname = $('#firstname').val();
			if(firstname.length<2) {
				$('#error').text('Doesn\'t sound like a valid First Name, please check!!!');
				return false;
			}
			if(!firstname.match(/^[a-zA-Z]+$/)) {
				$('#error').text('Invalid First Name must match ^[a-zA-Z]+$');
				return false;
			}
		}
		
		if($('#lastname').length) {
			var lastname = $('#lastname').val();
			if(lastname.length<2) {
				$('#error').text('Doesn\'t sound like a valid Last Name, please check!!!');
				return false;
			}
			if(!lastname.match(/^[a-zA-Z]+$/)) {
				$('#error').text('Invalid Last Name must match ^[a-zA-Z]+$');
				return false;
			}
		}

		if($('#password1').length)
		{
			if($('#password1').val()!=$('#password2').val()) {
				$('#error').text('Passwords Entered do not match, Please check again');
				return false;
			}
		}

		//Email Validation
		//The regex used is from reference http://stackoverflow.com/questions/2507030/email-validation-using-jquery
		if($('#email').length) {
			var email = $('#email').val();
			var emailReg = /^([\w-\.]+@([\w-]+\.)+[\w-]{2,4})?$/;
			if( !emailReg.test(email) ) {
				$('#error').text('Invalid Email must match ^([\w-\.]+@([\w-]+\.)+[\w-]{2,4})?$');
				return false;
			}
		}

		//Date Validation
		if($('#day').length) {
			var day = $('#day').val();
			var month = $('#month').val();
			var year = $('#year').val();
			if(month==2)
			{
				if((year%100==0 && year%400!=0) || year%4!=0) {
					if(day>28) {
						$('#error').text("Wrong date");
						return false;
					}
				}
				else
				{
					if(day>29) {
						$('#error').text("Wrong date");
						return false;
					}
				}
			}
			else if(month<=7){
				if(day==31 && month%2==0) {
					$('#error').text("Wrong date");
					return false;
				}
			}
			else	{
				if(day==31 && month%2==1) {
					$('#error').text("Wrong date");
					return false;
				}
			}
		}

		//Contact validation
		if($('#mobile').length) {
			var mobile = $('#mobile').val();
			if(mobile.length!=10) {
				$('#error').text('Number should be of 10 digit');
				return false;
			}
			if(!mobile.match(/^[0-9]+$/)) {
				$('#error').text('Invalid Number must match ^[0-9]+$');
				return false;
			}
		}
		if($('#landline').length) {
			var landline = $('#landline').val();
			if(!landline.match(/^[0-9]+$/)) {
				$('#error').text('Invalid Landline Number must match ^[0-9]+$');
				return false;
			}
		}
	})
});
