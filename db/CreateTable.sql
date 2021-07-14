CREATE TABLE IF NOT EXISTS history
             (
                          id INTEGER NOT NULL AUTO_INCREMENT,
                          artist VARCHAR (20) NOT NULL,
                          song VARCHAR (50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

LOCK TABLES `history` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `history` VALUES (1,'Sol','So Far Away');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;