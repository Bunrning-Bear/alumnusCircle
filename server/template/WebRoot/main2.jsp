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

<title>主页面</title>

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
	<h1>圈子列表</h1>
	<hr>
	<table border="0" width="60%" height="20%" frame="box" rules="rows">
			<tr>
				<td>圈子图标</td>
				<td>圈子名称</td>
				<td>圈子级别</td>
				<td>创建人</td>
				<td>创建理由</td>
				<td>审核状态</td>
			</tr>
			<c:forEach items="${list }" var="map">
			<tr>
				<td><img src="${map.ioc }"width="40px" height="60px"/></td>
				<td>${map.circle_name }</td>
				<td>${map.circle_jibie }</td>
				<td>${map.circle_creator }</td>
				<td>${map.reason }</td>
				<td>${map.result }</td>
				</tr>
			</c:forEach>
		</table>
	<!-- <font face="宋体" size=4 color="blue">如果没有你想要加入的圈子，定点击<a href="builder.jsp">创建圈子</a>!!!</font> -->
	</center>
</body>
</html>
