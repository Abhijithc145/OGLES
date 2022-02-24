-- MySQL dump 10.13  Distrib 8.0.28, for Linux (x86_64)
--
-- Host: localhost    Database: WATCHS
-- ------------------------------------------------------
-- Server version	8.0.28-0ubuntu0.20.04.3

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
-- Table structure for table `app_buyproduct`
--

DROP TABLE IF EXISTS `app_buyproduct`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `app_buyproduct` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `total` int unsigned NOT NULL,
  `quantity` int unsigned NOT NULL,
  `products_id` bigint NOT NULL,
  `value` int unsigned NOT NULL,
  PRIMARY KEY (`id`),
  KEY `app_buyproduct_products_id_aaf18377_fk_dash_product_id` (`products_id`),
  CONSTRAINT `app_buyproduct_products_id_aaf18377_fk_dash_product_id` FOREIGN KEY (`products_id`) REFERENCES `dash_product` (`id`),
  CONSTRAINT `app_buyproduct_chk_1` CHECK ((`total` >= 0)),
  CONSTRAINT `app_buyproduct_chk_2` CHECK ((`quantity` >= 0)),
  CONSTRAINT `app_buyproduct_chk_3` CHECK ((`value` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_buyproduct`
--

LOCK TABLES `app_buyproduct` WRITE;
/*!40000 ALTER TABLE `app_buyproduct` DISABLE KEYS */;
INSERT INTO `app_buyproduct` VALUES (1,1614,1,4,0);
/*!40000 ALTER TABLE `app_buyproduct` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app_cartproduct`
--

DROP TABLE IF EXISTS `app_cartproduct`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `app_cartproduct` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `total` int unsigned NOT NULL,
  `quantity` int unsigned NOT NULL,
  `products_id` bigint NOT NULL,
  `user_id` bigint DEFAULT NULL,
  `guest` varchar(300) DEFAULT NULL,
  `alltotal` int unsigned NOT NULL,
  PRIMARY KEY (`id`),
  KEY `app_cartproduct_products_id_20f73c78_fk_dash_product_id` (`products_id`),
  KEY `app_cartproduct_user_id_e6ab5bf0_fk_app_customuser_id` (`user_id`),
  CONSTRAINT `app_cartproduct_products_id_20f73c78_fk_dash_product_id` FOREIGN KEY (`products_id`) REFERENCES `dash_product` (`id`),
  CONSTRAINT `app_cartproduct_user_id_e6ab5bf0_fk_app_customuser_id` FOREIGN KEY (`user_id`) REFERENCES `app_customuser` (`id`),
  CONSTRAINT `app_cartproduct_chk_1` CHECK ((`total` >= 0)),
  CONSTRAINT `app_cartproduct_chk_2` CHECK ((`quantity` >= 0)),
  CONSTRAINT `app_cartproduct_chk_3` CHECK ((`alltotal` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=337 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_cartproduct`
--

LOCK TABLES `app_cartproduct` WRITE;
/*!40000 ALTER TABLE `app_cartproduct` DISABLE KEYS */;
INSERT INTO `app_cartproduct` VALUES (76,1566,1,2,7,'',1),(173,1614,1,4,1,'',1),(174,2786,1,5,1,'',1),(207,1614,1,4,10,NULL,1),(236,1968,1,3,9,'',1),(249,1172,1,5,16,NULL,1),(335,1968,1,3,5,'',1),(336,1172,1,5,2,'',1);
/*!40000 ALTER TABLE `app_cartproduct` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app_coupon`
--

DROP TABLE IF EXISTS `app_coupon`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `app_coupon` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `coupon_id` varchar(6) DEFAULT NULL,
  `coupon_offer` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `app_coupon_coupon_id_c0e7158e_uniq` (`coupon_id`)
) ENGINE=InnoDB AUTO_INCREMENT=80 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_coupon`
--

LOCK TABLES `app_coupon` WRITE;
/*!40000 ALTER TABLE `app_coupon` DISABLE KEYS */;
INSERT INTO `app_coupon` VALUES (70,'MH5Ck1',10),(71,'MH5Ck0',10),(72,'MH5Ck2',10),(73,'MH5Ck3',10),(74,'MH5Ck4',10),(75,'MH5Ck5',10),(76,'MH5Ck6',10),(77,'MH5Ck7',10),(78,'MH5Ck8',10),(79,'MH5Ck9',10);
/*!40000 ALTER TABLE `app_coupon` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app_customuser`
--

DROP TABLE IF EXISTS `app_customuser`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `app_customuser` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `first_name` varchar(100) NOT NULL,
  `last_name` varchar(100) NOT NULL,
  `email` varchar(254) NOT NULL,
  `number` varchar(15) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `number` (`number`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_customuser`
--

LOCK TABLES `app_customuser` WRITE;
/*!40000 ALTER TABLE `app_customuser` DISABLE KEYS */;
INSERT INTO `app_customuser` VALUES (1,'pbkdf2_sha256$320000$hvr0ef3InAVZYxObeF41mK$MgfxrSHyIQak9y7mzNTJ381uppM/0Jh5NiwRRYV5UOA=','2022-02-23 14:15:35.142566',1,'admin',1,1,'2022-02-10 04:44:54.031233','','','admin@gmail.com',''),(2,'pbkdf2_sha256$320000$uxFd3CSpKHFlIJfilbNgLZ$leISsccfDARj+JjSlsGae9sqhUoN2nBZIvgy1abpiYw=',NULL,0,'Sana',0,1,'2022-02-10 04:51:52.875541','sana','fathima','abhijithabhipgmr145@gmail.com','6427890234'),(4,'pbkdf2_sha256$320000$rPcKL5j9bANQqjk0alTUKD$0l6xB6ZwGIjGDLzyk0TTDNtezwMehExUC56sV+EOCAs=',NULL,0,'Abhi',0,1,'2022-02-10 16:34:59.927656','llkjhgf','khgf','abhi@gmail.com','7907127230'),(5,'pbkdf2_sha256$320000$THQHvTK62tjw7qQeRsAVDZ$TzIrzfBtN8jqSuK09vtslwDuz8GuoOcOJABrBaDNcKY=',NULL,0,'Thushad',0,1,'2022-02-11 06:14:20.143572','thus','dfg','thushad@gmail.com','6282575520'),(6,'pbkdf2_sha256$320000$mLcggIfxqw6PZgvwKrm8sV$b4dP71JT5ZZ31YrPTkaXkCzxH59nfw3Iref5hEmmch0=',NULL,0,'Rasif',0,1,'2022-02-13 06:11:19.860285','Muhammed','Rasif','rasif@gmail.com','9744088812'),(7,'pbkdf2_sha256$320000$CbGWBATK98POj8W3tSDwgL$NppbyQb85PyaQW3RKdg3QRn2kbn/yFh4+J58Tccz2KU=',NULL,0,'Lithin',0,1,'2022-02-13 07:16:35.148136','Lithin','CM','lithinc0@gmail.com','8078798842'),(8,'pbkdf2_sha256$320000$lLuJ8Gn5vz7bXAaZcbPDyC$5uTnSt1JsDGMZLH0Yoj/60uXbxhPU4EGVxYr6mdy+mU=',NULL,0,'kkkk',0,1,'2022-02-14 11:49:16.049901','Abhijith','c','abhijithabhipgmr@gmail.com','8'),(9,'pbkdf2_sha256$320000$eqxlBxEOwyFcoQ5B6WxMbw$f0EvMK13F7SbyFvh0ouQDMa9+jm+9gmcFoIp86Y7k+I=',NULL,0,'shahin',0,1,'2022-02-21 04:53:31.537929','Shahin','salim','shahinsalims@gmail.com','8921804'),(10,'pbkdf2_sha256$320000$IC7SCL0gZt2DA6UhexiK9O$/KyVBuuvM4qhpIpF50BK6EiL+01pI8rcFhGby9F9gLE=',NULL,0,'Kukku',0,1,'2022-02-21 08:50:22.724946','Abhijith','c','kukku@gmail.com','73066417272'),(11,'pbkdf2_sha256$320000$jDC7OJhWoujan2XD55pVuF$Ph9fsLkKO/aoq4XCf5hdvPacA5xR1anDIR9IigES0Do=',NULL,0,'Navya',0,1,'2022-02-22 05:34:48.978749','Navya','Balu','navya@gmail.com','7306641756'),(12,'pbkdf2_sha256$320000$e0uoCHofQDwMfOwQUst55p$yOKjNviGm2JkHsdXJT/OFiye+r0Ub3tAkY+jUeWVenc=',NULL,0,'chandu',0,1,'2022-02-22 05:38:39.845380','chandu','m','chandu@gmail.com','7396641726'),(13,'pbkdf2_sha256$320000$4TBDCfgmBSZ1CTwcQV7ii5$5PwKfA38Sr16fJXd/qjuhyUIXfUNa9DGLlpUXnd/Ny8=',NULL,0,'adhil',0,1,'2022-02-22 05:43:11.991827','adhil','adhil','adhil@gmail.com','7304641726'),(14,'pbkdf2_sha256$320000$iyptj2ntHNsq3UOFk3iSjh$HXZBK0q4ecJ13OyB5qN9LZEA7YQVThkyNTP1jHPmkVU=',NULL,0,'sharu',0,1,'2022-02-22 05:49:09.129555','sharu','n','sharum@gmail.com','7306661726'),(15,'pbkdf2_sha256$320000$rpPseiWFiJdKHKiDM99eY2$Pjc86hx6md6KEXlxoGRND8YZONSMsoX6bmfQtLPhS6g=',NULL,0,'Babu',0,1,'2022-02-22 05:55:04.759773','babu','b','babu@gmail.com','73061726'),(16,'pbkdf2_sha256$320000$eDOWZzzMpHROyqPcjHWhDg$z8opTwTbFH1S8y4JyMqmSZOYcm4UmQPnwRyinxfWwI8=',NULL,0,'aiswarya',0,1,'2022-02-22 06:00:57.790171','Aiswarya','R','aiswarya@gmail.com','8592863845'),(17,'pbkdf2_sha256$320000$CPwrotCOCuriYZAO16u03A$GeX30N2/wDQjnhs3bW1cbWGCwWvdwItWhPAQfi21lqk=',NULL,0,'Roshas',0,1,'2022-02-22 09:17:50.812068','Roshas','dfghj','roshas@gmail.com','7012598205'),(18,'pbkdf2_sha256$320000$D3gcOROx9ifwLqLrmeLYzv$tAynm/STWqF7LOmixOoB5mS+Kl+pHoRjgImSo73XN/c=',NULL,0,'Manaf',0,1,'2022-02-22 17:36:15.667458','Muhammad','manaf','manaf@gmail.com','7306172559'),(19,'pbkdf2_sha256$320000$YV629bsHhchLPXtZcwvnmj$Lp5isTvL385JFZW+aZBpktR//4u1/4j5Bcmfn1FS330=',NULL,0,'shahinsalim',0,1,'2022-02-24 02:50:04.464002','shahin','shahin','shahin@gmail.com','891849804'),(20,'pbkdf2_sha256$320000$qmXtbvTUOr9oVya0hUYCcR$tdRSDvwB/CFxdGeDnS7yx2BtHAAvV0KJuetaIdR4Ng4=',NULL,0,'a',0,1,'2022-02-24 02:58:39.155793','a','a','a@gmail.com','8592863045'),(21,'pbkdf2_sha256$320000$uUvaauv94NYvYb2bDOVas1$LGPMxZ/MYjyoOT7L8JLVOjCQAW+MU04VudOzhVsNAKY=',NULL,0,'Shanu',0,1,'2022-02-24 03:04:14.594754','fghjk','fghnm','shanu@gmail.com','730661726'),(22,'pbkdf2_sha256$320000$QIw6gMGTQaIcVte0mn9sII$JtIww9qWh+AOjkX5CF1D2X20XoprD+qSi/nSdZwHA74=',NULL,0,'reshinsuresh',0,1,'2022-02-24 03:09:34.364865','Reshin','Suresh','reshinsuresh1@gmail.com','7012828518'),(24,'pbkdf2_sha256$320000$rWwhUd3TyBRohCebUPsDJL$OYsxj/B0KVohpg4i18fXkqtRV8veyaRF1oJFNq02CBw=',NULL,0,'asdfghjkl',0,1,'2022-02-24 04:12:51.701616','qwertyuio','sdfghjkl','asdfghjl@gmail.com','73641726'),(25,'pbkdf2_sha256$320000$M05kadsREH4Mfysgpf8uxn$MWC12HPraKEFE6lEqmF1BKYIVZ+ehinUe/vUJ9vH+b8=',NULL,0,'zxcvbnm',0,1,'2022-02-24 04:18:07.937003','asdfghjk','wertyui','achasdfghju@gmail.com','7306641826'),(26,'pbkdf2_sha256$320000$SdLdXz327S2FEXAvakYqbE$DxLAxAAmSU7M889bTNMqOX+R6fJuS4J+6OwMf3EnH6c=',NULL,0,'sanh',0,1,'2022-02-24 04:22:43.696583','shan','cm','sha@gmail.com','7306641726');
/*!40000 ALTER TABLE `app_customuser` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app_customuser_groups`
--

DROP TABLE IF EXISTS `app_customuser_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `app_customuser_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `customuser_id` bigint NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `app_customuser_groups_customuser_id_group_id_a5a0ca22_uniq` (`customuser_id`,`group_id`),
  KEY `app_customuser_groups_group_id_47e49ebd_fk_auth_group_id` (`group_id`),
  CONSTRAINT `app_customuser_group_customuser_id_164d073f_fk_app_custo` FOREIGN KEY (`customuser_id`) REFERENCES `app_customuser` (`id`),
  CONSTRAINT `app_customuser_groups_group_id_47e49ebd_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_customuser_groups`
--

LOCK TABLES `app_customuser_groups` WRITE;
/*!40000 ALTER TABLE `app_customuser_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `app_customuser_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app_customuser_user_permissions`
--

DROP TABLE IF EXISTS `app_customuser_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `app_customuser_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `customuser_id` bigint NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `app_customuser_user_perm_customuser_id_permission_22e31019_uniq` (`customuser_id`,`permission_id`),
  KEY `app_customuser_user__permission_id_c5920c75_fk_auth_perm` (`permission_id`),
  CONSTRAINT `app_customuser_user__customuser_id_4bcbaafb_fk_app_custo` FOREIGN KEY (`customuser_id`) REFERENCES `app_customuser` (`id`),
  CONSTRAINT `app_customuser_user__permission_id_c5920c75_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_customuser_user_permissions`
--

LOCK TABLES `app_customuser_user_permissions` WRITE;
/*!40000 ALTER TABLE `app_customuser_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `app_customuser_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app_order_place`
--

DROP TABLE IF EXISTS `app_order_place`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `app_order_place` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `quantity` int unsigned NOT NULL,
  `orderdate` datetime(6) NOT NULL,
  `status` varchar(100) NOT NULL,
  `paymentmode` varchar(100) NOT NULL,
  `subtotal` bigint DEFAULT NULL,
  `address_id` bigint NOT NULL,
  `products_id` bigint NOT NULL,
  `user_id` bigint NOT NULL,
  `coupons_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `app_order_place_address_id_f61344ac_fk_app_user_details_id` (`address_id`),
  KEY `app_order_place_products_id_c0e7db0d_fk_dash_product_id` (`products_id`),
  KEY `app_order_place_user_id_398b327a_fk_app_customuser_id` (`user_id`),
  KEY `app_order_place_coupons_id_4cd9cb3c_fk_app_coupon_id` (`coupons_id`),
  CONSTRAINT `app_order_place_address_id_f61344ac_fk_app_user_details_id` FOREIGN KEY (`address_id`) REFERENCES `app_user_details` (`id`),
  CONSTRAINT `app_order_place_coupons_id_4cd9cb3c_fk_app_coupon_id` FOREIGN KEY (`coupons_id`) REFERENCES `app_coupon` (`id`),
  CONSTRAINT `app_order_place_products_id_c0e7db0d_fk_dash_product_id` FOREIGN KEY (`products_id`) REFERENCES `dash_product` (`id`),
  CONSTRAINT `app_order_place_user_id_398b327a_fk_app_customuser_id` FOREIGN KEY (`user_id`) REFERENCES `app_customuser` (`id`),
  CONSTRAINT `app_order_place_chk_1` CHECK ((`quantity` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=471 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_order_place`
--

LOCK TABLES `app_order_place` WRITE;
/*!40000 ALTER TABLE `app_order_place` DISABLE KEYS */;
INSERT INTO `app_order_place` VALUES (220,1,'2022-02-21 03:31:08.094836','Placed','cash_on_delivery',1771,29,3,4,NULL),(221,1,'2022-02-21 03:31:08.112526','Placed','cash_on_delivery',3223,29,4,4,NULL),(222,1,'2022-02-21 03:32:33.887817','Placed','cash_on_delivery',1968,29,3,4,NULL),(223,1,'2022-02-21 03:33:14.201115','Placed','cash_on_delivery',1899,29,4,4,NULL),(224,1,'2022-02-21 03:33:28.836039','Placed','cash_on_delivery',1379,29,5,4,NULL),(225,1,'2022-02-21 03:33:54.442822','Placed','cash_on_delivery',1379,29,5,4,NULL),(226,1,'2022-02-21 03:33:57.547004','Placed','cash_on_delivery',1379,29,5,4,NULL),(227,1,'2022-02-21 03:33:58.320432','Placed','cash_on_delivery',1379,29,5,4,NULL),(228,1,'2022-02-21 03:33:58.680288','Placed','cash_on_delivery',1379,29,5,4,NULL),(229,1,'2022-02-21 03:33:59.048753','Placed','cash_on_delivery',1379,29,5,4,NULL),(231,3,'2022-02-21 03:45:46.235933','Placed','cash_on_delivery',6928,29,4,4,NULL),(232,3,'2022-02-21 03:45:46.259249','Placed','cash_on_delivery',7175,29,5,4,NULL),(233,3,'2022-02-21 03:45:46.279696','Placed','cash_on_delivery',10237,29,3,4,NULL),(234,1,'2022-02-21 03:48:28.509670','Placed','cash_on_delivery',2344,29,3,4,NULL),(236,1,'2022-02-21 04:05:32.708249','Shipped','cash_on_delivery',2344,28,3,4,NULL),(237,1,'2022-02-21 04:18:42.741606','Placed','cash_on_delivery',2344,29,3,4,NULL),(238,1,'2022-02-21 04:18:59.434855','Delivered','cash_on_delivery',2344,28,3,4,NULL),(239,1,'2022-02-21 04:22:20.242709','Shipped','cash_on_delivery',1968,29,3,4,NULL),(240,1,'2022-02-21 04:22:20.260473','Delivered','cash_on_delivery',3582,29,4,4,NULL),(241,1,'2022-02-21 04:22:20.276972','Packed','cash_on_delivery',4754,29,5,4,NULL),(242,1,'2022-02-21 04:22:47.544817','Packed','cash_on_delivery',1379,29,5,4,NULL),(243,1,'2022-02-21 06:06:44.673285','Shipped','paypal',1968,52,3,9,NULL),(244,1,'2022-02-21 06:06:44.692470','Delivered','paypal',3582,52,4,9,NULL),(264,1,'2022-02-21 17:36:10.480708','Shipped','cash_on_delivery',1899,55,4,10,NULL),(266,1,'2022-02-21 17:39:32.544706','Placed','cash_on_delivery',1968,55,3,10,NULL),(267,1,'2022-02-21 17:41:40.854162','Placed','cash_on_delivery',1614,55,4,10,NULL),(269,1,'2022-02-21 17:48:53.161049','Placed','cash_on_delivery',1252,55,2,10,NULL),(284,2,'2022-02-22 03:31:23.388094','Placed','razorpay',3936,22,3,2,NULL),(285,4,'2022-02-22 03:31:23.406908','Placed','razorpay',10392,22,4,2,NULL),(286,2,'2022-02-22 03:33:02.156906','Placed','razorpay',3542,20,3,2,NULL),(287,2,'2022-02-22 03:33:02.176093','Placed','razorpay',6447,20,4,2,NULL),(289,1,'2022-02-22 03:35:42.146675','Placed','cash_on_delivery',1968,21,3,2,NULL),(290,1,'2022-02-22 03:37:42.529351','Placed','cash_on_delivery',1968,21,3,2,NULL),(291,1,'2022-02-22 03:39:42.863778','Placed','cash_on_delivery',1968,21,3,2,NULL),(292,1,'2022-02-22 03:41:31.820833','Placed','cash_on_delivery',1968,21,3,2,NULL),(293,1,'2022-02-22 03:41:32.885022','Placed','cash_on_delivery',1968,21,3,2,NULL),(294,1,'2022-02-22 03:41:33.283437','Placed','cash_on_delivery',1968,21,3,2,NULL),(295,1,'2022-02-22 03:41:33.620160','Placed','cash_on_delivery',1968,21,3,2,NULL),(296,1,'2022-02-22 03:41:33.960174','Placed','cash_on_delivery',1968,21,3,2,NULL),(297,1,'2022-02-22 03:41:40.889811','Placed','cash_on_delivery',1968,21,3,2,NULL),(298,1,'2022-02-22 03:41:41.820731','Placed','cash_on_delivery',1968,21,3,2,NULL),(299,1,'2022-02-22 03:41:42.193384','Placed','cash_on_delivery',1968,21,3,2,NULL),(300,1,'2022-02-22 03:41:42.559927','Placed','cash_on_delivery',1968,21,3,2,NULL),(301,1,'2022-02-22 03:41:42.880968','Placed','cash_on_delivery',1968,21,3,2,NULL),(302,1,'2022-02-22 03:41:43.244625','Placed','cash_on_delivery',1968,21,3,2,NULL),(303,1,'2022-02-22 03:42:06.271342','Shipped','cash_on_delivery',1968,21,3,2,NULL),(304,1,'2022-02-22 03:42:24.933738','Placed','cash_on_delivery',1968,21,3,2,NULL),(305,1,'2022-02-22 03:44:25.296822','Placed','cash_on_delivery',1968,21,3,2,NULL),(306,1,'2022-02-22 03:46:25.604341','Placed','cash_on_delivery',1968,21,3,2,NULL),(307,2,'2022-02-22 03:47:50.391633','Placed','razorpay',2504,22,2,2,NULL),(309,1,'2022-02-22 03:48:27.084626','Placed','razorpay',1026,22,2,2,NULL),(311,1,'2022-02-22 03:48:59.090770','Shipped','paypal',1968,22,3,2,NULL),(312,1,'2022-02-22 03:49:56.576734','cancelled','paypal',1252,25,2,2,NULL),(313,2,'2022-02-22 04:10:19.061156','Shipped','razorpay',2504,20,2,2,NULL),(314,2,'2022-02-22 04:10:19.078312','Shipped','razorpay',5732,20,4,2,NULL),(315,1,'2022-02-22 04:10:19.093228','Placed','razorpay',6904,20,5,2,NULL),(316,1,'2022-02-22 04:14:38.078266','Shipped','razorpay',1172,21,5,2,NULL),(317,1,'2022-02-22 04:15:04.064869','Placed','razorpay',1172,21,5,2,NULL),(318,1,'2022-02-22 04:17:38.423974','Placed','razorpay',1968,21,3,2,NULL),(319,1,'2022-02-22 08:18:35.231416','Placed','razorpay',1968,56,3,16,NULL),(320,3,'2022-02-22 08:19:28.963832','Placed','razorpay',5904,56,3,16,NULL),(321,1,'2022-02-22 08:24:41.711469','Placed','razorpay',1968,56,3,16,NULL),(322,1,'2022-02-22 08:42:28.352517','Placed','razorpay',1252,56,2,16,NULL),(323,1,'2022-02-22 08:43:47.730707','Placed','razorpay',1252,56,2,16,NULL),(324,1,'2022-02-22 08:45:09.681679','Placed','razorpay',1252,56,2,16,NULL),(325,2,'2022-02-22 08:45:58.243847','Placed','razorpay',3936,56,3,16,NULL),(326,2,'2022-02-22 09:12:52.587375','Placed','razorpay',3936,56,3,16,NULL),(327,1,'2022-02-22 09:30:20.172345','Placed','razorpay',1252,57,2,17,NULL),(328,1,'2022-02-22 09:37:11.363314','Placed','razorpay',1968,57,3,17,NULL),(329,1,'2022-02-22 09:43:21.392476','Placed','razorpay',1968,57,3,17,NULL),(330,1,'2022-02-22 09:45:45.037010','Placed','razorpay',1968,57,3,17,NULL),(331,1,'2022-02-22 09:47:40.015248','Placed','razorpay',1968,57,3,17,NULL),(332,1,'2022-02-22 10:03:50.480260','Placed','razorpay',1968,21,3,2,NULL),(333,1,'2022-02-22 10:04:40.675521','Placed','razorpay',1614,22,4,2,NULL),(334,1,'2022-02-22 10:14:42.328199','Placed','razorpay',1968,22,3,2,NULL),(335,1,'2022-02-22 10:15:26.298567','Placed','razorpay',1968,22,3,2,NULL),(336,1,'2022-02-22 10:15:47.992972','Placed','razorpay',1968,22,3,2,NULL),(337,1,'2022-02-22 10:22:41.640716','Placed','razorpay',1968,22,3,2,NULL),(338,1,'2022-02-22 10:26:44.336118','Placed','razorpay',1252,22,2,2,NULL),(339,1,'2022-02-22 10:27:20.315648','Placed','cash_on_delivery',1252,21,2,2,NULL),(340,1,'2022-02-22 10:29:06.701598','Placed','cash_on_delivery',1252,39,2,2,NULL),(341,1,'2022-02-22 10:29:31.246311','Placed','cash_on_delivery',1252,25,2,2,NULL),(342,1,'2022-02-22 10:31:31.660366','Placed','cash_on_delivery',1252,25,2,2,NULL),(343,1,'2022-02-22 10:32:15.024956','Placed','razorpay',1968,22,3,2,NULL),(344,1,'2022-02-22 10:35:03.496350','Placed','razorpay',1252,20,2,2,NULL),(345,1,'2022-02-22 10:36:12.816583','Placed','razorpay',1968,22,3,2,NULL),(346,1,'2022-02-22 10:38:37.738570','Placed','razorpay',1613,22,3,2,NULL),(347,1,'2022-02-22 10:42:01.937276','Placed','razorpay',1252,22,2,2,NULL),(348,1,'2022-02-22 10:42:47.221801','Placed','razorpay',1968,22,3,2,NULL),(349,1,'2022-02-22 10:46:37.665910','Placed','razorpay',1614,20,4,2,NULL),(350,1,'2022-02-22 10:48:48.438639','Placed','razorpay',1968,22,3,2,NULL),(351,1,'2022-02-22 10:50:48.776349','Placed','razorpay',1,22,3,2,NULL),(352,1,'2022-02-22 10:50:48.792443','cancelled','razorpay',1,22,4,2,NULL),(353,1,'2022-02-22 10:51:23.843087','Placed','razorpay',1019,21,5,2,NULL),(354,2,'2022-02-22 10:52:14.023749','Placed','razorpay',3936,22,3,2,NULL),(355,1,'2022-02-22 10:56:50.281694','Placed','razorpay',1252,22,2,2,NULL),(356,2,'2022-02-22 10:58:50.750372','cancelled','razorpay',3228,22,4,2,NULL),(357,1,'2022-02-22 11:00:51.357020','Placed','razorpay',1968,22,3,2,NULL),(358,1,'2022-02-22 11:01:36.116470','Placed','razorpay',1614,22,4,2,NULL),(359,1,'2022-02-22 11:02:02.901652','Placed','razorpay',1968,22,3,2,NULL),(360,1,'2022-02-22 11:02:51.842536','cancelled','razorpay',1968,22,3,2,NULL),(361,1,'2022-02-22 11:04:04.159447','Placed','razorpay',1968,22,3,2,NULL),(362,1,'2022-02-22 11:04:44.692373','Placed','razorpay',1968,22,3,2,NULL),(363,1,'2022-02-22 11:04:52.237477','Placed','razorpay',1968,22,3,2,NULL),(364,1,'2022-02-22 11:12:11.129194','Placed','razorpay',1771,22,3,2,NULL),(365,1,'2022-02-22 11:13:33.643266','Placed','cash_on_delivery',1968,22,3,2,NULL),(366,1,'2022-02-22 11:14:44.660565','Placed','razorpay',1614,22,4,2,NULL),(367,1,'2022-02-22 11:15:20.776652','cancelled','razorpay',1968,22,3,2,NULL),(368,1,'2022-02-22 11:16:13.879700','Placed','paypal',1252,22,2,2,NULL),(370,1,'2022-02-22 11:58:54.283405','Placed','cash_on_delivery',1614,22,4,2,NULL),(371,1,'2022-02-22 11:59:25.231368','Placed','cash_on_delivery',1968,22,3,2,NULL),(372,1,'2022-02-22 12:01:25.642217','Placed','cash_on_delivery',1968,22,3,2,NULL),(373,1,'2022-02-22 12:01:39.769103','Placed','cash_on_delivery',1968,22,3,2,NULL),(374,1,'2022-02-22 12:02:14.384130','Placed','razorpay',1614,22,4,2,NULL),(375,1,'2022-02-22 12:02:40.561109','cancelled','paypal',1614,22,4,2,NULL),(376,1,'2022-02-22 12:05:39.951559','Placed','razorpay',1968,22,3,2,NULL),(377,1,'2022-02-22 12:05:39.978130','cancelled','razorpay',5188,22,2,2,NULL),(378,1,'2022-02-22 12:06:06.616339','Placed','razorpay',1968,22,3,2,NULL),(379,1,'2022-02-22 12:06:50.588622','cancelled','razorpay',1968,22,3,2,NULL),(380,1,'2022-02-22 12:07:47.082336','Placed','cash_on_delivery',1968,22,3,2,NULL),(381,1,'2022-02-22 12:08:11.309615','Placed','paypal',1968,22,3,2,NULL),(382,1,'2022-02-22 12:08:41.566870','Placed','razorpay',1614,22,4,2,NULL),(383,1,'2022-02-22 12:10:07.359529','Placed','razorpay',1672,22,3,2,NULL),(384,1,'2022-02-22 12:10:50.025280','Placed','razorpay',1672,22,3,2,NULL),(385,1,'2022-02-22 12:12:40.263406','Placed','razorpay',1771,22,3,2,NULL),(386,1,'2022-02-22 12:13:35.491622','Placed','razorpay',1771,22,3,2,NULL),(387,1,'2022-02-22 12:14:47.511354','Placed','cash_on_delivery',1614,22,4,2,NULL),(388,1,'2022-02-22 12:15:36.870364','Placed','paypal',1614,22,4,2,NULL),(389,1,'2022-02-22 12:16:15.216190','Placed','razorpay',1614,25,4,2,NULL),(390,1,'2022-02-22 12:42:51.569109','Placed','razorpay',1614,22,4,2,NULL),(391,1,'2022-02-22 12:43:05.883249','Placed','razorpay',1614,22,4,2,NULL),(392,1,'2022-02-22 12:43:48.259160','Placed','razorpay',1172,22,5,2,NULL),(393,1,'2022-02-22 12:44:24.344552','Placed','razorpay',1614,22,4,2,NULL),(394,1,'2022-02-22 12:44:48.200634','Placed','cash_on_delivery',1172,22,5,2,NULL),(395,1,'2022-02-22 12:45:24.735682','Placed','paypal',1172,22,5,2,NULL),(396,1,'2022-02-22 12:46:08.213979','Placed','razorpay',1172,22,5,2,NULL),(398,1,'2022-02-22 12:46:50.297797','Placed','paypal',1172,22,5,2,NULL),(399,1,'2022-02-22 12:47:28.510011','Placed','razorpay',1172,22,5,2,NULL),(400,1,'2022-02-22 12:49:08.943055','Placed','razorpay',1452,22,4,2,NULL),(401,1,'2022-02-22 12:49:56.563533','Placed','paypal',1172,21,5,2,NULL),(402,1,'2022-02-22 12:50:16.004210','Placed','cash_on_delivery',1172,22,5,2,NULL),(403,1,'2022-02-22 17:37:56.456981','Placed','razorpay',1771,58,3,18,NULL),(406,1,'2022-02-22 17:44:23.233306','Placed','paypal',1968,58,3,18,NULL),(407,1,'2022-02-22 17:45:20.666671','Placed','razorpay',1172,58,5,18,NULL),(409,1,'2022-02-22 17:50:48.740034','Placed','razorpay',1172,58,5,18,NULL),(414,1,'2022-02-22 18:04:15.536379','Placed','paypal',1614,58,4,18,NULL),(415,1,'2022-02-22 18:11:07.487604','Placed','paypal',1968,58,3,18,NULL),(416,1,'2022-02-22 18:13:23.922187','Placed','razorpay',1771,58,3,18,NULL),(417,1,'2022-02-22 18:15:38.158233','Placed','paypal',1968,58,3,18,NULL),(418,1,'2022-02-22 18:16:17.466945','Placed','cash_on_delivery',1614,58,4,18,NULL),(419,1,'2022-02-22 18:25:45.933952','Placed','paypal',1614,58,4,18,NULL),(421,1,'2022-02-22 18:28:43.070792','Placed','paypal',1172,58,5,18,NULL),(422,1,'2022-02-22 18:32:10.788773','Placed','cash_on_delivery',1968,58,3,18,NULL),(424,1,'2022-02-22 18:36:25.693693','Placed','razorpay',1054,58,5,18,NULL),(425,1,'2022-02-22 18:37:08.488530','Placed','razorpay',1172,58,5,18,NULL),(426,1,'2022-02-22 18:39:22.244322','Placed','razorpay',1452,58,4,18,NULL),(427,2,'2022-02-23 02:32:04.751613','Placed','razorpay',2003,58,2,18,NULL),(428,1,'2022-02-23 02:32:52.357733','Placed','razorpay',1291,58,4,18,NULL),(429,1,'2022-02-23 02:34:25.781899','Placed','razorpay',1574,58,3,18,NULL),(430,1,'2022-02-23 02:47:31.502697','Placed','razorpay',1968,58,3,18,NULL),(431,1,'2022-02-23 02:48:30.176191','Placed','razorpay',1968,58,3,18,NULL),(432,1,'2022-02-23 02:49:03.726576','Placed','razorpay',1614,58,4,18,NULL),(433,1,'2022-02-23 02:50:26.587903','Placed','paypal',1172,58,5,18,NULL),(434,1,'2022-02-23 02:51:00.434375','Placed','paypal',1172,58,5,18,NULL),(435,1,'2022-02-23 02:51:28.414181','Placed','cash_on_delivery',1172,58,5,18,NULL),(436,1,'2022-02-23 02:52:41.670659','Placed','razorpay',1614,58,4,18,NULL),(437,1,'2022-02-23 02:53:27.326783','Placed','cash_on_delivery',1172,58,5,18,NULL),(439,2,'2022-02-23 02:58:03.033565','Placed','razorpay',13264,58,5,18,NULL),(441,3,'2022-02-23 03:00:53.012607','Placed','razorpay',3516,58,5,18,NULL),(442,1,'2022-02-23 03:01:39.572517','Placed','razorpay',1614,58,4,18,NULL),(443,1,'2022-02-23 03:02:45.278967','Placed','razorpay',1968,58,3,18,NULL),(444,1,'2022-02-23 03:03:15.798850','Placed','razorpay',1054,58,5,18,NULL),(445,1,'2022-02-23 03:07:25.200635','Placed','razorpay',1968,58,3,18,NULL),(446,1,'2022-02-23 03:07:39.794143','Placed','razorpay',1968,58,3,18,NULL),(448,1,'2022-02-23 03:22:14.777478','Placed','razorpay',1968,58,3,18,NULL),(449,3,'2022-02-23 05:34:53.615356','Placed','razorpay',5904,31,3,5,NULL),(451,1,'2022-02-23 05:36:46.273134','Placed','cash_on_delivery',1968,32,3,5,NULL),(452,1,'2022-02-23 05:37:09.925303','Placed','cash_on_delivery',2780,32,15,5,NULL),(453,1,'2022-02-23 05:38:06.932598','Placed','razorpay',1771,32,3,5,NULL),(454,1,'2022-02-23 05:38:36.269555','Placed','razorpay',1172,31,5,5,NULL),(455,1,'2022-02-23 05:39:34.222623','Placed','paypal',1968,32,3,5,NULL),(456,1,'2022-02-23 05:40:10.562158','Placed','paypal',1968,32,3,5,NULL),(457,1,'2022-02-23 05:41:04.686038','Placed','razorpay',1566,32,2,5,NULL),(458,1,'2022-02-23 05:42:06.815339','Placed','razorpay',1172,32,5,5,NULL),(459,1,'2022-02-23 05:43:06.361112','Placed','razorpay',1968,32,3,5,NULL),(460,1,'2022-02-23 05:44:39.494499','Placed','razorpay',1614,32,4,5,NULL),(461,1,'2022-02-23 05:45:15.956050','Placed','paypal',1172,49,5,5,NULL),(462,1,'2022-02-23 05:47:16.555982','Placed','paypal',1172,49,5,5,NULL),(463,1,'2022-02-23 05:49:16.926307','Placed','paypal',1172,49,5,5,NULL),(464,1,'2022-02-23 05:51:17.350471','Placed','paypal',1172,49,5,5,NULL),(466,1,'2022-02-23 05:55:50.695430','Placed','razorpay',1968,32,3,5,NULL),(467,1,'2022-02-23 05:55:50.712843','Placed','razorpay',5550,32,4,5,NULL),(468,1,'2022-02-23 06:13:10.373558','Placed','razorpay',1771,30,3,5,73),(469,1,'2022-02-23 06:13:10.391761','Placed','razorpay',4774,30,2,5,73),(470,1,'2022-02-23 06:21:10.875338','Placed','razorpay',1968,31,3,5,72);
/*!40000 ALTER TABLE `app_order_place` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app_user_details`
--

DROP TABLE IF EXISTS `app_user_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `app_user_details` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `locality` varchar(100) NOT NULL,
  `city` varchar(100) NOT NULL,
  `pincode` int NOT NULL,
  `state` varchar(100) NOT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `app_user_details_user_id_f417e019_fk_app_customuser_id` (`user_id`),
  CONSTRAINT `app_user_details_user_id_f417e019_fk_app_customuser_id` FOREIGN KEY (`user_id`) REFERENCES `app_customuser` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=59 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_user_details`
--

LOCK TABLES `app_user_details` WRITE;
/*!40000 ALTER TABLE `app_user_details` DISABLE KEYS */;
INSERT INTO `app_user_details` VALUES (20,'ABCD Building1','Kannur',4567856,'kerala',2),(21,'ABCD Building188888','Kannur',4567856,'kerala',2),(22,'ABCD Building1e','Kannur',4567856,'kerala',2),(23,'ABCD Building1e','Kannur',4567856,'kerala',2),(24,'ABCD Building1e','Kannur',4567856,'kerala',2),(25,'ABCD Building1e','Kannur',4567856,'kerala',2),(26,'ABCD Building1rrrrrrrr','Kannur',4567856,'kerala',2),(27,'qqqqqqqqqqq','wwwwwwww',66666,'kerala',4),(28,'ABCD Building1','Kannur',4567856,'kerala',4),(29,'ABCD Building1','Kannur',4567856,'kerala',4),(30,'ABCD Building1','Kannur',4567856,'kerala',5),(31,'ABCD Building1','Kannur',4567856,'',5),(32,'dddddd','Kakkkkk',5678987,'',5),(33,'ABCD Building1','Kannur',4567856,'kerala',5),(34,'ABCD Building1','Kannur',4567856,'kerala',2),(35,'Thommi Thaze','Kannirapally',686506,'Kerala',6),(36,'Cheriyanolickal','payavoor',670633,'kerala',7),(37,'qqqqqq','kollam',691510,'kerala',8),(38,'mmmmmmmmmmmmmm','Kannur',4567856,'kerala',5),(39,'bbbbbbbbbbbbbb3eee','Kazhikod',5678987,'kerala',2),(40,'ABCD Buildingeee','Kannur',4567856,'kerala',2),(41,'ertysd','Eranakulam',45678,'kerala',2),(42,'ABCD Building1','rty',252,'rtyu',2),(43,'ABCD Building1','Kazhikod',5678987,'kerala',2),(44,'ertysd','Eranakulam',45678,'kerala',2),(45,'ABCD Building1','Kazhikod',5678987,'kerala',2),(46,'ABCD Building1','Kannur',4567856,'kerala',2),(47,'Abhijith2','Kazhikod',5678987,'kerala',2),(48,'ABCD Building121','Kannur',456785633,'kerala',2),(49,'ABCD Building1','Kazhikod',5678987,'kerala',5),(50,'ABCD Building1','Eranakulam',45678,'kerala',5),(52,'padamugal','erannakulam',1678,'kerala',9),(55,'ABCD Building11111111111','Eranakulam',45678,'kerala',10),(56,'ABCD Building1','Kannur',4567856,'kerala',16),(57,'bbbbbbbbbbbbbb3','Kazhikod',5678987,'kerala',17),(58,'padamugal house','kochi',67893,'kerala',18);
/*!40000 ALTER TABLE `app_user_details` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app_wishlist_data`
--

DROP TABLE IF EXISTS `app_wishlist_data`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `app_wishlist_data` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `products_id` bigint NOT NULL,
  `user_id` bigint DEFAULT NULL,
  `guest` varchar(300) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `app_wishlist_data_products_id_1b4c1b2b_fk_dash_product_id` (`products_id`),
  KEY `app_wishlist_data_user_id_2d91eb63_fk_app_customuser_id` (`user_id`),
  CONSTRAINT `app_wishlist_data_products_id_1b4c1b2b_fk_dash_product_id` FOREIGN KEY (`products_id`) REFERENCES `dash_product` (`id`),
  CONSTRAINT `app_wishlist_data_user_id_2d91eb63_fk_app_customuser_id` FOREIGN KEY (`user_id`) REFERENCES `app_customuser` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_wishlist_data`
--

LOCK TABLES `app_wishlist_data` WRITE;
/*!40000 ALTER TABLE `app_wishlist_data` DISABLE KEYS */;
/*!40000 ALTER TABLE `app_wishlist_data` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=65 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add content type',4,'add_contenttype'),(14,'Can change content type',4,'change_contenttype'),(15,'Can delete content type',4,'delete_contenttype'),(16,'Can view content type',4,'view_contenttype'),(17,'Can add session',5,'add_session'),(18,'Can change session',5,'change_session'),(19,'Can delete session',5,'delete_session'),(20,'Can view session',5,'view_session'),(21,'Can add user',6,'add_customuser'),(22,'Can change user',6,'change_customuser'),(23,'Can delete user',6,'delete_customuser'),(24,'Can view user',6,'view_customuser'),(25,'Can add wishlist_data',7,'add_wishlist_data'),(26,'Can change wishlist_data',7,'change_wishlist_data'),(27,'Can delete wishlist_data',7,'delete_wishlist_data'),(28,'Can view wishlist_data',7,'view_wishlist_data'),(29,'Can add user_details',8,'add_user_details'),(30,'Can change user_details',8,'change_user_details'),(31,'Can delete user_details',8,'delete_user_details'),(32,'Can view user_details',8,'view_user_details'),(33,'Can add order_place',9,'add_order_place'),(34,'Can change order_place',9,'change_order_place'),(35,'Can delete order_place',9,'delete_order_place'),(36,'Can view order_place',9,'view_order_place'),(37,'Can add cartproduct',10,'add_cartproduct'),(38,'Can change cartproduct',10,'change_cartproduct'),(39,'Can delete cartproduct',10,'delete_cartproduct'),(40,'Can view cartproduct',10,'view_cartproduct'),(41,'Can add ads',11,'add_ads'),(42,'Can change ads',11,'change_ads'),(43,'Can delete ads',11,'delete_ads'),(44,'Can view ads',11,'view_ads'),(45,'Can add category',12,'add_category'),(46,'Can change category',12,'change_category'),(47,'Can delete category',12,'delete_category'),(48,'Can view category',12,'view_category'),(49,'Can add product',13,'add_product'),(50,'Can change product',13,'change_product'),(51,'Can delete product',13,'delete_product'),(52,'Can view product',13,'view_product'),(53,'Can add brand',14,'add_brand'),(54,'Can change brand',14,'change_brand'),(55,'Can delete brand',14,'delete_brand'),(56,'Can view brand',14,'view_brand'),(57,'Can add buyproduct',15,'add_buyproduct'),(58,'Can change buyproduct',15,'change_buyproduct'),(59,'Can delete buyproduct',15,'delete_buyproduct'),(60,'Can view buyproduct',15,'view_buyproduct'),(61,'Can add coupon',16,'add_coupon'),(62,'Can change coupon',16,'change_coupon'),(63,'Can delete coupon',16,'delete_coupon'),(64,'Can view coupon',16,'view_coupon');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dash_ads`
--

DROP TABLE IF EXISTS `dash_ads`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dash_ads` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `homeimage` varchar(100) NOT NULL,
  `homeimage1` varchar(100) NOT NULL,
  `menimage` varchar(100) NOT NULL,
  `menimage1` varchar(100) NOT NULL,
  `womenimage` varchar(100) NOT NULL,
  `womenimage1` varchar(100) NOT NULL,
  `sportsimage` varchar(100) NOT NULL,
  `sportsimage1` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dash_ads`
--

LOCK TABLES `dash_ads` WRITE;
/*!40000 ALTER TABLE `dash_ads` DISABLE KEYS */;
/*!40000 ALTER TABLE `dash_ads` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dash_brand`
--

DROP TABLE IF EXISTS `dash_brand`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dash_brand` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dash_brand`
--

LOCK TABLES `dash_brand` WRITE;
/*!40000 ALTER TABLE `dash_brand` DISABLE KEYS */;
INSERT INTO `dash_brand` VALUES (4,'Fast Track'),(7,'Fossil'),(6,'Maxima'),(3,'Reebok'),(1,'SONATA'),(2,'TIMEX'),(5,'TITAN');
/*!40000 ALTER TABLE `dash_brand` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dash_category`
--

DROP TABLE IF EXISTS `dash_category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dash_category` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `category_offer` int unsigned DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  CONSTRAINT `dash_category_chk_1` CHECK ((`category_offer` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dash_category`
--

LOCK TABLES `dash_category` WRITE;
/*!40000 ALTER TABLE `dash_category` DISABLE KEYS */;
INSERT INTO `dash_category` VALUES (1,'MEN',0),(2,'WOMEN',15),(3,'SPORTS',9);
/*!40000 ALTER TABLE `dash_category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dash_product`
--

DROP TABLE IF EXISTS `dash_product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dash_product` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `price` int unsigned NOT NULL,
  `stock` int unsigned NOT NULL,
  `image` varchar(100) NOT NULL,
  `image1` varchar(100) NOT NULL,
  `image2` varchar(100) NOT NULL,
  `category_id` bigint DEFAULT NULL,
  `brand_id` bigint DEFAULT NULL,
  `product_offer` int unsigned DEFAULT NULL,
  `discount_price` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `dash_product_category_id_49bbcebb_fk_dash_category_id` (`category_id`),
  KEY `dash_product_brand_id_2710eae9_fk_dash_brand_id` (`brand_id`),
  CONSTRAINT `dash_product_brand_id_2710eae9_fk_dash_brand_id` FOREIGN KEY (`brand_id`) REFERENCES `dash_brand` (`id`),
  CONSTRAINT `dash_product_category_id_49bbcebb_fk_dash_category_id` FOREIGN KEY (`category_id`) REFERENCES `dash_category` (`id`),
  CONSTRAINT `dash_product_chk_1` CHECK ((`price` >= 0)),
  CONSTRAINT `dash_product_chk_2` CHECK ((`stock` >= 0)),
  CONSTRAINT `dash_product_chk_3` CHECK ((`product_offer` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dash_product`
--

LOCK TABLES `dash_product` WRITE;
/*!40000 ALTER TABLE `dash_product` DISABLE KEYS */;
INSERT INTO `dash_product` VALUES (2,'Tees Analog',1566,91,'media/61FFBTzKiUL._UL1500__2Pshjoe.jpg','media/51SvUDjCQJL._UL1500_.jpg','media/61Fn1C65YL._UL1500__MAgPqcL.jpg',1,4,0,1566),(3,'Smartwatch',2344,32,'media/615fBi41SoL._SL1500__wbfnZCf.jpg','media/61obhxFq2rL._UL1500_.jpg','media/61uBp1muxeL._SL1500_.jpg',3,5,16,1968),(4,'Michael Kors',1899,29,'media/indian-rishtey-present-black-hours-represent-numerical-daniel-original-imaft29p2a_gquWigc.jpeg','media/indian-rishtey-present-black-hours-represent-numerical-daniel-original-imafjmzw97zkabzd.jpeg','media/original-dusk-1142-bk-skmei-original-imafw3ah2vhmgmh8_Jp1qYj0.jpeg',2,2,13,1614),(5,'Daniel Klein',1379,68,'media/71f3p9MEMnL._UL1500_.jpg','media/71iAOoWUoL._UL1500_.jpg','media/819jP1kB0UL._UL1500_.jpg',2,2,4,1172),(14,'LED-SQ YOUTH CLUB',1800,32,'media/digital-watch-for-boys-virani-enterprise-original-imagyf7gxuuxvefy.jpeg','media/luxurious-fashion-silicone-black-colored-led-dail-watch-for-kids-original-imafzhy_EoytWdO.jpeg','media/digital-watch-for-boys-virani-enterprise-original-imagyf7gfb5vzkws_Jz1DnN4.jpeg',3,3,20,1440),(15,'KL-1C',2780,67,'media/kl-1c-killer-original-imag4gwsya4esygr.jpeg','media/kl-1c-killer-original-imag4gwsfjnbphhv.jpeg','media/kl-1c-killer-original-imag4gwstyzzdcfy.jpeg',1,6,0,2780),(16,'Stylish Square',2630,55,'media/1-stylish-square-dial-smooth-silicon-strap-addi-stylish-designer-original-imag6fh_rAfB8bn.jpeg','media/1-stylish-square-dial-smooth-silicon-strap-addi-stylish-designer-original-imag6fh_EzlnakX.jpeg','media/stylish-square-dial-smooth-silicon-strap-addi-stylish-designer-original-imag5yhntdejfgua.jpeg',1,1,0,NULL),(18,'ANLG-448-BLACK-BLK',3456,89,'media/anlg-448-black-blk-analogue-original-imag3uxbqxkwvdep.jpeg','media/anlg-448-black-blk-analogue-original-imag3uxbd5jcy3z5.jpeg','media/anlg-448-black-blk-analogue-original-imafvdhzzxrzzyvc.jpeg',1,3,0,3456),(19,'P-W 5107',3455,78,'media/p-w-5107-papio-original-imafz534e4yyew66.jpeg','media/p-w-5107-papio-original-imafz534fpszh4y8.jpeg','media/p-w-5107-papio-original-imagyv82yfjperwf.jpeg',2,7,0,2936),(20,'K021 Flower',2340,78,'media/k021-flower-design-on-dial-and-strap-unique-watch-for-women-original-imafnqytmb9qyygv.jpeg','media/new-facy-flower-printed-rubber-strap-ideal-watch-for-women-knack-original-imafqf9_yz1mJ7e.jpeg','media/ac0316-spinoza-original-imafderjwrypb8hz.jpeg',2,1,0,1989),(21,'KNACK',5290,78,'media/all-black-fashion-watch-unique-time-indicator-dail-soft-durable-original-imafvusrhawt4znw.jpeg','media/stylish-silicone-stap-comfortable-to-wear-watch-knack-original-imafw9zhf4stwayt_pAjyvc1.jpeg','media/s-006-full-black-matrix-luxurios-collection-stylish-silicone-original-imafnhxgmcefdsxg.jpeg',3,3,0,4813);
/*!40000 ALTER TABLE `dash_product` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_app_customuser_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_app_customuser_id` FOREIGN KEY (`user_id`) REFERENCES `app_customuser` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=184 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2022-02-17 05:14:15.713241','9','Coupon object (9)',3,'',16,1),(2,'2022-02-17 05:14:15.718220','8','Coupon object (8)',3,'',16,1),(3,'2022-02-17 05:14:15.723945','7','Coupon object (7)',3,'',16,1),(4,'2022-02-17 05:14:15.727127','6','Coupon object (6)',3,'',16,1),(5,'2022-02-17 05:14:15.731000','5','Coupon object (5)',3,'',16,1),(6,'2022-02-17 05:14:15.734859','4','Coupon object (4)',3,'',16,1),(7,'2022-02-17 05:14:15.739675','3','Coupon object (3)',3,'',16,1),(8,'2022-02-17 05:14:15.746684','2','Coupon object (2)',3,'',16,1),(9,'2022-02-17 05:14:15.750383','1','Coupon object (1)',3,'',16,1),(10,'2022-02-19 02:51:59.125802','193','order_place object (193)',3,'',9,1),(11,'2022-02-19 02:51:59.130479','189','order_place object (189)',3,'',9,1),(12,'2022-02-19 02:51:59.134813','188','order_place object (188)',3,'',9,1),(13,'2022-02-19 02:51:59.141358','187','order_place object (187)',3,'',9,1),(14,'2022-02-19 02:51:59.145704','186','order_place object (186)',3,'',9,1),(15,'2022-02-19 02:51:59.151575','185','order_place object (185)',3,'',9,1),(16,'2022-02-19 02:51:59.160890','184','order_place object (184)',3,'',9,1),(17,'2022-02-19 02:51:59.165941','183','order_place object (183)',3,'',9,1),(18,'2022-02-19 02:51:59.171153','182','order_place object (182)',3,'',9,1),(19,'2022-02-19 02:51:59.175191','180','order_place object (180)',3,'',9,1),(20,'2022-02-19 02:51:59.179513','179','order_place object (179)',3,'',9,1),(21,'2022-02-19 02:51:59.185497','178','order_place object (178)',3,'',9,1),(22,'2022-02-19 02:51:59.190427','177','order_place object (177)',3,'',9,1),(23,'2022-02-19 02:51:59.194360','176','order_place object (176)',3,'',9,1),(24,'2022-02-19 02:51:59.197918','175','order_place object (175)',3,'',9,1),(25,'2022-02-19 02:51:59.203022','174','order_place object (174)',3,'',9,1),(26,'2022-02-19 02:51:59.208286','173','order_place object (173)',3,'',9,1),(27,'2022-02-19 02:51:59.212487','172','order_place object (172)',3,'',9,1),(28,'2022-02-19 02:51:59.218347','171','order_place object (171)',3,'',9,1),(29,'2022-02-19 02:51:59.227423','170','order_place object (170)',3,'',9,1),(30,'2022-02-19 02:51:59.234833','169','order_place object (169)',3,'',9,1),(31,'2022-02-19 02:51:59.242872','168','order_place object (168)',3,'',9,1),(32,'2022-02-19 02:51:59.248389','162','order_place object (162)',3,'',9,1),(33,'2022-02-19 02:51:59.253647','157','order_place object (157)',3,'',9,1),(34,'2022-02-19 02:51:59.258307','156','order_place object (156)',3,'',9,1),(35,'2022-02-19 02:51:59.261842','154','order_place object (154)',3,'',9,1),(36,'2022-02-19 02:51:59.267892','153','order_place object (153)',3,'',9,1),(37,'2022-02-19 02:51:59.272246','152','order_place object (152)',3,'',9,1),(38,'2022-02-19 02:51:59.275506','151','order_place object (151)',3,'',9,1),(39,'2022-02-19 02:51:59.280310','150','order_place object (150)',3,'',9,1),(40,'2022-02-19 02:51:59.286103','149','order_place object (149)',3,'',9,1),(41,'2022-02-19 02:51:59.290662','148','order_place object (148)',3,'',9,1),(42,'2022-02-19 02:51:59.293794','147','order_place object (147)',3,'',9,1),(43,'2022-02-19 02:51:59.297078','146','order_place object (146)',3,'',9,1),(44,'2022-02-19 02:51:59.301519','145','order_place object (145)',3,'',9,1),(45,'2022-02-19 02:51:59.305960','144','order_place object (144)',3,'',9,1),(46,'2022-02-19 02:51:59.312879','143','order_place object (143)',3,'',9,1),(47,'2022-02-19 02:51:59.318595','142','order_place object (142)',3,'',9,1),(48,'2022-02-19 02:51:59.324101','141','order_place object (141)',3,'',9,1),(49,'2022-02-19 02:51:59.328189','140','order_place object (140)',3,'',9,1),(50,'2022-02-19 02:51:59.332635','139','order_place object (139)',3,'',9,1),(51,'2022-02-19 02:51:59.336851','138','order_place object (138)',3,'',9,1),(52,'2022-02-19 02:51:59.340359','137','order_place object (137)',3,'',9,1),(53,'2022-02-19 02:51:59.343926','136','order_place object (136)',3,'',9,1),(54,'2022-02-19 02:51:59.348539','135','order_place object (135)',3,'',9,1),(55,'2022-02-19 02:51:59.352031','134','order_place object (134)',3,'',9,1),(56,'2022-02-19 02:51:59.355696','133','order_place object (133)',3,'',9,1),(57,'2022-02-19 02:51:59.360326','132','order_place object (132)',3,'',9,1),(58,'2022-02-19 02:51:59.364609','131','order_place object (131)',3,'',9,1),(59,'2022-02-19 02:51:59.370038','130','order_place object (130)',3,'',9,1),(60,'2022-02-19 02:51:59.373874','129','order_place object (129)',3,'',9,1),(61,'2022-02-19 02:51:59.377447','128','order_place object (128)',3,'',9,1),(62,'2022-02-19 02:51:59.381082','127','order_place object (127)',3,'',9,1),(63,'2022-02-19 02:51:59.385743','126','order_place object (126)',3,'',9,1),(64,'2022-02-19 02:51:59.391539','125','order_place object (125)',3,'',9,1),(65,'2022-02-19 02:51:59.395020','124','order_place object (124)',3,'',9,1),(66,'2022-02-19 02:51:59.399683','123','order_place object (123)',3,'',9,1),(67,'2022-02-19 02:51:59.404140','122','order_place object (122)',3,'',9,1),(68,'2022-02-19 02:51:59.410427','120','order_place object (120)',3,'',9,1),(69,'2022-02-19 02:51:59.415359','119','order_place object (119)',3,'',9,1),(70,'2022-02-19 02:51:59.420614','118','order_place object (118)',3,'',9,1),(71,'2022-02-19 02:51:59.424827','117','order_place object (117)',3,'',9,1),(72,'2022-02-19 02:51:59.428681','115','order_place object (115)',3,'',9,1),(73,'2022-02-19 02:51:59.433229','114','order_place object (114)',3,'',9,1),(74,'2022-02-19 02:51:59.437969','109','order_place object (109)',3,'',9,1),(75,'2022-02-19 02:51:59.441678','108','order_place object (108)',3,'',9,1),(76,'2022-02-19 02:51:59.444860','107','order_place object (107)',3,'',9,1),(77,'2022-02-19 02:51:59.448367','105','order_place object (105)',3,'',9,1),(78,'2022-02-19 02:51:59.453609','104','order_place object (104)',3,'',9,1),(79,'2022-02-19 02:51:59.457300','103','order_place object (103)',3,'',9,1),(80,'2022-02-19 02:51:59.460635','101','order_place object (101)',3,'',9,1),(81,'2022-02-19 02:51:59.464343','100','order_place object (100)',3,'',9,1),(82,'2022-02-19 02:51:59.468998','96','order_place object (96)',3,'',9,1),(83,'2022-02-19 02:51:59.473954','94','order_place object (94)',3,'',9,1),(84,'2022-02-19 02:51:59.477654','93','order_place object (93)',3,'',9,1),(85,'2022-02-19 02:51:59.481498','92','order_place object (92)',3,'',9,1),(86,'2022-02-19 02:51:59.484960','90','order_place object (90)',3,'',9,1),(87,'2022-02-19 02:51:59.489041','89','order_place object (89)',3,'',9,1),(88,'2022-02-19 02:51:59.493280','88','order_place object (88)',3,'',9,1),(89,'2022-02-19 02:51:59.496641','87','order_place object (87)',3,'',9,1),(90,'2022-02-19 02:51:59.500364','86','order_place object (86)',3,'',9,1),(91,'2022-02-19 02:51:59.503787','85','order_place object (85)',3,'',9,1),(92,'2022-02-19 02:51:59.507470','84','order_place object (84)',3,'',9,1),(93,'2022-02-19 02:51:59.511185','83','order_place object (83)',3,'',9,1),(94,'2022-02-19 02:51:59.515245','82','order_place object (82)',3,'',9,1),(95,'2022-02-19 02:55:04.366757','202','order_place object (202)',3,'',9,1),(96,'2022-02-19 02:55:04.371865','201','order_place object (201)',3,'',9,1),(97,'2022-02-19 02:55:04.377128','200','order_place object (200)',3,'',9,1),(98,'2022-02-19 02:55:04.381798','199','order_place object (199)',3,'',9,1),(99,'2022-02-19 02:55:04.385581','197','order_place object (197)',3,'',9,1),(100,'2022-02-19 02:55:04.389454','196','order_place object (196)',3,'',9,1),(101,'2022-02-19 02:55:04.393173','194','order_place object (194)',3,'',9,1),(102,'2022-02-19 02:55:04.396574','191','order_place object (191)',3,'',9,1),(103,'2022-02-19 02:55:04.400348','81','order_place object (81)',3,'',9,1),(104,'2022-02-19 02:55:04.404377','80','order_place object (80)',3,'',9,1),(105,'2022-02-19 02:55:04.408174','79','order_place object (79)',3,'',9,1),(106,'2022-02-19 02:55:04.411379','78','order_place object (78)',3,'',9,1),(107,'2022-02-19 02:55:04.416205','77','order_place object (77)',3,'',9,1),(108,'2022-02-19 02:55:04.419974','76','order_place object (76)',3,'',9,1),(109,'2022-02-19 02:55:04.424765','74','order_place object (74)',3,'',9,1),(110,'2022-02-19 02:55:04.428262','73','order_place object (73)',3,'',9,1),(111,'2022-02-19 02:55:04.431433','70','order_place object (70)',3,'',9,1),(112,'2022-02-19 02:55:04.436326','69','order_place object (69)',3,'',9,1),(113,'2022-02-19 02:55:04.440687','67','order_place object (67)',3,'',9,1),(114,'2022-02-19 02:55:04.444697','66','order_place object (66)',3,'',9,1),(115,'2022-02-19 02:55:04.448409','65','order_place object (65)',3,'',9,1),(116,'2022-02-19 02:55:04.452005','64','order_place object (64)',3,'',9,1),(117,'2022-02-19 02:55:04.455946','62','order_place object (62)',3,'',9,1),(118,'2022-02-19 02:55:04.459481','60','order_place object (60)',3,'',9,1),(119,'2022-02-19 02:55:04.463084','58','order_place object (58)',3,'',9,1),(120,'2022-02-19 02:55:04.467701','57','order_place object (57)',3,'',9,1),(121,'2022-02-19 02:55:04.474717','56','order_place object (56)',3,'',9,1),(122,'2022-02-19 02:55:04.479281','54','order_place object (54)',3,'',9,1),(123,'2022-02-19 02:55:04.483965','52','order_place object (52)',3,'',9,1),(124,'2022-02-19 02:55:04.487795','51','order_place object (51)',3,'',9,1),(125,'2022-02-19 02:55:04.492877','50','order_place object (50)',3,'',9,1),(126,'2022-02-19 02:55:04.496924','49','order_place object (49)',3,'',9,1),(127,'2022-02-19 02:55:04.500056','48','order_place object (48)',3,'',9,1),(128,'2022-02-19 02:55:04.503422','46','order_place object (46)',3,'',9,1),(129,'2022-02-19 02:55:04.507995','45','order_place object (45)',3,'',9,1),(130,'2022-02-19 02:55:04.512109','43','order_place object (43)',3,'',9,1),(131,'2022-02-19 02:55:04.516614','42','order_place object (42)',3,'',9,1),(132,'2022-02-19 02:55:04.519786','41','order_place object (41)',3,'',9,1),(133,'2022-02-19 02:55:04.523453','39','order_place object (39)',3,'',9,1),(134,'2022-02-19 02:55:04.528074','37','order_place object (37)',3,'',9,1),(135,'2022-02-19 02:55:04.532157','36','order_place object (36)',3,'',9,1),(136,'2022-02-19 02:55:04.535977','33','order_place object (33)',3,'',9,1),(137,'2022-02-19 02:55:04.540508','31','order_place object (31)',3,'',9,1),(138,'2022-02-19 02:55:04.544411','30','order_place object (30)',3,'',9,1),(139,'2022-02-19 02:55:04.548441','27','order_place object (27)',3,'',9,1),(140,'2022-02-19 02:55:04.553891','26','order_place object (26)',3,'',9,1),(141,'2022-02-19 02:55:04.558508','25','order_place object (25)',3,'',9,1),(142,'2022-02-19 02:55:04.563187','24','order_place object (24)',3,'',9,1),(143,'2022-02-19 02:55:04.567344','23','order_place object (23)',3,'',9,1),(144,'2022-02-19 02:55:04.572233','22','order_place object (22)',3,'',9,1),(145,'2022-02-19 02:55:04.576069','20','order_place object (20)',3,'',9,1),(146,'2022-02-19 02:55:04.579454','19','order_place object (19)',3,'',9,1),(147,'2022-02-19 02:55:04.584072','18','order_place object (18)',3,'',9,1),(148,'2022-02-19 02:55:04.588416','17','order_place object (17)',3,'',9,1),(149,'2022-02-19 02:55:04.592718','16','order_place object (16)',3,'',9,1),(150,'2022-02-19 02:55:04.597297','15','order_place object (15)',3,'',9,1),(151,'2022-02-19 02:55:04.600986','14','order_place object (14)',3,'',9,1),(152,'2022-02-19 02:55:04.605208','13','order_place object (13)',3,'',9,1),(153,'2022-02-19 02:55:04.609989','12','order_place object (12)',3,'',9,1),(154,'2022-02-19 02:55:04.614517','11','order_place object (11)',3,'',9,1),(155,'2022-02-19 02:55:04.617558','10','order_place object (10)',3,'',9,1),(156,'2022-02-19 02:55:04.621177','9','order_place object (9)',3,'',9,1),(157,'2022-02-19 02:55:04.625693','8','order_place object (8)',3,'',9,1),(158,'2022-02-19 02:55:04.629615','6','order_place object (6)',3,'',9,1),(159,'2022-02-19 02:55:04.633864','5','order_place object (5)',3,'',9,1),(160,'2022-02-19 02:55:04.637345','4','order_place object (4)',3,'',9,1),(161,'2022-02-19 02:55:04.643198','3','order_place object (3)',3,'',9,1),(162,'2022-02-19 02:55:04.652060','2','order_place object (2)',3,'',9,1),(163,'2022-02-19 02:55:04.657594','1','order_place object (1)',3,'',9,1),(164,'2022-02-20 17:47:27.708219','219','order_place object (219)',3,'',9,1),(165,'2022-02-20 17:47:27.712373','218','order_place object (218)',3,'',9,1),(166,'2022-02-20 17:47:27.716113','217','order_place object (217)',3,'',9,1),(167,'2022-02-20 17:47:27.719712','216','order_place object (216)',3,'',9,1),(168,'2022-02-20 17:47:27.724737','215','order_place object (215)',3,'',9,1),(169,'2022-02-20 17:47:27.728306','214','order_place object (214)',3,'',9,1),(170,'2022-02-20 17:47:27.732232','213','order_place object (213)',3,'',9,1),(171,'2022-02-20 17:47:27.736036','212','order_place object (212)',3,'',9,1),(172,'2022-02-20 17:47:27.740266','211','order_place object (211)',3,'',9,1),(173,'2022-02-20 17:47:27.743698','210','order_place object (210)',3,'',9,1),(174,'2022-02-20 17:47:27.746840','209','order_place object (209)',3,'',9,1),(175,'2022-02-20 17:47:27.750093','208','order_place object (208)',3,'',9,1),(176,'2022-02-20 17:47:27.755252','207','order_place object (207)',3,'',9,1),(177,'2022-02-20 17:47:27.759685','206','order_place object (206)',3,'',9,1),(178,'2022-02-20 17:47:27.763833','205','order_place object (205)',3,'',9,1),(179,'2022-02-20 17:47:27.767389','204','order_place object (204)',3,'',9,1),(180,'2022-02-20 17:47:27.770531','203','order_place object (203)',3,'',9,1),(181,'2022-02-20 17:47:27.773813','198','order_place object (198)',3,'',9,1),(182,'2022-02-20 17:47:27.779869','68','order_place object (68)',3,'',9,1),(183,'2022-02-20 17:47:27.784723','63','order_place object (63)',3,'',9,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(15,'app','buyproduct'),(10,'app','cartproduct'),(16,'app','coupon'),(6,'app','customuser'),(9,'app','order_place'),(8,'app','user_details'),(7,'app','wishlist_data'),(3,'auth','group'),(2,'auth','permission'),(4,'contenttypes','contenttype'),(11,'dash','ads'),(14,'dash','brand'),(12,'dash','category'),(13,'dash','product'),(5,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=43 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2022-02-10 04:41:52.691966'),(2,'dash','0001_initial','2022-02-10 04:41:52.842074'),(3,'contenttypes','0002_remove_content_type_name','2022-02-10 04:41:52.953344'),(4,'auth','0001_initial','2022-02-10 04:41:53.322495'),(5,'auth','0002_alter_permission_name_max_length','2022-02-10 04:41:53.396355'),(6,'auth','0003_alter_user_email_max_length','2022-02-10 04:41:53.412303'),(7,'auth','0004_alter_user_username_opts','2022-02-10 04:41:53.428072'),(8,'auth','0005_alter_user_last_login_null','2022-02-10 04:41:53.440798'),(9,'auth','0006_require_contenttypes_0002','2022-02-10 04:41:53.448491'),(10,'auth','0007_alter_validators_add_error_messages','2022-02-10 04:41:53.459709'),(11,'auth','0008_alter_user_username_max_length','2022-02-10 04:41:53.472312'),(12,'auth','0009_alter_user_last_name_max_length','2022-02-10 04:41:53.486049'),(13,'auth','0010_alter_group_name_max_length','2022-02-10 04:41:53.516635'),(14,'auth','0011_update_proxy_permissions','2022-02-10 04:41:53.533660'),(15,'auth','0012_alter_user_first_name_max_length','2022-02-10 04:41:53.547079'),(16,'app','0001_initial','2022-02-10 04:41:54.598653'),(17,'admin','0001_initial','2022-02-10 04:41:54.800354'),(18,'admin','0002_logentry_remove_auto_add','2022-02-10 04:41:54.826525'),(19,'admin','0003_logentry_add_action_flag_choices','2022-02-10 04:41:54.846091'),(20,'sessions','0001_initial','2022-02-10 04:41:54.891650'),(21,'dash','0002_brand_remove_product_brand','2022-02-10 05:06:55.553810'),(22,'dash','0003_product_brand','2022-02-10 05:36:39.933341'),(23,'app','0002_buyproduct','2022-02-14 03:57:51.737550'),(24,'app','0003_remove_buyproduct_user','2022-02-14 04:47:33.628096'),(25,'app','0004_alter_order_place_status','2022-02-14 14:18:04.399463'),(26,'app','0005_buyproduct_value','2022-02-14 15:45:31.383674'),(27,'dash','0004_category_category_offer_product_product_offer','2022-02-15 04:06:32.453322'),(28,'app','0006_buyproduct_user','2022-02-15 12:25:38.999130'),(29,'app','0007_remove_buyproduct_user','2022-02-15 12:41:39.016999'),(30,'app','0008_cartproduct_guest','2022-02-16 04:09:03.798976'),(31,'app','0009_coupon','2022-02-16 13:42:56.523015'),(32,'dash','0005_product_discount_price','2022-02-16 13:42:56.578844'),(33,'app','0010_coupon_coupon_offer','2022-02-16 15:18:46.834334'),(34,'app','0011_order_place_coupons','2022-02-16 15:18:46.953838'),(35,'app','0012_alter_coupon_coupon_offer','2022-02-17 04:00:31.858680'),(36,'app','0013_alter_coupon_coupon_id','2022-02-17 05:14:57.954736'),(37,'app','0014_alter_coupon_coupon_offer','2022-02-17 05:18:00.005724'),(38,'app','0015_alter_cartproduct_guest_alter_cartproduct_user','2022-02-17 13:49:55.242261'),(39,'app','0016_cartproduct_retotal','2022-02-19 05:15:57.109736'),(40,'app','0017_remove_cartproduct_retotal','2022-02-19 05:39:28.917698'),(41,'app','0018_wishlist_data_guest_alter_wishlist_data_user','2022-02-22 06:50:02.985686'),(42,'app','0019_cartproduct_alltotal','2022-02-22 09:02:04.534809');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('0szsh6iai438pfsp4mcaxtspsuyddes8','.eJxVjT0PgyAURf8LsyF8qA8cu3frbh4PKNZWEoWp6X-vJg7tes-9577ZiLWksW5hHSfPBiZZ85s5pDksB_APXO6ZU17KOjl-VPhJN37NPjwvZ_dPkHBL-xqs1Bqww9gJ0k6CBoBA0SjRQescKjTgtTJCG-GVsTb6QGQjWBN7ol1KKdCca8FXYYPsZduw42GX31LdEnr2-QJxXUNK:1nMl2N:ac7yWpD1UEevhcvJywhhnM1PM9_kRhULTdctKP8O4Xo','2022-03-09 06:22:07.335360'),('ag0w8in40vz9sie5lvy9izrwrmybvwm1','.eJxVjDsOgzAQBe_iOrL8CeyaMj1nQOu1HRMSLIGpotw9IFEk7Zt58xYDbTUP2xqXYQyiE1pcfjdPPMX5AOFB871ILnNdRi8PRZ50lX0J8Xk73b9ApjXvb3DaWqCGUqPYeg0WACInNKqBq_dkCCFYg8qiCgadSyEyuwQOU8u8RzlHnspW6VVFp12Lny8pzz3Y:1nN5dM:nurYPB8lNTHBR3Tp7lhDlHX1uGqNebzkETec8-lI2yM','2022-03-10 04:21:40.431594');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-02-24 20:51:56
