-- MySQL dump 10.13  Distrib 5.7.31, for Linux (aarch64)
--
-- Host: 127.0.0.1    Database: Maintenance
-- ------------------------------------------------------
-- Server version	5.5.5-10.2.32-MariaDB-1:10.2.32+maria~bionic

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `alarms_yaskawa`
--

DROP TABLE IF EXISTS `alarms_yaskawa`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `alarms_yaskawa` (
  `robot_id` int(11) NOT NULL,
  `AlarmCode` int(4) NOT NULL,
  `AlarmData` int(4) DEFAULT NULL,
  `AlarmType` tinyint(4) DEFAULT NULL,
  `AlarmTime` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `AlarmName` varchar(255) NOT NULL,
  `AlarmCategory` tinyint(4) NOT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alarms_yaskawa`
--

LOCK TABLES `alarms_yaskawa` WRITE;
/*!40000 ALTER TABLE `alarms_yaskawa` DISABLE KEYS */;
INSERT INTO `alarms_yaskawa` VALUES (1,1377,1,3,'2020-01-07 18:58:00','エンコーダ断線検出(サーボ)',1,6),(1,1221,17,1,'2020-01-07 17:21:00','イーサネット初期化異常',1,7),(1,4744,0,0,'2020-07-09 15:41:00','機械安全PPｲﾈｰﾌﾞﾙ信号不一致',2,8),(1,4460,0,1,'2020-06-18 16:35:00','演算命令０除算',2,9),(1,4744,0,0,'2020-06-01 18:15:00','機械安全PPｲﾈｰﾌﾞﾙ信号不一致',2,10),(1,4744,0,0,'2020-05-27 18:56:00','機械安全PPｲﾈｰﾌﾞﾙ信号不一致',2,11),(1,4460,0,1,'2020-04-20 20:18:00','演算命令０除算',2,13),(1,4460,0,1,'2020-04-20 20:16:00','演算命令０除算',2,14),(1,4460,0,1,'2020-04-20 20:15:00','演算命令０除算',2,15),(1,4460,0,1,'2020-04-20 20:13:00','演算命令０除算',2,16),(1,4460,0,1,'2020-04-20 20:11:00','演算命令０除算',2,17),(1,802,2,1,'2020-01-07 16:50:00','ファイルＩ／Ｏエラー(ACP01 SD)',5,18),(1,270,0,1,'2020-01-07 16:50:00','ﾒﾓﾘｴﾗｰ(SDﾊﾞｯｸｱｯﾌﾟﾌｧｲﾙ)',5,20),(1,1220,1001,1,'2020-01-17 11:32:00','LAN通信パラメータ異常',1,21),(1,1220,1001,1,'2020-01-17 11:30:00','LAN通信パラメータ異常',1,22),(1,1377,2,3,'2020-01-07 19:00:00','エンコーダ断線検出(サーボ)',1,25),(1,801,370,1,'2020-01-07 16:50:00','ファイルロードエラー(ACP01 SD)',5,26),(1,4744,0,0,'2020-05-27 18:35:00','機械安全PPｲﾈｰﾌﾞﾙ信号不一致',2,27),(1,1220,1001,1,'2020-01-17 11:27:00','LAN通信パラメータ異常',1,28),(1,1306,62,3,'2020-01-07 19:00:00','アンプタイプミスマッチ',1,29);
/*!40000 ALTER TABLE `alarms_yaskawa` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-07-31 13:52:04
