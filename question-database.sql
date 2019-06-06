# ************************************************************
# Sequel Pro SQL dump
# Version 4541
#
# http://www.sequelpro.com/
# https://github.com/sequelpro/sequelpro
#
# Host: liangxiaowei.mysql.rds.aliyuncs.com (MySQL 5.6.16-log)
# Database: gps_status
# Generation Time: 2019-05-17 03:06:29 +0000
# ************************************************************


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


# Dump of table category
# ------------------------------------------------------------

DROP TABLE IF EXISTS `category`;

CREATE TABLE `category` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `category_name` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `category` WRITE;
/*!40000 ALTER TABLE `category` DISABLE KEYS */;

INSERT INTO `category` (`id`, `category_name`)
VALUES
	(1,'Java'),
	(2,'JavaScript'),
	(3,'Python'),
	(4,'Php');

/*!40000 ALTER TABLE `category` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table question_tag_rel
# ------------------------------------------------------------

DROP TABLE IF EXISTS `question_tag_rel`;

CREATE TABLE `question_tag_rel` (
  `question_id` int(11) unsigned NOT NULL,
  `tag_id` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`question_id`,`tag_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table questions
# ------------------------------------------------------------

DROP TABLE IF EXISTS `questions`;

CREATE TABLE `questions` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `question` text,
  `answer` text,
  `category_id` int(11) DEFAULT NULL,
  `status` varchar(10) DEFAULT 'submitted' COMMENT 'submited/padding/published',
  `user_id` int(11) DEFAULT NULL,
  `address` varchar(200) DEFAULT NULL,
  `latitude` double DEFAULT NULL,
  `longitude` double DEFAULT NULL,
  `created_at` int(11) DEFAULT NULL,
  `first_name` varchar(40) DEFAULT NULL,
  `last_name` varchar(50) DEFAULT NULL,
  `contact` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table reg_user
# ------------------------------------------------------------

DROP TABLE IF EXISTS `reg_user`;

CREATE TABLE `reg_user` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `email` varchar(100) DEFAULT NULL,
  `password` varchar(128) DEFAULT NULL,
  `first_name` varchar(100) DEFAULT NULL,
  `last_name` varchar(100) DEFAULT NULL,
  `level` varchar(10) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `active_key` varchar(120) DEFAULT NULL,
  `reg_time` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `reg_user` WRITE;
/*!40000 ALTER TABLE `reg_user` DISABLE KEYS */;

INSERT INTO `reg_user` (`id`, `email`, `password`, `first_name`, `last_name`, `level`, `status`, `active_key`, `reg_time`)
VALUES
	(8,'wattsappbronx@outlook.com','1','User','Wattsappbronx','admin',2,NULL,1555577838);

/*!40000 ALTER TABLE `reg_user` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table tags
# ------------------------------------------------------------

DROP TABLE IF EXISTS `tags`;

CREATE TABLE `tags` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `tags` WRITE;
/*!40000 ALTER TABLE `tags` DISABLE KEYS */;

INSERT INTO `tags` (`id`, `name`)
VALUES
	(1,'Who'),
	(2,'News'),
	(3,'Work');

/*!40000 ALTER TABLE `tags` ENABLE KEYS */;
UNLOCK TABLES;



/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
