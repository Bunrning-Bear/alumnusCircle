<%@ page language="java" import="java.util.*" pageEncoding="utf-8"%>
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

<title>创建圈子</title>

<meta http-equiv="pragma" content="no-cache">
<meta http-equiv="cache-control" content="no-cache">
<meta http-equiv="expires" content="0">
<meta http-equiv="keywords" content="keyword1,keyword2,keyword3">
<meta http-equiv="description" content="This is my page">
<!--
	<link rel="stylesheet" type="text/css" href="styles.css">
	-->

</head>

<body>
<h1>创建圈子</h1>
<hr>
	<form action="./builder" method="post" enctype="multipart/form-data">
		<table>
			<tr>
				<td>圈子图表</td>
				<td><input type="file" name="file" /></td>
			</tr>
			<tr>
				<td>圈子名称</td>
				<td><input type="text" name="name" /></td>
			</tr>
			<tr>
				<td>圈子创建人</td>
				<td><input type="text" name="username" /></td>
			</tr>
			<tr>
				<td>圈子级别</td>
				<td><input type="text" name="jibie"/>(A、B、C)</td>
			</tr>
			<tr>
				<td>圈子创建理由</td>
				<td><textarea cols="10" rows="8" name="reason"></textarea></td>
			</tr>
			<tr>
			<td colspan="1"><input type="submit" value="提交" /></td>
			</tr>
		</table>
	</form>
</body>
</html>
