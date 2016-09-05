<%@ page language="java" import="java.util.*" pageEncoding="ISO-8859-1"%>
<%
	String path = request.getContextPath();
	String basePath = request.getScheme() + "://"
			+ request.getServerName() + ":" + request.getServerPort()
			+ path + "/";
%>

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head>
<base href="<%=basePath%>">

<title></title>

<meta http-equiv="pragma" content="no-cache">
<meta http-equiv="cache-control" content="no-cache">
<meta http-equiv="expires" content="0">
<meta http-equiv="keywords" content="keyword1,keyword2,keyword3">
<meta http-equiv="description" content="This is my page">
<!--
	<link rel="stylesheet" type="text/css" href="styles.css">
	-->

</head>
<SCRIPT LANGUAGE="JavaScript">
	function json(param) {
		var t = param;
		var jsonobj = eval('(' + t + ')');
		window.document.write(jsonobj.firstName);
		window.document.write(jsonobj.lastName);
	}
	/* var t = "{'firstName': 'cyra', 'lastName': 'richardson', 'address': { 'streetAddress': '1 Microsoft way', 'city': 'Redmond', 'state': 'WA', 'postalCode': 98052 },'phoneNumbers': [ '425-777-7777','206-777-7777' ] }";
	var jsonobj = eval('(' + t + ')');
	alert(jsonobj.firstName);
	alert(jsonobj.lastName);
	var t2 = "[{name:'zhangsan',age:'24'},{name:'lisi',age:'30'},{name:'wangwu',age:'16'},{name:'tianqi',age:'7'}] ";
	var myobj = eval(t2);
	for ( var i = 0; i < myobj.length; i++) {
		alert(myobj[i].name);
		alert(myobj[i].age);
	}
	var t3 = "[['<a href=# onclick=openLink(14113295100,社旗县国税局桥头税务所,14113295100,d6d223892dc94f5bb501d4408a68333d,swjg_dm);>14113295100</a>','社旗县国税局桥头税务所','社旗县城郊乡长江路西段']]";
	//通过eval() 函数可以将JSON字符串转化为对象 
	var obj = eval(t3);
	for ( var i = 0; i < obj.length; i++) {
		for ( var j = 0; j < obj[i].length; j++) {
			alert(obj[i][j]);
		}
	} */
</SCRIPT>
<body>
	<table>
		<tr>
			<td><input type="text" name="json" onclick="json({'firstName': 'cyra', 'lastName': 'richardson', 'address': { 'streetAddress': '1 Microsoft way', 'city': 'Redmond', 'state': 'WA', 'postalCode': 98052 },'phoneNumbers': [ '425-777-7777','206-777-7777' ] })"/></td>
		</tr>
	</table>
</body>
</html>
