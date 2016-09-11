-- phpMyAdmin SQL Dump
-- version 4.0.10deb1
-- http://www.phpmyadmin.net
--
-- 主机: localhost
-- 生成日期: 2016-09-11 08:42:13
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
  `cid` int(11) NOT NULL AUTO_INCREMENT,
  `umeng_cid` varchar(32) NOT NULL,
  `umeng_virtual_cid` varchar(32) NOT NULL,
  `icon_url` varchar(255) NOT NULL,
  PRIMARY KEY (`cid`),
  KEY `umeng_cid` (`umeng_cid`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=24 ;

--
-- 转存表中的数据 `ac_circle_table`
--

INSERT INTO `ac_circle_table` (`cid`, `umeng_cid`, `umeng_virtual_cid`, `icon_url`) VALUES
(3, '57d2bbb7d36ef3ede32366f5', '57d2bbb7d36ef381d0510ea1', 'http://tupian.qqjay.com/tou3/2016/0605/222393536f052f6d5c1e293b8e065164.jpg'),
(4, '57d2bc9dd36ef3ede32367be', '57d2bc9dd36ef3ede32367ba', 'http://tupian.qqjay.com/tou3/2016/0605/222393536f052f6d5c1e293b8e065164.jpg'),
(17, '57d2ca3eb9a9960c9cb47a56', '57d2ca3eb9a9967859f14965', 'http://img1.imgtn.bdimg.com/it/u=1372134302,958716461&fm=206&gp=0.jpg'),
(18, '57d2dd11d36ef3fc508aee94', '57d2dd11b9a9967859f14f8e', 'http://img1.imgtn.bdimg.com/it/u=1372134302,958716461&fm=206&gp=0.jpg'),
(20, '57d3eb28b9a9964cdcff2cc1', '57d3eb28b9a9967859f15edc', 'http://img5.imgtn.bdimg.com/it/u=2856180651,1164389396&fm=206&gp=0.jpg'),
(21, '57d402d8b9a9965b02927330', '57d402d8b9a996112cc6cdf4', 'http://img5.imgtn.bdimg.com/it/u=2856180651,1164389396&fm=206&gp=0.jpg'),
(22, '57d421abd36ef3fc508b350f', '57d421abd36ef3fc508b350c', 'http://tupian.qqjay.com/tou3/2016/0605/222393536f052f6d5c1e293b8e065164.jpg'),
(23, '57d421abd36ef3fc508b350f', '57d421abd36ef3fc508b350c', 'http://tupian.qqjay.com/tou3/2016/0605/222393536f052f6d5c1e293b8e065164.jpg');

-- --------------------------------------------------------

--
-- 表的结构 `ac_manual_review_table`
--

CREATE TABLE IF NOT EXISTS `ac_manual_review_table` (
  `review_id` int(11) NOT NULL AUTO_INCREMENT COMMENT '请求id',
  `result` tinyint(1) NOT NULL DEFAULT '0' COMMENT '请求结果:0为处理,1接受.2拒绝',
  `circle_name` varchar(30) NOT NULL COMMENT '圈子名字',
  `circle_type_name` varchar(20) NOT NULL,
  `circle_icon_url` varchar(255) NOT NULL COMMENT '圈子的头像的url',
  `creator_uid` char(32) NOT NULL COMMENT '圈子的创建人的uid',
  `reason_message` varchar(340) NOT NULL COMMENT '创建的理由',
  `description` varchar(300) DEFAULT NULL,
  `creator_name` varchar(12) NOT NULL,
  PRIMARY KEY (`review_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=12 ;

--
-- 转存表中的数据 `ac_manual_review_table`
--

INSERT INTO `ac_manual_review_table` (`review_id`, `result`, `circle_name`, `circle_type_name`, `circle_icon_url`, `creator_uid`, `reason_message`, `description`, `creator_name`) VALUES
(1, 2, 'new circle 544', '学院圈', 'http://img1.imgtn.bdimg.com/it/u=1372134302,958716461&fm=206&gp=0.jpg', '14', 'I love you!', 'the circle will be beautiful!', '刘龙飞'),
(2, 2, 'ＩＯＳ开发小组', '职业圈', 'http://img1.imgtn.bdimg.com/it/u=1372134302,958716461&fm=206&gp=0.jpg', '14', '汇聚ＩＯＳ开发的大神,一起谈到交流', '汇聚所有IOS开发大神', '曾博晖'),
(3, 1, '带你装逼，带你飞 二号', '创业圈', 'http://img1.imgtn.bdimg.com/it/u=1372134302,958716461&fm=206&gp=0.jpg', '30', '大神不需要理由', '大神再此，带你装逼，带你飞', '大神'),
(4, 1, 'lol四个圈', '社团圈', 'http://img5.imgtn.bdimg.com/it/u=2856180651,1164389396&fm=206&gp=0.jpg', '37', 'lolololololololololo', '撸啊撸，撸啊撸，撸啊撸，撸啊撸', '大神爸爸'),
(5, 1, 'Dead', '兴趣圈', 'http://img5.imgtn.bdimg.com/it/u=2856180651,1164389396&fm=206&gp=0.jpg', '36', 'Jjjjjjjjj', 'Go dIe', '吴卓凡'),
(6, 0, 'life', '兴趣圈', 'http://img5.imgtn.bdimg.com/it/u=2856180651,1164389396&fm=206&gp=0.jpg', '36', 'Jjjjjjjjj', 'Go dIe', '吴卓凡'),
(7, 1, 'android开发小组2', '职业圈', 'http://tupian.qqjay.com/tou3/2016/0605/222393536f052f6d5c1e293b8e065164.jpg', '36', '汇聚android开发的大神,一起谈到交流', '汇聚所有android开发大神', '吴卓凡'),
(8, 0, 'sadasdas', '兴趣圈', 'http://img5.imgtn.bdimg.com/it/u=2856180651,1164389396&fm=206&gp=0.jpg', '30', 'sadasdas', 'Drfff', '大神'),
(9, 0, 'asdasd', '兴趣圈', 'http://img5.imgtn.bdimg.com/it/u=2856180651,1164389396&fm=206&gp=0.jpg', '30', 'Hghgb', 'Hh', '大神'),
(10, 0, 'kkljkljlkj', '兴趣圈', 'http://img5.imgtn.bdimg.com/it/u=2856180651,1164389396&fm=206&gp=0.jpg', '30', 'Jnjkbjk', 'Jkjjkhjkhj', '大神'),
(11, 0, 'jhjhjhjk', '兴趣圈', 'http://img5.imgtn.bdimg.com/it/u=2856180651,1164389396&fm=206&gp=0.jpg', '30', 'Kjkjk kjklklke', 'Jhjkhjkhjkhhjk', '大神');

-- --------------------------------------------------------

--
-- 表的结构 `ac_message_circle_table`
--

CREATE TABLE IF NOT EXISTS `ac_message_circle_table` (
  `mc_id` int(11) NOT NULL AUTO_INCREMENT,
  `umeng_circle_id` varchar(32) NOT NULL,
  `cid` varchar(32) NOT NULL,
  `message_queue` varchar(510) NOT NULL DEFAULT '_',
  `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`mc_id`),
  KEY `umeng_circle_id` (`cid`),
  KEY `umeng_circle_id_2` (`umeng_circle_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=23 ;

--
-- 转存表中的数据 `ac_message_circle_table`
--

INSERT INTO `ac_message_circle_table` (`mc_id`, `umeng_circle_id`, `cid`, `message_queue`, `update_time`) VALUES
(3, '57d2bbb7d36ef3ede32366f5', '3', '_', '2016-09-09 13:40:07'),
(4, '57d2bc9dd36ef3ede32367be', '4', '_', '2016-09-09 13:43:57'),
(17, '57d2ca3eb9a9960c9cb47a56', '17', '_', '2016-09-11 00:28:26'),
(18, '57d2dd11d36ef3fc508aee94', '18', '_', '2016-09-11 00:28:28'),
(19, '57d3eb28b9a9964cdcff2cc1', '19', '_', '2016-09-10 11:14:48'),
(20, '57d3eb28b9a9964cdcff2cc1', '20', '_', '2016-09-10 11:22:30'),
(21, '57d402d8b9a9965b02927330', '21', '_', '2016-09-10 12:55:52'),
(22, '57d421abd36ef3fc508b350f', '23', '_', '2016-09-10 15:09:47');

-- --------------------------------------------------------

--
-- 表的结构 `ac_message_table`
--

CREATE TABLE IF NOT EXISTS `ac_message_table` (
  `mid` int(11) NOT NULL AUTO_INCREMENT COMMENT '消息id',
  `type` tinyint(4) NOT NULL COMMENT '消息类型的说明字段',
  `message` varchar(1022) NOT NULL COMMENT '消息字段,是一个json数组',
  `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `finished` tinyint(1) NOT NULL DEFAULT '0' COMMENT '标记该消息是否已经被处理',
  PRIMARY KEY (`mid`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=42 ;

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
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=59 ;

--
-- 转存表中的数据 `ac_message_user_table`
--

INSERT INTO `ac_message_user_table` (`mu_id`, `uid`, `message_queue`, `update_time`) VALUES
(9, 11, '_', '2016-09-09 13:10:53'),
(10, 14, '_', '2016-09-11 00:29:01'),
(11, 15, '_', '2016-09-09 13:42:17'),
(12, 16, '_', '2016-09-09 13:42:41'),
(13, 17, '_', '2016-09-09 13:43:49'),
(14, 23, '_', '2016-09-09 13:56:17'),
(15, 24, '_', '2016-09-09 13:56:24'),
(16, 25, '_', '2016-09-09 14:02:46'),
(17, 26, '_', '2016-09-09 14:02:49'),
(18, 27, '_', '2016-09-09 14:04:33'),
(19, 28, '_', '2016-09-09 14:04:35'),
(20, 29, '_', '2016-09-09 14:20:17'),
(21, 30, '_', '2016-09-11 00:29:01'),
(22, 31, '_', '2016-09-09 14:24:17'),
(23, 32, '_', '2016-09-09 14:24:25'),
(24, 33, '_', '2016-09-09 14:55:49'),
(25, 34, '_', '2016-09-09 16:14:29'),
(26, 35, '_', '2016-09-09 16:19:20'),
(27, 36, '_', '2016-09-11 00:29:01'),
(28, 37, '_', '2016-09-11 00:29:01'),
(29, 38, '_', '2016-09-09 16:34:46'),
(30, 39, '_', '2016-09-09 16:48:02'),
(31, 40, '_', '2016-09-09 16:51:59'),
(32, 41, '_', '2016-09-09 17:11:15'),
(33, 42, '_', '2016-09-09 17:17:42'),
(34, 43, '_', '2016-09-09 17:21:30'),
(35, 44, '_', '2016-09-09 17:25:15'),
(36, 45, '_', '2016-09-09 17:28:44'),
(37, 46, '_', '2016-09-09 17:30:31'),
(38, 47, '_', '2016-09-09 17:35:55'),
(39, 48, '_', '2016-09-09 17:35:56'),
(40, 49, '_', '2016-09-09 17:35:58'),
(41, 50, '_', '2016-09-09 17:36:11'),
(42, 51, '_', '2016-09-09 17:36:13'),
(43, 52, '_', '2016-09-09 17:36:14'),
(44, 53, '_', '2016-09-09 17:36:15'),
(45, 54, '_', '2016-09-09 17:36:18'),
(46, 55, '_', '2016-09-09 17:36:25'),
(47, 56, '_', '2016-09-09 17:38:51'),
(48, 57, '_', '2016-09-09 17:38:54'),
(49, 58, '_', '2016-09-09 17:38:57'),
(50, 59, '_', '2016-09-09 17:44:58'),
(51, 60, '_', '2016-09-09 17:46:26'),
(52, 61, '_', '2016-09-09 17:48:37'),
(53, 62, '_', '2016-09-11 00:29:01'),
(54, 63, '_', '2016-09-09 17:52:49'),
(55, 64, '_', '2016-09-09 18:05:14'),
(56, 65, '_', '2016-09-09 18:10:34'),
(57, 66, '_', '2016-09-09 18:15:56'),
(58, 98, '_', '2016-09-10 10:47:25');

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
  `access_token` char(128) DEFAULT NULL,
  `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `umeng_id` varchar(24) DEFAULT ''' ''',
  PRIMARY KEY (`uid`),
  KEY `telephone` (`telephone`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=99 ;

--
-- 转存表中的数据 `ac_user_base_info`
--

INSERT INTO `ac_user_base_info` (`uid`, `adlevel`, `telephone`, `password`, `stu_id`, `access_token`, `update_time`, `umeng_id`) VALUES
(11, 0, '15996195485', 'cxh1234567', '95850831', '3eb436281264285cfa0d429a44b14617714371c8d2d7bcc5e1accc72735fd98da561fbc04fdf97e45c694d7dcf65f59868f0f1a255f1ca2f8c719db5586f6f43', '2016-09-09 13:10:53', '57d2b4ddb9a9967859f13e83'),
(12, 0, '15996161384', 'cxh1234567', '37496359', '3eb436281264285cfa0d429a44b14617714371c8d2d7bcc5e1accc72735fd98dd0056b6e75441869d2e798c50504c45cea4ca245c1aa26c0d5dce94bbd9b389e', '2016-09-09 13:13:54', ''' '''),
(13, 0, '15996169854', 'cxh1234567', '25897183', '3eb436281264285cfa0d429a44b14617714371c8d2d7bcc5e1accc72735fd98d705b6c6b928b5e453e92c1e9de431db62fa2ff3ecf7c8c90bcadeff502d97775', '2016-09-09 13:17:21', ''' '''),
(14, 0, '15996156914', 'cxh1234567', '97234774', '3eb436281264285cfa0d429a44b14617714371c8d2d7bcc5e1accc72735fd98df7b7cd46fe9c0ff1ad9658868ca7713e0f336f6a2b78a7071eab6eb5f8da38fa', '2016-09-09 13:17:56', '57d2b683d36ef35ee383d5e1'),
(15, 0, '15996195815', 'cxh1234567', '52583225', '3eb436281264285cfa0d429a44b14617714371c8d2d7bcc5e1accc72735fd98d616e32f6ec2ba36b9bd16f074f78b15fdbd02e3e72f17398cc69f0f80bc3ed64', '2016-09-09 13:42:17', '57d2bc39b9a9967859f142b5'),
(16, 0, '15996136665', 'cxh1234567', '49193496', '3eb436281264285cfa0d429a44b14617714371c8d2d7bcc5e1accc72735fd98d89b23f445cdfc8a6acc018dbd19feb58611a82bc137c76ff9210d54f8a5d4713', '2016-09-09 13:42:41', '57d2bc51d36ef381d0510fe0'),
(17, 0, '15996110751', 'cxh1234567', '28179787', '3eb436281264285cfa0d429a44b14617714371c8d2d7bcc5e1accc72735fd98d62567c857d7841da460533b2cb2a665b4a2a4443a731205d46cc18bcbc276c51', '2016-09-09 13:43:49', '57d2bc95b9a9964d13fd62b8'),
(26, 0, '15514410026', 'zbj123', '58040458', '3eb436281264285cfa0d429a44b14617714371c8d2d7bcc5e1accc72735fd98d3395b6709d913440943401884139a5205ef9ac262ee13f0a66b2db2af38c1248', '2016-09-09 14:02:49', '57d2be74d36ef3ede3236960'),
(27, 0, '15514410023', 'cxh123', '42445555', '3eb436281264285cfa0d429a44b14617714371c8d2d7bcc5e1accc72735fd98d2f9d3487b5ed6421bd496b4a5679ffe5809ba46119696d4174fbf9d5e03a3957', '2016-09-09 14:04:33', '57d2c171b9a9960c9cb478db'),
(29, 0, '15850682388', 'zbh123456', '87910776', '3eb436281264285cfa0d429a44b14617714371c8d2d7bcc5e1accc72735fd98db4dfd4d9d6b9a17bd38b83f92d2db289ca8936ee045deecf1da8141352b4a6f0', '2016-09-09 14:20:17', '57d2c521d36ef35ee383d99d'),
(30, 0, '15888888888', 'llf123456', '80965087', '3eb436281264285cfa0d429a44b14617714371c8d2d7bcc5e1accc72735fd98de8ba2438d81056e30fd1760e84018d156edd5099cacc2e313f99a627a9e17e3e', '2016-09-09 14:24:15', '57d2c60fd36ef3ede3236ebb'),
(33, 0, '15666666666', 'zbh123', '54877994', '3eb436281264285cfa0d429a44b14617714371c8d2d7bcc5e1accc72735fd98dd5c657f7a2c4f35a166a1e5cb39dd74b51b4816c0cd1269c854aca9b1c3fe8d6', '2016-09-09 14:55:49', '57d2cd75b9a996412946ef75'),
(34, 0, '18888888888', 'zbh123', '11578961', '3eb436281264285cfa0d429a44b14617714371c8d2d7bcc5e1accc72735fd98d9ef10d9ac8910cf47865ba442b5f7ef860d5052057875131a506f41120545a04', '2016-09-09 16:14:29', '57d2dfe5b9a9963fa44b2267'),
(35, 0, '18866666666', 'zbh123', '27103558', '3eb436281264285cfa0d429a44b14617714371c8d2d7bcc5e1accc72735fd98de5a01f17809b08f3044c05777c4a242e0576af2323b30a04370869095d441bb1', '2016-09-09 16:19:20', '57d2e108d36ef3fc508af59d'),
(36, 0, '18888888886', 'zbh123', '37265970', '3eb436281264285cfa0d429a44b14617714371c8d2d7bcc5e1accc72735fd98d5096e13b42fb621088f5e3b199a10a383d2db4a9dfe50afb5e9210c8241dfb01', '2016-09-09 16:25:28', '57d2e278b9a996414d2786b0'),
(37, 0, '15999999999', 'zbh123', '89815390', '3eb436281264285cfa0d429a44b14617714371c8d2d7bcc5e1accc72735fd98d1e84463e355adaba1193b1873e024fc25831d672491c7c429c1e840c0721ffce', '2016-09-09 16:32:11', '57d2e40bb9a9965b930836bb'),
(38, 0, '13888888888', 'zbh123', '78165943', '3eb436281264285cfa0d429a44b14617714371c8d2d7bcc5e1accc72735fd98d04b923a3e4f6e56a00de28d85823e30d062c891cac58467d98eaa0ea460631a3', '2016-09-09 16:34:46', '57d2e4a6d36ef3fc508afc0d'),
(39, 0, '13666666666', 'zbh123', '81769798', '3eb436281264285cfa0d429a44b14617714371c8d2d7bcc5e1accc72735fd98de58261439fb409f3d690da15a3480f9f4d30e281724f0dee10dbc59a23118758', '2016-09-09 16:48:02', '57d2e7c1d36ef381d0513040'),
(40, 0, '15699999999', 'zbh123', '80099337', '3eb436281264285cfa0d429a44b14617714371c8d2d7bcc5e1accc72735fd98d64da3d3ef604596bd1b5576ef4172bfaf75db18f9ef80634cc8e777b0fefa274', '2016-09-09 16:51:59', '57d2e8aeb9a996407f8b96c4'),
(41, 0, '15369936993', 'zbh123', '56419471', '3eb436281264285cfa0d429a44b14617714371c8d2d7bcc5e1accc72735fd98db1ba39fd7b63b6b9cc5d8f9911f023138e1272575038b32e35ea9343b6c203a6', '2016-09-09 17:11:15', '57d2ed32d36ef381d05130da'),
(42, 0, '13568974222', 'zbh521', '30053453', '3eb436281264285cfa0d429a44b14617714371c8d2d7bcc5e1accc72735fd98d3a36bd3ed4e85c661cbeb919a04fb6807d6e05536fd1be1767fc6181c1daeff8', '2016-09-09 17:17:42', '57d2eeb6b9a9964ee18c5908'),
(43, 0, '18969969699', 'zbh123', '59481670', '3eb436281264285cfa0d429a44b14617714371c8d2d7bcc5e1accc72735fd98d5bbeb7cfb5b92d213dd745f6f105fef9aabc2c45e9fe266606c07c8e5b675b64', '2016-09-09 17:21:30', '57d2ef9ab9a9964ca6d4321e'),
(44, 0, '15999996669', 'zbh123', '91987110', '3eb436281264285cfa0d429a44b14617714371c8d2d7bcc5e1accc72735fd98da9c67d85aeeb7d0565653ee372dda14dfcd4df3cbe76c116a8debe10c10be643', '2016-09-09 17:25:15', '57d2f07ad36ef3fc508b11ed'),
(45, 0, '15699999955', 'vvvvvvvv', '94612181', '3eb436281264285cfa0d429a44b14617714371c8d2d7bcc5e1accc72735fd98d2058337bd970d81f6ff3df83aba8cacb7fbc07b944212d397c451bf43389ef58', '2016-09-09 17:28:44', '57d2f14cd36ef381d0513134'),
(46, 0, '18899696966', 'gggggggg', '80432959', '3eb436281264285cfa0d429a44b14617714371c8d2d7bcc5e1accc72735fd98d0cd724052ad6588cbfe2398df54e6ca767b3314198531111d2579c32321755b7', '2016-09-09 17:30:31', '57d2f1b7d36ef3fc508b1221'),
(47, 0, '15151874563', 'wzf123456', '90588102', '3eb436281264285cfa0d429a44b14617714371c8d2d7bcc5e1accc72735fd98da9d413be4190075da3d91a6b6c364f900e880dd6b62f1e0358324503db8d3935', '2016-09-09 17:35:55', '57d2f2fad36ef3fc508b1280'),
(48, 0, '15151874563', 'wzf123456', '61623697', '3eb436281264285cfa0d429a44b14617714371c8d2d7bcc5e1accc72735fd98da9d413be4190075da3d91a6b6c364f900e880dd6b62f1e0358324503db8d3935', '2016-09-09 17:35:56', '57d2f2fad36ef3fc508b1280'),
(49, 0, '15151874563', 'wzf123456', '13950776', '3eb436281264285cfa0d429a44b14617714371c8d2d7bcc5e1accc72735fd98da9d413be4190075da3d91a6b6c364f900e880dd6b62f1e0358324503db8d3935', '2016-09-09 17:35:58', '57d2f2fad36ef3fc508b1280'),
(50, 0, '15151874563', 'wzf123456', '21256016', '3eb436281264285cfa0d429a44b14617714371c8d2d7bcc5e1accc72735fd98da9d413be4190075da3d91a6b6c364f900e880dd6b62f1e0358324503db8d3935', '2016-09-09 17:36:11', '57d2f2fad36ef3fc508b1280'),
(51, 0, '15151874563', 'wzf123456', '64373811', '3eb436281264285cfa0d429a44b14617714371c8d2d7bcc5e1accc72735fd98da9d413be4190075da3d91a6b6c364f900e880dd6b62f1e0358324503db8d3935', '2016-09-09 17:36:13', '57d2f2fad36ef3fc508b1280'),
(52, 0, '15151874563', 'wzf123456', '86194059', '3eb436281264285cfa0d429a44b14617714371c8d2d7bcc5e1accc72735fd98da9d413be4190075da3d91a6b6c364f900e880dd6b62f1e0358324503db8d3935', '2016-09-09 17:36:14', '57d2f2fad36ef3fc508b1280'),
(53, 0, '15151874563', 'wzf123456', '19848193', '3eb436281264285cfa0d429a44b14617714371c8d2d7bcc5e1accc72735fd98da9d413be4190075da3d91a6b6c364f900e880dd6b62f1e0358324503db8d3935', '2016-09-09 17:36:15', '57d2f2fad36ef3fc508b1280'),
(54, 0, '15151874563', 'wzf123456', '96201120', '3eb436281264285cfa0d429a44b14617714371c8d2d7bcc5e1accc72735fd98da9d413be4190075da3d91a6b6c364f900e880dd6b62f1e0358324503db8d3935', '2016-09-09 17:36:18', '57d2f2fad36ef3fc508b1280'),
(55, 0, '15151874563', 'wzf123456', '90136677', '3eb436281264285cfa0d429a44b14617714371c8d2d7bcc5e1accc72735fd98da9d413be4190075da3d91a6b6c364f900e880dd6b62f1e0358324503db8d3935', '2016-09-09 17:36:25', '57d2f2fad36ef3fc508b1280'),
(56, 0, '15151871234', 'wzf123456', '24814544', '3eb436281264285cfa0d429a44b14617714371c8d2d7bcc5e1accc72735fd98d4eff0b0fcd88a4340cdda62bc777dd0ad3029e4dc99e398622b9ff7f58bf4932', '2016-09-09 17:38:51', '57d2f3aad36ef3fc508b128d'),
(57, 0, '15151871234', 'wzf123456', '13986486', '3eb436281264285cfa0d429a44b14617714371c8d2d7bcc5e1accc72735fd98d4eff0b0fcd88a4340cdda62bc777dd0ad3029e4dc99e398622b9ff7f58bf4932', '2016-09-09 17:38:54', '57d2f3aad36ef3fc508b128d'),
(58, 0, '15151871234', 'wzf123456', '65971497', '3eb436281264285cfa0d429a44b14617714371c8d2d7bcc5e1accc72735fd98d4eff0b0fcd88a4340cdda62bc777dd0ad3029e4dc99e398622b9ff7f58bf4932', '2016-09-09 17:38:57', '57d2f3aad36ef3fc508b128d'),
(59, 0, '15599699688', 'zbh123', '54836470', '3eb436281264285cfa0d429a44b14617714371c8d2d7bcc5e1accc72735fd98db197a1195a49f09ee551197f1f0757dee9a16871b82b9c1d11405a808e1084e3', '2016-09-09 17:44:58', '57d2f51ab9a9965b029267a9'),
(60, 0, '15689898989', 'zbh123', '37996110', '3eb436281264285cfa0d429a44b14617714371c8d2d7bcc5e1accc72735fd98ddf5ca573ff8f2682c26f9c66473f809a5d0e2d63ae118dd283d60c3a9a260edf', '2016-09-09 17:46:26', '57d2f571d36ef3fc508b12b2'),
(61, 0, '15647898989', 'zcx445', '98228579', '3eb436281264285cfa0d429a44b14617714371c8d2d7bcc5e1accc72735fd98d9f6da4e4c78d776ac5def43b4d3a680908820bb626124b2e5e0f89f4a6ad7e21', '2016-09-09 17:48:37', '57d2f5f4d36ef3fc508b12bf'),
(62, 0, '15689236999', 'xcf324', '89195595', '3eb436281264285cfa0d429a44b14617714371c8d2d7bcc5e1accc72735fd98d363cfcf1df11c667566c357c73e022749fad0ce18f561314eadd7f121fb9e664', '2016-09-09 17:51:10', '57d2f68eb9a9965b029267b8'),
(63, 0, '15623456789', 'jjkk777', '36557680', '3eb436281264285cfa0d429a44b14617714371c8d2d7bcc5e1accc72735fd98d54a244c16de88b489a91c528aa6025ec4c93fa15c1159b15b66489bc43326ded', '2016-09-09 17:52:49', '57d2f6f1d36ef3fbfcb03943'),
(64, 1, '15195861108', 'e10adc3949ba59abbe56e057f20f883e', '32462530', '3eb436281264285cfa0d429a44b14617714371c8d2d7bcc5e1accc72735fd98d60b1a8506cb695e750626832a67db984ee03a956f34261dd15f1bf1e733104a0', '2016-09-10 07:56:55', '57d2f9dab9a9963aecd1af26'),
(98, 0, '15996122757', 'cxh1234567', '66545865', '3eb436281264285cfa0d429a44b14617714371c8d2d7bcc5e1accc72735fd98dab31019191c1d8f519e0801847f06079d7356dc2b7dd2ad465c8cb16949c399b', '2016-09-10 10:47:25', '57d3e4bcd36ef3fc508b2e3d');

-- --------------------------------------------------------

--
-- 表的结构 `ac_user_detail_info`
--

CREATE TABLE IF NOT EXISTS `ac_user_detail_info` (
  `detail_id` int(11) NOT NULL AUTO_INCREMENT COMMENT '详细信息列表的id',
  `uid` int(11) NOT NULL COMMENT '用户id',
  `icon_url` varchar(255) NOT NULL COMMENT '头像url地址',
  `admission_year` smallint(4) unsigned NOT NULL COMMENT '入学年份',
  `faculty` varchar(20) NOT NULL COMMENT '院系ＩＤ',
  `major` varchar(20) NOT NULL COMMENT '专业id',
  `name` varchar(8) NOT NULL COMMENT '真实姓名',
  `gender` tinyint(1) NOT NULL COMMENT '性别',
  `job` varchar(20) NOT NULL COMMENT '工作',
  `city` varchar(20) NOT NULL COMMENT '城市编号',
  `tags` varchar(350) NOT NULL DEFAULT '{}' COMMENT '个性标签',
  `instroduction` varchar(350) NOT NULL DEFAULT '{}' COMMENT '个性介绍',
  `my_circle_list` varchar(1022) NOT NULL DEFAULT '_' COMMENT '他加入的圈子列表',
  `company` varchar(20) NOT NULL COMMENT '公司名称',
  `company_publicity_level` tinyint(1) NOT NULL DEFAULT '0' COMMENT '公司的开放程度',
  `public_contact_list` varchar(126) NOT NULL DEFAULT '{}' COMMENT '公开的联系方式列表',
  `protect_contact_list` varchar(126) NOT NULL DEFAULT '{}' COMMENT '仅圈内好友可见的联系方式列表',
  `job_list` varchar(1022) NOT NULL DEFAULT '{}' COMMENT '工作经历列表',
  `job_list_level` tinyint(1) NOT NULL DEFAULT '0' COMMENT '工作列表的公开程度',
  `last_update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `admin_circle_list` varchar(655) DEFAULT '_',
  `create_circle_list` varchar(655) DEFAULT '_',
  `state` varchar(20) NOT NULL,
  `country` varchar(20) NOT NULL,
  PRIMARY KEY (`detail_id`),
  UNIQUE KEY `detail_id` (`detail_id`),
  KEY `uid` (`detail_id`),
  KEY `uid_2` (`uid`),
  KEY `uid_3` (`uid`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=59 ;

--
-- 转存表中的数据 `ac_user_detail_info`
--

INSERT INTO `ac_user_detail_info` (`detail_id`, `uid`, `icon_url`, `admission_year`, `faculty`, `major`, `name`, `gender`, `job`, `city`, `tags`, `instroduction`, `my_circle_list`, `company`, `company_publicity_level`, `public_contact_list`, `protect_contact_list`, `job_list`, `job_list_level`, `last_update_time`, `admin_circle_list`, `create_circle_list`, `state`, `country`) VALUES
(9, 11, 'http://tupian.qqjay.com/tou3/2016/0605/222393536f052f6d5c1e293b8e065164.jpg', 2014, '软件', '能源与环境学院', '刘龙飞', 0, '设计师', '南京', '{}', '{}', '_', 'google China', 0, '{}', '{}', '{}', 0, '2016-09-09 13:10:53', '_', '_', '江苏', '中国'),
(10, 14, 'http://tupian.qqjay.com/tou3/2016/0605/222393536f052f6d5c1e293b8e065164.jpg', 2014, '生物医学工程硕士', '生物科学与医学工程学院(研)', '刘龙飞', 0, '设计师', '杭州', '{}', '{}', '_', 'google China', 0, '{}', '{}', '{}', 0, '2016-09-09 13:17:56', '_', '_', '浙江', '中国'),
(11, 15, 'http://tupian.qqjay.com/tou3/2016/0605/222393536f052f6d5c1e293b8e065164.jpg', 2014, '建筑设计及其理论', '建筑学院(研)', '曾博晖', 0, '设计师', '洛阳', '{}', '{}', '_', 'google China', 0, '{}', '{}', '{}', 0, '2016-09-09 13:42:17', '_', '_', '河南', '中国'),
(12, 16, 'http://tupian.qqjay.com/tou3/2016/0605/222393536f052f6d5c1e293b8e065164.jpg', 2014, '建筑设计及其理论', '建筑学院(研)', '曾博晖', 0, '设计师', '洛阳', '{}', '{}', '_', 'google China', 0, '{}', '{}', '{}', 0, '2016-09-09 13:42:41', '_', '_', '河南', '中国'),
(13, 17, 'http://tupian.qqjay.com/tou3/2016/0605/222393536f052f6d5c1e293b8e065164.jpg', 2014, '建筑设计及其理论', '建筑学院(研)', '曾博晖', 0, '设计师', '洛阳', '{}', '{}', '_', 'google China', 0, '{}', '{}', '{}', 0, '2016-09-09 13:43:49', '_', '_', '河南', '中国'),
(14, 23, 'http://b.hiphotos.baidu.com/zhidao/wh%3D450%2C600/sign=45f10be75edf8db1bc7b74603c13f162/023b5bb5c9ea15ce2f42ea76b6003af33a87b224.jpg', 1988, '建筑学院', '建筑学', '曾博晖', 1, '首席执行官', '费耶特维尔', '{}', '{}', '_', '阿里巴巴', 0, '{}', '{}', '{}', 0, '2016-09-09 13:56:17', '_', '_', '阿肯色', '美国'),
(15, 24, 'http://b.hiphotos.baidu.com/zhidao/wh%3D450%2C600/sign=45f10be75edf8db1bc7b74603c13f162/023b5bb5c9ea15ce2f42ea76b6003af33a87b224.jpg', 1988, '建筑学院', '建筑学', '曾博晖', 1, '首席执行官', '费耶特维尔', '{}', '{}', '_', '阿里巴巴', 0, '{}', '{}', '{}', 0, '2016-09-09 13:56:24', '_', '_', '阿肯色', '美国'),
(16, 25, 'http://b.hiphotos.baidu.com/zhidao/wh%3D450%2C600/sign=45f10be75edf8db1bc7b74603c13f162/023b5bb5c9ea15ce2f42ea76b6003af33a87b224.jpg', 1952, '数学系', '数学与应用数学', '曾博晖', 1, '首席执行官', '费耶特维尔', '{}', '{}', '_', '阿里巴巴', 0, '{}', '{}', '{}', 0, '2016-09-09 14:02:46', '_', '_', '阿肯色', '美国'),
(17, 26, 'http://b.hiphotos.baidu.com/zhidao/wh%3D450%2C600/sign=45f10be75edf8db1bc7b74603c13f162/023b5bb5c9ea15ce2f42ea76b6003af33a87b224.jpg', 1952, '数学系', '数学与应用数学', '曾博晖', 1, '首席执行官', '费耶特维尔', '{}', '{}', '_', '阿里巴巴', 0, '{}', '{}', '{}', 0, '2016-09-09 14:02:49', '_', '_', '阿肯色', '美国'),
(18, 27, 'http://b.hiphotos.baidu.com/zhidao/wh%3D450%2C600/sign=45f10be75edf8db1bc7b74603c13f162/023b5bb5c9ea15ce2f42ea76b6003af33a87b224.jpg', 1965, '土木工程学院', '土木工程', '曾博晖', 1, '高级架构师', '贝尔法斯特', '{}', '{}', '_', '阿里巴巴', 0, '{}', '{}', '{}', 0, '2016-09-09 14:04:33', '_', '_', '北爱尔兰', '英国'),
(19, 28, 'http://b.hiphotos.baidu.com/zhidao/wh%3D450%2C600/sign=45f10be75edf8db1bc7b74603c13f162/023b5bb5c9ea15ce2f42ea76b6003af33a87b224.jpg', 1965, '土木工程学院', '土木工程', '曾博晖', 1, '高级架构师', '贝尔法斯特', '{}', '{}', '_', '阿里巴巴', 0, '{}', '{}', '{}', 0, '2016-09-09 14:04:35', '_', '_', '北爱尔兰', '英国'),
(20, 29, 'http://b.hiphotos.baidu.com/zhidao/wh%3D450%2C600/sign=45f10be75edf8db1bc7b74603c13f162/023b5bb5c9ea15ce2f42ea76b6003af33a87b224.jpg', 1952, '建筑学院', '建筑学', '白洋', 1, 'student', '南京', '{}', '{}', '_', 'the SEU', 0, '{}', '{}', '{}', 0, '2016-09-09 14:20:17', '_', '_', '江苏', '中国'),
(21, 30, 'http://b.hiphotos.baidu.com/zhidao/wh%3D450%2C600/sign=45f10be75edf8db1bc7b74603c13f162/023b5bb5c9ea15ce2f42ea76b6003af33a87b224.jpg', 1970, '电子科学与工程学院(研)', '光学工程', '大神', 1, '执行总裁', '杭州', '{}', '{}', '_', '阿里巴巴', 0, '{}', '{}', '{}', 0, '2016-09-09 14:24:15', '_', '_17_18_', '浙江', '中国'),
(22, 31, 'http://b.hiphotos.baidu.com/zhidao/wh%3D450%2C600/sign=45f10be75edf8db1bc7b74603c13f162/023b5bb5c9ea15ce2f42ea76b6003af33a87b224.jpg', 1970, '电子科学与工程学院(研)', '光学工程', '大神', 1, '执行总裁', '杭州', '{}', '{}', '_', '阿里巴巴', 0, '{}', '{}', '{}', 0, '2016-09-09 14:24:17', '_', '_', '浙江', '中国'),
(23, 32, 'http://b.hiphotos.baidu.com/zhidao/wh%3D450%2C600/sign=45f10be75edf8db1bc7b74603c13f162/023b5bb5c9ea15ce2f42ea76b6003af33a87b224.jpg', 1970, '电子科学与工程学院(研)', '光学工程', '大神', 1, '执行总裁', '杭州', '{}', '{}', '_', '阿里巴巴', 0, '{}', '{}', '{}', 0, '2016-09-09 14:24:25', '_', '_', '浙江', '中国'),
(24, 33, 'http://b.hiphotos.baidu.com/zhidao/wh%3D450%2C600/sign=45f10be75edf8db1bc7b74603c13f162/023b5bb5c9ea15ce2f42ea76b6003af33a87b224.jpg', 1988, '信息科学与工程学院(研)', '信息安全', '男神', 1, '首席执行官', '费耶特维尔', '{}', '{}', '_', '谷歌', 0, '{}', '{}', '{}', 0, '2016-09-09 14:55:49', '_', '_', '阿肯色', '美国'),
(25, 34, 'http://b.hiphotos.baidu.com/zhidao/wh%3D450%2C600/sign=45f10be75edf8db1bc7b74603c13f162/023b5bb5c9ea15ce2f42ea76b6003af33a87b224.jpg', 1952, '建筑学院(研)', '美术学', '曾博晖', 1, 'student', '南京', '{}', '{}', '_', 'the SEU', 0, '{}', '{}', '{}', 0, '2016-09-09 16:14:29', '_', '_', '江苏', '中国'),
(26, 35, 'http://b.hiphotos.baidu.com/zhidao/wh%3D450%2C600/sign=45f10be75edf8db1bc7b74603c13f162/023b5bb5c9ea15ce2f42ea76b6003af33a87b224.jpg', 1952, '建筑学院(研)', '美术学', '崔浩宇', 1, 'student', '南京', '{}', '{}', '_', 'the SEU', 0, '{}', '{}', '{}', 0, '2016-09-09 16:19:20', '_', '_', '江苏', '中国'),
(27, 36, 'http://b.hiphotos.baidu.com/zhidao/wh%3D450%2C600/sign=45f10be75edf8db1bc7b74603c13f162/023b5bb5c9ea15ce2f42ea76b6003af33a87b224.jpg', 1952, '建筑学院(研)', '美术学', '吴卓凡', 1, 'student', '南京', '{}', '{}', '_21_23_18_', 'the SEU', 0, '{}', '{}', '{}', 0, '2016-09-09 16:25:28', '_', '_21_23_', '江苏', '中国'),
(28, 37, 'http://b.hiphotos.baidu.com/zhidao/wh%3D450%2C600/sign=45f10be75edf8db1bc7b74603c13f162/023b5bb5c9ea15ce2f42ea76b6003af33a87b224.jpg', 1952, '建筑学院(研)', '美术学', '大神爸爸', 1, 'student', '南京', '{}', '{}', '_20_', 'the SEU', 0, '{}', '{}', '{}', 0, '2016-09-09 16:32:11', '_', '_20_', '江苏', '中国'),
(29, 38, 'http://b.hiphotos.baidu.com/zhidao/wh%3D450%2C600/sign=45f10be75edf8db1bc7b74603c13f162/023b5bb5c9ea15ce2f42ea76b6003af33a87b224.jpg', 1952, '建筑学院(研)', '美术学', '刘畅', 1, 'student', '南京', '{}', '{}', '_', 'the SEU', 0, '{}', '{}', '{}', 0, '2016-09-09 16:34:46', '_', '_', '江苏', '中国'),
(30, 39, 'http://b.hiphotos.baidu.com/zhidao/wh%3D450%2C600/sign=45f10be75edf8db1bc7b74603c13f162/023b5bb5c9ea15ce2f42ea76b6003af33a87b224.jpg', 1952, '建筑学院(研)', '美术学', '陈二逼', 1, 'student', '南京', '{}', '{}', '_', 'the SEU', 0, '{}', '{}', '{}', 0, '2016-09-09 16:48:02', '_', '_', '江苏', '中国'),
(31, 40, 'http://b.hiphotos.baidu.com/zhidao/wh%3D450%2C600/sign=45f10be75edf8db1bc7b74603c13f162/023b5bb5c9ea15ce2f42ea76b6003af33a87b224.jpg', 1952, '建筑学院(研)', '美术学', '雄辉', 1, 'student', '南京', '{}', '{}', '_', 'the SEU', 0, '{}', '{}', '{}', 0, '2016-09-09 16:51:59', '_', '_', '江苏', '中国'),
(32, 41, 'http://b.hiphotos.baidu.com/zhidao/wh%3D450%2C600/sign=45f10be75edf8db1bc7b74603c13f162/023b5bb5c9ea15ce2f42ea76b6003af33a87b224.jpg', 1952, '建筑学院(研)', '美术学', '你哪呢', 1, 'student', '南京', '{}', '{}', '_', 'the SEU', 0, '{}', '{}', '{}', 0, '2016-09-09 17:11:15', '_', '_', '江苏', '中国'),
(33, 42, 'http://b.hiphotos.baidu.com/zhidao/wh%3D450%2C600/sign=45f10be75edf8db1bc7b74603c13f162/023b5bb5c9ea15ce2f42ea76b6003af33a87b224.jpg', 1952, '建筑学院(研)', '美术学', '博晖', 1, 'student', '南京', '{}', '{}', '_', 'the SEU', 0, '{}', '{}', '{}', 0, '2016-09-09 17:17:42', '_', '_', '江苏', '中国'),
(34, 43, 'http://b.hiphotos.baidu.com/zhidao/wh%3D450%2C600/sign=45f10be75edf8db1bc7b74603c13f162/023b5bb5c9ea15ce2f42ea76b6003af33a87b224.jpg', 1952, '建筑学院(研)', '美术学', '陈晓华', 1, 'student', '南京', '{}', '{}', '_', 'the SEU', 0, '{}', '{}', '{}', 0, '2016-09-09 17:21:30', '_', '_', '江苏', '中国'),
(35, 44, 'http://b.hiphotos.baidu.com/zhidao/wh%3D450%2C600/sign=45f10be75edf8db1bc7b74603c13f162/023b5bb5c9ea15ce2f42ea76b6003af33a87b224.jpg', 1952, '建筑学院(研)', '美术学', '嘿嘿嘿', 1, 'student', '南京', '{}', '{}', '_', 'the SEU', 0, '{}', '{}', '{}', 0, '2016-09-09 17:25:15', '_', '_', '江苏', '中国'),
(36, 45, 'http://b.hiphotos.baidu.com/zhidao/wh%3D450%2C600/sign=45f10be75edf8db1bc7b74603c13f162/023b5bb5c9ea15ce2f42ea76b6003af33a87b224.jpg', 1956, '数学系(研)', '统计学', '啵啵啵', 1, 'student', '南京', '{}', '{}', '_', 'the SEU', 0, '{}', '{}', '{}', 0, '2016-09-09 17:28:44', '_', '_', '江苏', '中国'),
(37, 46, 'http://b.hiphotos.baidu.com/zhidao/wh%3D450%2C600/sign=45f10be75edf8db1bc7b74603c13f162/023b5bb5c9ea15ce2f42ea76b6003af33a87b224.jpg', 1952, '经济管理学院(研)', '国民经济学', '呵呵呵', 1, 'student', '南京', '{}', '{}', '_', 'the SEU', 0, '{}', '{}', '{}', 0, '2016-09-09 17:30:31', '_', '_', '江苏', '中国'),
(38, 47, 'http://b.hiphotos.baidu.com/zhidao/wh%3D450%2C600/sign=45f10be75edf8db1bc7b74603c13f162/023b5bb5c9ea15ce2f42ea76b6003af33a87b224.jpg', 1952, '建筑学院(研)', '美术学', '吴卓凡', 1, 'student', '南京', '{}', '{}', '_', 'the SEU', 0, '{}', '{}', '{}', 0, '2016-09-09 17:35:55', '_', '_', '江苏', '中国'),
(39, 48, 'http://b.hiphotos.baidu.com/zhidao/wh%3D450%2C600/sign=45f10be75edf8db1bc7b74603c13f162/023b5bb5c9ea15ce2f42ea76b6003af33a87b224.jpg', 1952, '建筑学院(研)', '美术学', '吴卓凡', 1, 'student', '南京', '{}', '{}', '_', 'the SEU', 0, '{}', '{}', '{}', 0, '2016-09-09 17:35:56', '_', '_', '江苏', '中国'),
(40, 49, 'http://b.hiphotos.baidu.com/zhidao/wh%3D450%2C600/sign=45f10be75edf8db1bc7b74603c13f162/023b5bb5c9ea15ce2f42ea76b6003af33a87b224.jpg', 1952, '建筑学院(研)', '美术学', '吴卓凡', 1, 'student', '南京', '{}', '{}', '_', 'the SEU', 0, '{}', '{}', '{}', 0, '2016-09-09 17:35:58', '_', '_', '江苏', '中国'),
(41, 50, 'http://b.hiphotos.baidu.com/zhidao/wh%3D450%2C600/sign=45f10be75edf8db1bc7b74603c13f162/023b5bb5c9ea15ce2f42ea76b6003af33a87b224.jpg', 1952, '建筑学院(研)', '美术学', '吴卓凡', 1, '我的天', '费耶特维尔', '{}', '{}', '_', '我的天', 0, '{}', '{}', '{}', 0, '2016-09-09 17:36:11', '_', '_', '阿肯色', '美国'),
(42, 51, 'http://b.hiphotos.baidu.com/zhidao/wh%3D450%2C600/sign=45f10be75edf8db1bc7b74603c13f162/023b5bb5c9ea15ce2f42ea76b6003af33a87b224.jpg', 1952, '建筑学院(研)', '美术学', '吴卓凡', 1, '我的天', '费耶特维尔', '{}', '{}', '_', '我的天', 0, '{}', '{}', '{}', 0, '2016-09-09 17:36:13', '_', '_', '阿肯色', '美国'),
(43, 52, 'http://b.hiphotos.baidu.com/zhidao/wh%3D450%2C600/sign=45f10be75edf8db1bc7b74603c13f162/023b5bb5c9ea15ce2f42ea76b6003af33a87b224.jpg', 1952, '建筑学院(研)', '美术学', '吴卓凡', 1, '我的天', '费耶特维尔', '{}', '{}', '_', '我的天', 0, '{}', '{}', '{}', 0, '2016-09-09 17:36:14', '_', '_', '阿肯色', '美国'),
(44, 53, 'http://b.hiphotos.baidu.com/zhidao/wh%3D450%2C600/sign=45f10be75edf8db1bc7b74603c13f162/023b5bb5c9ea15ce2f42ea76b6003af33a87b224.jpg', 1952, '建筑学院(研)', '美术学', '吴卓凡', 1, '我的天', '费耶特维尔', '{}', '{}', '_', '我的天', 0, '{}', '{}', '{}', 0, '2016-09-09 17:36:15', '_', '_', '阿肯色', '美国'),
(45, 54, 'http://b.hiphotos.baidu.com/zhidao/wh%3D450%2C600/sign=45f10be75edf8db1bc7b74603c13f162/023b5bb5c9ea15ce2f42ea76b6003af33a87b224.jpg', 1952, '建筑学院(研)', '美术学', '吴卓凡', 1, '我的天', '费耶特维尔', '{}', '{}', '_', '我的天', 0, '{}', '{}', '{}', 0, '2016-09-09 17:36:18', '_', '_', '阿肯色', '美国'),
(46, 55, 'http://b.hiphotos.baidu.com/zhidao/wh%3D450%2C600/sign=45f10be75edf8db1bc7b74603c13f162/023b5bb5c9ea15ce2f42ea76b6003af33a87b224.jpg', 1952, '建筑学院(研)', '美术学', '吴卓凡', 1, '我的天', '费耶特维尔', '{}', '{}', '_', '我的天', 0, '{}', '{}', '{}', 0, '2016-09-09 17:36:25', '_', '_', '阿肯色', '美国'),
(47, 56, 'http://b.hiphotos.baidu.com/zhidao/wh%3D450%2C600/sign=45f10be75edf8db1bc7b74603c13f162/023b5bb5c9ea15ce2f42ea76b6003af33a87b224.jpg', 1952, '建筑学院(研)', '美术学', '吴卓凡', 1, 'student', '南京', '{}', '{}', '_', 'the SEU', 0, '{}', '{}', '{}', 0, '2016-09-09 17:38:51', '_', '_', '江苏', '中国'),
(48, 57, 'http://b.hiphotos.baidu.com/zhidao/wh%3D450%2C600/sign=45f10be75edf8db1bc7b74603c13f162/023b5bb5c9ea15ce2f42ea76b6003af33a87b224.jpg', 1952, '建筑学院(研)', '美术学', '吴卓凡', 1, 'student', '南京', '{}', '{}', '_', 'the SEU', 0, '{}', '{}', '{}', 0, '2016-09-09 17:38:54', '_', '_', '江苏', '中国'),
(49, 58, 'http://b.hiphotos.baidu.com/zhidao/wh%3D450%2C600/sign=45f10be75edf8db1bc7b74603c13f162/023b5bb5c9ea15ce2f42ea76b6003af33a87b224.jpg', 1952, '建筑学院(研)', '美术学', '吴卓凡', 1, 'student', '南京', '{}', '{}', '_', 'the SEU', 0, '{}', '{}', '{}', 0, '2016-09-09 17:38:57', '_', '_', '江苏', '中国'),
(50, 59, 'http://b.hiphotos.baidu.com/zhidao/wh%3D450%2C600/sign=45f10be75edf8db1bc7b74603c13f162/023b5bb5c9ea15ce2f42ea76b6003af33a87b224.jpg', 1952, '建筑学院(研)', '美术学', '成本', 1, 'student', '南京', '{}', '{}', '_', 'the SEU', 0, '{}', '{}', '{}', 0, '2016-09-09 17:44:58', '_', '_', '江苏', '中国'),
(51, 60, 'http://b.hiphotos.baidu.com/zhidao/wh%3D450%2C600/sign=45f10be75edf8db1bc7b74603c13f162/023b5bb5c9ea15ce2f42ea76b6003af33a87b224.jpg', 1952, '建筑学院(研)', '美术学', '吼吼吼', 1, 'student', '南京', '{}', '{}', '_', 'the SEU', 0, '{}', '{}', '{}', 0, '2016-09-09 17:46:26', '_', '_', '江苏', '中国'),
(52, 61, 'http://b.hiphotos.baidu.com/zhidao/wh%3D450%2C600/sign=45f10be75edf8db1bc7b74603c13f162/023b5bb5c9ea15ce2f42ea76b6003af33a87b224.jpg', 1952, '建筑学院(研)', '美术学', '李龙飞', 1, 'student', '南京', '{}', '{}', '_', 'the SEU', 0, '{}', '{}', '{}', 0, '2016-09-09 17:48:37', '_', '_', '江苏', '中国'),
(53, 62, 'http://b.hiphotos.baidu.com/zhidao/wh%3D450%2C600/sign=45f10be75edf8db1bc7b74603c13f162/023b5bb5c9ea15ce2f42ea76b6003af33a87b224.jpg', 1952, '建筑学院(研)', '美术学', '学不会', 1, 'student', '南京', '{}', '{}', '_57d402d8b9a9965b02927330_17_', 'the SEU', 0, '{}', '{}', '{}', 0, '2016-09-09 17:51:10', '_', '_', '江苏', '中国'),
(54, 63, 'http://b.hiphotos.baidu.com/zhidao/wh%3D450%2C600/sign=45f10be75edf8db1bc7b74603c13f162/023b5bb5c9ea15ce2f42ea76b6003af33a87b224.jpg', 1952, '建筑学院(研)', '美术学', '慧慧回家', 1, 'student', '南京', '{}', '{}', '_', 'the SEU', 0, '{}', '{}', '{}', 0, '2016-09-09 17:52:49', '_', '_', '江苏', '中国'),
(55, 64, 'http://b.hiphotos.baidu.com/zhidao/wh%3D450%2C600/sign=45f10be75edf8db1bc7b74603c13f162/023b5bb5c9ea15ce2f42ea76b6003af33a87b224.jpg', 1952, '建筑学院(研)', '美术学', '你哪呢', 1, '斧子', '费耶特维尔', '{}', '{}', '_', '德莱文', 0, '{}', '{}', '{}', 0, '2016-09-09 18:05:14', '_', '_', '阿肯色', '美国'),
(56, 65, 'http://b.hiphotos.baidu.com/zhidao/wh%3D450%2C600/sign=45f10be75edf8db1bc7b74603c13f162/023b5bb5c9ea15ce2f42ea76b6003af33a87b224.jpg', 1952, '建筑学院(研)', '美术学', '陈三胖', 1, '打杂', '费耶特维尔', '{}', '{}', '_', '阿里巴巴', 0, '{}', '{}', '{}', 0, '2016-09-09 18:10:34', '_', '_', '阿肯色', '美国'),
(57, 66, 'http://b.hiphotos.baidu.com/zhidao/wh%3D450%2C600/sign=45f10be75edf8db1bc7b74603c13f162/023b5bb5c9ea15ce2f42ea76b6003af33a87b224.jpg', 1952, '建筑学院(研)', '美术学', '曾博晖', 1, '开车', '费耶特维尔', '{}', '{}', '_', '阿里巴巴', 0, '{}', '{}', '{}', 0, '2016-09-09 18:15:56', '_', '_', '阿肯色', '美国'),
(58, 98, 'http://tupian.qqjay.com/tou3/2016/0605/222393536f052f6d5c1e293b8e065164.jpg', 2014, '建筑设计及其理论', '建筑学院(研)', '曾博晖', 0, '设计师', '洛阳', '{}', '{}', '_', 'google China', 0, '{}', '{}', '{}', 0, '2016-09-10 10:47:25', '_', '_', '河南', '中国');

-- --------------------------------------------------------

--
-- 表的结构 `ac_user_list_info`
--

CREATE TABLE IF NOT EXISTS `ac_user_list_info` (
  `list_id` int(11) NOT NULL AUTO_INCREMENT COMMENT '列表信息id',
  `country` varchar(20) NOT NULL,
  `state` varchar(20) NOT NULL,
  `uid` int(11) NOT NULL COMMENT '外键，关联 user_info(id)',
  `icon_url` varchar(255) NOT NULL COMMENT '头像的url地址',
  `name` varchar(9) NOT NULL COMMENT '姓名',
  `faculty` varchar(20) NOT NULL COMMENT '院系id',
  `major` varchar(20) NOT NULL COMMENT '专业id',
  `job` varchar(16) NOT NULL COMMENT '现在工作[可修改]',
  `gender` tinyint(1) NOT NULL COMMENT '性别',
  `publicity_level` tinyint(1) NOT NULL DEFAULT '0' COMMENT 'bool类型，设置能否被模糊搜索匹配到',
  `admission_year` smallint(4) NOT NULL COMMENT '入学年份',
  `city` varchar(20) NOT NULL,
  PRIMARY KEY (`list_id`),
  KEY `uid` (`uid`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=59 ;

--
-- 转存表中的数据 `ac_user_list_info`
--

INSERT INTO `ac_user_list_info` (`list_id`, `country`, `state`, `uid`, `icon_url`, `name`, `faculty`, `major`, `job`, `gender`, `publicity_level`, `admission_year`, `city`) VALUES
(9, '中国', '江苏', 11, 'http://tupian.qqjay.com/tou3/2016/0605/222393536f052f6d5c1e293b8e065164.jpg', '刘龙飞', '软件', '能源与环境学院', '设计师', 0, 0, 2014, '南京'),
(10, '中国', '浙江', 14, 'http://tupian.qqjay.com/tou3/2016/0605/222393536f052f6d5c1e293b8e065164.jpg', '刘龙飞', '生物医学工程硕士', '生物科学与医学工程学院(研)', '设计师', 0, 0, 2014, '杭州'),
(11, '中国', '河南', 15, 'http://tupian.qqjay.com/tou3/2016/0605/222393536f052f6d5c1e293b8e065164.jpg', '曾博晖', '建筑设计及其理论', '建筑学院(研)', '设计师', 0, 0, 2014, '洛阳'),
(12, '中国', '河南', 16, 'http://tupian.qqjay.com/tou3/2016/0605/222393536f052f6d5c1e293b8e065164.jpg', '曾博晖', '建筑设计及其理论', '建筑学院(研)', '设计师', 0, 0, 2014, '洛阳'),
(13, '中国', '河南', 17, 'http://tupian.qqjay.com/tou3/2016/0605/222393536f052f6d5c1e293b8e065164.jpg', '曾博晖', '建筑设计及其理论', '建筑学院(研)', '设计师', 0, 0, 2014, '洛阳'),
(14, '美国', '阿肯色', 23, 'http://b.hiphotos.baidu.com/zhidao/wh%3D450%2C600/sign=45f10be75edf8db1bc7b74603c13f162/023b5bb5c9ea15ce2f42ea76b6003af33a87b224.jpg', '曾博晖', '建筑学院', '建筑学', '首席执行官', 1, 0, 1988, '费耶特维尔'),
(15, '美国', '阿肯色', 24, 'http://b.hiphotos.baidu.com/zhidao/wh%3D450%2C600/sign=45f10be75edf8db1bc7b74603c13f162/023b5bb5c9ea15ce2f42ea76b6003af33a87b224.jpg', '曾博晖', '建筑学院', '建筑学', '首席执行官', 1, 0, 1988, '费耶特维尔'),
(16, '美国', '阿肯色', 25, 'http://b.hiphotos.baidu.com/zhidao/wh%3D450%2C600/sign=45f10be75edf8db1bc7b74603c13f162/023b5bb5c9ea15ce2f42ea76b6003af33a87b224.jpg', '曾博晖', '数学系', '数学与应用数学', '首席执行官', 1, 0, 1952, '费耶特维尔'),
(17, '美国', '阿肯色', 26, 'http://b.hiphotos.baidu.com/zhidao/wh%3D450%2C600/sign=45f10be75edf8db1bc7b74603c13f162/023b5bb5c9ea15ce2f42ea76b6003af33a87b224.jpg', '曾博晖', '数学系', '数学与应用数学', '首席执行官', 1, 0, 1952, '费耶特维尔'),
(18, '英国', '北爱尔兰', 27, 'http://b.hiphotos.baidu.com/zhidao/wh%3D450%2C600/sign=45f10be75edf8db1bc7b74603c13f162/023b5bb5c9ea15ce2f42ea76b6003af33a87b224.jpg', '曾博晖', '土木工程学院', '土木工程', '高级架构师', 1, 0, 1965, '贝尔法斯特'),
(19, '英国', '北爱尔兰', 28, 'http://b.hiphotos.baidu.com/zhidao/wh%3D450%2C600/sign=45f10be75edf8db1bc7b74603c13f162/023b5bb5c9ea15ce2f42ea76b6003af33a87b224.jpg', '曾博晖', '土木工程学院', '土木工程', '高级架构师', 1, 0, 1965, '贝尔法斯特'),
(20, '中国', '江苏', 29, 'http://b.hiphotos.baidu.com/zhidao/wh%3D450%2C600/sign=45f10be75edf8db1bc7b74603c13f162/023b5bb5c9ea15ce2f42ea76b6003af33a87b224.jpg', '白洋', '建筑学院', '建筑学', 'student', 1, 0, 1952, '南京'),
(21, '中国', '浙江', 30, 'http://b.hiphotos.baidu.com/zhidao/wh%3D450%2C600/sign=45f10be75edf8db1bc7b74603c13f162/023b5bb5c9ea15ce2f42ea76b6003af33a87b224.jpg', '大神', '电子科学与工程学院(研)', '光学工程', '执行总裁', 1, 0, 1970, '杭州'),
(22, '中国', '浙江', 31, 'http://b.hiphotos.baidu.com/zhidao/wh%3D450%2C600/sign=45f10be75edf8db1bc7b74603c13f162/023b5bb5c9ea15ce2f42ea76b6003af33a87b224.jpg', '大神', '电子科学与工程学院(研)', '光学工程', '执行总裁', 1, 0, 1970, '杭州'),
(23, '中国', '浙江', 32, 'http://b.hiphotos.baidu.com/zhidao/wh%3D450%2C600/sign=45f10be75edf8db1bc7b74603c13f162/023b5bb5c9ea15ce2f42ea76b6003af33a87b224.jpg', '大神', '电子科学与工程学院(研)', '光学工程', '执行总裁', 1, 0, 1970, '杭州'),
(24, '美国', '阿肯色', 33, 'http://b.hiphotos.baidu.com/zhidao/wh%3D450%2C600/sign=45f10be75edf8db1bc7b74603c13f162/023b5bb5c9ea15ce2f42ea76b6003af33a87b224.jpg', '男神', '信息科学与工程学院(研)', '信息安全', '首席执行官', 1, 0, 1988, '费耶特维尔'),
(25, '中国', '江苏', 34, 'http://b.hiphotos.baidu.com/zhidao/wh%3D450%2C600/sign=45f10be75edf8db1bc7b74603c13f162/023b5bb5c9ea15ce2f42ea76b6003af33a87b224.jpg', '曾博晖', '建筑学院(研)', '美术学', 'student', 1, 0, 1952, '南京'),
(26, '中国', '江苏', 35, 'http://b.hiphotos.baidu.com/zhidao/wh%3D450%2C600/sign=45f10be75edf8db1bc7b74603c13f162/023b5bb5c9ea15ce2f42ea76b6003af33a87b224.jpg', '崔浩宇', '建筑学院(研)', '美术学', 'student', 1, 0, 1952, '南京'),
(27, '中国', '江苏', 36, 'http://b.hiphotos.baidu.com/zhidao/wh%3D450%2C600/sign=45f10be75edf8db1bc7b74603c13f162/023b5bb5c9ea15ce2f42ea76b6003af33a87b224.jpg', '吴卓凡', '建筑学院(研)', '美术学', 'student', 1, 0, 1952, '南京'),
(28, '中国', '江苏', 37, 'http://b.hiphotos.baidu.com/zhidao/wh%3D450%2C600/sign=45f10be75edf8db1bc7b74603c13f162/023b5bb5c9ea15ce2f42ea76b6003af33a87b224.jpg', '大神爸爸', '建筑学院(研)', '美术学', 'student', 1, 0, 1952, '南京'),
(29, '中国', '江苏', 38, 'http://b.hiphotos.baidu.com/zhidao/wh%3D450%2C600/sign=45f10be75edf8db1bc7b74603c13f162/023b5bb5c9ea15ce2f42ea76b6003af33a87b224.jpg', '刘畅', '建筑学院(研)', '美术学', 'student', 1, 0, 1952, '南京'),
(30, '中国', '江苏', 39, 'http://b.hiphotos.baidu.com/zhidao/wh%3D450%2C600/sign=45f10be75edf8db1bc7b74603c13f162/023b5bb5c9ea15ce2f42ea76b6003af33a87b224.jpg', '陈二逼', '建筑学院(研)', '美术学', 'student', 1, 0, 1952, '南京'),
(31, '中国', '江苏', 40, 'http://b.hiphotos.baidu.com/zhidao/wh%3D450%2C600/sign=45f10be75edf8db1bc7b74603c13f162/023b5bb5c9ea15ce2f42ea76b6003af33a87b224.jpg', '雄辉', '建筑学院(研)', '美术学', 'student', 1, 0, 1952, '南京'),
(32, '中国', '江苏', 41, 'http://b.hiphotos.baidu.com/zhidao/wh%3D450%2C600/sign=45f10be75edf8db1bc7b74603c13f162/023b5bb5c9ea15ce2f42ea76b6003af33a87b224.jpg', '你哪呢', '建筑学院(研)', '美术学', 'student', 1, 0, 1952, '南京'),
(33, '中国', '江苏', 42, 'http://b.hiphotos.baidu.com/zhidao/wh%3D450%2C600/sign=45f10be75edf8db1bc7b74603c13f162/023b5bb5c9ea15ce2f42ea76b6003af33a87b224.jpg', '博晖', '建筑学院(研)', '美术学', 'student', 1, 0, 1952, '南京'),
(34, '中国', '江苏', 43, 'http://b.hiphotos.baidu.com/zhidao/wh%3D450%2C600/sign=45f10be75edf8db1bc7b74603c13f162/023b5bb5c9ea15ce2f42ea76b6003af33a87b224.jpg', '陈晓华', '建筑学院(研)', '美术学', 'student', 1, 0, 1952, '南京'),
(35, '中国', '江苏', 44, 'http://b.hiphotos.baidu.com/zhidao/wh%3D450%2C600/sign=45f10be75edf8db1bc7b74603c13f162/023b5bb5c9ea15ce2f42ea76b6003af33a87b224.jpg', '嘿嘿嘿', '建筑学院(研)', '美术学', 'student', 1, 0, 1952, '南京'),
(36, '中国', '江苏', 45, 'http://b.hiphotos.baidu.com/zhidao/wh%3D450%2C600/sign=45f10be75edf8db1bc7b74603c13f162/023b5bb5c9ea15ce2f42ea76b6003af33a87b224.jpg', '啵啵啵', '数学系(研)', '统计学', 'student', 1, 0, 1956, '南京'),
(37, '中国', '江苏', 46, 'http://b.hiphotos.baidu.com/zhidao/wh%3D450%2C600/sign=45f10be75edf8db1bc7b74603c13f162/023b5bb5c9ea15ce2f42ea76b6003af33a87b224.jpg', '呵呵呵', '经济管理学院(研)', '国民经济学', 'student', 1, 0, 1952, '南京'),
(38, '中国', '江苏', 47, 'http://b.hiphotos.baidu.com/zhidao/wh%3D450%2C600/sign=45f10be75edf8db1bc7b74603c13f162/023b5bb5c9ea15ce2f42ea76b6003af33a87b224.jpg', '吴卓凡', '建筑学院(研)', '美术学', 'student', 1, 0, 1952, '南京'),
(39, '中国', '江苏', 48, 'http://b.hiphotos.baidu.com/zhidao/wh%3D450%2C600/sign=45f10be75edf8db1bc7b74603c13f162/023b5bb5c9ea15ce2f42ea76b6003af33a87b224.jpg', '吴卓凡', '建筑学院(研)', '美术学', 'student', 1, 0, 1952, '南京'),
(40, '中国', '江苏', 49, 'http://b.hiphotos.baidu.com/zhidao/wh%3D450%2C600/sign=45f10be75edf8db1bc7b74603c13f162/023b5bb5c9ea15ce2f42ea76b6003af33a87b224.jpg', '吴卓凡', '建筑学院(研)', '美术学', 'student', 1, 0, 1952, '南京'),
(41, '美国', '阿肯色', 50, 'http://b.hiphotos.baidu.com/zhidao/wh%3D450%2C600/sign=45f10be75edf8db1bc7b74603c13f162/023b5bb5c9ea15ce2f42ea76b6003af33a87b224.jpg', '吴卓凡', '建筑学院(研)', '美术学', '我的天', 1, 0, 1952, '费耶特维尔'),
(42, '美国', '阿肯色', 51, 'http://b.hiphotos.baidu.com/zhidao/wh%3D450%2C600/sign=45f10be75edf8db1bc7b74603c13f162/023b5bb5c9ea15ce2f42ea76b6003af33a87b224.jpg', '吴卓凡', '建筑学院(研)', '美术学', '我的天', 1, 0, 1952, '费耶特维尔'),
(43, '美国', '阿肯色', 52, 'http://b.hiphotos.baidu.com/zhidao/wh%3D450%2C600/sign=45f10be75edf8db1bc7b74603c13f162/023b5bb5c9ea15ce2f42ea76b6003af33a87b224.jpg', '吴卓凡', '建筑学院(研)', '美术学', '我的天', 1, 0, 1952, '费耶特维尔'),
(44, '美国', '阿肯色', 53, 'http://b.hiphotos.baidu.com/zhidao/wh%3D450%2C600/sign=45f10be75edf8db1bc7b74603c13f162/023b5bb5c9ea15ce2f42ea76b6003af33a87b224.jpg', '吴卓凡', '建筑学院(研)', '美术学', '我的天', 1, 0, 1952, '费耶特维尔'),
(45, '美国', '阿肯色', 54, 'http://b.hiphotos.baidu.com/zhidao/wh%3D450%2C600/sign=45f10be75edf8db1bc7b74603c13f162/023b5bb5c9ea15ce2f42ea76b6003af33a87b224.jpg', '吴卓凡', '建筑学院(研)', '美术学', '我的天', 1, 0, 1952, '费耶特维尔'),
(46, '美国', '阿肯色', 55, 'http://b.hiphotos.baidu.com/zhidao/wh%3D450%2C600/sign=45f10be75edf8db1bc7b74603c13f162/023b5bb5c9ea15ce2f42ea76b6003af33a87b224.jpg', '吴卓凡', '建筑学院(研)', '美术学', '我的天', 1, 0, 1952, '费耶特维尔'),
(47, '中国', '江苏', 56, 'http://b.hiphotos.baidu.com/zhidao/wh%3D450%2C600/sign=45f10be75edf8db1bc7b74603c13f162/023b5bb5c9ea15ce2f42ea76b6003af33a87b224.jpg', '吴卓凡', '建筑学院(研)', '美术学', 'student', 1, 0, 1952, '南京'),
(48, '中国', '江苏', 57, 'http://b.hiphotos.baidu.com/zhidao/wh%3D450%2C600/sign=45f10be75edf8db1bc7b74603c13f162/023b5bb5c9ea15ce2f42ea76b6003af33a87b224.jpg', '吴卓凡', '建筑学院(研)', '美术学', 'student', 1, 0, 1952, '南京'),
(49, '中国', '江苏', 58, 'http://b.hiphotos.baidu.com/zhidao/wh%3D450%2C600/sign=45f10be75edf8db1bc7b74603c13f162/023b5bb5c9ea15ce2f42ea76b6003af33a87b224.jpg', '吴卓凡', '建筑学院(研)', '美术学', 'student', 1, 0, 1952, '南京'),
(50, '中国', '江苏', 59, 'http://b.hiphotos.baidu.com/zhidao/wh%3D450%2C600/sign=45f10be75edf8db1bc7b74603c13f162/023b5bb5c9ea15ce2f42ea76b6003af33a87b224.jpg', '成本', '建筑学院(研)', '美术学', 'student', 1, 0, 1952, '南京'),
(51, '中国', '江苏', 60, 'http://b.hiphotos.baidu.com/zhidao/wh%3D450%2C600/sign=45f10be75edf8db1bc7b74603c13f162/023b5bb5c9ea15ce2f42ea76b6003af33a87b224.jpg', '吼吼吼', '建筑学院(研)', '美术学', 'student', 1, 0, 1952, '南京'),
(52, '中国', '江苏', 61, 'http://b.hiphotos.baidu.com/zhidao/wh%3D450%2C600/sign=45f10be75edf8db1bc7b74603c13f162/023b5bb5c9ea15ce2f42ea76b6003af33a87b224.jpg', '李龙飞', '建筑学院(研)', '美术学', 'student', 1, 0, 1952, '南京'),
(53, '中国', '江苏', 62, 'http://b.hiphotos.baidu.com/zhidao/wh%3D450%2C600/sign=45f10be75edf8db1bc7b74603c13f162/023b5bb5c9ea15ce2f42ea76b6003af33a87b224.jpg', '学不会', '建筑学院(研)', '美术学', 'student', 1, 0, 1952, '南京'),
(54, '中国', '江苏', 63, 'http://b.hiphotos.baidu.com/zhidao/wh%3D450%2C600/sign=45f10be75edf8db1bc7b74603c13f162/023b5bb5c9ea15ce2f42ea76b6003af33a87b224.jpg', '慧慧回家', '建筑学院(研)', '美术学', 'student', 1, 0, 1952, '南京'),
(55, '美国', '阿肯色', 64, 'http://b.hiphotos.baidu.com/zhidao/wh%3D450%2C600/sign=45f10be75edf8db1bc7b74603c13f162/023b5bb5c9ea15ce2f42ea76b6003af33a87b224.jpg', '你哪呢', '建筑学院(研)', '美术学', '斧子', 1, 0, 1952, '费耶特维尔'),
(56, '美国', '阿肯色', 65, 'http://b.hiphotos.baidu.com/zhidao/wh%3D450%2C600/sign=45f10be75edf8db1bc7b74603c13f162/023b5bb5c9ea15ce2f42ea76b6003af33a87b224.jpg', '陈三胖', '建筑学院(研)', '美术学', '打杂', 1, 0, 1952, '费耶特维尔'),
(57, '美国', '阿肯色', 66, 'http://b.hiphotos.baidu.com/zhidao/wh%3D450%2C600/sign=45f10be75edf8db1bc7b74603c13f162/023b5bb5c9ea15ce2f42ea76b6003af33a87b224.jpg', '曾博晖', '建筑学院(研)', '美术学', '开车', 1, 0, 1952, '费耶特维尔'),
(58, '中国', '河南', 98, 'http://tupian.qqjay.com/tou3/2016/0605/222393536f052f6d5c1e293b8e065164.jpg', '曾博晖', '建筑设计及其理论', '建筑学院(研)', '设计师', 0, 0, 2014, '洛阳');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
