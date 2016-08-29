-- phpMyAdmin SQL Dump
-- version 4.0.10deb1
-- http://www.phpmyadmin.net
--
-- 主机: localhost
-- 生成日期: 2016-08-29 11:26:15
-- 服务器版本: 5.5.50-0ubuntu0.14.04.1
-- PHP 版本: 5.5.9-1ubuntu4.19

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- 数据库: `alumnuscircle`
--

-- --------------------------------------------------------

--
-- 表的结构 `ac_circle_table`
--

CREATE TABLE IF NOT EXISTS `ac_circle_table` (
  `c_id` int(11) NOT NULL AUTO_INCREMENT,
  `umeng_cid` varchar(32) NOT NULL,
  `umeng_virtual_cid` varchar(32) NOT NULL,
  `circle_type_id` varchar(32) NOT NULL,
  PRIMARY KEY (`c_id`),
  KEY `umeng_cid` (`umeng_cid`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=5 ;

--
-- 转存表中的数据 `ac_circle_table`
--

INSERT INTO `ac_circle_table` (`c_id`, `umeng_cid`, `umeng_virtual_cid`, `circle_type_id`) VALUES
(1, '57c19db1d36ef30b9126b2a0', '57c30d76d36ef35df6a4c266', '1'),
(2, '57c19db1d36ef30b9126b2a0', '57c30d76d36ef35df6a4c266', '1'),
(3, '57c399b4b9a99622684af017', '57c399b4b9a996211fb398a1', '1'),
(4, '57c399b4b9a99622684af017', '57c399b4b9a996211fb398a1', '1');

-- --------------------------------------------------------

--
-- 表的结构 `ac_manual_review_table`
--

CREATE TABLE IF NOT EXISTS `ac_manual_review_table` (
  `review_id` int(11) NOT NULL AUTO_INCREMENT COMMENT '请求id',
  `result` tinyint(1) NOT NULL DEFAULT '0' COMMENT '请求结果:0为处理,1接受.2拒绝',
  `circle_name` varchar(30) NOT NULL COMMENT '圈子名字',
  `circle_type_id` char(32) NOT NULL COMMENT '圈子类型的umengid',
  `circle_type_name` varchar(20) NOT NULL,
  `circle_icon_url` varchar(255) NOT NULL COMMENT '圈子的头像的url',
  `creator_uid` char(32) NOT NULL COMMENT '圈子的创建人的uid',
  `reason_message` varchar(340) NOT NULL COMMENT '创建的理由',
  `description` varchar(300) DEFAULT NULL,
  PRIMARY KEY (`review_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=91 ;

--
-- 转存表中的数据 `ac_manual_review_table`
--

INSERT INTO `ac_manual_review_table` (`review_id`, `result`, `circle_name`, `circle_type_id`, `circle_type_name`, `circle_icon_url`, `creator_uid`, `reason_message`, `description`) VALUES
(1, 1, 'new circle 905', '1', '学院圈', 'default', '123', 'I love you!', 'the circle will be beautiful!'),
(81, 0, 'new circle 743', '1', '学院圈', 'default', '123', 'I love you!', 'the circle will be beautiful!'),
(82, 0, 'new circle 585', '1', '学院圈', 'default', '123', 'I love you!', 'the circle will be beautiful!'),
(83, 0, 'new circle 961', '1', '学院圈', 'default', '123', 'I love you!', 'the circle will be beautiful!'),
(84, 0, 'new circle 361', '1', '学院圈', 'default', '123', 'I love you!', 'the circle will be beautiful!'),
(85, 0, 'new circle 459', '1', '学院圈', 'default', '123', 'I love you!', 'the circle will be beautiful!'),
(86, 0, 'new circle 442', '1', '学院圈', 'default', '123', 'I love you!', 'the circle will be beautiful!'),
(87, 0, 'new circle 661', '1', '学院圈', 'default', '123', 'I love you!', 'the circle will be beautiful!'),
(88, 0, 'new circle 438', '1', '学院圈', 'default', '123', 'I love you!', 'the circle will be beautiful!'),
(89, 0, 'new circle 700', '1', '学院圈', 'default', '123', 'I love you!', 'the circle will be beautiful!'),
(90, 0, 'new circle 397', '1', '学院圈', 'default', '123', 'I love you!', 'the circle will be beautiful!');

-- --------------------------------------------------------

--
-- 表的结构 `ac_message_circle_table`
--

CREATE TABLE IF NOT EXISTS `ac_message_circle_table` (
  `mc_id` int(11) NOT NULL,
  `umeng_circle_id` varchar(32) NOT NULL,
  `queue_list` varchar(510) NOT NULL DEFAULT '_',
  `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`mc_id`),
  KEY `umeng_circle_id` (`umeng_circle_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 表的结构 `ac_message_table`
--

CREATE TABLE IF NOT EXISTS `ac_message_table` (
  `m_id` int(11) NOT NULL AUTO_INCREMENT COMMENT '消息id',
  `type` tinyint(4) NOT NULL COMMENT '消息类型的说明字段',
  `message` varchar(1022) NOT NULL COMMENT '消息字段,是一个json数组',
  PRIMARY KEY (`m_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- 表的结构 `ac_message_user_table`
--

CREATE TABLE IF NOT EXISTS `ac_message_user_table` (
  `mu_id` int(11) NOT NULL AUTO_INCREMENT,
  `uid` int(11) NOT NULL,
  `message_queue` varchar(510) NOT NULL DEFAULT '_',
  `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`mu_id`),
  KEY `uid` (`uid`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=32 ;

--
-- 转存表中的数据 `ac_message_user_table`
--

INSERT INTO `ac_message_user_table` (`mu_id`, `uid`, `message_queue`, `update_time`) VALUES
(1, 245, '_', '2016-08-28 16:59:00'),
(2, 246, '_', '2016-08-28 16:59:00'),
(3, 247, '_', '2016-08-28 16:59:21'),
(4, 248, '_', '2016-08-28 16:59:21'),
(5, 1, '_', '2016-08-28 17:11:37'),
(6, 2, '_', '2016-08-28 17:11:38'),
(7, 3, '_', '2016-08-28 17:13:27'),
(8, 4, '_', '2016-08-28 17:19:54'),
(9, 5, '_', '2016-08-28 17:36:52'),
(10, 6, '_', '2016-08-29 01:13:52'),
(11, 7, '_', '2016-08-29 01:35:00'),
(12, 8, '_', '2016-08-29 01:43:57'),
(13, 9, '_', '2016-08-29 01:44:45'),
(14, 10, '_', '2016-08-29 01:48:25'),
(15, 11, '_', '2016-08-29 01:55:16'),
(16, 12, '_', '2016-08-29 02:06:39'),
(17, 13, '_', '2016-08-29 02:07:06'),
(18, 14, '_', '2016-08-29 02:07:55'),
(19, 15, '_', '2016-08-29 02:08:14'),
(20, 16, '_', '2016-08-29 02:09:19'),
(21, 17, '_', '2016-08-29 02:10:59'),
(22, 18, '_', '2016-08-29 02:34:04'),
(23, 19, '_', '2016-08-29 02:38:54'),
(24, 20, '_', '2016-08-29 02:41:27'),
(25, 21, '_', '2016-08-29 02:43:54'),
(26, 22, '_', '2016-08-29 02:45:23'),
(27, 23, '_', '2016-08-29 02:45:35'),
(28, 24, '_', '2016-08-29 02:52:40'),
(29, 25, '_', '2016-08-29 02:53:26'),
(30, 26, '_', '2016-08-29 03:01:28'),
(31, 27, '_', '2016-08-29 03:04:20');

-- --------------------------------------------------------

--
-- 表的结构 `ac_user_base_info`
--

CREATE TABLE IF NOT EXISTS `ac_user_base_info` (
  `uid` int(11) NOT NULL AUTO_INCREMENT,
  `adlevel` tinyint(1) NOT NULL DEFAULT '0',
  `telephone` char(11) NOT NULL COMMENT '用户的登陆名,手机号',
  `password` varchar(32) NOT NULL COMMENT '密码',
  `stu_id` char(8) NOT NULL COMMENT '用户的学号',
  `access_token` char(128) NOT NULL,
  `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`uid`),
  KEY `telephone` (`telephone`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=28 ;

--
-- 转存表中的数据 `ac_user_base_info`
--

INSERT INTO `ac_user_base_info` (`uid`, `adlevel`, `telephone`, `password`, `stu_id`, `access_token`, `update_time`) VALUES
(1, 0, '15896193612', 'cxh1234567', '59670868', '3eb436281264285cfa0d429a44b14617714371c8d2d7bcc5e1accc72735fd98d7d7fc757bd74f021bc460eac18156192843816bbfcca11cf55a34dbc517fc482', '2016-08-28 17:11:37'),
(2, 0, '15896193612', 'cxh1234567', '77296394', '3eb436281264285cfa0d429a44b14617714371c8d2d7bcc5e1accc72735fd98d7d7fc757bd74f021bc460eac18156192843816bbfcca11cf55a34dbc517fc482', '2016-08-28 17:11:38'),
(3, 0, '15896110759', 'cxh1234567', '12570763', '3eb436281264285cfa0d429a44b14617714371c8d2d7bcc5e1accc72735fd98da53758a72748d8d3c77a35293b2fea764f8c47295a565751b3bb56a626d47afe', '2016-08-28 17:13:27'),
(4, 0, '15896179781', 'cxh1234567', '20979794', '3eb436281264285cfa0d429a44b14617714371c8d2d7bcc5e1accc72735fd98dcc35783bfaa759c093e94a426f1389f581c35c10a965bd981cbfbf19c286efc0', '2016-08-28 17:19:54'),
(5, 0, '15896160304', 'cxh1234567', '44450471', '3eb436281264285cfa0d429a44b14617714371c8d2d7bcc5e1accc72735fd98dd87af195ac248a4598af46567ca12f9744d892beebe02633026ef1a5db89a7f7', '2016-08-28 17:36:52'),
(6, 0, '15896160474', 'cxh1234567', '23825249', '3eb436281264285cfa0d429a44b14617714371c8d2d7bcc5e1accc72735fd98d8967e7cd62de282519c2448b4c5251d3a11cd79fb3ec12efb98b1ca43f7831c2', '2016-08-29 01:13:52'),
(7, 1, '15195861108', 'e10adc3949ba59abbe56e057f20f883e', '96973449', '3eb436281264285cfa0d429a44b14617714371c8d2d7bcc5e1accc72735fd98d9d026169d445c3834203b6c341ab156b285b9c02c3eb20138d2f69f29697142c', '2016-08-29 01:34:59'),
(10, 0, '15896160557', 'cxh1234567', '93578247', '3eb436281264285cfa0d429a44b14617714371c8d2d7bcc5e1accc72735fd98d53d3c5e30dcda5fd996f086cae924f1731308b3554fbced5524c740aee165e00', '2016-08-29 01:48:25'),
(12, 0, '15896119172', 'cxh1234567', '99103031', '3eb436281264285cfa0d429a44b14617714371c8d2d7bcc5e1accc72735fd98de1d98399621e5d1d6800b1d8765465cabfd3484287b3610a3e424eadbd9d02cc', '2016-08-29 02:06:39'),
(13, 0, '15896160100', 'cxh1234567', '50519211', '3eb436281264285cfa0d429a44b14617714371c8d2d7bcc5e1accc72735fd98d87e2765f6e518c848bd16caf0dc87bf0b1a9c5b463a4b3038624fa7c44484f54', '2016-08-29 02:07:06'),
(14, 0, '15896153684', 'cxh1234567', '11787321', '3eb436281264285cfa0d429a44b14617714371c8d2d7bcc5e1accc72735fd98db0a2b776b0fd447a470c40373424f0329d3c45b987d8eea58b084ab43a9b6f09', '2016-08-29 02:07:55'),
(15, 0, '15896139739', 'cxh1234567', '76328001', '3eb436281264285cfa0d429a44b14617714371c8d2d7bcc5e1accc72735fd98d06ed34d966bfd431cab17f61dfb56fb755d7c796fc60d76fd6e79680fc15275f', '2016-08-29 02:08:14'),
(16, 0, '15896125889', 'cxh1234567', '44462875', '3eb436281264285cfa0d429a44b14617714371c8d2d7bcc5e1accc72735fd98db7b27fb964453c5a7f02f03a90494d7e64f9e101ea0991a5f2fdf8f706e5a5d9', '2016-08-29 02:09:19'),
(17, 0, '15896170905', 'cxh1234567', '58856689', '3eb436281264285cfa0d429a44b14617714371c8d2d7bcc5e1accc72735fd98d3b425dee9b05b47c99766f4d84db1473059866f9f98e2d245d08bdecf76ad343', '2016-08-29 02:10:58'),
(18, 0, '15896128022', 'cxh1234567', '32190975', '3eb436281264285cfa0d429a44b14617714371c8d2d7bcc5e1accc72735fd98d2135d7421f8906f55c7193175be2815523c35e75236b64352e37161ceb2086eb', '2016-08-29 02:34:04'),
(19, 0, '15896115650', 'cxh1234567', '65377214', '3eb436281264285cfa0d429a44b14617714371c8d2d7bcc5e1accc72735fd98d003a3447bd056299147a29e52e3e5d13d4345dc6579eb0493b61a29970912f01', '2016-08-29 02:38:54'),
(20, 0, '15896148397', 'cxh1234567', '63877021', '3eb436281264285cfa0d429a44b14617714371c8d2d7bcc5e1accc72735fd98deffa8e0b0c8a45f9856964c120e6da8801fd55dc46efecc23c193172162e90c4', '2016-08-29 02:41:26'),
(21, 0, '15896190480', 'cxh1234567', '29420250', '3eb436281264285cfa0d429a44b14617714371c8d2d7bcc5e1accc72735fd98de51904e69b99fdb34540403ba457e45b1479851f19b88522d4f2ef60fd4217c8', '2016-08-29 02:43:54'),
(22, 0, '15896165359', 'cxh1234567', '27510340', '3eb436281264285cfa0d429a44b14617714371c8d2d7bcc5e1accc72735fd98dbdd7dcd112ff6d4b8fc75f37f91f6d25266dbfebe58faacfdbe2d43c3d80ec97', '2016-08-29 02:45:23'),
(23, 0, '15896144175', 'cxh1234567', '20978396', '3eb436281264285cfa0d429a44b14617714371c8d2d7bcc5e1accc72735fd98de320017159f4997ea6d12b3726abe85b08beae840f067f66155b9c8ef5c7d1db', '2016-08-29 02:45:35'),
(24, 0, '15896184914', 'cxh1234567', '25601166', '3eb436281264285cfa0d429a44b14617714371c8d2d7bcc5e1accc72735fd98d609239e65aa3ad3f20308acab52e4974c0f7db3b60e7b1944985fd74df2cd9dc', '2016-08-29 02:52:39'),
(25, 0, '15896129110', 'cxh1234567', '33116489', '3eb436281264285cfa0d429a44b14617714371c8d2d7bcc5e1accc72735fd98d4fa4eafb79bccd14c1ee24daacb3ce028ce6a199d29049d6e0e0d77517a662d9', '2016-08-29 02:53:25'),
(26, 0, '15896114648', 'cxh1234567', '40072310', '3eb436281264285cfa0d429a44b14617714371c8d2d7bcc5e1accc72735fd98d7a802273b5d5c0a2b11d3feae42266957601afc48bdca29e65e04345e3efc822', '2016-08-29 03:01:27'),
(27, 0, '15896184440', 'cxh1234567', '33801435', '3eb436281264285cfa0d429a44b14617714371c8d2d7bcc5e1accc72735fd98d4d455792a4062787c5ae8fbee68e2bd6bcb606062423051c307631d37a04e80b', '2016-08-29 03:04:20');

-- --------------------------------------------------------

--
-- 表的结构 `ac_user_detail_info`
--

CREATE TABLE IF NOT EXISTS `ac_user_detail_info` (
  `detail_id` int(11) NOT NULL AUTO_INCREMENT COMMENT '详细信息列表的id',
  `uid` int(11) NOT NULL COMMENT '用户id',
  `icon_url` varchar(128) NOT NULL COMMENT '头像url地址',
  `admission_year` smallint(4) unsigned NOT NULL COMMENT '入学年份',
  `faculty_id` tinyint(3) unsigned NOT NULL COMMENT '院系id',
  `major_id` tinyint(3) unsigned NOT NULL COMMENT '专业id',
  `name` varchar(8) NOT NULL COMMENT '真实姓名',
  `gender` tinyint(1) NOT NULL COMMENT '性别',
  `job` varchar(20) NOT NULL COMMENT '工作',
  `city` int(11) NOT NULL COMMENT '城市编号',
  `tags` varchar(350) NOT NULL DEFAULT '{}' COMMENT '个性标签',
  `instroduction` varchar(350) NOT NULL DEFAULT '{}' COMMENT '个性介绍',
  `my_circle_list` varchar(1022) NOT NULL DEFAULT '{}' COMMENT '他加入的圈子列表',
  `company` varchar(20) NOT NULL COMMENT '公司名称',
  `company_publicity_level` tinyint(1) NOT NULL DEFAULT '0' COMMENT '公司的开放程度',
  `public_contact_list` varchar(126) NOT NULL DEFAULT '{}' COMMENT '公开的联系方式列表',
  `protect_contact_list` varchar(126) NOT NULL DEFAULT '{}' COMMENT '仅圈内好友可见的联系方式列表',
  `job_list` varchar(1022) NOT NULL DEFAULT '{}' COMMENT '工作经历列表',
  `job_list_level` tinyint(1) NOT NULL DEFAULT '0' COMMENT '工作列表的公开程度',
  PRIMARY KEY (`detail_id`),
  KEY `uid` (`detail_id`),
  KEY `uid_2` (`uid`),
  KEY `uid_3` (`uid`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=28 ;

--
-- 转存表中的数据 `ac_user_detail_info`
--

INSERT INTO `ac_user_detail_info` (`detail_id`, `uid`, `icon_url`, `admission_year`, `faculty_id`, `major_id`, `name`, `gender`, `job`, `city`, `tags`, `instroduction`, `my_circle_list`, `company`, `company_publicity_level`, `public_contact_list`, `protect_contact_list`, `job_list`, `job_list_level`) VALUES
(1, 1, 'default', 2014, 71, 1, '陈雄辉', 0, 'worker100', 321, '{}', '{}', '{}', 'another company', 0, '{}', '{}', '{}', 0),
(2, 2, 'default', 2014, 71, 1, '陈雄辉', 0, 'student', 123, '{}', '{}', '{}', 'google China', 0, '{}', '{}', '{}', 0),
(3, 3, 'default', 2014, 71, 1, '陈雄辉', 0, 'student', 123, '{}', '{}', '{}', 'google China', 0, '{}', '{}', '{}', 0),
(4, 4, 'default', 2014, 71, 1, '陈雄辉', 0, 'student', 123, '{}', '{}', '{}', 'google China', 0, '{}', '{}', '{}', 0),
(5, 5, 'default', 2014, 71, 1, '陈雄辉', 0, 'student', 123, '{}', '{}', '{}', 'google China', 0, '{}', '{}', '{}', 0),
(6, 6, 'default', 2014, 71, 1, '陈雄辉', 0, 'student', 123, '{}', '{}', '{}', 'google China', 0, '{}', '{}', '{}', 0),
(7, 7, 'default', 2014, 71, 1, '陈雄辉', 0, 'student', 123, '{}', '{}', '{}', 'google China', 0, '{}', '{}', '{}', 0),
(8, 8, 'default', 2014, 71, 1, '陈雄辉', 0, 'student', 123, '{}', '{}', '{}', 'google China', 0, '{}', '{}', '{}', 0),
(9, 9, 'default', 2014, 71, 1, '陈雄辉', 0, 'student', 123, '{}', '{}', '{}', 'google China', 0, '{}', '{}', '{}', 0),
(10, 10, 'default', 2014, 71, 1, '陈雄辉', 0, 'student', 123, '{}', '{}', '{}', 'google China', 0, '{}', '{}', '{}', 0),
(11, 11, 'default', 2014, 71, 1, '陈雄辉', 0, 'student', 123, '{}', '{}', '{}', 'google China', 0, '{}', '{}', '{}', 0),
(12, 12, 'default', 2014, 71, 1, '陈雄辉', 0, 'student', 123, '{}', '{}', '{}', 'google China', 0, '{}', '{}', '{}', 0),
(13, 13, 'default', 2014, 71, 1, '陈雄辉', 0, 'student', 123, '{}', '{}', '{}', 'google China', 0, '{}', '{}', '{}', 0),
(14, 14, 'default', 2014, 71, 1, '陈雄辉', 0, 'student', 123, '{}', '{}', '{}', 'google China', 0, '{}', '{}', '{}', 0),
(15, 15, 'default', 2014, 71, 1, '陈雄辉', 0, 'student', 123, '{}', '{}', '{}', 'google China', 0, '{}', '{}', '{}', 0),
(16, 16, 'default', 2014, 71, 1, '陈雄辉', 0, 'student', 123, '{}', '{}', '{}', 'google China', 0, '{}', '{}', '{}', 0),
(17, 17, 'default', 2014, 71, 1, '陈雄辉', 0, 'student', 123, '{}', '{}', '{}', 'google China', 0, '{}', '{}', '{}', 0),
(18, 18, 'default', 2014, 71, 1, '陈雄辉', 0, 'student', 123, '{}', '{}', '{}', 'google China', 0, '{}', '{}', '{}', 0),
(19, 19, 'default', 2014, 71, 1, '陈雄辉', 0, 'student', 123, '{}', '{}', '{}', 'google China', 0, '{}', '{}', '{}', 0),
(20, 20, 'default', 2014, 71, 1, '陈雄辉', 0, 'student', 123, '{}', '{}', '{}', 'google China', 0, '{}', '{}', '{}', 0),
(21, 21, 'default', 2014, 71, 1, '陈雄辉', 0, 'student', 123, '{}', '{}', '{}', 'google China', 0, '{}', '{}', '{}', 0),
(22, 22, 'default', 2014, 71, 1, '陈雄辉', 0, 'student', 123, '{}', '{}', '{}', 'google China', 0, '{}', '{}', '{}', 0),
(23, 23, 'default', 2014, 71, 1, '陈雄辉', 0, 'student', 123, '{}', '{}', '{}', 'google China', 0, '{}', '{}', '{}', 0),
(24, 24, 'default', 2014, 71, 1, '陈雄辉', 0, 'student', 123, '{}', '{}', '{}', 'google China', 0, '{}', '{}', '{}', 0),
(25, 25, 'default', 2014, 71, 1, '陈雄辉', 0, 'student', 123, '{}', '{}', '{}', 'google China', 0, '{}', '{}', '{}', 0),
(26, 26, 'default', 2014, 71, 1, '陈雄辉', 0, 'student', 123, '{}', '{}', '{}', 'google China', 0, '{}', '{}', '{}', 0),
(27, 27, 'default', 2014, 71, 1, '陈雄辉', 0, 'student', 123, '{}', '{}', '{}', 'google China', 0, '{}', '{}', '{}', 0);

-- --------------------------------------------------------

--
-- 表的结构 `ac_user_list_info`
--

CREATE TABLE IF NOT EXISTS `ac_user_list_info` (
  `list_id` int(11) NOT NULL AUTO_INCREMENT COMMENT '列表信息id',
  `uid` int(11) NOT NULL COMMENT '外键，关联 user_info(id)',
  `icon_url` varchar(128) NOT NULL COMMENT '头像的url地址',
  `name` varchar(9) NOT NULL COMMENT '姓名',
  `faculty_id` tinyint(3) NOT NULL COMMENT '院系id',
  `major_id` tinyint(3) NOT NULL COMMENT '专业id',
  `job` varchar(16) NOT NULL COMMENT '现在工作[可修改]',
  `gender` tinyint(1) NOT NULL COMMENT '性别',
  `publicity_level` tinyint(1) NOT NULL DEFAULT '0' COMMENT 'bool类型，设置能否被模糊搜索匹配到',
  `admission_year` smallint(4) NOT NULL COMMENT '入学年份',
  `city` int(11) NOT NULL,
  PRIMARY KEY (`list_id`),
  KEY `uid` (`uid`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=28 ;

--
-- 转存表中的数据 `ac_user_list_info`
--

INSERT INTO `ac_user_list_info` (`list_id`, `uid`, `icon_url`, `name`, `faculty_id`, `major_id`, `job`, `gender`, `publicity_level`, `admission_year`, `city`) VALUES
(1, 1, 'default', '陈雄辉', 71, 1, 'worker100', 0, 0, 2014, 321),
(2, 2, 'default', '陈雄辉', 71, 1, 'student', 0, 0, 2014, 123),
(3, 3, 'default', '陈雄辉', 71, 1, 'student', 0, 0, 2014, 123),
(4, 4, 'default', '陈雄辉', 71, 1, 'student', 0, 0, 2014, 123),
(5, 5, 'default', '陈雄辉', 71, 1, 'student', 0, 0, 2014, 123),
(6, 6, 'default', '陈雄辉', 71, 1, 'student', 0, 0, 2014, 123),
(7, 7, 'default', '陈雄辉', 71, 1, 'student', 0, 0, 2014, 123),
(8, 8, 'default', '陈雄辉', 71, 1, 'student', 0, 0, 2014, 123),
(9, 9, 'default', '陈雄辉', 71, 1, 'student', 0, 0, 2014, 123),
(10, 10, 'default', '陈雄辉', 71, 1, 'student', 0, 0, 2014, 123),
(11, 11, 'default', '陈雄辉', 71, 1, 'student', 0, 0, 2014, 123),
(12, 12, 'default', '陈雄辉', 71, 1, 'student', 0, 0, 2014, 123),
(13, 13, 'default', '陈雄辉', 71, 1, 'student', 0, 0, 2014, 123),
(14, 14, 'default', '陈雄辉', 71, 1, 'student', 0, 0, 2014, 123),
(15, 15, 'default', '陈雄辉', 71, 1, 'student', 0, 0, 2014, 123),
(16, 16, 'default', '陈雄辉', 71, 1, 'student', 0, 0, 2014, 123),
(17, 17, 'default', '陈雄辉', 71, 1, 'student', 0, 0, 2014, 123),
(18, 18, 'default', '陈雄辉', 71, 1, 'student', 0, 0, 2014, 123),
(19, 19, 'default', '陈雄辉', 71, 1, 'student', 0, 0, 2014, 123),
(20, 20, 'default', '陈雄辉', 71, 1, 'student', 0, 0, 2014, 123),
(21, 21, 'default', '陈雄辉', 71, 1, 'student', 0, 0, 2014, 123),
(22, 22, 'default', '陈雄辉', 71, 1, 'student', 0, 0, 2014, 123),
(23, 23, 'default', '陈雄辉', 71, 1, 'student', 0, 0, 2014, 123),
(24, 24, 'default', '陈雄辉', 71, 1, 'student', 0, 0, 2014, 123),
(25, 25, 'default', '陈雄辉', 71, 1, 'student', 0, 0, 2014, 123),
(26, 26, 'default', '陈雄辉', 71, 1, 'student', 0, 0, 2014, 123),
(27, 27, 'default', '陈雄辉', 71, 1, 'student', 0, 0, 2014, 123);

-- --------------------------------------------------------

--
-- 表的结构 `ac_user_message_table`
--

CREATE TABLE IF NOT EXISTS `ac_user_message_table` (
  `um_id` int(11) NOT NULL AUTO_INCREMENT COMMENT '用户维护的新消息列表的id',
  `uid` int(11) NOT NULL COMMENT '用户的id',
  `message_queue` varchar(510) NOT NULL DEFAULT '{}' COMMENT '用户的消息队列',
  `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '这个消息队列的最后更新日期',
  PRIMARY KEY (`um_id`),
  KEY `uid` (`uid`),
  KEY `uid_2` (`uid`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=111 ;

--
-- 转存表中的数据 `ac_user_message_table`
--

INSERT INTO `ac_user_message_table` (`um_id`, `uid`, `message_queue`, `update_time`) VALUES
(1, 131, '{}', '2016-08-27 03:10:35'),
(2, 132, '{}', '2016-08-27 03:11:36'),
(3, 133, '{}', '2016-08-27 04:10:35'),
(4, 134, '{}', '2016-08-27 04:11:13'),
(5, 135, '{}', '2016-08-27 04:12:39'),
(6, 137, '{}', '2016-08-27 04:13:45'),
(7, 1, '{}', '2016-08-27 04:20:56'),
(8, 139, '{}', '2016-08-27 04:21:54'),
(9, 140, '{}', '2016-08-27 04:23:12'),
(10, 141, '{}', '2016-08-27 10:34:56'),
(11, 142, '{}', '2016-08-27 10:35:51'),
(12, 143, '{}', '2016-08-27 10:36:24'),
(13, 144, '{}', '2016-08-27 10:36:51'),
(14, 145, '{}', '2016-08-27 10:37:54'),
(15, 146, '{}', '2016-08-27 10:48:22'),
(16, 147, '{}', '2016-08-27 10:48:30'),
(17, 148, '{}', '2016-08-27 10:52:19'),
(18, 149, '{}', '2016-08-27 10:52:43'),
(19, 150, '{}', '2016-08-27 10:53:06'),
(20, 151, '{}', '2016-08-27 10:54:11'),
(21, 152, '{}', '2016-08-27 10:55:03'),
(22, 153, '{}', '2016-08-27 11:07:16'),
(23, 154, '{}', '2016-08-27 11:19:52'),
(24, 155, '{}', '2016-08-27 11:20:31'),
(25, 156, '{}', '2016-08-27 11:20:55'),
(26, 157, '{}', '2016-08-27 11:21:20'),
(27, 158, '{}', '2016-08-27 11:55:41'),
(28, 159, '{}', '2016-08-27 11:56:31'),
(29, 160, '{}', '2016-08-27 11:57:05'),
(30, 161, '{}', '2016-08-27 11:57:25'),
(31, 162, '{}', '2016-08-27 11:58:33'),
(32, 163, '{}', '2016-08-27 11:59:05'),
(33, 164, '{}', '2016-08-27 12:00:49'),
(34, 165, '{}', '2016-08-27 12:01:49'),
(35, 166, '{}', '2016-08-27 12:04:44'),
(36, 167, '{}', '2016-08-27 12:05:56'),
(37, 168, '{}', '2016-08-27 12:06:05'),
(38, 169, '{}', '2016-08-27 12:12:43'),
(39, 170, '{}', '2016-08-27 12:13:29'),
(40, 171, '{}', '2016-08-27 12:13:55'),
(41, 172, '{}', '2016-08-27 12:15:48'),
(42, 173, '{}', '2016-08-27 12:17:51'),
(43, 174, '{}', '2016-08-27 12:19:17'),
(44, 175, '{}', '2016-08-27 12:19:57'),
(45, 176, '{}', '2016-08-27 12:20:48'),
(46, 177, '{}', '2016-08-27 12:21:29'),
(47, 178, '{}', '2016-08-27 12:21:49'),
(48, 179, '{}', '2016-08-27 12:22:39'),
(49, 180, '{}', '2016-08-27 12:23:28'),
(50, 181, '{}', '2016-08-27 12:43:26'),
(51, 182, '{}', '2016-08-27 12:59:08'),
(52, 183, '{}', '2016-08-27 13:00:02'),
(53, 184, '{}', '2016-08-27 13:00:39'),
(54, 185, '{}', '2016-08-27 13:00:50'),
(55, 186, '{}', '2016-08-27 13:20:01'),
(56, 187, '{}', '2016-08-27 13:20:37'),
(57, 188, '{}', '2016-08-27 13:21:08'),
(58, 189, '{}', '2016-08-27 13:24:15'),
(59, 190, '{}', '2016-08-27 13:29:03'),
(60, 191, '{}', '2016-08-27 13:30:36'),
(61, 192, '{}', '2016-08-27 13:31:30'),
(62, 193, '{}', '2016-08-27 13:38:01'),
(63, 194, '{}', '2016-08-27 13:38:58'),
(64, 195, '{}', '2016-08-27 13:40:55'),
(65, 196, '{}', '2016-08-27 13:42:03'),
(66, 197, '{}', '2016-08-27 13:43:53'),
(67, 198, '{}', '2016-08-27 13:45:08'),
(68, 199, '{}', '2016-08-27 13:49:11'),
(69, 200, '{}', '2016-08-27 13:55:53'),
(70, 201, '{}', '2016-08-27 13:56:31'),
(71, 202, '{}', '2016-08-27 14:03:08'),
(72, 203, '{}', '2016-08-27 14:03:22'),
(73, 204, '{}', '2016-08-27 14:04:13'),
(74, 205, '{}', '2016-08-27 14:04:40'),
(75, 206, '{}', '2016-08-27 14:04:43'),
(76, 207, '{}', '2016-08-27 14:06:32'),
(77, 208, '{}', '2016-08-27 14:06:53'),
(78, 209, '{}', '2016-08-27 14:07:49'),
(79, 210, '{}', '2016-08-28 05:44:37'),
(80, 211, '{}', '2016-08-28 05:45:41'),
(81, 212, '{}', '2016-08-28 05:46:37'),
(82, 213, '{}', '2016-08-28 05:48:23'),
(83, 214, '{}', '2016-08-28 05:48:35'),
(84, 215, '{}', '2016-08-28 05:50:39'),
(85, 216, '{}', '2016-08-28 05:51:45'),
(86, 218, '{}', '2016-08-28 05:53:01'),
(87, 219, '{}', '2016-08-28 05:53:15'),
(88, 220, '{}', '2016-08-28 05:56:49'),
(89, 221, '{}', '2016-08-28 06:00:15'),
(90, 222, '{}', '2016-08-28 06:00:35'),
(91, 223, '{}', '2016-08-28 06:05:57'),
(92, 224, '{}', '2016-08-28 10:05:43'),
(93, 225, '{}', '2016-08-28 10:06:21'),
(94, 226, '{}', '2016-08-28 10:07:10'),
(95, 227, '{}', '2016-08-28 10:08:26'),
(96, 228, '{}', '2016-08-28 10:09:15'),
(97, 229, '{}', '2016-08-28 10:09:45'),
(98, 230, '{}', '2016-08-28 10:10:47'),
(99, 231, '{}', '2016-08-28 16:12:36'),
(100, 232, '{}', '2016-08-28 16:12:36'),
(101, 233, '{}', '2016-08-28 16:15:01'),
(102, 234, '{}', '2016-08-28 16:15:02'),
(103, 235, '{}', '2016-08-28 16:15:24'),
(104, 236, '{}', '2016-08-28 16:15:25'),
(105, 237, '{}', '2016-08-28 16:16:47'),
(106, 238, '{}', '2016-08-28 16:16:49'),
(107, 239, '{}', '2016-08-28 16:17:36'),
(108, 240, '{}', '2016-08-28 16:17:36'),
(109, 241, '{}', '2016-08-28 16:18:50'),
(110, 242, '{}', '2016-08-28 16:18:51');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
