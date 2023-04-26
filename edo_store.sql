-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 26 Apr 2023 pada 20.20
-- Versi server: 10.4.20-MariaDB
-- Versi PHP: 8.0.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `edo_store`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `product`
--

CREATE TABLE `product` (
  `item_id` int(25) NOT NULL,
  `item_name` varchar(15) NOT NULL,
  `type_item` varchar(15) NOT NULL,
  `color` varchar(15) NOT NULL,
  `storage` varchar(15) NOT NULL,
  `imei` int(15) NOT NULL,
  `price` int(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `product`
--

INSERT INTO `product` (`item_id`, `item_name`, `type_item`, `color`, `storage`, `imei`, `price`) VALUES
(1, 'SAMSUNG J1', 'Handphone', 'White', '64 GB', 2147483647, 2500000),
(2, 'IPHONE XR', 'Handphone', 'Red', '128 GB', 2147483647, 5500000),
(3, 'LENOVO X451', 'Laptop', 'Silver', '256 GB', 2147483647, 6500000),
(4, 'ASUS ZENBOOK', 'Laptop', 'White', '256 GB', 2147483647, 13000000),
(5, 'OPPO F5', 'Handphone', 'Black', '64 GB', 2147483647, 3500000);

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `product`
--
ALTER TABLE `product`
  ADD PRIMARY KEY (`item_id`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `product`
--
ALTER TABLE `product`
  MODIFY `item_id` int(25) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
