package com.alumnuscircle.connections.Item;

/**
 * Created by 曾博晖 on 2016/8/23.
 * 人脉中每条条目成员的类
 * 2016年8月23日15:41:58
 * 各项数据成员类型为String
 * 即为
 * 头像Url地址，用户名，用户地址
 * 用户学院，用户年级，用户班级，
 * 以及用户的职业
 * @author 曾博晖
 */

public class ContactsItem {
    private String headImgUrl;
    private String userName;
    private String userLocation;
    private String userFaculty;
    private String userGrade;
    private String userClass;
    private String userJob;
    /**
     * 构造函数，传入每一个Item的各项数据
     * 曾博晖
     * 各项数据成员类型为String
     * 依次代表
     * 头像Url地址，用户名，用户地址
     * 用户学院，用户年级，用户班级，
     * 以及用户的职业
     * @author 曾博晖
     * 2016年8月23日15:51:02
     * 创建*/
    public ContactsItem(String url,String name,String location,String faculty,
                        String grade,String userClass,
                        String job){
        this.headImgUrl=url;
        this.userName=name;
        this.userLocation=location;
        this.userFaculty=faculty;
        this.userGrade=grade;
        this.userClass=userClass;
        this.userJob=job;
    }
    public String getHeadImgUrl(){return headImgUrl;}
    public String getUserName(){return userName;}
    public String getUserLocation(){return userLocation;}
    public String getUserFaculty(){return userFaculty;}
    public String getUserGrade(){return userGrade;}
    public String getUserClass(){return userClass;}
    public String getUserJob(){return userJob;}
}
