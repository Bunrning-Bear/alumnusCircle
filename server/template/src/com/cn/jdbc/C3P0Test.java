package com.cn.jdbc;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

import org.junit.Test;

import cn.itcast.utils.JDBCUtils;

import com.mchange.v2.c3p0.ComboPooledDataSource;

public class C3P0Test {
	@Test
	public void demo2() throws SQLException {
		// 使用c3p0配置文件
		// ComboPooledDataSource dataSource = new ComboPooledDataSource();
		// //使用默认
		ComboPooledDataSource dataSource = new ComboPooledDataSource("jdbc");
		// 自动加载src/c3p0-config.xml

		Connection conn = dataSource.getConnection();
		String sql = "select * from user";
		PreparedStatement stmt = conn.prepareStatement(sql);

		ResultSet rs = stmt.executeQuery();

		while (rs.next()) {
			System.out.println(rs.getString("username"));
		}

		JDBCUtils.release(rs, stmt, conn);
	}

	@Test
	public void demo1() throws Exception {
		// 创建一个连接池
		ComboPooledDataSource dataSource = new ComboPooledDataSource();
		// 手动设置四个参数
		dataSource.setDriverClass("com.mysql.jdbc.Driver");
		dataSource.setJdbcUrl("jdbc:mysql:///day14");
		dataSource.setUser("root");
		dataSource.setPassword("123");

		Connection conn = dataSource.getConnection();
		String sql = "select * from account";
		PreparedStatement stmt = conn.prepareStatement(sql);

		ResultSet rs = stmt.executeQuery();

		while (rs.next()) {
			System.out.println(rs.getString("name"));
		}

		JDBCUtils.release(rs, stmt, conn);
	}
}
