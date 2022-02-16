-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Tempo de geração: 18-Dez-2021 às 01:40
-- Versão do servidor: 8.0.27
-- versão do PHP: 7.4.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `exemplo`
--
CREATE DATABASE IF NOT EXISTS `exemplo` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `exemplo`;

-- --------------------------------------------------------

--
-- Estrutura da tabela `amigos`
--

DROP TABLE IF EXISTS `amigos`;
CREATE TABLE IF NOT EXISTS `amigos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(30) NOT NULL,
  `sexo` enum('M','F') NOT NULL,
  `idade` date NOT NULL,
  `numero` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nome` (`nome`),
  UNIQUE KEY `idade` (`idade`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb3;

--
-- Extraindo dados da tabela `amigos`
--

INSERT INTO `amigos` (`id`, `nome`, `sexo`, `idade`, `numero`) VALUES
(1, 'maria', 'F', '1994-12-16', 549845748),
(2, 'joão', 'M', '1993-02-01', 785888);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
