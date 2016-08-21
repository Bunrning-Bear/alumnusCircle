-- phpMyAdmin SQL Dump
-- version 4.5.1
-- http://www.phpmyadmin.net
--
-- Host: 180.153.57.193
-- Generation Time: 2016-07-29 03:24:20
-- 服务器版本： 5.5.49-0ubuntu0.12.04.1
-- PHP Version: 5.6.23

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `papacamera`
--

-- --------------------------------------------------------

--
-- 表的结构 `advert_fn`
--

CREATE TABLE `advert_fn` (
  `fn_id` int(11) NOT NULL COMMENT '记录功能id，主键，id=0表示暂无功能',
  `fn_type_id` tinyint(4) NOT NULL DEFAULT '0' COMMENT '功能id',
  `fn_url` varchar(300) NOT NULL DEFAULT '' COMMENT '根据不同内容存储跳转url'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='用于将广告的功能id和具体的url链接进行对应';

--
-- 转存表中的数据 `advert_fn`
--

INSERT INTO `advert_fn` (`fn_id`, `fn_type_id`, `fn_url`) VALUES
(0, 0, ''),
(1, 1, 'https://movie.douban.com/subject/5045678/'),
(2, 2, 'dayu_01.mp4'),
(3, 3, 'movie'),
(4, 4, 'https://manzong.tmall.com/p/rd796552.htm?spm=a1z10.1-b.w11347119-14603850203.1.DSgaNz'),
(5, 5, 'movie'),
(6, 1, 'http://challenge.pepsi.com.cn/'),
(7, 2, 'http://oos.ctyunapi.cn/papacamera/food/pepsi/video/pepsi_02.mp4?Expires=1474339887&AWSAccessKeyId=acc2c5f81e0f33f7bd84&Signature=3Fo9Y0n6fEDbY6drFhhsGM%2Bazw8%3D'),
(8, 3, 'shop'),
(9, 4, 'https://item.taobao.com/item.htm?spm=a230r.1.14.4.DfqmPo&id=531179074337&ns=1&abbucket=8#detail'),
(10, 5, 'pepsi'),
(11, 6, 'http://mp.weixin.qq.com/s?__biz=MzA5MzI3ODYyNQ==&mid=2651780563&idx=2&sn=fd1f8382300b87c49a3d90a076c87119&scene=23&srcid=0721ueAfUPCpKcmt4PpYIM2p#rd'),
(12, 6, 'http://emoji.pepsi.com.cn/?hmsr=wechat'),
(13, 6, 'http://challenge.pepsi.com.cn/'),
(14, 6, 'http://fun.alipay.com/zhlj/'),
(15, 6, 'http://www.adidas.com/us/'),
(16, 6, 'http://www.lancome.com.cn/landing/enjoy-gifts-link.html');

-- --------------------------------------------------------

--
-- 表的结构 `advert_fn_type`
--

CREATE TABLE `advert_fn_type` (
  `ad_fn_type_id` tinyint(4) NOT NULL COMMENT '功能id',
  `ad_fn_type_name` varchar(10) NOT NULL COMMENT '功能名称'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `advert_fn_type`
--

INSERT INTO `advert_fn_type` (`ad_fn_type_id`, `ad_fn_type_name`) VALUES
(0, '暂无'),
(1, '官网'),
(2, '视频'),
(3, '导航'),
(4, '商城'),
(5, '优惠'),
(6, '活动');

-- --------------------------------------------------------

--
-- 表的结构 `advert_info`
--

CREATE TABLE `advert_info` (
  `ad_id` int(11) NOT NULL COMMENT '广告id',
  `ad_name` varchar(50) NOT NULL COMMENT '广告名称',
  `ad_pic_url` varchar(200) NOT NULL COMMENT '广告正面样张图片地址',
  `ad_type_id` tinyint(4) NOT NULL DEFAULT '0' COMMENT '广告的类型id,为advert_type表的外键',
  `ad_topic_url` varchar(200) NOT NULL DEFAULT '' COMMENT '广告主题图片的url地址',
  `ad_count` bigint(20) NOT NULL DEFAULT '0' COMMENT '该广告被识别的次数',
  `ad_fn0_id` int(11) NOT NULL COMMENT '功能菜单中的该广告图片点击后跳转的功能id',
  `ad_fn1_id` int(11) NOT NULL DEFAULT '0' COMMENT '该广告功能1对应的id，为advert_fn的外键',
  `ad_fn2_id` int(11) NOT NULL DEFAULT '0' COMMENT '该广告功能2对应的id，为advert_fn的外键',
  `ad_fn3_id` int(11) NOT NULL DEFAULT '0',
  `ad_fn4_id` int(11) NOT NULL DEFAULT '0',
  `ad_fn5_id` int(11) NOT NULL DEFAULT '0',
  `ad_fn6_id` int(11) NOT NULL DEFAULT '0',
  `ad_fn7_id` int(11) NOT NULL DEFAULT '0',
  `ad_fn8_id` int(11) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='所有发布的广告。不同位置发布的同一个广告在本表中只占一项';

--
-- 转存表中的数据 `advert_info`
--

INSERT INTO `advert_info` (`ad_id`, `ad_name`, `ad_pic_url`, `ad_type_id`, `ad_topic_url`, `ad_count`, `ad_fn0_id`, `ad_fn1_id`, `ad_fn2_id`, `ad_fn3_id`, `ad_fn4_id`, `ad_fn5_id`, `ad_fn6_id`, `ad_fn7_id`, `ad_fn8_id`) VALUES
(1, '大鱼海棠', 'http://oos.ctyunapi.cn/papacamera/movie/dayuhaitang/pic/dayu_01.jpg?Expires=1474277896&AWSAccessKeyId=acc2c5f81e0f33f7bd84&Signature=Ah0LNvPi6Pg1HxM9WKEuMm3XjtI%3D', 1, 'http://oos.ctyunapi.cn/papacamera/movie/dayuhaitang/pic/dayu_01.jpg?Expires=1474277896&AWSAccessKeyId=acc2c5f81e0f33f7bd84&Signature=Ah0LNvPi6Pg1HxM9WKEuMm3XjtI%3D', 1, 11, 1, 2, 3, 4, 5, 0, 0, 0),
(2, '百事可乐-emoji罐', 'http://oos.ctyunapi.cn/papacamera/food/pepsi/pic/pepsi_02.jpg?Expires=1474336455&AWSAccessKeyId=acc2c5f81e0f33f7bd84&Signature=251Vwc5O23U9ClAdIVRwbD/ZWv0%3D', 2, 'http://oos.ctyunapi.cn/papacamera/food/pepsi/pic/pepsi_02.jpg?Expires=1474336455&AWSAccessKeyId=acc2c5f81e0f33f7bd84&Signature=251Vwc5O23U9ClAdIVRwbD/ZWv0%3D', 20, 12, 6, 7, 8, 9, 10, 0, 0, 0),
(3, '百事可乐-百事挑赞', 'http://oos.ctyunapi.cn/papacamera/food/pepsi/pic/pepsi_01.jpg?Expires=1474338004&AWSAccessKeyId=acc2c5f81e0f33f7bd84&Signature=zrE1cK1wNMoYq22wqxJGhn8UjT8%3D', 2, 'http://oos.ctyunapi.cn/papacamera/food/pepsi/pic/pepsi_01.jpg?Expires=1474338004&AWSAccessKeyId=acc2c5f81e0f33f7bd84&Signature=zrE1cK1wNMoYq22wqxJGhn8UjT8%3D', 13, 13, 0, 0, 0, 0, 0, 0, 0, 0),
(4, '支付宝-九周年', 'http://oos.ctyunapi.cn/papacamera/internet/alipay/pic/alipay_01.jpg?Expires=1474340177&AWSAccessKeyId=acc2c5f81e0f33f7bd84&Signature=80DksazqfN3nIAnZlzbeu8LNNj0%3D', 3, 'http://oos.ctyunapi.cn/papacamera/internet/alipay/pic/alipay_01.jpg?Expires=1474340177&AWSAccessKeyId=acc2c5f81e0f33f7bd84&Signature=80DksazqfN3nIAnZlzbeu8LNNj0%3D', 10, 14, 0, 0, 0, 0, 0, 0, 0, 0),
(6, '阿迪达斯', 'http://oos.ctyunapi.cn/papacamera/clothing/adidas/pic/adidas_01.jpg?Expires=1474340638&AWSAccessKeyId=acc2c5f81e0f33f7bd84&Signature=W9yLQei%2Bh2ukETsIXdsoh9uAkFo%3D', 4, 'http://oos.ctyunapi.cn/papacamera/clothing/adidas/pic/adidas_01.jpg?Expires=1474340638&AWSAccessKeyId=acc2c5f81e0f33f7bd84&Signature=W9yLQei%2Bh2ukETsIXdsoh9uAkFo%3D', 9, 15, 0, 0, 0, 0, 0, 0, 0, 0),
(7, '兰蔻梦魅香水', 'http://oos.ctyunapi.cn/papacamera/luxury/lancome/pic/lancome_01.jpg?Expires=1474341177&AWSAccessKeyId=acc2c5f81e0f33f7bd84&Signature=vlC0u4OOguX0tOMTdJ7phlVArhw%3D', 5, 'http://oos.ctyunapi.cn/papacamera/luxury/lancome/pic/lancome_01.jpg?Expires=1474341177&AWSAccessKeyId=acc2c5f81e0f33f7bd84&Signature=vlC0u4OOguX0tOMTdJ7phlVArhw%3D', 30, 16, 0, 0, 0, 0, 0, 0, 0, 0),
(8, 'vivo', 'http://oos.ctyunapi.cn/papacamera/luxury/lancome/pic/lancome_01.jpg?Expires=1474341177&AWSAccessKeyId=acc2c5f81e0f33f7bd84&Signature=vlC0u4OOguX0tOMTdJ7phlVArhw%3D', 1, 'http://oos.ctyunapi.cn/papacamera/luxury/lancome/pic/lancome_01.jpg?Expires=1474341177&AWSAccessKeyId=acc2c5f81e0f33f7bd84&Signature=vlC0u4OOguX0tOMTdJ7phlVArhw%3D', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
(9, '不二情书', 'http://oos.ctyunapi.cn/papacamera/luxury/lancome/pic/lancome_01.jpg?Expires=1474341177&AWSAccessKeyId=acc2c5f81e0f33f7bd84&Signature=vlC0u4OOguX0tOMTdJ7phlVArhw%3D', 1, 'http://oos.ctyunapi.cn/papacamera/luxury/lancome/pic/lancome_01.jpg?Expires=1474341177&AWSAccessKeyId=acc2c5f81e0f33f7bd84&Signature=vlC0u4OOguX0tOMTdJ7phlVArhw%3D', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
(10, '海峡城', 'http://oos.ctyunapi.cn/papacamera/luxury/lancome/pic/lancome_01.jpg?Expires=1474341177&AWSAccessKeyId=acc2c5f81e0f33f7bd84&Signature=vlC0u4OOguX0tOMTdJ7phlVArhw%3D', 1, 'http://oos.ctyunapi.cn/papacamera/luxury/lancome/pic/lancome_01.jpg?Expires=1474341177&AWSAccessKeyId=acc2c5f81e0f33f7bd84&Signature=vlC0u4OOguX0tOMTdJ7phlVArhw%3D', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
(11, '康师傅', 'http://oos.ctyunapi.cn/papacamera/luxury/lancome/pic/lancome_01.jpg?Expires=1474341177&AWSAccessKeyId=acc2c5f81e0f33f7bd84&Signature=vlC0u4OOguX0tOMTdJ7phlVArhw%3D', 1, 'http://oos.ctyunapi.cn/papacamera/luxury/lancome/pic/lancome_01.jpg?Expires=1474341177&AWSAccessKeyId=acc2c5f81e0f33f7bd84&Signature=vlC0u4OOguX0tOMTdJ7phlVArhw%3D', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
(12, '51job', 'http://oos.ctyunapi.cn/papacamera/luxury/lancome/pic/lancome_01.jpg?Expires=1474341177&AWSAccessKeyId=acc2c5f81e0f33f7bd84&Signature=vlC0u4OOguX0tOMTdJ7phlVArhw%3D', 1, 'http://oos.ctyunapi.cn/papacamera/luxury/lancome/pic/lancome_01.jpg?Expires=1474341177&AWSAccessKeyId=acc2c5f81e0f33f7bd84&Signature=vlC0u4OOguX0tOMTdJ7phlVArhw%3D', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
(13, '维多利亚', 'http://oos.ctyunapi.cn/papacamera/luxury/lancome/pic/lancome_01.jpg?Expires=1474341177&AWSAccessKeyId=acc2c5f81e0f33f7bd84&Signature=vlC0u4OOguX0tOMTdJ7phlVArhw%3D', 1, 'http://oos.ctyunapi.cn/papacamera/luxury/lancome/pic/lancome_01.jpg?Expires=1474341177&AWSAccessKeyId=acc2c5f81e0f33f7bd84&Signature=vlC0u4OOguX0tOMTdJ7phlVArhw%3D', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
(14, 'espoir', 'http://oos.ctyunapi.cn/papacamera/luxury/lancome/pic/lancome_01.jpg?Expires=1474341177&AWSAccessKeyId=acc2c5f81e0f33f7bd84&Signature=vlC0u4OOguX0tOMTdJ7phlVArhw%3D', 1, 'http://oos.ctyunapi.cn/papacamera/luxury/lancome/pic/lancome_01.jpg?Expires=1474341177&AWSAccessKeyId=acc2c5f81e0f33f7bd84&Signature=vlC0u4OOguX0tOMTdJ7phlVArhw%3D', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
(15, '苏宁易购', 'http://oos.ctyunapi.cn/papacamera/luxury/lancome/pic/lancome_01.jpg?Expires=1474341177&AWSAccessKeyId=acc2c5f81e0f33f7bd84&Signature=vlC0u4OOguX0tOMTdJ7phlVArhw%3D', 1, 'http://oos.ctyunapi.cn/papacamera/luxury/lancome/pic/lancome_01.jpg?Expires=1474341177&AWSAccessKeyId=acc2c5f81e0f33f7bd84&Signature=vlC0u4OOguX0tOMTdJ7phlVArhw%3D', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0);

-- --------------------------------------------------------

--
-- 表的结构 `advert_type`
--

CREATE TABLE `advert_type` (
  `ad_type_id` tinyint(4) NOT NULL COMMENT '广告类型ID主键、自增',
  `ad_type_class_1` varchar(40) NOT NULL DEFAULT '其他' COMMENT '广告所属一级分类（例如食品、化妆品、房地产等）',
  `ad_type_class_2` varchar(40) NOT NULL DEFAULT '其他' COMMENT '二级分类'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='定义每个广告所属的类型。';

--
-- 转存表中的数据 `advert_type`
--

INSERT INTO `advert_type` (`ad_type_id`, `ad_type_class_1`, `ad_type_class_2`) VALUES
(1, '娱乐', '电影'),
(2, '食品', '饮料'),
(3, '互联网公司', '金融'),
(4, '服饰', '大众'),
(5, '奢侈品', '化妆');

-- --------------------------------------------------------

--
-- 表的结构 `app_circular`
--

CREATE TABLE `app_circular` (
  `cl_id` tinyint(4) NOT NULL COMMENT '轮播内容id，主键，自增',
  `cl_type` tinyint(4) NOT NULL COMMENT '轮播内容类型，1代表广告，2代表活动，3代表任务',
  `cl_pic_url` varchar(500) NOT NULL COMMENT '轮播图地址',
  `cl_detail_url` varchar(500) NOT NULL COMMENT '点击以后的跳转链接url'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='APP首页的轮播表(内容可能为广告，活动或者任务），点击以后跳转到相应url';

--
-- 转存表中的数据 `app_circular`
--

INSERT INTO `app_circular` (`cl_id`, `cl_type`, `cl_pic_url`, `cl_detail_url`) VALUES
(1, 1, 'http://oos.ctyunapi.cn/papacamera/app_circular/1/pic/1.jpg?Expires=1474772371&AWSAccessKeyId=acc2c5f81e0f33f7bd84&Signature=TmUVoJ2Qz3tCE73JGS/PZI6i53k%3D', 'http://movie.mtime.com135022/'),
(2, 1, 'http://oos.ctyunapi.cn/papacamera/app_circular/2/pic/2.jpg?Expires=1474772736&AWSAccessKeyId=acc2c5f81e0f33f7bd84&Signature=BJCFbHaFwpOH2kZtQUhan3na4v4%3D', 'http://challenge.pepsi.com.cn/'),
(3, 1, 'http://oos.ctyunapi.cn/papacamera/app_circular/3/alipay_01.jpg?Expires=1474772802&AWSAccessKeyId=acc2c5f81e0f33f7bd84&Signature=g5LAbcJd1Z8117o582v9wBmD8V8%3D', 'http://fun.alipay.com/zhlj/'),
(4, 1, 'http://oos.ctyunapi.cn/papacamera/app_circular/4/4.jpg?Expires=1474773037&AWSAccessKeyId=acc2c5f81e0f33f7bd84&Signature=oMX%2BdbH7fKMe/XsOk9py6s9kNLw%3D', 'http://www.adidas.com/us/'),
(5, 1, 'http://oos.ctyunapi.cn/papacamera/app_circular/5/5.jpg?Expires=1474772915&AWSAccessKeyId=acc2c5f81e0f33f7bd84&Signature=sXxuBF3eecu%2BddY423ok/8li174%3D', 'http://www.lancome.com.cn/landing/enjoy-gifts-link.html');

-- --------------------------------------------------------

--
-- 表的结构 `app_feedback`
--

CREATE TABLE `app_feedback` (
  `fb_id` int(11) NOT NULL COMMENT '反馈消息id,主键，自增',
  `fb_user_id` int(11) DEFAULT NULL COMMENT '反馈用户id（如果已经登录）',
  `fb_user_phone` varchar(20) DEFAULT '' COMMENT '反馈用户的联系方式',
  `fb_time` datetime NOT NULL COMMENT '反馈时间',
  `fb_content` varchar(500) NOT NULL DEFAULT '' COMMENT '反馈的具体内容'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='用户反馈信息表';

--
-- 转存表中的数据 `app_feedback`
--

INSERT INTO `app_feedback` (`fb_id`, `fb_user_id`, `fb_user_phone`, `fb_time`, `fb_content`) VALUES
(1, NULL, '17751781351', '0000-00-00 00:00:00', 'è¿™æ˜¯ä¸€æ¡åé¦ˆä¿¡æ¯'),
(2, NULL, '15851856957', '0000-00-00 00:00:00', 'è¿™æ˜¯ä¸€æ¡æµ‹è¯•åé¦ˆï¼'),
(3, NULL, '15851856958', '0000-00-00 00:00:00', 'aaaa'),
(4, NULL, '15851856958', '0000-00-00 00:00:00', 'ssss'),
(5, NULL, '15851856958', '0000-00-00 00:00:00', 'aaaa'),
(6, NULL, '15851856958', '0000-00-00 00:00:00', 'aaaaa'),
(7, NULL, '18997210014', '0000-00-00 00:00:00', 'wwww'),
(8, NULL, '15851856958', '0000-00-00 00:00:00', 'sssss'),
(9, NULL, '15851856958', '0000-00-00 00:00:00', 'qqqq'),
(10, NULL, '15851856958', '0000-00-00 00:00:00', 'aaaaa'),
(11, NULL, '15851856958', '0000-00-00 00:00:00', 'aaaaa'),
(12, NULL, '15877664444', '0000-00-00 00:00:00', '这个应用不错'),
(13, NULL, '15877664444', '0000-00-00 00:00:00', '这个应用不错'),
(14, NULL, '15386869595', '0000-00-00 00:00:00', '这是一条反馈！'),
(15, NULL, '17751781351', '0000-00-00 00:00:00', '大蠢驴');

-- --------------------------------------------------------

--
-- 表的结构 `coupon_info`
--

CREATE TABLE `coupon_info` (
  `cp_id` int(11) NOT NULL COMMENT '优惠券id，主键，自增',
  `cp_name` varchar(50) NOT NULL COMMENT '优惠券名称',
  `cp_pic_url` varchar(300) NOT NULL COMMENT '优惠券图片链接',
  `cp_type_id` tinyint(4) NOT NULL COMMENT '优惠券类型id，coupon_type表主键',
  `cp_pub_time` datetime NOT NULL COMMENT '优惠券获奖情况公布时间（该时间后用户无法再申请领取该优惠券）',
  `cp_detail_url` varchar(300) NOT NULL COMMENT '优惠券详情页面url',
  `cp_ad_id` int(11) NOT NULL COMMENT '优惠券关联的广告id，advert_info表主键',
  `cp_provider` varchar(500) NOT NULL COMMENT '优惠券提供商简介',
  `cp_content` varchar(500) NOT NULL COMMENT '优惠券内容信息',
  `cp_price` varchar(50) NOT NULL COMMENT '优惠价值',
  `cp_copies` varchar(50) NOT NULL COMMENT '优惠份数',
  `cp_usetype` tinyint(4) NOT NULL COMMENT '优惠券兑奖方式（1-商家确认，2-优惠码，）',
  `cp_useurl` varchar(100) DEFAULT NULL COMMENT '优惠券兑换链接',
  `cp_uselimit` varchar(50) NOT NULL COMMENT '优惠券使用限制',
  `cp_endtime` datetime NOT NULL COMMENT '优惠券过期时间',
  `cp_contact` varchar(50) NOT NULL COMMENT '优惠券提供商联系方式'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='优惠券信息表';

--
-- 转存表中的数据 `coupon_info`
--

INSERT INTO `coupon_info` (`cp_id`, `cp_name`, `cp_pic_url`, `cp_type_id`, `cp_pub_time`, `cp_detail_url`, `cp_ad_id`, `cp_provider`, `cp_content`, `cp_price`, `cp_copies`, `cp_usetype`, `cp_useurl`, `cp_uselimit`, `cp_endtime`, `cp_contact`) VALUES
(1, '啪啪相机发布会 珍藏款啪啪熊公仔一个', 'http://oos.ctyunapi.cn/papacamera/app_coupon/1/pic/1.jpg?Expires=1521446695&AWSAccessKeyId=acc2c5f81e0f33f7bd84&Signature=oy3qEN6r9I/UO3dRO6Y7Pw9pDj0%3D', 1, '2016-07-27 16:07:56', 'html/coupon/coupon.html', 1, '啪啪相机基于AR技术，致力于为户外媒体广告行业提供服务，为用户带来极致的使用体验，实现户外媒体广告的二次呈现。啪啪相机基于AR技术，致力于为户外媒体广告行业提供服务，为用户带来极致的使用体验，实现户外媒体广告的二次呈现。啪啪相机基于AR技术，致力于为户外媒体广告行业提供服务，为用户带来极致的使用体验，实现户外媒体广告的二次呈现。', '啪啪相机发布会 珍藏款啪啪熊公仔一个', '每件价值233元', '限量100份', 1, NULL, '无限制', '2016-08-16 16:38:04', '地址：秣周东路悠谷创业园 电话：XXXXXXX 微信公众号：啪啪相机 '),
(2, '啪啪相机发布会 珍藏款啪啪熊T恤一件', 'http://oos.ctyunapi.cn/papacamera/app_coupon/1/pic/1.jpg?Expires=1521446695&AWSAccessKeyId=acc2c5f81e0f33f7bd84&Signature=oy3qEN6r9I/UO3dRO6Y7Pw9pDj0%3D', 1, '2016-07-27 16:08:01', 'html/coupon/coupon.html', 2, '啪啪相机基于AR技术，致力于为户外媒体广告行业提供服务，为用户带来极致的使用体验，实现户外媒体广告的二次呈现。', '啪啪相机发布会 珍藏款啪啪熊T恤一件', '每件价值233元', '限量100份', 1, NULL, '无限制', '2016-07-16 16:38:18', '地址：秣周东路悠谷创业园 电话：XXXXXXX 微信公众号：啪啪相机 '),
(3, '啪啪相机发布会 珍藏款啪啪熊亚麻手袋一个', 'http://oos.ctyunapi.cn/papacamera/app_coupon/1/pic/1.jpg?Expires=1521446695&AWSAccessKeyId=acc2c5f81e0f33f7bd84&Signature=oy3qEN6r9I/UO3dRO6Y7Pw9pDj0%3D', 1, '2016-07-27 16:08:04', 'html/coupon/coupon.html', 1, '啪啪相机基于AR技术，致力于为户外媒体广告行业提供服务，为用户带来极致的使用体验，实现户外媒体广告的二次呈现。', '啪啪相机发布会 珍藏款啪啪熊亚麻手袋一个', '每件价值233元', '限量100份', 1, NULL, '无限制', '2016-07-16 16:38:23', '地址：秣周东路悠谷创业园 电话：XXXXXXX 微信公众号：啪啪相机 ');

-- --------------------------------------------------------

--
-- 表的结构 `coupon_type`
--

CREATE TABLE `coupon_type` (
  `cp_type_id` tinyint(4) NOT NULL COMMENT '优惠券类型ID，主键，自增',
  `cp_type_value` varchar(20) NOT NULL DEFAULT '' COMMENT '对应的优惠券类型描述'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='描述优惠券类型ID与具体内容对应关系的表';

--
-- 转存表中的数据 `coupon_type`
--

INSERT INTO `coupon_type` (`cp_type_id`, `cp_type_value`) VALUES
(1, '免费领取'),
(2, '免费名额'),
(3, '折扣优惠');

-- --------------------------------------------------------

--
-- 表的结构 `moments_comment`
--

CREATE TABLE `moments_comment` (
  `mom_com_id` int(11) NOT NULL COMMENT '该条评论消息的ID',
  `mom_com_user_id` int(11) NOT NULL DEFAULT '0' COMMENT '评论用户id,user表外键',
  `mom_com_msg_id` int(11) NOT NULL DEFAULT '0' COMMENT '被评论的消息id,moments_msg表外键',
  `mom_com_content` varchar(200) NOT NULL DEFAULT '' COMMENT '评论内容',
  `mom_com_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '评论的当前时间'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='用户关于啪啪圈消息的评论信息。';

--
-- 转存表中的数据 `moments_comment`
--

INSERT INTO `moments_comment` (`mom_com_id`, `mom_com_user_id`, `mom_com_msg_id`, `mom_com_content`, `mom_com_time`) VALUES
(1, 0, 0, 'tummmm', '2016-07-27 02:23:00'),
(2, 0, 0, 'tummmm', '2016-07-27 02:23:04');

-- --------------------------------------------------------

--
-- 表的结构 `moments_like`
--

CREATE TABLE `moments_like` (
  `mom_like_id` int(11) NOT NULL COMMENT '该条点赞消息的ID',
  `mom_like_user_id` int(11) DEFAULT '0' COMMENT '点赞人用户ID，user表外键',
  `mom_like_msg_id` int(11) DEFAULT '0' COMMENT '被点赞的消息ID，moments_message表外键'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='用户关于啪啪圈消息的点赞信息';

--
-- 转存表中的数据 `moments_like`
--

INSERT INTO `moments_like` (`mom_like_id`, `mom_like_user_id`, `mom_like_msg_id`) VALUES
(1, 0, 0),
(2, 0, 0);

-- --------------------------------------------------------

--
-- 表的结构 `moments_msg`
--

CREATE TABLE `moments_msg` (
  `mom_msg_id` int(11) NOT NULL COMMENT '啪啪圈消息id',
  `mom_msg_user_id` int(11) DEFAULT '0' COMMENT '发消息人的ID,user_info表外键',
  `mom_msg_type` int(11) DEFAULT '0' COMMENT '消息类型 0-原创消息',
  `mom_msg_text` varchar(500) DEFAULT '' COMMENT '消息文字内容',
  `mom_msg_pic_url` varchar(500) DEFAULT '' COMMENT '消息图片url列表',
  `mom_msg_like_num` int(11) DEFAULT '0' COMMENT '消息点赞数',
  `mom_msg_comment_num` int(11) DEFAULT '0' COMMENT '消息评论数',
  `mom_msg_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '消息的发送时间'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `moments_msg`
--

INSERT INTO `moments_msg` (`mom_msg_id`, `mom_msg_user_id`, `mom_msg_type`, `mom_msg_text`, `mom_msg_pic_url`, `mom_msg_like_num`, `mom_msg_comment_num`, `mom_msg_time`) VALUES
(1, 0, 0, '价格与会，。', '', 0, 0, '2016-07-27 02:09:48'),
(2, 0, 0, '价格与会，。', '', 0, 0, '2016-07-27 02:09:54');

-- --------------------------------------------------------

--
-- 表的结构 `news_info`
--

CREATE TABLE `news_info` (
  `news_id` int(11) NOT NULL COMMENT '新闻id',
  `news_title` varchar(255) DEFAULT '' COMMENT '新闻标题',
  `news_url` varchar(255) DEFAULT '' COMMENT '新闻链接',
  `news_count` int(11) DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='定义啪啪头条需要显示的新闻内容';

--
-- 转存表中的数据 `news_info`
--

INSERT INTO `news_info` (`news_id`, `news_title`, `news_url`, `news_count`) VALUES
(1, '“口袋妖怪 Go”爆红', 'http://www.hq.xinhuanet.com/news/2016-07/21/c_1119254014.htm', 0),
(2, '用一淘比价,不做冤大头', 'http://www.etao.com/go/act/yuandatou.php', 0),
(3, '雅虎，美国老兵不会死去', 'http://36kr.com/p/5050082.html', 0),
(4, 'Bilibili线下演唱会', 'http://36kr.com/p/5049955.html', 0);

-- --------------------------------------------------------

--
-- 表的结构 `user_coupon`
--

CREATE TABLE `user_coupon` (
  `user_cp_id` int(11) NOT NULL COMMENT '该表主键，自增',
  `user_id` int(11) NOT NULL COMMENT '用户id，user_info表主键',
  `cp_id` int(11) NOT NULL COMMENT '该用户申请领取的某一优惠券id，coupon_info表主键',
  `user_cp_state_id` tinyint(4) NOT NULL COMMENT '该用户-优惠券关系当前状态id，user_coupon_state表主键',
  `user_coupon_code` varchar(20) DEFAULT NULL COMMENT '兑换码'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='用户与各优惠券的关系表';

--
-- 转存表中的数据 `user_coupon`
--

INSERT INTO `user_coupon` (`user_cp_id`, `user_id`, `cp_id`, `user_cp_state_id`, `user_coupon_code`) VALUES
(1, 1, 1, 1, 'afef34fss4445');

-- --------------------------------------------------------

--
-- 表的结构 `user_coupon_state`
--

CREATE TABLE `user_coupon_state` (
  `user_cp_state_id` tinyint(4) NOT NULL COMMENT '优惠券状态id',
  `cp_state_value` varchar(10) NOT NULL COMMENT '优惠券状态名称',
  `cp_state_detail` varchar(30) NOT NULL COMMENT '优惠券状态详细描述'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='优惠券状态id与显示内容对应表';

--
-- 转存表中的数据 `user_coupon_state`
--

INSERT INTO `user_coupon_state` (`user_cp_state_id`, `cp_state_value`, `cp_state_detail`) VALUES
(0, '未参加', '想要获得，赶快查看详情'),
(1, '不感兴趣', ''),
(2, '已参加', '您已确认参加本次优惠活动'),
(3, '已获得', '您已获得优惠，点击查看详情'),
(4, '未获得', '很遗憾，您未能获得本次优惠'),
(5, '已使用', '该项优惠已使用，谢谢'),
(6, '已赠送', '该项优惠已赠送他人，谢谢'),
(7, '即将过期', '优惠即将过期，可使用或转增他人'),
(8, '已过期', '该优惠已过期');

-- --------------------------------------------------------

--
-- 表的结构 `user_info`
--

CREATE TABLE `user_info` (
  `user_id` int(8) NOT NULL COMMENT '用户id',
  `user_name` varchar(50) DEFAULT NULL COMMENT '用户昵称',
  `user_passwd` varchar(100) DEFAULT NULL COMMENT '用户密码',
  `user_phone` varchar(20) DEFAULT NULL COMMENT '用户电话号码',
  `user_qq_id` varchar(20) DEFAULT NULL COMMENT '用户QQ号',
  `user_wechat_id` varchar(20) DEFAULT NULL COMMENT '用户微信号'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='存储用户信息';

--
-- 转存表中的数据 `user_info`
--

INSERT INTO `user_info` (`user_id`, `user_name`, `user_passwd`, `user_phone`, `user_qq_id`, `user_wechat_id`) VALUES
(1, 'yyz1', 'yyz1', NULL, NULL, NULL),
(2, 'yyz2', 'yyz2', NULL, NULL, NULL),
(3, 'yyz3', 'yyz3', NULL, NULL, NULL),
(4, 'wuzhengfan', 'qwaszx', NULL, NULL, NULL),
(5, 'hahaha', '15326536987', '17751781352', NULL, NULL),
(6, 'yyz1', 'yyz1', '15851856958', NULL, NULL),
(7, 'qwert', 'qwe123456', '15851856957', NULL, NULL),
(8, 'wuzhengfan', '123456', '17751781351', NULL, NULL),
(9, '吴正凡', '123456', '18888888888', NULL, NULL),
(10, 'baiyang', '123456', '13350695069', NULL, NULL),
(11, 'fengseng', '123456', '13354678988', NULL, NULL),
(12, 'wuzhengfanTYU', '789', '15851853218', NULL, NULL),
(13, 'hdhdhhdjd', 'dbdhdjdjd', '15154236981', NULL, NULL),
(14, 'rthhguvj', 'fgcihig', '13258745692', NULL, NULL),
(15, 'xiao', '123456', '13934567890', NULL, NULL),
(16, 'xiao', '56565', '15634567890', NULL, NULL),
(17, 'fs', '111111', '15851866958', NULL, NULL),
(18, 'qqq', '111111', '15855754444', NULL, NULL),
(19, '111', '111111', '15851856959', NULL, NULL),
(20, '12306', '123456', '17751848556', NULL, NULL),
(21, 'wu', '123456', '13333333333', NULL, NULL),
(22, 'hahaha', '123456', '17751386159', NULL, NULL),
(23, '175185', '123456', '17751836542', NULL, NULL),
(24, '154873', '123456', '15151689652', NULL, NULL),
(25, '218567', '123456', '15151873028', NULL, NULL),
(26, '1530962627', '123456', '15895632145', NULL, NULL),
(27, '123456', '123456', '15187654231', NULL, NULL),
(28, 'advert', '222222', '15877664444', NULL, NULL),
(29, 'baiyang', '123123', '15851856547', NULL, NULL),
(30, 'baiyanmg', '111111', '15851853215', NULL, NULL);

-- --------------------------------------------------------

--
-- 表的结构 `video_info`
--

CREATE TABLE `video_info` (
  `video_id` int(11) NOT NULL COMMENT '频视ID，主键，自增',
  `video_title` varchar(50) DEFAULT '' COMMENT '频视标题',
  `video_thumbnail_url` varchar(200) DEFAULT '' COMMENT '视频缩略图url',
  `video_content_url` varchar(200) DEFAULT '' COMMENT '视频链接url',
  `video_count` int(11) DEFAULT '0' COMMENT '点击人数'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='存储短视频信息';

--
-- 转存表中的数据 `video_info`
--

INSERT INTO `video_info` (`video_id`, `video_title`, `video_thumbnail_url`, `video_content_url`, `video_count`) VALUES
(1, 'KKKL', 'http://oos.ctyunapi.cn/papacamera/app_circular/1/pic/1.jpg?Expires=1474772371&AWSAccessKeyId=acc2c5f81e0f33f7bd84&Signature=TmUVoJ2Qz3tCE73JGS/PZI6i53k%3D', 'kkkl.mp4', 10),
(2, 'ex1', 'http://oos.ctyunapi.cn/papacamera/app_circular/1/pic/1.jpg?Expires=1474772371&AWSAccessKeyId=acc2c5f81e0f33f7bd84&Signature=TmUVoJ2Qz3tCE73JGS/PZI6i53k%3D', 'ex1.mp4', 0),
(3, 'ex2', 'http://oos.ctyunapi.cn/papacamera/app_circular/1/pic/1.jpg?Expires=1474772371&AWSAccessKeyId=acc2c5f81e0f33f7bd84&Signature=TmUVoJ2Qz3tCE73JGS/PZI6i53k%3D', 'ex2.mp4', 0),
(4, 'ex3', 'http://oos.ctyunapi.cn/papacamera/app_circular/1/pic/1.jpg?Expires=1474772371&AWSAccessKeyId=acc2c5f81e0f33f7bd84&Signature=TmUVoJ2Qz3tCE73JGS/PZI6i53k%3D', '', 0),
(5, 'ex4', 'http://oos.ctyunapi.cn/papacamera/app_circular/1/pic/1.jpg?Expires=1474772371&AWSAccessKeyId=acc2c5f81e0f33f7bd84&Signature=TmUVoJ2Qz3tCE73JGS/PZI6i53k%3D', 'ex4.mp4', 0),
(6, 'ex5', 'http://oos.ctyunapi.cn/papacamera/app_circular/1/pic/1.jpg?Expires=1474772371&AWSAccessKeyId=acc2c5f81e0f33f7bd84&Signature=TmUVoJ2Qz3tCE73JGS/PZI6i53k%3D', '', 0),
(7, 'ex6', 'http://oos.ctyunapi.cn/papacamera/app_circular/1/pic/1.jpg?Expires=1474772371&AWSAccessKeyId=acc2c5f81e0f33f7bd84&Signature=TmUVoJ2Qz3tCE73JGS/PZI6i53k%3D', 'ex6.mp4', 0),
(8, 'ex7', 'http://oos.ctyunapi.cn/papacamera/app_circular/1/pic/1.jpg?Expires=1474772371&AWSAccessKeyId=acc2c5f81e0f33f7bd84&Signature=TmUVoJ2Qz3tCE73JGS/PZI6i53k%3D', '', 0);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `advert_fn`
--
ALTER TABLE `advert_fn`
  ADD PRIMARY KEY (`fn_id`),
  ADD KEY `fn_type_id` (`fn_type_id`);

--
-- Indexes for table `advert_fn_type`
--
ALTER TABLE `advert_fn_type`
  ADD PRIMARY KEY (`ad_fn_type_id`);

--
-- Indexes for table `advert_info`
--
ALTER TABLE `advert_info`
  ADD PRIMARY KEY (`ad_id`),
  ADD KEY `广告类别` (`ad_type_id`),
  ADD KEY `功能` (`ad_fn1_id`,`ad_fn2_id`,`ad_fn3_id`,`ad_fn4_id`,`ad_fn5_id`,`ad_fn6_id`,`ad_fn7_id`,`ad_fn8_id`),
  ADD KEY `ad_fn0_id` (`ad_fn0_id`),
  ADD KEY `ad_fn2_id` (`ad_fn2_id`),
  ADD KEY `ad_fn3_id` (`ad_fn3_id`),
  ADD KEY `ad_fn4_id` (`ad_fn4_id`),
  ADD KEY `ad_fn5_id` (`ad_fn5_id`),
  ADD KEY `ad_fn6_id` (`ad_fn6_id`),
  ADD KEY `ad_fn7_id` (`ad_fn7_id`),
  ADD KEY `ad_fn8_id` (`ad_fn8_id`);

--
-- Indexes for table `advert_type`
--
ALTER TABLE `advert_type`
  ADD PRIMARY KEY (`ad_type_id`);

--
-- Indexes for table `app_circular`
--
ALTER TABLE `app_circular`
  ADD PRIMARY KEY (`cl_id`);

--
-- Indexes for table `app_feedback`
--
ALTER TABLE `app_feedback`
  ADD PRIMARY KEY (`fb_id`);

--
-- Indexes for table `coupon_info`
--
ALTER TABLE `coupon_info`
  ADD PRIMARY KEY (`cp_id`),
  ADD KEY `cp_type_id` (`cp_type_id`);

--
-- Indexes for table `coupon_type`
--
ALTER TABLE `coupon_type`
  ADD PRIMARY KEY (`cp_type_id`);

--
-- Indexes for table `moments_comment`
--
ALTER TABLE `moments_comment`
  ADD PRIMARY KEY (`mom_com_id`);

--
-- Indexes for table `moments_like`
--
ALTER TABLE `moments_like`
  ADD PRIMARY KEY (`mom_like_id`);

--
-- Indexes for table `moments_msg`
--
ALTER TABLE `moments_msg`
  ADD PRIMARY KEY (`mom_msg_id`);

--
-- Indexes for table `news_info`
--
ALTER TABLE `news_info`
  ADD PRIMARY KEY (`news_id`);

--
-- Indexes for table `user_coupon`
--
ALTER TABLE `user_coupon`
  ADD PRIMARY KEY (`user_cp_id`);

--
-- Indexes for table `user_coupon_state`
--
ALTER TABLE `user_coupon_state`
  ADD PRIMARY KEY (`user_cp_state_id`);

--
-- Indexes for table `user_info`
--
ALTER TABLE `user_info`
  ADD PRIMARY KEY (`user_id`);

--
-- Indexes for table `video_info`
--
ALTER TABLE `video_info`
  ADD PRIMARY KEY (`video_id`);

--
-- 在导出的表使用AUTO_INCREMENT
--

--
-- 使用表AUTO_INCREMENT `advert_fn`
--
ALTER TABLE `advert_fn`
  MODIFY `fn_id` int(11) NOT NULL AUTO_INCREMENT COMMENT '记录功能id，主键，id=0表示暂无功能', AUTO_INCREMENT=17;
--
-- 使用表AUTO_INCREMENT `advert_info`
--
ALTER TABLE `advert_info`
  MODIFY `ad_id` int(11) NOT NULL AUTO_INCREMENT COMMENT '广告id', AUTO_INCREMENT=16;
--
-- 使用表AUTO_INCREMENT `advert_type`
--
ALTER TABLE `advert_type`
  MODIFY `ad_type_id` tinyint(4) NOT NULL AUTO_INCREMENT COMMENT '广告类型ID主键、自增', AUTO_INCREMENT=6;
--
-- 使用表AUTO_INCREMENT `app_circular`
--
ALTER TABLE `app_circular`
  MODIFY `cl_id` tinyint(4) NOT NULL AUTO_INCREMENT COMMENT '轮播内容id，主键，自增', AUTO_INCREMENT=6;
--
-- 使用表AUTO_INCREMENT `app_feedback`
--
ALTER TABLE `app_feedback`
  MODIFY `fb_id` int(11) NOT NULL AUTO_INCREMENT COMMENT '反馈消息id,主键，自增', AUTO_INCREMENT=16;
--
-- 使用表AUTO_INCREMENT `coupon_info`
--
ALTER TABLE `coupon_info`
  MODIFY `cp_id` int(11) NOT NULL AUTO_INCREMENT COMMENT '优惠券id，主键，自增', AUTO_INCREMENT=4;
--
-- 使用表AUTO_INCREMENT `coupon_type`
--
ALTER TABLE `coupon_type`
  MODIFY `cp_type_id` tinyint(4) NOT NULL AUTO_INCREMENT COMMENT '优惠券类型ID，主键，自增', AUTO_INCREMENT=4;
--
-- 使用表AUTO_INCREMENT `moments_comment`
--
ALTER TABLE `moments_comment`
  MODIFY `mom_com_id` int(11) NOT NULL AUTO_INCREMENT COMMENT '该条评论消息的ID', AUTO_INCREMENT=3;
--
-- 使用表AUTO_INCREMENT `moments_like`
--
ALTER TABLE `moments_like`
  MODIFY `mom_like_id` int(11) NOT NULL AUTO_INCREMENT COMMENT '该条点赞消息的ID', AUTO_INCREMENT=3;
--
-- 使用表AUTO_INCREMENT `moments_msg`
--
ALTER TABLE `moments_msg`
  MODIFY `mom_msg_id` int(11) NOT NULL AUTO_INCREMENT COMMENT '啪啪圈消息id', AUTO_INCREMENT=3;
--
-- 使用表AUTO_INCREMENT `news_info`
--
ALTER TABLE `news_info`
  MODIFY `news_id` int(11) NOT NULL AUTO_INCREMENT COMMENT '新闻id', AUTO_INCREMENT=6;
--
-- 使用表AUTO_INCREMENT `user_coupon`
--
ALTER TABLE `user_coupon`
  MODIFY `user_cp_id` int(11) NOT NULL AUTO_INCREMENT COMMENT '该表主键，自增', AUTO_INCREMENT=2;
--
-- 使用表AUTO_INCREMENT `user_coupon_state`
--
ALTER TABLE `user_coupon_state`
  MODIFY `user_cp_state_id` tinyint(4) NOT NULL AUTO_INCREMENT COMMENT '优惠券状态id', AUTO_INCREMENT=9;
--
-- 使用表AUTO_INCREMENT `user_info`
--
ALTER TABLE `user_info`
  MODIFY `user_id` int(8) NOT NULL AUTO_INCREMENT COMMENT '用户id', AUTO_INCREMENT=31;
--
-- 使用表AUTO_INCREMENT `video_info`
--
ALTER TABLE `video_info`
  MODIFY `video_id` int(11) NOT NULL AUTO_INCREMENT COMMENT '频视ID，主键，自增', AUTO_INCREMENT=9;
--
-- 限制导出的表
--

--
-- 限制表 `advert_fn`
--
ALTER TABLE `advert_fn`
  ADD CONSTRAINT `advert_fn_ibfk_1` FOREIGN KEY (`fn_type_id`) REFERENCES `advert_fn_type` (`ad_fn_type_id`) ON UPDATE CASCADE;

--
-- 限制表 `advert_info`
--
ALTER TABLE `advert_info`
  ADD CONSTRAINT `advert_info_ibfk_1` FOREIGN KEY (`ad_type_id`) REFERENCES `advert_type` (`ad_type_id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `advert_info_ibfk_10` FOREIGN KEY (`ad_fn7_id`) REFERENCES `advert_fn` (`fn_id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `advert_info_ibfk_11` FOREIGN KEY (`ad_fn8_id`) REFERENCES `advert_fn` (`fn_id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `advert_info_ibfk_3` FOREIGN KEY (`ad_fn1_id`) REFERENCES `advert_fn` (`fn_id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `advert_info_ibfk_4` FOREIGN KEY (`ad_fn0_id`) REFERENCES `advert_fn` (`fn_id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `advert_info_ibfk_5` FOREIGN KEY (`ad_fn2_id`) REFERENCES `advert_fn` (`fn_id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `advert_info_ibfk_6` FOREIGN KEY (`ad_fn3_id`) REFERENCES `advert_fn` (`fn_id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `advert_info_ibfk_7` FOREIGN KEY (`ad_fn4_id`) REFERENCES `advert_fn` (`fn_id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `advert_info_ibfk_8` FOREIGN KEY (`ad_fn5_id`) REFERENCES `advert_fn` (`fn_id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `advert_info_ibfk_9` FOREIGN KEY (`ad_fn6_id`) REFERENCES `advert_fn` (`fn_id`) ON UPDATE CASCADE;

--
-- 限制表 `coupon_info`
--
ALTER TABLE `coupon_info`
  ADD CONSTRAINT `coupon_info_ibfk_1` FOREIGN KEY (`cp_type_id`) REFERENCES `coupon_type` (`cp_type_id`) ON UPDATE CASCADE;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
