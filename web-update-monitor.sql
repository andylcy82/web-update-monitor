-- phpMyAdmin SQL Dump
-- version 4.8.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Mar 03, 2023 at 03:57 AM
-- Server version: 5.7.23
-- PHP Version: 7.2.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


CREATE TABLE IF NOT EXISTS `check_results` (
  `date_time` datetime NOT NULL,
  `url_serial` int(11) NOT NULL,
  `check_update_flag` tinyint(4) NOT NULL,
  PRIMARY KEY (`date_time`,`url_serial`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


CREATE TABLE IF NOT EXISTS `receiver_email_list` (
  `serial` int(11) NOT NULL AUTO_INCREMENT,
  `send_when_no_update` tinyint(4) NOT NULL,
  `send_when_update` tinyint(4) NOT NULL,
  `send_when_error` tinyint(4) NOT NULL,
  `email` varchar(100) NOT NULL,
  PRIMARY KEY (`serial`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


CREATE TABLE IF NOT EXISTS `url_list` (
  `serial` int(11) NOT NULL AUTO_INCREMENT,
  `URL` varchar(200) NOT NULL,
  `name` varchar(100) NOT NULL,
  `keyword` varchar(100) NOT NULL,
  `wrap` varchar(100) NOT NULL,
  `no_update_subject` varchar(100) NOT NULL,
  `no_update_message` text NOT NULL,
  `update_subject` varchar(100) NOT NULL,
  `update_message` text NOT NULL,
  `check_flag` tinyint(4) NOT NULL,
  PRIMARY KEY (`serial`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
COMMIT;
