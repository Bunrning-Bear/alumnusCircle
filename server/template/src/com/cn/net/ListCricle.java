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

public class ListCricle extends HttpServlet {

	/**
	 * 
	 */
	private static final long serialVersionUID = 1L;

	public void doGet(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {
		doPost(request, response);
	}

	public void doPost(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {
		String sql = "select result,circle_name,circle_creator,circle_jibie,reason,ioc from circle";
		ComboPooledDataSource dataSource = new ComboPooledDataSource("jdbc");
		Connection conn;
		try {
			conn = dataSource.getConnection();
			PreparedStatement stmt = conn.prepareStatement(sql);
			stmt = conn.prepareStatement(sql);
			ResultSet rS = stmt.executeQuery();
			List<Map<String, String>> lMaps = new ArrayList<Map<String, String>>();
			Map<String, String> dataMap = new HashMap<String, String>();
			while (rS.next()) {
				if (rS.getString("result").equals("0")) {
					continue;
				}
				dataMap.put("circle_name", rS.getString("circle_name"));
				dataMap.put("circle_creator", rS.getString("circle_creator"));
				dataMap.put("circle_jibie", rS.getString("circle_jibie"));
				dataMap.put("reason", rS.getString("reason"));
				dataMap.put("ioc", "./img/" + rS.getString("ioc"));
				if (rS.getString("result").equals("1")) {
					dataMap.put("result", "同意");
				} else if (rS.getString("result").equals("2")) {
					dataMap.put("result", "拒绝");
				}
				lMaps.add(dataMap);
				dataMap = new HashMap<String, String>();
			}
			rS.close();
			request.setAttribute("list", lMaps);
			request.getRequestDispatcher("./main2.jsp").forward(request,
					response);
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}

}
