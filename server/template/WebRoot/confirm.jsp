<%@ page language="java" import="java.util.*" pageEncoding="utf-8"%>
<%@taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
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

<title>管理员界面</title>

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
<center>
	<h1>确认圈子</h1>
	<hr>
	<form action="./confirm" method="post">
		<table border="0" align="center" width="60%" height="20%"frame="box" rules="rows">
			<tr>
				<td>圈子图标</td>
				<td>圈子名称</td>
				<td>圈子级别</td>
				<td>创建人</td>
				<td>创建理由</td>
				<td></td>
			</tr>
			<c:forEach items="${list }" var="map">
				<tr>
					<td><img src="${map.ioc }" width="40px" height="60px" /></td>
					<td>${map.circle_name }</td>
					<td>${map.circle_jibie }</td>
					<td>${map.circle_creator }</td>
					<td>${map.reason }</td>
					<td><select name=${map.circle_name } id=${map.circle_name }>
							<option value="1">确认</option>
							<option value="2">拒绝</option>
					</select></td>
				</tr>
			</c:forEach>
			<tr>
				<td colspan="6" align="center"><input type="submit" value="提交" /></td>
			</tr>
		</table>
	</form>
	</center>
</body>
</html>