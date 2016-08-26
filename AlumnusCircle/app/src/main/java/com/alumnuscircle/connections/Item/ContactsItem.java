package com.alumnuscircle.connections.Item;

/**
 * Created by 曾博晖 on 2016/8/23.
 * 人脉中每条条目成员的类
 * 2016年8月23日15:41:58
 */

public class ContactsItem {
    private String headImgUrl;
    private String userName;
    private String userLocation;
    private String userGrade;
    private String userClass;
    private String userJob;
    /**
     * 构造函数，传入每一个Item的各项数据
     * 曾博晖
     * 2016年8月23日15:51:02
     * 创建*/
    public ContactsItem(String url,String name,String location,
                        String grade,String userclass,
                        String job){
        this.headImgUrl=url;
        this.userName=name;
        this.userLocation=location;
        this.userGrade=grade;
        this.userClass=userclass;
        this.userJob=job;
    }
    public String getHeadImgUrl(){return headImgUrl;}
    public String getUserName(){return userName;}
    public String getUserLocation(){return userLocation;}
    public String getUserGrade(){return userGrade;}
    public String getUserClass(){return userClass;}
    public String getUserJob(){return userJob;}
}
