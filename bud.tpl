<!DOCTYPE html>
	<html>
	<head>
		<title></title>
		<link rel="stylesheet" type="text/css" href="">
		<style>#grad{
	background: linear-gradient(magenta, powderblue);
}</style>
	</head>
	<body>
	<div id="grad">
	% rebase('base.tpl')
	<h2>Fyrirsögn</h2>
	<div>
	    % for i in range(len(products)):
	       <p> <a href="/cart/add/{{ products[i]["pid"] }}"> {{ products[i]["name"] }} </a> </p>
	    % end
	</div>
	</form>
	</div>
	</body>
	</html>