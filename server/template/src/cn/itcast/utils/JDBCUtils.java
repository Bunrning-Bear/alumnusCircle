package cn.itcast.utils;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ResourceBundle;

/**
 * JDBC 工具类，抽取公共方法
 * 
 * @author seawind
 * 
 */
public class JDBCUtils {
	private static final String DRIVERCLASS;
	private static final String URL;
	private static final String USER;
	private static final String PWD;

	static {
		ResourceBundle bundle = ResourceBundle.getBundle("dbconfig");
		DRIVERCLASS = bundle.getString("DRIVERCLASS");
		URL = bundle.getString("URL");
		USER = bundle.getString("USER");
		PWD = bundle.getString("PWD");
	}

	// 建立连接
	public static Connection getConnection() throws Exception {
		loadDriver();
		return DriverManager.getConnection(URL, USER, PWD);
	}

	// 装载驱动
	private static void loadDriver() throws ClassNotFoundException {
		Class.forName(DRIVERCLASS);
	}

	// 释放资源
	public static void release(ResultSet rs, Statement stmt, Connection conn) {
		if (rs != null) {
			try {
				rs.close();
			} catch (SQLException e) {
				e.printStackTrace();
			}
			rs = null;
		}

		release(stmt, conn);
	}

	public static void release(Statement stmt, Connection conn) {
		if (stmt != null) {
			try {
				stmt.close();
			} catch (SQLException e) {
				e.printStackTrace();
			}
			stmt = null;
		}
		if (conn != null) {
			try {
				conn.close();
			} catch (SQLException e) {
				e.printStackTrace();
			}
			conn = null;
		}
	}
}
