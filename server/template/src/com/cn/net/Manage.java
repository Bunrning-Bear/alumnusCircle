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

import com.mchange.v2.c3p0.ComboPooledDataSource;

public class Manage extends HttpServlet {

	public void doGet(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {
		doPost(request, response);
	}

	public void doPost(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {
		String sql = "select circle_name,circle_creator,circle_jibie,reason,ioc from circle where result=?";
		ComboPooledDataSource dataSource = new ComboPooledDataSource("jdbc");
		Connection conn;
		try {
			conn = dataSource.getConnection();
			PreparedStatement stmt = conn.prepareStatement(sql);
			stmt = conn.prepareStatement(sql);
			stmt.setString(1, "0");
			ResultSet rS = stmt.executeQuery();
			List<Map<String, String>> lMaps = new ArrayList<Map<String, String>>();
			Map<String, String> dataMap = new HashMap<String, String>();
			while (rS.next()) {
				dataMap.put("circle_name", rS.getString("circle_name"));
				dataMap.put("circle_creator", rS.getString("circle_creator"));
				dataMap.put("circle_jibie", rS.getString("circle_jibie"));
				dataMap.put("reason", rS.getString("reason"));
				dataMap.put("ioc", "./img/" + rS.getString("ioc"));
				lMaps.add(dataMap);
				dataMap = new HashMap<String, String>();
			}
			rS.close();
			request.getSession().setAttribute("list", lMaps);
			request.getRequestDispatcher("./confirm.jsp").forward(request,
					response);
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}

	}

}
