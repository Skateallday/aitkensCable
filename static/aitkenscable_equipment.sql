-- phpMyAdmin SQL Dump
-- version 4.7.7
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: May 31, 2019 at 11:33 AM
-- Server version: 10.1.38-MariaDB-cll-lve
-- PHP Version: 5.6.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `aitkenscable_equipment`
--

-- --------------------------------------------------------

--
-- Table structure for table `cable_basket`
--

CREATE TABLE `cable_basket` (
  `id` int(11) NOT NULL,
  `model_name` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `width` int(4) DEFAULT NULL,
  `model_ref` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `cable_Ladder`
--

CREATE TABLE `cable_Ladder` (
  `id` int(11) NOT NULL,
  `model_name` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `width` int(4) DEFAULT NULL,
  `model_ref` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `cable_tray`
--

CREATE TABLE `cable_tray` (
  `id` int(11) NOT NULL,
  `item_name` varchar(64) COLLATE utf8mb4_unicode_ci NOT NULL,
  `50mm` varchar(6) COLLATE utf8mb4_unicode_ci NOT NULL,
  `75mm` varchar(6) COLLATE utf8mb4_unicode_ci NOT NULL,
  `100m` varchar(6) COLLATE utf8mb4_unicode_ci NOT NULL,
  `150mm` varchar(6) COLLATE utf8mb4_unicode_ci NOT NULL,
  `225mm` varchar(6) COLLATE utf8mb4_unicode_ci NOT NULL,
  `300mm` varchar(6) COLLATE utf8mb4_unicode_ci NOT NULL,
  `450mm` varchar(6) COLLATE utf8mb4_unicode_ci NOT NULL,
  `600mm` varchar(6) COLLATE utf8mb4_unicode_ci NOT NULL,
  `750mm` varchar(6) COLLATE utf8mb4_unicode_ci NOT NULL,
  `900mm` varchar(6) COLLATE utf8mb4_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `cable_trunking`
--

CREATE TABLE `cable_trunking` (
  `id` int(3) NOT NULL,
  `item_name` varchar(64) COLLATE utf8mb4_unicode_ci NOT NULL,
  `50x50` varchar(7) COLLATE utf8mb4_unicode_ci NOT NULL,
  `75x50` varchar(7) COLLATE utf8mb4_unicode_ci NOT NULL,
  `75x75` varchar(7) COLLATE utf8mb4_unicode_ci NOT NULL,
  `100x50` varchar(7) COLLATE utf8mb4_unicode_ci NOT NULL,
  `100x100` varchar(7) COLLATE utf8mb4_unicode_ci NOT NULL,
  `150x50` varchar(7) COLLATE utf8mb4_unicode_ci NOT NULL,
  `150x75` varchar(7) COLLATE utf8mb4_unicode_ci NOT NULL,
  `150x100` varchar(7) COLLATE utf8mb4_unicode_ci NOT NULL,
  `150x150` varchar(7) COLLATE utf8mb4_unicode_ci NOT NULL,
  `200x100` varchar(7) COLLATE utf8mb4_unicode_ci NOT NULL,
  `225x50` varchar(7) COLLATE utf8mb4_unicode_ci NOT NULL,
  `225x150` varchar(7) COLLATE utf8mb4_unicode_ci NOT NULL,
  `300x150` varchar(7) COLLATE utf8mb4_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `channel_support`
--

CREATE TABLE `channel_support` (
  `id` int(11) NOT NULL,
  `item_name` varchar(64) COLLATE utf8mb4_unicode_ci NOT NULL,
  `part_ref` varchar(24) COLLATE utf8mb4_unicode_ci NOT NULL,
  `weight` decimal(8,0) DEFAULT NULL,
  `thickeness` decimal(4,0) DEFAULT NULL,
  `thread` varchar(4) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `width` int(4) DEFAULT NULL,
  `size` varchar(8) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `diameter` varchar(8) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `material` varchar(8) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `finish` varchar(8) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `length` varchar(8) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `desc.` varchar(8) COLLATE utf8mb4_unicode_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `dado_trunking`
--

CREATE TABLE `dado_trunking` (
  `id` int(11) NOT NULL,
  `item_name` varchar(64) COLLATE utf8mb4_unicode_ci NOT NULL,
  `part_ref` varchar(8) COLLATE utf8mb4_unicode_ci NOT NULL,
  `size` varchar(24) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `pack_quantity` int(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `Floor_Service_Box`
--

CREATE TABLE `Floor_Service_Box` (
  `Model_Name` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `Model_Desc` text COLLATE utf8mb4_unicode_ci NOT NULL,
  `Model_ID` varchar(10) COLLATE utf8mb4_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `lighting_trunking`
--

CREATE TABLE `lighting_trunking` (
  `id` int(3) NOT NULL,
  `item_name` varchar(64) COLLATE utf8mb4_unicode_ci NOT NULL,
  `code` varchar(7) COLLATE utf8mb4_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `plastic_conduit`
--

CREATE TABLE `plastic_conduit` (
  `id` int(11) NOT NULL,
  `item_name` varchar(64) COLLATE utf8mb4_unicode_ci NOT NULL,
  `part_ref` varchar(16) COLLATE utf8mb4_unicode_ci NOT NULL,
  `length` varchar(8) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `box_quantity` int(4) DEFAULT NULL,
  `size` varchar(8) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `thread` varchar(8) COLLATE utf8mb4_unicode_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `roof_support_systems`
--

CREATE TABLE `roof_support_systems` (
  `Product_Code` varchar(9) COLLATE utf8mb4_unicode_ci NOT NULL,
  `Model` varchar(60) COLLATE utf8mb4_unicode_ci NOT NULL,
  `Height` int(4) DEFAULT NULL,
  `Width` int(4) DEFAULT NULL,
  `Length` int(4) DEFAULT NULL,
  `Max.Loading` int(4) DEFAULT NULL,
  `AFXWeight` decimal(4,0) DEFAULT NULL,
  `Height_With_Foot` varchar(10) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `Load_Bearing` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `cable_basket`
--
ALTER TABLE `cable_basket`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `cable_Ladder`
--
ALTER TABLE `cable_Ladder`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `cable_tray`
--
ALTER TABLE `cable_tray`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `cable_trunking`
--
ALTER TABLE `cable_trunking`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `channel_support`
--
ALTER TABLE `channel_support`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `dado_trunking`
--
ALTER TABLE `dado_trunking`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `lighting_trunking`
--
ALTER TABLE `lighting_trunking`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `plastic_conduit`
--
ALTER TABLE `plastic_conduit`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `cable_basket`
--
ALTER TABLE `cable_basket`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `cable_Ladder`
--
ALTER TABLE `cable_Ladder`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `cable_tray`
--
ALTER TABLE `cable_tray`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `cable_trunking`
--
ALTER TABLE `cable_trunking`
  MODIFY `id` int(3) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `channel_support`
--
ALTER TABLE `channel_support`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `dado_trunking`
--
ALTER TABLE `dado_trunking`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `lighting_trunking`
--
ALTER TABLE `lighting_trunking`
  MODIFY `id` int(3) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `plastic_conduit`
--
ALTER TABLE `plastic_conduit`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
