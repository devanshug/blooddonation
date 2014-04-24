function captchas_image_error (image)
{
	if (!image.timeout) return true;
	image.src = image.src.replace (/^http:\/\/image\.captchas\.net/,'http://image.backup.captchas.net');
	return captchas_image_loaded (image);
}
function captchas_image_loaded (image)
{
	if (!image.timeout) return true;
	window.clearTimeout (image.timeout);
	image.timeout = false;
	return true;
}
var image = document.getElementById (cap_id);
image.onerror = function() {return captchas_image_error (image);};
image.onload = function() {return captchas_image_loaded (image);};
image.timeout = window.setTimeout("captchas_image_error (document.getElementById (cap_id))",10000);
image.src = image.src;
