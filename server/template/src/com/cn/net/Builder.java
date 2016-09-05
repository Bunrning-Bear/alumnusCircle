package com.cn.net;

import java.io.BufferedInputStream;
import java.io.BufferedOutputStream;
import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
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

import org.apache.commons.fileupload.FileItem;
import org.apache.commons.fileupload.FileUploadException;
import org.apache.commons.fileupload.disk.DiskFileItemFactory;
import org.apache.commons.fileupload.servlet.ServletFileUpload;

import cn.itcast.utils.JDBCUtils;

import com.mchange.v2.c3p0.ComboPooledDataSource;

public class Builder extends HttpServlet {

	public void doGet(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {
		doPost(request, response);
	}

	public void doPost(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {
		request.setCharacterEncoding("utf-8");
		Map<String, String> data = new HashMap<String, String>();
		if (ServletFileUpload.isMultipartContent(request)) {
			// 步骤一 构造工厂
			DiskFileItemFactory factory = new DiskFileItemFactory();
			// 设置缓冲区大小和临时目录
			factory.setSizeThreshold(1024 * 1024 * 8);// 8M 临时缓冲区（上传文件不大于8M
			// 不会产生临时文件）
			File repository = new File(getServletContext().getRealPath(
					"/WEB-INF/tmp"));
			factory.setRepository(repository);// 当上传文件超过8M 会在临时目录中产生临时文件

			// 步骤二 获得解析器
			ServletFileUpload upload = new ServletFileUpload(factory);
			// 步骤三 对请求体内容进行解析
			try {
				List<FileItem> list = upload.parseRequest(request);
				// 步骤四 遍历FileItem 集合
				for (FileItem fileItem : list) {
					// 步骤五 判断每个FileItem 是不是文件上传项
					if (fileItem.isFormField()) {
						// 不是上传文件
						String name = fileItem.getFieldName(); // name属性
						String value = fileItem.getString("utf-8"); // value
						data.put(name, value);
						System.out.println("普通form项：" + name + "----" + value);
					} else {
						// 是上传文件
						String filename = fileItem.getName(); // 文件名
						data.put("filename", filename);
						// 解决老版本浏览器IE6 文件路径存在问题
						if (filename.contains("\\")) {
							filename = filename.substring(filename
									.lastIndexOf("\\") + 1);
						}
						InputStream in = new BufferedInputStream(
								fileItem.getInputStream()); // 文件内容
						System.out.println("文件上传项：" + filename);

						// 生成随机目录
						File path = new File(
								"D:\\MyEclipse_Workspaces\\NetSite\\WebRoot\\img");
						if (!path.exists()) {
							path.mkdirs();
						}
						// 将文件内容输出WEB-INF/upload 目录
						File targetFile = new File(path, filename);
						OutputStream out = new BufferedOutputStream(
								new FileOutputStream(targetFile));
						int temp;
						while ((temp = in.read()) != -1) {
							out.write(temp);
						}
						out.close();
						in.close();

						// 删除临时文件(必须将文件流关掉)
						fileItem.delete();
					}
				}
			} catch (FileUploadException e) {
				e.printStackTrace();
			}
		}

		ComboPooledDataSource dataSource = new ComboPooledDataSource("jdbc");
		Connection conn;
		try {
			conn = dataSource.getConnection();
			String sql = "insert into circle values(?,?,?,?,?,?,?)";
			PreparedStatement stmt = conn.prepareStatement(sql);
			stmt.setString(1, null);
			stmt.setString(2, data.get("name"));
			stmt.setString(3, data.get("username"));
			stmt.setString(4, data.get("jibie"));
			stmt.setString(5, data.get("reason"));
			stmt.setString(6, "0");
			stmt.setString(7, data.get("filename"));
			int i = stmt.executeUpdate();

			if (i > 0) {
				sql = "select role from user where username=?";
				stmt = conn.prepareStatement(sql);
				stmt.setString(1,
						(String) request.getSession().getAttribute("user"));
				ResultSet rs = stmt.executeQuery();
				if (rs.next()) {
					if (rs.getString("role").equals("admin")) {
						sql = "select circle_name,circle_creator,circle_jibie,reason,ioc from circle where result=?";
						stmt = conn.prepareStatement(sql);
						stmt.setString(1, "0");
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
							dataMap.put("ioc", "./img/" + rS.getString("ioc"));
							lMaps.add(dataMap);
							dataMap = new HashMap<String, String>();
						}
						rS.close();
						request.setAttribute("list", lMaps);
						request.getRequestDispatcher("./confirm.jsp").forward(
								request, response);
					} else {
						request.getRequestDispatcher("./wait.jsp").forward(
								request, response);
					}
				}
				rs.close();
			}
			JDBCUtils.release(stmt, conn);
		} catch (SQLException e) {
			e.printStackTrace();
		}
	}
}
