CREATE TABLE `offer_transactions` (
  `transactionId` int NOT NULL,
  `offerId` int DEFAULT NULL,
  `requestId` int DEFAULT NULL,
  `quantity_fulfilled` varchar(45) DEFAULT NULL,
  `transaction_date` datetime DEFAULT NULL,
  `final_cost` varchar(45) DEFAULT NULL,
  `delivery_type` varchar(45) DEFAULT NULL,
  `is_supplier` tinyint DEFAULT NULL,
  `score` int DEFAULT NULL,
  `desc` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`transactionId`),
  KEY `fk_transactions_offer` (`offerId`),
  CONSTRAINT `fk_transactions_offer` FOREIGN KEY (`offerId`) REFERENCES `offers` (`offerId`)
) COLLATE='utf8_unicode_ci' ENGINE=InnoDB;

CREATE TABLE `offers` (
  `offerId` int NOT NULL,
  `user_email` varchar(64) DEFAULT NULL,
  `quantity` float DEFAULT NULL,
  `item` varchar(32) DEFAULT NULL,
  `price` float DEFAULT NULL,
  `willing_to_transport` tinyint DEFAULT NULL,
  PRIMARY KEY (`offerId`),
  KEY `fk_email_idx` (`user_email`),
  CONSTRAINT `fk_offer_email` FOREIGN KEY (`user_email`) REFERENCES `users` (`email`)
) COLLATE='utf8_unicode_ci' ENGINE=InnoDB;

CREATE TABLE `request_transactions` (
  `transactionId` int NOT NULL,
  `requestId` int DEFAULT NULL,
  `quantity_fulfilled` varchar(45) DEFAULT NULL,
  `transaction_date` datetime DEFAULT NULL,
  `final_cost` varchar(45) DEFAULT NULL,
  `delivery_type` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`transactionId`),
  KEY `fk_transactions_request_idx` (`requestId`),
  CONSTRAINT `fk_transactions_request` FOREIGN KEY (`requestId`) REFERENCES `requests` (`requestId`)
) COLLATE='utf8_unicode_ci' ENGINE=InnoDB;

CREATE TABLE `requests` (
  `requestId` int NOT NULL,
  `user_email` varchar(64) DEFAULT NULL,
  `min_quantity` float DEFAULT NULL,
  `quantity` float DEFAULT NULL,
  `urgency` smallint DEFAULT NULL,
  `item` varchar(32) DEFAULT NULL,
  `fulfilled` tinyint DEFAULT NULL,
  `is_surplus` tinyint DEFAULT NULL,
  PRIMARY KEY (`requestId`),
  KEY `fk_email_idx` (`user_email`),
  CONSTRAINT `fk_requests_email` FOREIGN KEY (`user_email`) REFERENCES `users` (`email`) ON DELETE CASCADE ON UPDATE CASCADE
) COLLATE='utf8_unicode_ci' ENGINE=InnoDB;

CREATE TABLE `users` (
  `username` varchar(16) NOT NULL,
  `password` varchar(64) NOT NULL,
  `email` varchar(64) NOT NULL,
  `phone` char(10) DEFAULT NULL,
  `picture` varchar(64) DEFAULT NULL,
  `street` varchar(64) NOT NULL,
  `city` varchar(64) NOT NULL,
  `state` varchar(16) NOT NULL,
  `zipcode` char(5) NOT NULL,
  `fname` varchar(32) NOT NULL,
  `lname` varchar(32) NOT NULL,
  `num_transactions` int NOT NULL,
  `rating` int NOT NULL,
  PRIMARY KEY (`email`)
) COLLATE='utf8_unicode_ci' ENGINE=InnoDB;
