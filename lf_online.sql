-- MySQL dump 10.13  Distrib 8.0.25, for Linux (x86_64)
--
-- Host: localhost    Database: lifechoices_online
-- ------------------------------------------------------
-- Server version	8.0.25-0ubuntu0.21.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Users`
--

DROP TABLE IF EXISTS `Users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Users` (
  `ID` varchar(13) NOT NULL,
  `name` varchar(25) NOT NULL,
  `surname` varchar(30) NOT NULL,
  `phone` varchar(10) NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Users`
--

LOCK TABLES `Users` WRITE;
/*!40000 ALTER TABLE `Users` DISABLE KEYS */;
INSERT INTO `Users` VALUES ('9710295431089','Simphiwe','Sithole','044678854'),('0202285068088','Brent','Johnson','0621532382'),('0212235091080','Adam','Africa','0837936404'),('9811145170081','Ronald','Terblanche','0811236436'),('9903155793082','Luyanda','Dingindlela','1234567890'),('9903200072086','Zoe','Eripse','0849219477');
/*!40000 ALTER TABLE `Users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `admin_users`
--

DROP TABLE IF EXISTS `admin_users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `admin_users` (
  `ID` varchar(13) NOT NULL,
  `password` varchar(15) NOT NULL,
  UNIQUE KEY `password` (`password`),
  KEY `ID` (`ID`),
  CONSTRAINT `admin_users_ibfk_1` FOREIGN KEY (`ID`) REFERENCES `Users` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin_users`
--

LOCK TABLES `admin_users` WRITE;
/*!40000 ALTER TABLE `admin_users` DISABLE KEYS */;
INSERT INTO `admin_users` VALUES ('9710295431089','sts2021');
/*!40000 ALTER TABLE `admin_users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `next_of_kin`
--

DROP TABLE IF EXISTS `next_of_kin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `next_of_kin` (
  `ID` varchar(13) DEFAULT NULL,
  `name` varchar(25) NOT NULL,
  `phone` varchar(10) NOT NULL,
  KEY `ID` (`ID`),
  CONSTRAINT `next_of_kin_ibfk_1` FOREIGN KEY (`ID`) REFERENCES `Users` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `next_of_kin`
--

LOCK TABLES `next_of_kin` WRITE;
/*!40000 ALTER TABLE `next_of_kin` DISABLE KEYS */;
INSERT INTO `next_of_kin` VALUES ('9811145170081','Merle','0813570081'),('0012085583081','Neil','0857934522'),('0202285068088','Craig','0722774038'),('0212235091080','big man','0857934579'),('9903200072086','madam','0727956430'),('9903155793082','pretty big man','9876543211');
/*!40000 ALTER TABLE `next_of_kin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `register`
--

DROP TABLE IF EXISTS `register`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `register` (
  `Date` varchar(10) NOT NULL,
  `ID` varchar(13) DEFAULT NULL,
  `name` varchar(20) DEFAULT NULL,
  `time_in` varchar(5) NOT NULL,
  `time_out` varchar(5) NOT NULL DEFAULT '--:--',
  KEY `ID` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `register`
--

LOCK TABLES `register` WRITE;
/*!40000 ALTER TABLE `register` DISABLE KEYS */;
INSERT INTO `register` VALUES ('2021-07-06','9710295431089','Simphiwe','11:7','17:10'),('2021-07-07','9710295431089','Simphiwe','15:09','16:07'),('2021-07-07','9710295431089','Simphiwe','14:14','18:06'),('2021-07-09','9710295431089','Simphiwe','16:43','16:44');
/*!40000 ALTER TABLE `register` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-07-10 15:36:40
