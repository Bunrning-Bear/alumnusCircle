package com.cn.net;

import java.io.IOException;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import cn.itcast.utils.JDBCUtils;

import com.mchange.v2.c3p0.ComboPooledDataSource;

public class Login extends HttpServlet {

	public void doGet(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {
		doPost(request, response);
	}

	public void doPost(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {
		request.setCharacterEncoding("utf-8");
		String username = request.getParameter("username");
		String password = request.getParameter("password");
		ComboPooledDataSource dataSource = new ComboPooledDataSource("jdbc");
		Connection conn;
		try {
			conn = dataSource.getConnection();
			String sql = "select password from user where username=?";
			PreparedStatement stmt = conn.prepareStatement(sql);
			stmt.setString(1, username);
			ResultSet rs = stmt.executeQuery();
			if (rs.next()) {
				if (password.equals(rs.getString("password"))) {
					request.getRequestDispatcher("./manage.jsp").forward(
							request, response);
				} else {
					request.setAttribute("msg", "密码错误！！！");
					request.getRequestDispatcher("./login.jsp").forward(
							request, response);
				}
			} else {
				request.setAttribute("msg", "用户不存在！！！");
				request.getRequestDispatcher("./login.jsp").forward(request,
						response);
			}
			JDBCUtils.release(rs, stmt, conn);
		} catch (SQLException e) {
			e.printStackTrace();
		}
		request.getSession().setAttribute("user", username);
	}

}
