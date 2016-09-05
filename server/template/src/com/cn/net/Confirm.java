package com.cn.net;

import java.io.IOException;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

import cn.itcast.utils.JDBCUtils;

import com.mchange.v2.c3p0.ComboPooledDataSource;

public class Confirm extends HttpServlet {

	public void doGet(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {
		doPost(request, response);
	}

	public void doPost(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {
		request.setCharacterEncoding("utf-8");
		HttpSession session = request.getSession();
		List<Map<String, String>> lmMaps = (List<Map<String, String>>) session
				.getAttribute("list");
		ComboPooledDataSource dataSource = new ComboPooledDataSource("jdbc");
		Connection conn;
		try {
			conn = dataSource.getConnection();
			String sql = "select role from user where username=?";
			PreparedStatement stmt = conn.prepareStatement(sql);
			stmt.setString(1, (String) request.getSession()
					.getAttribute("user"));
			ResultSet rs = stmt.executeQuery();
			if (rs.next()) {
				if (rs.getString("role").equals("admin")) {

					for (Map<String, String> map : lmMaps) {
						String paramString = map.get("circle_name");
						String vaString = request.getParameter(paramString);
						System.out.println(paramString + ":" + vaString);
						sql = "update circle set result=" + vaString
								+ " where circle_name=?";
						stmt = conn.prepareStatement(sql);
						// stmt.setString(1, vaString);
						stmt.setString(1, paramString);
						int index = stmt.executeUpdate();
						if (index > 0) {
							sql = "select result,circle_name,circle_creator,circle_jibie,reason,ioc from circle";
							stmt = conn.prepareStatement(sql);
							ResultSet rS = stmt.executeQuery();
							List<Map<String, String>> lMaps = new ArrayList<Map<String, String>>();
							Map<String, String> dataMap = new HashMap<String, String>();
							while (rS.next()) {
								dataMap.put("circle_name",
										rS.getString("circle_name"));
								dataMap.put("circle_creator",
										rS.getString("circle_creator"));
								dataMap.put("circle_jibie",
										rS.getString("circle_jibie"));
								dataMap.put("reason", rS.getString("reason"));
								dataMap.put("ioc",
										"./img/" + rS.getString("ioc"));
								if (rS.getString("result").equals("1")) {
									dataMap.put("result", "同意");
								} else if (rS.getString("result").equals("2")) {
									dataMap.put("result", "拒绝");
								}
								lMaps.add(dataMap);
								dataMap = new HashMap<String, String>();
							}
							rS.close();
							stmt.close();
							request.setAttribute("list", lMaps);

						}
					}
					request.getRequestDispatcher("./main2.jsp").forward(
							request, response);
				} else {
					request.getRequestDispatcher("./wait.jsp").forward(request,
							response);
				}
			}
			rs.close();
			JDBCUtils.release(stmt, conn);
		} catch (SQLException e) {
			e.printStackTrace();
		}
	}
}
