-- phpMyAdmin SQL Dump
-- version 4.0.10deb1
-- http://www.phpmyadmin.net
--
-- 主机: localhost
-- 生成日期: 2016-09-01 17:22:22
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
  `circle_type_id` varchar(32) NOT NULL,
  PRIMARY KEY (`cid`),
  KEY `umeng_cid` (`umeng_cid`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=16 ;

--
-- 转存表中的数据 `ac_circle_table`
--

INSERT INTO `ac_circle_table` (`cid`, `umeng_cid`, `umeng_virtual_cid`, `circle_type_id`) VALUES
(6, '57c3e00ab9a9963e49b994a2', '57c3e00ab9a99622684afc1f', '1'),
(9, '57c3e00ab9a9963e49b994a2', '57c3e00ab9a99622684afc1f', '1'),
(10, '57c3ea89b9a9964bf8c59e3c', '57c3ea89d36ef34b91cfdea2', '1'),
(11, '57c3ea9ab9a9964bf8c59e40', '57c3ea9ab9a99666179c6c3a', '1'),
(12, '57c69c35d36ef3151eb80a92', '57c69c35b9a9964ef66ecc1f', '1'),
(13, '57c69cb1b9a99673549eb1a0', '57c69cb1d36ef3151eb80b0b', '1'),
(14, '57c69cbbb9a99622684b2d23', '57c69cbab9a9965edeffa3e7', '1'),
(15, '57c69d68d36ef3151eb80bac', '57c69d67d36ef3151eb80ba9', '1');

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
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=112 ;

--
-- 转存表中的数据 `ac_manual_review_table`
--

INSERT INTO `ac_manual_review_table` (`review_id`, `result`, `circle_name`, `circle_type_id`, `circle_type_name`, `circle_icon_url`, `creator_uid`, `reason_message`, `description`) VALUES
(1, 1, 'new circle 905', '1', '学院圈', 'default', '123', 'I love you!', 'the circle will be beautiful!'),
(81, 0, 'new circle 743', '1', '学院圈', 'default', '123', 'I love you!', 'the circle will be beautiful!'),
(82, 0, 'new circle 585', '1', '学院圈', 'default', '123', 'I love you!', 'the circle will be beautiful!'),
(83, 0, 'new circle 961', '1', '学院圈', 'default', '123', 'I love you!', 'the circle will be beautiful!'),
(84, 1, 'new circle 361', '1', '学院圈', 'default', '123', 'I love you!', 'the circle will be beautiful!'),
(85, 1, 'new circle 459', '1', '学院圈', 'default', '123', 'I love you!', 'the circle will be beautiful!'),
(86, 0, 'new circle 442', '1', '学院圈', 'default', '123', 'I love you!', 'the circle will be beautiful!'),
(87, 1, 'new circle 661', '1', '学院圈', 'default', '123', 'I love you!', 'the circle will be beautiful!'),
(88, 1, 'new circle 438', '1', '学院圈', 'default', '123', 'I love you!', 'the circle will be beautiful!'),
(89, 1, 'new circle 700', '1', '学院圈', 'default', '123', 'I love you!', 'the circle will be beautiful!'),
(90, 1, 'new circle 397', '1', '学院圈', 'default', '123', 'I love you!', 'the circle will be beautiful!'),
(91, 1, 'new circle 983', '1', '学院圈', 'default', '123', 'I love you!', 'the circle will be beautiful!'),
(92, 0, 'new circle 590', '1', '学院圈', 'default', '123', 'I love you!', 'the circle will be beautiful!'),
(93, 0, 'new circle 399', '1', '学院圈', 'default', '123', 'I love you!', 'the circle will be beautiful!'),
(94, 0, 'new circle 108', '1', '学院圈', 'default', '123', 'I love you!', 'the circle will be beautiful!'),
(95, 0, 'new circle 582', '1', '学院圈', 'default', '123', 'I love you!', 'the circle will be beautiful!'),
(96, 0, 'new circle 68', '1', '学院圈', 'default', '123', 'I love you!', 'the circle will be beautiful!'),
(97, 0, 'new circle 734', '1', '学院圈', 'default', '123', 'I love you!', 'the circle will be beautiful!'),
(98, 0, 'new circle 342', '1', '学院圈', 'default', '123', 'I love you!', 'the circle will be beautiful!'),
(99, 0, 'new circle 750', '1', '学院圈', 'default', '123', 'I love you!', 'the circle will be beautiful!'),
(100, 0, 'new circle 8', '1', '学院圈', 'default', '123', 'I love you!', 'the circle will be beautiful!'),
(101, 0, 'new circle 800', '1', '学院圈', 'default', '123', 'I love you!', 'the circle will be beautiful!'),
(102, 0, 'new circle 889', '1', '学院圈', 'default', '123', 'I love you!', 'the circle will be beautiful!'),
(103, 0, 'new circle 211', '1', '学院圈', 'default', '123', 'I love you!', 'the circle will be beautiful!'),
(104, 0, 'new circle 633', '1', '学院圈', 'default', '123', 'I love you!', 'the circle will be beautiful!'),
(105, 0, 'new circle 755', '1', '学院圈', 'default', '123', 'I love you!', 'the circle will be beautiful!'),
(106, 0, 'new circle 951', '1', '学院圈', 'default', '123', 'I love you!', 'the circle will be beautiful!'),
(107, 0, 'new circle 494', '1', '学院圈', 'default', '123', 'I love you!', 'the circle will be beautiful!'),
(108, 0, 'new circle 166', '1', '学院圈', 'default', '123', 'I love you!', 'the circle will be beautiful!'),
(109, 0, 'new circle 16', '1', '学院圈', 'default', '123', 'I love you!', 'the circle will be beautiful!'),
(110, 0, 'new circle 178', '1', '学院圈', 'default', '123', 'I love you!', 'the circle will be beautiful!'),
(111, 0, 'new circle 767', '1', '学院圈', 'default', '123', 'I love you!', 'the circle will be beautiful!');

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
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=9 ;

--
-- 转存表中的数据 `ac_message_circle_table`
--

INSERT INTO `ac_message_circle_table` (`mc_id`, `umeng_circle_id`, `cid`, `message_queue`, `update_time`) VALUES
(2, '57c3e00ab9a9963e49b994a2', '9', '_', '2016-08-30 07:46:17'),
(3, '57c3ea89b9a9964bf8c59e3c', '10', '_', '2016-08-30 07:46:17'),
(4, '57c3ea9ab9a9964bf8c59e40', '11', '_', '2016-08-30 07:46:17'),
(5, '57c69c35d36ef3151eb80a92', '12', '_', '2016-08-30 07:46:17'),
(6, '57c69cb1b9a99673549eb1a0', '13', '_', '2016-08-30 07:46:17'),
(7, '57c69cbbb9a99622684b2d23', '14', '_172_174_176_178_182_184_186_188_190_192_194_196_198_200_202_204_206_208_210_212_214_216_218_220_222_224_226_228_230_232_234_236_238_240_242_244_246_248_250_252_254_256_258_260_262_264_266_268_270_272_274_276_278_280_282_284_286_288_290_292_294_', '2016-09-01 08:46:26'),
(8, '57c69d68d36ef3151eb80bac', '15', '_95_98_101_104_107_110_113_116_119_122_125_128_131_134_137_140_143_', '2016-08-30 07:46:17');

-- --------------------------------------------------------

--
-- 表的结构 `ac_message_table`
--

CREATE TABLE IF NOT EXISTS `ac_message_table` (
  `mid` int(11) NOT NULL AUTO_INCREMENT COMMENT '消息id',
  `type` tinyint(4) NOT NULL COMMENT '消息类型的说明字段',
  `message` varchar(1022) NOT NULL COMMENT '消息字段,是一个json数组',
  `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`mid`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=295 ;

--
-- 转存表中的数据 `ac_message_table`
--

INSERT INTO `ac_message_table` (`mid`, `type`, `message`, `update_time`) VALUES
(1, 1, '{test}', '0000-00-00 00:00:00'),
(2, 1, '{test}', '0000-00-00 00:00:00'),
(3, 1, '{test}', '0000-00-00 00:00:00'),
(4, 1, '{test}', '0000-00-00 00:00:00'),
(5, 1, '{test}', '0000-00-00 00:00:00'),
(6, 1, '{test}', '0000-00-00 00:00:00'),
(7, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-08-31 09:21:39'),
(8, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-08-31 09:26:41'),
(9, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-08-31 09:26:49'),
(10, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-08-31 09:26:58'),
(11, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-08-31 09:29:23'),
(12, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-08-31 09:29:24'),
(13, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-08-31 09:29:25'),
(14, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-08-31 09:29:37'),
(15, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-08-31 09:29:37'),
(16, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-08-31 09:29:38'),
(17, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-08-31 09:32:27'),
(18, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-08-31 09:33:09'),
(19, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-08-31 09:33:09'),
(20, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-08-31 09:33:09'),
(21, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-08-31 09:33:09'),
(22, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-08-31 09:33:09'),
(23, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-08-31 09:33:26'),
(24, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-08-31 09:33:26'),
(25, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-08-31 09:33:26'),
(26, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-08-31 09:33:26'),
(27, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-08-31 09:33:26'),
(28, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-08-31 09:39:28'),
(29, 1, '{''circle_name'': ''group message.'', ''circle_id'': ''999''}', '2016-08-31 09:39:28'),
(30, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-08-31 09:42:55'),
(31, 1, '{''circle_name'': ''group message.'', ''circle_id'': ''999''}', '2016-08-31 09:42:55'),
(32, 1, '{''circle_name'': ''circle message.'', ''circle_id'': ''999''}', '2016-08-31 09:42:55'),
(33, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-08-31 09:45:40'),
(34, 1, '{''circle_name'': ''group message.'', ''circle_id'': ''999''}', '2016-08-31 09:45:40'),
(35, 1, '{''circle_name'': ''circle message.'', ''circle_id'': ''999''}', '2016-08-31 09:45:40'),
(36, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-08-31 09:46:49'),
(37, 1, '{''circle_name'': ''group message.'', ''circle_id'': ''999''}', '2016-08-31 09:46:49'),
(38, 1, '{''circle_name'': ''circle message.'', ''circle_id'': ''999''}', '2016-08-31 09:46:49'),
(39, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-08-31 09:47:11'),
(40, 1, '{''circle_name'': ''group message.'', ''circle_id'': ''999''}', '2016-08-31 09:47:11'),
(41, 1, '{''circle_name'': ''circle message.'', ''circle_id'': ''999''}', '2016-08-31 09:47:11'),
(42, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-08-31 09:47:29'),
(43, 1, '{''circle_name'': ''group message.'', ''circle_id'': ''999''}', '2016-08-31 09:47:29'),
(44, 1, '{''circle_name'': ''circle message.'', ''circle_id'': ''999''}', '2016-08-31 09:47:29'),
(45, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-08-31 09:47:46'),
(46, 1, '{''circle_name'': ''group message.'', ''circle_id'': ''999''}', '2016-08-31 09:47:46'),
(47, 1, '{''circle_name'': ''circle message.'', ''circle_id'': ''999''}', '2016-08-31 09:47:46'),
(48, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-08-31 09:48:00'),
(49, 1, '{''circle_name'': ''group message.'', ''circle_id'': ''999''}', '2016-08-31 09:48:00'),
(50, 1, '{''circle_name'': ''circle message.'', ''circle_id'': ''999''}', '2016-08-31 09:48:00'),
(51, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-08-31 09:48:54'),
(52, 1, '{''circle_name'': ''group message.'', ''circle_id'': ''999''}', '2016-08-31 09:48:54'),
(53, 1, '{''circle_name'': ''circle message.'', ''circle_id'': ''999''}', '2016-08-31 09:48:54'),
(54, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-08-31 09:49:17'),
(55, 1, '{''circle_name'': ''group message.'', ''circle_id'': ''999''}', '2016-08-31 09:49:17'),
(56, 1, '{''circle_name'': ''circle message.'', ''circle_id'': ''999''}', '2016-08-31 09:49:17'),
(57, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-08-31 09:49:31'),
(58, 1, '{''circle_name'': ''group message.'', ''circle_id'': ''999''}', '2016-08-31 09:49:31'),
(59, 1, '{''circle_name'': ''circle message.'', ''circle_id'': ''999''}', '2016-08-31 09:49:31'),
(60, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-08-31 09:49:37'),
(61, 1, '{''circle_name'': ''group message.'', ''circle_id'': ''999''}', '2016-08-31 09:49:37'),
(62, 1, '{''circle_name'': ''circle message.'', ''circle_id'': ''999''}', '2016-08-31 09:49:37'),
(63, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-08-31 09:50:09'),
(64, 1, '{''circle_name'': ''group message.'', ''circle_id'': ''999''}', '2016-08-31 09:50:09'),
(65, 1, '{''circle_name'': ''circle message.'', ''circle_id'': ''999''}', '2016-08-31 09:50:09'),
(66, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-08-31 09:50:29'),
(67, 1, '{''circle_name'': ''group message.'', ''circle_id'': ''999''}', '2016-08-31 09:50:29'),
(68, 1, '{''circle_name'': ''circle message.'', ''circle_id'': ''999''}', '2016-08-31 09:50:29'),
(69, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-08-31 09:50:38'),
(70, 1, '{''circle_name'': ''group message.'', ''circle_id'': ''999''}', '2016-08-31 09:50:38'),
(71, 1, '{''circle_name'': ''circle message.'', ''circle_id'': ''999''}', '2016-08-31 09:50:38'),
(72, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-08-31 09:50:39'),
(73, 1, '{''circle_name'': ''group message.'', ''circle_id'': ''999''}', '2016-08-31 09:50:39'),
(74, 1, '{''circle_name'': ''circle message.'', ''circle_id'': ''999''}', '2016-08-31 09:50:39'),
(75, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-08-31 09:50:46'),
(76, 1, '{''circle_name'': ''group message.'', ''circle_id'': ''999''}', '2016-08-31 09:50:46'),
(77, 1, '{''circle_name'': ''circle message.'', ''circle_id'': ''999''}', '2016-08-31 09:50:46'),
(78, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-08-31 09:51:00'),
(79, 1, '{''circle_name'': ''group message.'', ''circle_id'': ''999''}', '2016-08-31 09:51:00'),
(80, 1, '{''circle_name'': ''circle message.'', ''circle_id'': ''999''}', '2016-08-31 09:51:00'),
(81, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-08-31 09:51:17'),
(82, 1, '{''circle_name'': ''group message.'', ''circle_id'': ''999''}', '2016-08-31 09:51:17'),
(83, 1, '{''circle_name'': ''circle message.'', ''circle_id'': ''999''}', '2016-08-31 09:51:17'),
(84, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-08-31 09:52:04'),
(85, 1, '{''circle_name'': ''group message.'', ''circle_id'': ''999''}', '2016-08-31 09:52:04'),
(86, 1, '{''circle_name'': ''circle message.'', ''circle_id'': ''999''}', '2016-08-31 09:52:04'),
(87, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-08-31 09:52:32'),
(88, 1, '{''circle_name'': ''group message.'', ''circle_id'': ''999''}', '2016-08-31 09:52:32'),
(89, 1, '{''circle_name'': ''circle message.'', ''circle_id'': ''999''}', '2016-08-31 09:52:32'),
(90, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-08-31 09:53:18'),
(91, 1, '{''circle_name'': ''group message.'', ''circle_id'': ''999''}', '2016-08-31 09:53:18'),
(92, 1, '{''circle_name'': ''circle message.'', ''circle_id'': ''999''}', '2016-08-31 09:53:18'),
(93, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-08-31 09:53:30'),
(94, 1, '{''circle_name'': ''group message.'', ''circle_id'': ''999''}', '2016-08-31 09:53:30'),
(95, 1, '{''circle_name'': ''circle message.'', ''circle_id'': ''999''}', '2016-08-31 09:53:30'),
(96, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-08-31 09:57:00'),
(97, 1, '{''circle_name'': ''group message.'', ''circle_id'': ''999''}', '2016-08-31 09:57:00'),
(98, 1, '{''circle_name'': ''circle message.'', ''circle_id'': ''999''}', '2016-08-31 09:57:00'),
(99, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-08-31 09:57:06'),
(100, 1, '{''circle_name'': ''group message.'', ''circle_id'': ''999''}', '2016-08-31 09:57:06'),
(101, 1, '{''circle_name'': ''circle message.'', ''circle_id'': ''999''}', '2016-08-31 09:57:06'),
(102, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-08-31 09:57:22'),
(103, 1, '{''circle_name'': ''group message.'', ''circle_id'': ''999''}', '2016-08-31 09:57:22'),
(104, 1, '{''circle_name'': ''circle message.'', ''circle_id'': ''999''}', '2016-08-31 09:57:22'),
(105, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-08-31 09:57:28'),
(106, 1, '{''circle_name'': ''group message.'', ''circle_id'': ''999''}', '2016-08-31 09:57:28'),
(107, 1, '{''circle_name'': ''circle message.'', ''circle_id'': ''999''}', '2016-08-31 09:57:28'),
(108, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-08-31 09:57:59'),
(109, 1, '{''circle_name'': ''group message.'', ''circle_id'': ''999''}', '2016-08-31 09:57:59'),
(110, 1, '{''circle_name'': ''circle message.'', ''circle_id'': ''999''}', '2016-08-31 09:57:59'),
(111, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-08-31 10:00:19'),
(112, 1, '{''circle_name'': ''group message.'', ''circle_id'': ''999''}', '2016-08-31 10:00:19'),
(113, 1, '{''circle_name'': ''circle message.'', ''circle_id'': ''999''}', '2016-08-31 10:00:19'),
(114, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-08-31 10:01:06'),
(115, 1, '{''circle_name'': ''group message.'', ''circle_id'': ''999''}', '2016-08-31 10:01:06'),
(116, 1, '{''circle_name'': ''circle message.'', ''circle_id'': ''999''}', '2016-08-31 10:01:06'),
(117, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-08-31 10:02:48'),
(118, 1, '{''circle_name'': ''group message.'', ''circle_id'': ''999''}', '2016-08-31 10:02:48'),
(119, 1, '{''circle_name'': ''circle message.'', ''circle_id'': ''999''}', '2016-08-31 10:02:48'),
(120, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-08-31 10:02:50'),
(121, 1, '{''circle_name'': ''group message.'', ''circle_id'': ''999''}', '2016-08-31 10:02:50'),
(122, 1, '{''circle_name'': ''circle message.'', ''circle_id'': ''999''}', '2016-08-31 10:02:50'),
(123, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-08-31 10:05:30'),
(124, 1, '{''circle_name'': ''group message.'', ''circle_id'': ''999''}', '2016-08-31 10:05:30'),
(125, 1, '{''circle_name'': ''circle message.'', ''circle_id'': ''999''}', '2016-08-31 10:05:30'),
(126, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-08-31 10:07:02'),
(127, 1, '{''circle_name'': ''group message.'', ''circle_id'': ''999''}', '2016-08-31 10:07:02'),
(128, 1, '{''circle_name'': ''circle message.'', ''circle_id'': ''999''}', '2016-08-31 10:07:02'),
(129, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-08-31 10:07:43'),
(130, 1, '{''circle_name'': ''group message.'', ''circle_id'': ''999''}', '2016-08-31 10:07:43'),
(131, 1, '{''circle_name'': ''circle message.'', ''circle_id'': ''999''}', '2016-08-31 10:07:43'),
(132, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-08-31 10:08:05'),
(133, 1, '{''circle_name'': ''group message.'', ''circle_id'': ''999''}', '2016-08-31 10:08:05'),
(134, 1, '{''circle_name'': ''circle message.'', ''circle_id'': ''999''}', '2016-08-31 10:08:05'),
(135, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-08-31 10:09:14'),
(136, 1, '{''circle_name'': ''group message.'', ''circle_id'': ''999''}', '2016-08-31 10:09:14'),
(137, 1, '{''circle_name'': ''circle message.'', ''circle_id'': ''999''}', '2016-08-31 10:09:14'),
(138, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-08-31 10:11:26'),
(139, 1, '{''circle_name'': ''group message.'', ''circle_id'': ''999''}', '2016-08-31 10:11:26'),
(140, 1, '{''circle_name'': ''circle message.'', ''circle_id'': ''999''}', '2016-08-31 10:11:26'),
(141, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-08-31 10:11:48'),
(142, 1, '{''circle_name'': ''group message.'', ''circle_id'': ''999''}', '2016-08-31 10:11:48'),
(143, 1, '{''circle_name'': ''circle message.'', ''circle_id'': ''999''}', '2016-08-31 10:11:48'),
(144, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-08-31 10:15:11'),
(145, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-08-31 10:15:40'),
(146, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-08-31 10:19:23'),
(147, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-08-31 10:19:35'),
(148, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-08-31 10:20:42'),
(149, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-08-31 10:20:58'),
(150, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-08-31 10:21:11'),
(151, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-08-31 10:21:30'),
(152, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-08-31 10:21:54'),
(153, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-08-31 10:23:19'),
(154, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-08-31 12:14:03'),
(155, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-08-31 12:16:19'),
(156, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-08-31 12:37:46'),
(157, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-08-31 12:38:43'),
(158, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-08-31 12:38:53'),
(159, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-08-31 12:39:19'),
(160, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-08-31 12:39:25'),
(161, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-08-31 12:39:29'),
(162, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-08-31 12:39:33'),
(163, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-08-31 12:40:43'),
(164, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-08-31 12:42:07'),
(165, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-08-31 12:42:44'),
(166, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-08-31 13:06:58'),
(167, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-08-31 13:07:32'),
(168, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-08-31 13:08:14'),
(169, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-08-31 13:09:48'),
(170, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-08-31 14:00:28'),
(171, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-08-31 14:02:53'),
(172, 1, '{''circle_name'': ''circle message.'', ''circle_id'': ''999''}', '2016-08-31 14:02:53'),
(173, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-08-31 14:03:05'),
(174, 1, '{''circle_name'': ''circle message.'', ''circle_id'': ''999''}', '2016-08-31 14:03:06'),
(175, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-08-31 14:04:51'),
(176, 1, '{''circle_name'': ''circle message.'', ''circle_id'': ''999''}', '2016-08-31 14:04:51'),
(177, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-08-31 14:05:25'),
(178, 1, '{''circle_name'': ''circle message.'', ''circle_id'': ''999''}', '2016-08-31 14:05:25'),
(179, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-08-31 14:05:35'),
(180, 1, '{''circle_name'': ''circle message.'', ''circle_id'': ''999''}', '2016-08-31 14:05:35'),
(181, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-08-31 14:05:47'),
(182, 1, '{''circle_name'': ''circle message.'', ''circle_id'': ''999''}', '2016-08-31 14:05:47'),
(183, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-08-31 14:08:19'),
(184, 1, '{''circle_name'': ''circle message.'', ''circle_id'': ''999''}', '2016-08-31 14:08:19'),
(185, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-08-31 14:08:24'),
(186, 1, '{''circle_name'': ''circle message.'', ''circle_id'': ''999''}', '2016-08-31 14:08:24'),
(187, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-08-31 14:08:26'),
(188, 1, '{''circle_name'': ''circle message.'', ''circle_id'': ''999''}', '2016-08-31 14:08:26'),
(189, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-08-31 14:08:49'),
(190, 1, '{''circle_name'': ''circle message.'', ''circle_id'': ''999''}', '2016-08-31 14:08:49'),
(191, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-08-31 14:11:49'),
(192, 1, '{''circle_name'': ''circle message.'', ''circle_id'': ''999''}', '2016-08-31 14:11:49'),
(193, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-08-31 14:13:53'),
(194, 1, '{''circle_name'': ''circle message.'', ''circle_id'': ''999''}', '2016-08-31 14:13:53'),
(195, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-08-31 14:15:35'),
(196, 1, '{''circle_name'': ''circle message.'', ''circle_id'': ''999''}', '2016-08-31 14:15:35'),
(197, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-08-31 14:15:51'),
(198, 1, '{''circle_name'': ''circle message.'', ''circle_id'': ''999''}', '2016-08-31 14:15:51'),
(199, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-09-01 06:30:21'),
(200, 1, '{''circle_name'': ''circle message.'', ''circle_id'': ''999''}', '2016-09-01 06:30:21'),
(201, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-09-01 06:30:41'),
(202, 1, '{''circle_name'': ''circle message.'', ''circle_id'': ''999''}', '2016-09-01 06:30:41'),
(203, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-09-01 06:30:50'),
(204, 1, '{''circle_name'': ''circle message.'', ''circle_id'': ''999''}', '2016-09-01 06:30:50'),
(205, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-09-01 06:31:22'),
(206, 1, '{''circle_name'': ''circle message.'', ''circle_id'': ''999''}', '2016-09-01 06:31:22'),
(207, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-09-01 06:31:44'),
(208, 1, '{''circle_name'': ''circle message.'', ''circle_id'': ''999''}', '2016-09-01 06:31:44'),
(209, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-09-01 06:32:31'),
(210, 1, '{''circle_name'': ''circle message.'', ''circle_id'': ''999''}', '2016-09-01 06:32:31'),
(211, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-09-01 06:32:43'),
(212, 1, '{''circle_name'': ''circle message.'', ''circle_id'': ''999''}', '2016-09-01 06:32:43'),
(213, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-09-01 06:45:18'),
(214, 1, '{''circle_name'': ''circle message.'', ''circle_id'': ''999''}', '2016-09-01 06:45:18'),
(215, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-09-01 06:45:26'),
(216, 1, '{''circle_name'': ''circle message.'', ''circle_id'': ''999''}', '2016-09-01 06:45:26'),
(217, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-09-01 06:46:18'),
(218, 1, '{''circle_name'': ''circle message.'', ''circle_id'': ''999''}', '2016-09-01 06:46:18'),
(219, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-09-01 06:46:54'),
(220, 1, '{''circle_name'': ''circle message.'', ''circle_id'': ''999''}', '2016-09-01 06:46:54'),
(221, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-09-01 06:47:56'),
(222, 1, '{''circle_name'': ''circle message.'', ''circle_id'': ''999''}', '2016-09-01 06:47:56'),
(223, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-09-01 06:48:21'),
(224, 1, '{''circle_name'': ''circle message.'', ''circle_id'': ''999''}', '2016-09-01 06:48:21'),
(225, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-09-01 06:48:52'),
(226, 1, '{''circle_name'': ''circle message.'', ''circle_id'': ''999''}', '2016-09-01 06:48:52'),
(227, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-09-01 06:50:33'),
(228, 1, '{''circle_name'': ''circle message.'', ''circle_id'': ''999''}', '2016-09-01 06:50:33'),
(229, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-09-01 06:50:40'),
(230, 1, '{''circle_name'': ''circle message.'', ''circle_id'': ''999''}', '2016-09-01 06:50:40'),
(231, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-09-01 06:50:46'),
(232, 1, '{''circle_name'': ''circle message.'', ''circle_id'': ''999''}', '2016-09-01 06:50:46'),
(233, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-09-01 06:50:52'),
(234, 1, '{''circle_name'': ''circle message.'', ''circle_id'': ''999''}', '2016-09-01 06:50:52'),
(235, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-09-01 06:52:23'),
(236, 1, '{''circle_name'': ''circle message.'', ''circle_id'': ''999''}', '2016-09-01 06:52:23'),
(237, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-09-01 06:52:36'),
(238, 1, '{''circle_name'': ''circle message.'', ''circle_id'': ''999''}', '2016-09-01 06:52:36'),
(239, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-09-01 06:57:17'),
(240, 1, '{''circle_name'': ''circle message.'', ''circle_id'': ''999''}', '2016-09-01 06:57:17'),
(241, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-09-01 06:57:54'),
(242, 1, '{''circle_name'': ''circle message.'', ''circle_id'': ''999''}', '2016-09-01 06:57:54'),
(243, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-09-01 06:58:24'),
(244, 1, '{''circle_name'': ''circle message.'', ''circle_id'': ''999''}', '2016-09-01 06:58:24'),
(245, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-09-01 06:58:44'),
(246, 1, '{''circle_name'': ''circle message.'', ''circle_id'': ''999''}', '2016-09-01 06:58:44'),
(247, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-09-01 06:59:09'),
(248, 1, '{''circle_name'': ''circle message.'', ''circle_id'': ''999''}', '2016-09-01 06:59:09'),
(249, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-09-01 07:00:03'),
(250, 1, '{''circle_name'': ''circle message.'', ''circle_id'': ''999''}', '2016-09-01 07:00:03'),
(251, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-09-01 07:05:46'),
(252, 1, '{''circle_name'': ''circle message.'', ''circle_id'': ''999''}', '2016-09-01 07:05:46'),
(253, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-09-01 07:06:30'),
(254, 1, '{''circle_name'': ''circle message.'', ''circle_id'': ''999''}', '2016-09-01 07:06:30'),
(255, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-09-01 07:15:32'),
(256, 1, '{''circle_name'': ''circle message.'', ''circle_id'': ''999''}', '2016-09-01 07:15:32'),
(257, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-09-01 07:16:05'),
(258, 1, '{''circle_name'': ''circle message.'', ''circle_id'': ''999''}', '2016-09-01 07:16:05'),
(259, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-09-01 07:16:54'),
(260, 1, '{''circle_name'': ''circle message.'', ''circle_id'': ''999''}', '2016-09-01 07:16:54'),
(261, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-09-01 07:22:03'),
(262, 1, '{''circle_name'': ''circle message.'', ''circle_id'': ''999''}', '2016-09-01 07:22:03'),
(263, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-09-01 07:22:35'),
(264, 1, '{''circle_name'': ''circle message.'', ''circle_id'': ''999''}', '2016-09-01 07:22:35'),
(265, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-09-01 07:23:39'),
(266, 1, '{''circle_name'': ''circle message.'', ''circle_id'': ''999''}', '2016-09-01 07:23:39'),
(267, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-09-01 07:27:55'),
(268, 1, '{''circle_name'': ''circle message.'', ''circle_id'': ''999''}', '2016-09-01 07:27:55'),
(269, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-09-01 07:28:41'),
(270, 1, '{''circle_name'': ''circle message.'', ''circle_id'': ''999''}', '2016-09-01 07:28:41'),
(271, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-09-01 07:30:15'),
(272, 1, '{''circle_name'': ''circle message.'', ''circle_id'': ''999''}', '2016-09-01 07:30:15'),
(273, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-09-01 07:30:50'),
(274, 1, '{''circle_name'': ''circle message.'', ''circle_id'': ''999''}', '2016-09-01 07:30:50'),
(275, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-09-01 07:35:19'),
(276, 1, '{''circle_name'': ''circle message.'', ''circle_id'': ''999''}', '2016-09-01 07:35:19'),
(277, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-09-01 07:35:47'),
(278, 1, '{''circle_name'': ''circle message.'', ''circle_id'': ''999''}', '2016-09-01 07:35:47'),
(279, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-09-01 08:24:26'),
(280, 1, '{''circle_name'': ''circle message.'', ''circle_id'': ''999''}', '2016-09-01 08:24:26'),
(281, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-09-01 08:26:49'),
(282, 1, '{''circle_name'': ''circle message.'', ''circle_id'': ''999''}', '2016-09-01 08:26:49'),
(283, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-09-01 08:28:42'),
(284, 1, '{''circle_name'': ''circle message.'', ''circle_id'': ''999''}', '2016-09-01 08:28:42'),
(285, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-09-01 08:28:59'),
(286, 1, '{''circle_name'': ''circle message.'', ''circle_id'': ''999''}', '2016-09-01 08:28:59'),
(287, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-09-01 08:29:13'),
(288, 1, '{''circle_name'': ''circle message.'', ''circle_id'': ''999''}', '2016-09-01 08:29:13'),
(289, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-09-01 08:29:26'),
(290, 1, '{''circle_name'': ''circle message.'', ''circle_id'': ''999''}', '2016-09-01 08:29:26'),
(291, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-09-01 08:29:42'),
(292, 1, '{''circle_name'': ''circle message.'', ''circle_id'': ''999''}', '2016-09-01 08:29:43'),
(293, 1, '{''circle_name'': ''i apply a circle'', ''circle_id'': ''999''}', '2016-09-01 08:46:26'),
(294, 1, '{''circle_name'': ''circle message.'', ''circle_id'': ''999''}', '2016-09-01 08:46:26');

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
(1, 245, '_test_test', '2016-08-29 12:57:41'),
(2, 246, '_', '2016-08-28 16:59:00'),
(3, 247, '_', '2016-08-28 16:59:21'),
(4, 248, '_', '2016-08-28 16:59:21'),
(5, 1, '_5_', '2016-08-31 10:24:01'),
(6, 2, '_', '2016-08-28 17:11:38'),
(7, 3, '_141_144_', '2016-08-31 10:15:11'),
(8, 4, '_', '2016-08-28 17:19:54'),
(9, 5, '_14_15_16_17_18_19_23_24_28_29_30_31_33_34_36_37_39_40_42_43_45_46_48_49_51_52_54_55_57_58_60_61_63_64_66_67_69_70_72_73_75_76_78_79_81_82_84_85_87_88_90_91_93_94_96_97_99_100_102_103_105_106_108_109_111_112_114_115_117_118_120_121_123_124_126_127_129_130_132_133_135_136_138_139_142_', '2016-08-31 10:11:48'),
(10, 6, '_20_25_29_31_34_37_40_43_46_49_52_55_58_61_64_67_70_73_76_79_82_85_88_91_94_97_100_103_106_109_112_115_118_121_124_127_130_133_136_139_142_', '2016-08-31 10:11:48'),
(11, 7, '_21_26_29_31_34_37_40_43_46_49_52_55_58_61_64_67_70_73_76_79_82_85_88_91_94_97_100_103_106_109_112_115_118_121_124_127_130_133_136_139_142_', '2016-08-31 10:11:48'),
(12, 8, '_22_27_29_31_34_37_40_43_46_49_52_55_58_61_64_67_70_73_76_79_82_85_88_91_94_97_100_103_106_109_112_115_118_121_124_127_130_133_136_139_142_', '2016-08-31 10:11:48'),
(13, 9, '_', '2016-08-29 01:44:45'),
(14, 10, '_', '2016-08-29 01:48:25'),
(15, 11, '_', '2016-08-29 01:55:16'),
(16, 12, '_', '2016-08-29 02:06:39'),
(17, 13, '_', '2016-08-29 02:07:06'),
(18, 14, '_199_201_203_205_207_209_211_213_215_217_219_221_223_225_227_229_231_233_235_237_239_241_243_245_247_249_251_253_255_257_259_261_263_265_267_269_271_273_275_277_279_281_283_285_287_289_291_293_', '2016-09-01 08:46:26'),
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
(31, 27, '_', '2016-08-29 03:04:20'),
(32, 28, '_', '2016-08-29 03:36:52'),
(33, 29, '_', '2016-08-29 07:00:17'),
(34, 30, '_', '2016-08-29 07:02:02'),
(35, 31, '_', '2016-08-29 07:11:04'),
(36, 32, '_', '2016-08-29 07:13:30'),
(37, 33, '_', '2016-08-29 07:13:45'),
(38, 34, '_', '2016-08-29 07:43:02'),
(39, 35, '_', '2016-08-29 07:44:01'),
(40, 36, '_', '2016-08-29 07:44:30'),
(41, 37, '_', '2016-08-29 07:45:01'),
(42, 38, '_', '2016-08-29 07:45:17'),
(43, 39, '_', '2016-08-29 07:46:05'),
(44, 40, '_', '2016-08-29 07:46:15'),
(45, 41, '_', '2016-08-29 07:55:51'),
(46, 42, '_', '2016-08-29 07:55:56'),
(47, 43, '_', '2016-08-29 07:56:08'),
(48, 44, '_', '2016-08-29 09:09:16'),
(49, 45, '_', '2016-08-29 09:11:04'),
(50, 46, '_', '2016-08-29 09:14:07'),
(51, 47, '_', '2016-08-29 09:14:43'),
(52, 48, '_', '2016-08-29 14:14:34'),
(53, 49, '_', '2016-08-29 14:32:10'),
(54, 50, '_', '2016-08-29 14:34:32'),
(55, 51, '_', '2016-08-29 14:35:47'),
(56, 52, '_', '2016-08-29 14:37:08'),
(57, 53, '_', '2016-08-29 16:18:38'),
(58, 54, '_', '2016-08-29 16:23:07');

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
  PRIMARY KEY (`uid`),
  KEY `telephone` (`telephone`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=55 ;

--
-- 转存表中的数据 `ac_user_base_info`
--

INSERT INTO `ac_user_base_info` (`uid`, `adlevel`, `telephone`, `password`, `stu_id`, `access_token`, `update_time`) VALUES
(1, 1, '15896193612', 'cxh1234567', '59670868', '3eb436281264285cfa0d429a44b14617714371c8d2d7bcc5e1accc72735fd98d7d7fc757bd74f021bc460eac18156192843816bbfcca11cf55a34dbc517fc482', '2016-08-28 17:11:37'),
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
(27, 0, '15896184440', 'cxh1234567', '33801435', '3eb436281264285cfa0d429a44b14617714371c8d2d7bcc5e1accc72735fd98d4d455792a4062787c5ae8fbee68e2bd6bcb606062423051c307631d37a04e80b', '2016-08-29 03:04:20'),
(28, 0, '15896196493', 'cxh1234567', '15717460', '3eb436281264285cfa0d429a44b14617714371c8d2d7bcc5e1accc72735fd98db38dc0e965b55a1adce743eef1377cf321bf97f94fc570fc731965ba630708f5', '2016-08-29 03:36:52'),
(29, 0, '15896179846', 'cxh1234567', '31648942', '3eb436281264285cfa0d429a44b14617714371c8d2d7bcc5e1accc72735fd98d22521b7a8f158e3624b90a8c87816b7726b6d9aebaf5279dee96e0a7e97cf52b', '2016-08-29 07:00:17'),
(30, 0, '15896148631', 'cxh1234567', '30371329', '3eb436281264285cfa0d429a44b14617714371c8d2d7bcc5e1accc72735fd98d46bc502b9ef5894c4895ebda84ac81ac64d7fd3bdb911bf77305c617b38c99c3', '2016-08-29 07:02:01'),
(31, 0, '15896136219', 'cxh1234567', '39551973', '3eb436281264285cfa0d429a44b14617714371c8d2d7bcc5e1accc72735fd98de09b6e00d1cfc7983fd7006649b3c4c3f739e98cd718d574398d51111421b232', '2016-08-29 07:11:04'),
(32, 0, '15896146087', 'cxh1234567', '58786689', '3eb436281264285cfa0d429a44b14617714371c8d2d7bcc5e1accc72735fd98d883afd86076446a681363c6ab09e55dde21f90add30d0058541c3810600170dc', '2016-08-29 07:13:30'),
(33, 0, '15896124998', 'cxh1234567', '93507870', '3eb436281264285cfa0d429a44b14617714371c8d2d7bcc5e1accc72735fd98d3dcd5a32bca6371851221780342087fbe06fb6b6bb8211a8f634b46d19a4e874', '2016-08-29 07:13:44'),
(34, 0, '15896179234', 'cxh1234567', '30985993', '3eb436281264285cfa0d429a44b14617714371c8d2d7bcc5e1accc72735fd98d223aee4521b2bfff4bb51ba878b5137c80751138bcc3dfe8f17ec40d6394ec57', '2016-08-29 07:43:02'),
(35, 0, '15896144913', 'cxh1234567', '11903054', '3eb436281264285cfa0d429a44b14617714371c8d2d7bcc5e1accc72735fd98df303d8dc601108e0b06e61f7391dcaf441954bc27b34753b60bf0ccf40c328e3', '2016-08-29 07:44:00'),
(36, 0, '15896112513', 'cxh1234567', '47656145', '3eb436281264285cfa0d429a44b14617714371c8d2d7bcc5e1accc72735fd98d455ee3953ca488a413b0c0c94d085ef27fd2717b6555efe494d49088056a87b9', '2016-08-29 07:44:30'),
(37, 0, '15896137479', 'cxh1234567', '11417205', '3eb436281264285cfa0d429a44b14617714371c8d2d7bcc5e1accc72735fd98ddb4aef08f61ae5d6d059ca92a3065a0e148cd65099c80383d9991428a0fcce2d', '2016-08-29 07:45:01'),
(38, 0, '15896181421', 'cxh1234567', '49552044', '3eb436281264285cfa0d429a44b14617714371c8d2d7bcc5e1accc72735fd98d6d8eb077bf09fbe63a1903155a9e90c5a09eb26a9d84fb00c03b285598515e98', '2016-08-29 07:45:16'),
(39, 0, '15896180195', 'cxh1234567', '53250832', '3eb436281264285cfa0d429a44b14617714371c8d2d7bcc5e1accc72735fd98df3a42713e45df142812fb700e0bebef6e4cd7819b3f4d8faeed3980ec4b9fd93', '2016-08-29 07:46:04'),
(40, 0, '15896112109', 'cxh1234567', '67122741', '3eb436281264285cfa0d429a44b14617714371c8d2d7bcc5e1accc72735fd98d76d8ed477739b5beef2aebf215488d8d44f2f619920bced355b98b25fb2b3585', '2016-08-29 07:46:15'),
(41, 0, '15896169340', 'cxh1234567', '32282535', '3eb436281264285cfa0d429a44b14617714371c8d2d7bcc5e1accc72735fd98def31c80562f99debd2051b726be0434a059f01c5f6395b13c86777fa463bd25b', '2016-08-29 07:55:51'),
(42, 0, '15896171979', 'cxh1234567', '51743362', '3eb436281264285cfa0d429a44b14617714371c8d2d7bcc5e1accc72735fd98dd1d60e8f00c4a754aef92b0c8caca02708b388dafd77b5321b03324a6bc1a5b6', '2016-08-29 07:55:56'),
(43, 0, '15896190258', 'cxh1234567', '57969870', '3eb436281264285cfa0d429a44b14617714371c8d2d7bcc5e1accc72735fd98dafb329465f02c10af4ae39c69771d86165d264332c53d1371053a1059303f1fe', '2016-08-29 07:56:07'),
(44, 0, '15896164674', 'cxh1234567', '32602312', '3eb436281264285cfa0d429a44b14617714371c8d2d7bcc5e1accc72735fd98d79130b822d5898314107cc9042f49fe9784a3302f70a45d77da74feb4286f911', '2016-08-29 09:09:16'),
(45, 0, '15896134123', 'cxh1234567', '75750966', '3eb436281264285cfa0d429a44b14617714371c8d2d7bcc5e1accc72735fd98d28ecccc27c962a326acee10970a07ff231964e2a597c8ae96da802a7af9b2239', '2016-08-29 09:11:04'),
(46, 0, '15896196081', 'cxh1234567', '77297526', '3eb436281264285cfa0d429a44b14617714371c8d2d7bcc5e1accc72735fd98de7dab42054170f3546e1a0b401053866a89df84000581f389a77f8a8893ce787', '2016-08-29 09:14:07'),
(47, 0, '15896130851', 'cxh1234567', '72589709', '3eb436281264285cfa0d429a44b14617714371c8d2d7bcc5e1accc72735fd98dbba779b9ce4a53a11ee65d01f87d9ea3bfcfe7a2f26cae91ed1e1baed858f1f2', '2016-08-29 09:14:43'),
(48, 0, '15896163558', 'cxh1234567', '77912794', '3eb436281264285cfa0d429a44b14617714371c8d2d7bcc5e1accc72735fd98d2f7edc0f69a9fa6a9eb5fec5343c00e4e1c5121dae8c42868da7d368b4833eb9', '2016-08-29 14:14:34'),
(49, 0, '15896185976', 'cxh1234567', '39328633', '3eb436281264285cfa0d429a44b14617714371c8d2d7bcc5e1accc72735fd98ddcb44dc9a96112617a94b3d59adc877c893842f776d2b0315f3d5bf502ce7d82', '2016-08-29 14:32:10'),
(50, 0, '15896120044', 'cxh1234567', '76636786', '3eb436281264285cfa0d429a44b14617714371c8d2d7bcc5e1accc72735fd98dc4f53dc2570b6f84ec5659a9d2e6eee0f910a18de4654e8ecd1337f7003c439b', '2016-08-29 14:34:32'),
(51, 0, '15896186343', 'cxh1234567', '31580014', '3eb436281264285cfa0d429a44b14617714371c8d2d7bcc5e1accc72735fd98ddfb01c1f2b70ed54189d23f3664d294e8cd8c8a9f8c09f086976f7c56076fdd1', '2016-08-29 14:35:47'),
(52, 0, '15896164896', 'cxh1234567', '67261464', '3eb436281264285cfa0d429a44b14617714371c8d2d7bcc5e1accc72735fd98d3e8a602c994480e0dc5dd79eb3eea570f12a1e59a83b7b5e7123bb4225380ca4', '2016-08-29 14:37:08'),
(53, 0, '15896113544', 'cxh1234567', '69526738', '3eb436281264285cfa0d429a44b14617714371c8d2d7bcc5e1accc72735fd98dd742070073e1ddc3311757ec458a1e63ae05ae9ed84a60e7e98327801bee7a76', '2016-08-29 16:18:37'),
(54, 0, '15896180655', 'cxh1234567', '50327841', '3eb436281264285cfa0d429a44b14617714371c8d2d7bcc5e1accc72735fd98dfaa045318457a143f9add93e5f153b55013c1a407454075d79339a6ee742dea6', '2016-08-29 16:23:07');

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
  `last_update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`detail_id`),
  KEY `uid` (`detail_id`),
  KEY `uid_2` (`uid`),
  KEY `uid_3` (`uid`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=55 ;

--
-- 转存表中的数据 `ac_user_detail_info`
--

INSERT INTO `ac_user_detail_info` (`detail_id`, `uid`, `icon_url`, `admission_year`, `faculty_id`, `major_id`, `name`, `gender`, `job`, `city`, `tags`, `instroduction`, `my_circle_list`, `company`, `company_publicity_level`, `public_contact_list`, `protect_contact_list`, `job_list`, `job_list_level`, `last_update_time`) VALUES
(1, 1, 'default', 2014, 71, 1, '陈雄辉', 0, 'worker96', 321, '{}', '{}', '{}', 'another company', 0, '{}', '{}', '{}', 0, '2016-08-28 17:11:37'),
(2, 2, 'default', 2014, 71, 1, '陈雄辉', 0, 'student', 123, '{}', '{}', '{}', 'google China', 0, '{}', '{}', '{}', 0, '2016-08-28 17:11:37'),
(3, 3, 'default', 2014, 71, 1, '陈雄辉', 0, 'student', 123, '{}', '{}', '{}', 'google China', 0, '{}', '{}', '{}', 0, '2016-08-28 17:11:37'),
(4, 4, 'default', 2014, 71, 1, '陈雄辉', 0, 'student', 123, '{}', '{}', '{}', 'google China', 0, '{}', '{}', '{}', 0, '2016-08-28 17:11:37'),
(5, 5, 'default', 2014, 71, 1, '陈雄辉', 0, 'student', 123, '{}', '{}', '{}', 'google China', 0, '{}', '{}', '{}', 0, '2016-08-28 17:11:37'),
(6, 6, 'default', 2014, 71, 1, '陈雄辉', 0, 'student', 123, '{}', '{}', '{}', 'google China', 0, '{}', '{}', '{}', 0, '2016-08-28 17:11:37'),
(7, 7, 'default', 2014, 71, 1, '陈雄辉', 0, 'student', 123, '{}', '{}', '{}', 'google China', 0, '{}', '{}', '{}', 0, '2016-08-28 17:11:37'),
(8, 8, 'default', 2014, 71, 1, '陈雄辉', 0, 'student', 123, '{}', '{}', '{}', 'google China', 0, '{}', '{}', '{}', 0, '2016-08-28 17:11:37'),
(9, 9, 'default', 2014, 71, 1, '陈雄辉', 0, 'student', 123, '{}', '{}', '{}', 'google China', 0, '{}', '{}', '{}', 0, '2016-08-28 17:11:37'),
(10, 10, 'default', 2014, 71, 1, '陈雄辉', 0, 'student', 123, '{}', '{}', '{}', 'google China', 0, '{}', '{}', '{}', 0, '2016-08-28 17:11:37'),
(11, 11, 'default', 2014, 71, 1, '陈雄辉', 0, 'student', 123, '{}', '{}', '{}', 'google China', 0, '{}', '{}', '{}', 0, '2016-08-28 17:11:37'),
(12, 12, 'default', 2014, 71, 1, '陈雄辉', 0, 'student', 123, '{}', '{}', '{}', 'google China', 0, '{}', '{}', '{}', 0, '2016-08-28 17:11:37'),
(13, 13, 'default', 2014, 71, 1, '陈雄辉', 0, 'student', 123, '{}', '{}', '{}', 'google China', 0, '{}', '{}', '{}', 0, '2016-08-28 17:11:37'),
(14, 14, 'default', 2014, 71, 1, '陈雄辉', 0, 'student', 123, '{}', '{}', '{}', 'google China', 0, '{}', '{}', '{}', 0, '2016-08-28 17:11:37'),
(15, 15, 'default', 2014, 71, 1, '陈雄辉', 0, 'student', 123, '{}', '{}', '{}', 'google China', 0, '{}', '{}', '{}', 0, '2016-08-28 17:11:37'),
(16, 16, 'default', 2014, 71, 1, '陈雄辉', 0, 'student', 123, '{}', '{}', '{}', 'google China', 0, '{}', '{}', '{}', 0, '2016-08-28 17:11:37'),
(17, 17, 'default', 2014, 71, 1, '陈雄辉', 0, 'student', 123, '{}', '{}', '{}', 'google China', 0, '{}', '{}', '{}', 0, '2016-08-28 17:11:37'),
(18, 18, 'default', 2014, 71, 1, '陈雄辉', 0, 'student', 123, '{}', '{}', '{}', 'google China', 0, '{}', '{}', '{}', 0, '2016-08-28 17:11:37'),
(19, 19, 'default', 2014, 71, 1, '陈雄辉', 0, 'student', 123, '{}', '{}', '{}', 'google China', 0, '{}', '{}', '{}', 0, '2016-08-28 17:11:37'),
(20, 20, 'default', 2014, 71, 1, '陈雄辉', 0, 'student', 123, '{}', '{}', '{}', 'google China', 0, '{}', '{}', '{}', 0, '2016-08-28 17:11:37'),
(21, 21, 'default', 2014, 71, 1, '陈雄辉', 0, 'student', 123, '{}', '{}', '{}', 'google China', 0, '{}', '{}', '{}', 0, '2016-08-28 17:11:37'),
(22, 22, 'default', 2014, 71, 1, '陈雄辉', 0, 'student', 123, '{}', '{}', '{}', 'google China', 0, '{}', '{}', '{}', 0, '2016-08-28 17:11:37'),
(23, 23, 'default', 2014, 71, 1, '陈雄辉', 0, 'student', 123, '{}', '{}', '{}', 'google China', 0, '{}', '{}', '{}', 0, '2016-08-28 17:11:37'),
(24, 24, 'default', 2014, 71, 1, '陈雄辉', 0, 'student', 123, '{}', '{}', '{}', 'google China', 0, '{}', '{}', '{}', 0, '2016-08-28 17:11:37'),
(25, 25, 'default', 2014, 71, 1, '陈雄辉', 0, 'student', 123, '{}', '{}', '{}', 'google China', 0, '{}', '{}', '{}', 0, '2016-08-28 17:11:37'),
(26, 26, 'default', 2014, 71, 1, '陈雄辉', 0, 'student', 123, '{}', '{}', '{}', 'google China', 0, '{}', '{}', '{}', 0, '2016-08-28 17:11:37'),
(27, 27, 'default', 2014, 71, 1, '陈雄辉', 0, 'student', 123, '{}', '{}', '{}', 'google China', 0, '{}', '{}', '{}', 0, '2016-08-28 17:11:37'),
(28, 28, 'default', 2014, 71, 1, '陈雄辉', 0, 'student', 123, '{}', '{}', '{}', 'google China', 0, '{}', '{}', '{}', 0, '2016-08-28 17:11:37'),
(29, 29, 'default', 2014, 71, 1, '陈雄辉', 0, 'student', 123, '{}', '{}', '{}', 'google China', 0, '{}', '{}', '{}', 0, '2016-08-28 17:11:37'),
(30, 30, 'default', 2014, 71, 1, '陈雄辉', 0, 'student', 123, '{}', '{}', '{}', 'google China', 0, '{}', '{}', '{}', 0, '2016-08-28 17:11:37'),
(31, 31, 'default', 2014, 71, 1, '陈雄辉', 0, 'student', 123, '{}', '{}', '{}', 'google China', 0, '{}', '{}', '{}', 0, '2016-08-28 17:11:37'),
(32, 32, 'default', 2014, 71, 1, '陈雄辉', 0, 'student', 123, '{}', '{}', '{}', 'google China', 0, '{}', '{}', '{}', 0, '2016-08-28 17:11:37'),
(33, 33, 'default', 2014, 71, 1, '陈雄辉', 0, 'student', 123, '{}', '{}', '{}', 'google China', 0, '{}', '{}', '{}', 0, '2016-08-28 17:11:37'),
(34, 34, 'default', 2014, 71, 1, '陈雄辉', 0, 'student', 123, '{}', '{}', '{}', 'google China', 0, '{}', '{}', '{}', 0, '2016-08-28 17:11:37'),
(35, 35, 'default', 2014, 71, 1, '陈雄辉', 0, 'student', 123, '{}', '{}', '{}', 'google China', 0, '{}', '{}', '{}', 0, '2016-08-28 17:11:37'),
(36, 36, 'default', 2014, 71, 1, '陈雄辉', 0, 'student', 123, '{}', '{}', '{}', 'google China', 0, '{}', '{}', '{}', 0, '2016-08-28 17:11:37'),
(37, 37, 'default', 2014, 71, 1, '陈雄辉', 0, 'student', 123, '{}', '{}', '{}', 'google China', 0, '{}', '{}', '{}', 0, '2016-08-28 17:11:37'),
(38, 38, 'default', 2014, 71, 1, '陈雄辉', 0, 'student', 123, '{}', '{}', '{}', 'google China', 0, '{}', '{}', '{}', 0, '2016-08-28 17:11:37'),
(39, 39, 'default', 2014, 71, 1, '陈雄辉', 0, 'student', 123, '{}', '{}', '{}', 'google China', 0, '{}', '{}', '{}', 0, '2016-08-28 17:11:37'),
(40, 40, 'default', 2014, 71, 1, '陈雄辉', 0, 'student', 123, '{}', '{}', '{}', 'google China', 0, '{}', '{}', '{}', 0, '2016-08-28 17:11:37'),
(41, 41, 'default', 2014, 71, 1, '陈雄辉', 0, 'student', 123, '{}', '{}', '{}', 'google China', 0, '{}', '{}', '{}', 0, '2016-08-28 17:11:37'),
(42, 42, 'default', 2014, 71, 1, '陈雄辉', 0, 'student', 123, '{}', '{}', '{}', 'google China', 0, '{}', '{}', '{}', 0, '2016-08-28 17:11:37'),
(43, 43, 'default', 2014, 71, 1, '陈雄辉', 0, 'student', 123, '{}', '{}', '{}', 'google China', 0, '{}', '{}', '{}', 0, '2016-08-28 17:11:37'),
(44, 44, 'default', 2014, 71, 1, '陈雄辉', 0, 'student', 123, '{}', '{}', '{}', 'google China', 0, '{}', '{}', '{}', 0, '2016-08-28 17:11:37'),
(45, 45, 'default', 2014, 71, 1, '陈雄辉', 0, 'student', 123, '{}', '{}', '{}', 'google China', 0, '{}', '{}', '{}', 0, '2016-08-28 17:11:37'),
(46, 46, 'default', 2014, 71, 1, '陈雄辉', 0, 'student', 123, '{}', '{}', '{}', 'google China', 0, '{}', '{}', '{}', 0, '2016-08-28 17:11:37'),
(47, 47, 'default', 2014, 71, 1, '陈雄辉', 0, 'student', 123, '{}', '{}', '{}', 'google China', 0, '{}', '{}', '{}', 0, '2016-08-28 17:11:37'),
(48, 48, 'default', 2014, 71, 1, '陈雄辉', 0, 'student', 123, '{}', '{}', '{}', 'google China', 0, '{}', '{}', '{}', 0, '2016-08-28 17:11:37'),
(49, 49, 'default', 2014, 71, 1, '陈雄辉', 0, 'student', 123, '{}', '{}', '{}', 'google China', 0, '{}', '{}', '{}', 0, '2016-08-28 17:11:37'),
(50, 50, 'default', 2014, 71, 1, '陈雄辉', 0, 'student', 123, '{}', '{}', '{}', 'google China', 0, '{}', '{}', '{}', 0, '2016-08-28 17:11:37'),
(51, 51, 'default', 2014, 71, 1, '陈雄辉', 0, 'student', 123, '{}', '{}', '{}', 'google China', 0, '{}', '{}', '{}', 0, '2016-08-28 17:11:37'),
(52, 52, 'default', 2014, 71, 1, '陈雄辉', 0, 'student', 123, '{}', '{}', '{}', 'google China', 0, '{}', '{}', '{}', 0, '2016-08-28 17:11:37'),
(53, 53, 'default', 2014, 71, 1, '陈雄辉', 0, 'student', 123, '{}', '{}', '{}', 'google China', 0, '{}', '{}', '{}', 0, '2016-08-28 17:11:37'),
(54, 54, 'default', 2014, 71, 1, '陈雄辉', 0, 'student', 123, '{}', '{}', '{}', 'google China', 0, '{}', '{}', '{}', 0, '2016-08-28 17:11:37');

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
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=55 ;

--
-- 转存表中的数据 `ac_user_list_info`
--

INSERT INTO `ac_user_list_info` (`list_id`, `uid`, `icon_url`, `name`, `faculty_id`, `major_id`, `job`, `gender`, `publicity_level`, `admission_year`, `city`) VALUES
(1, 1, 'default', '陈雄辉', 71, 1, 'worker96', 0, 0, 2014, 321),
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
(27, 27, 'default', '陈雄辉', 71, 1, 'student', 0, 0, 2014, 123),
(28, 28, 'default', '陈雄辉', 71, 1, 'student', 0, 0, 2014, 123),
(29, 29, 'default', '陈雄辉', 71, 1, 'student', 0, 0, 2014, 123),
(30, 30, 'default', '陈雄辉', 71, 1, 'student', 0, 0, 2014, 123),
(31, 31, 'default', '陈雄辉', 71, 1, 'student', 0, 0, 2014, 123),
(32, 32, 'default', '陈雄辉', 71, 1, 'student', 0, 0, 2014, 123),
(33, 33, 'default', '陈雄辉', 71, 1, 'student', 0, 0, 2014, 123),
(34, 34, 'default', '陈雄辉', 71, 1, 'student', 0, 0, 2014, 123),
(35, 35, 'default', '陈雄辉', 71, 1, 'student', 0, 0, 2014, 123),
(36, 36, 'default', '陈雄辉', 71, 1, 'student', 0, 0, 2014, 123),
(37, 37, 'default', '陈雄辉', 71, 1, 'student', 0, 0, 2014, 123),
(38, 38, 'default', '陈雄辉', 71, 1, 'student', 0, 0, 2014, 123),
(39, 39, 'default', '陈雄辉', 71, 1, 'student', 0, 0, 2014, 123),
(40, 40, 'default', '陈雄辉', 71, 1, 'student', 0, 0, 2014, 123),
(41, 41, 'default', '陈雄辉', 71, 1, 'student', 0, 0, 2014, 123),
(42, 42, 'default', '陈雄辉', 71, 1, 'student', 0, 0, 2014, 123),
(43, 43, 'default', '陈雄辉', 71, 1, 'student', 0, 0, 2014, 123),
(44, 44, 'default', '陈雄辉', 71, 1, 'student', 0, 0, 2014, 123),
(45, 45, 'default', '陈雄辉', 71, 1, 'student', 0, 0, 2014, 123),
(46, 46, 'default', '陈雄辉', 71, 1, 'student', 0, 0, 2014, 123),
(47, 47, 'default', '陈雄辉', 71, 1, 'student', 0, 0, 2014, 123),
(48, 48, 'default', '陈雄辉', 71, 1, 'student', 0, 0, 2014, 123),
(49, 49, 'default', '陈雄辉', 71, 1, 'student', 0, 0, 2014, 123),
(50, 50, 'default', '陈雄辉', 71, 1, 'student', 0, 0, 2014, 123),
(51, 51, 'default', '陈雄辉', 71, 1, 'student', 0, 0, 2014, 123),
(52, 52, 'default', '陈雄辉', 71, 1, 'student', 0, 0, 2014, 123),
(53, 53, 'default', '陈雄辉', 71, 1, 'student', 0, 0, 2014, 123),
(54, 54, 'default', '陈雄辉', 71, 1, 'student', 0, 0, 2014, 123);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
