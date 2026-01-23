-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 22, 2026 at 11:24 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `task_tracker`
--

-- --------------------------------------------------------

--
-- Table structure for table `projects`
--

CREATE TABLE `projects` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `projects`
--

INSERT INTO `projects` (`id`, `name`, `user_id`) VALUES
(1, 'Proyek Pengembangan Aplikasi A', 1),
(2, 'Rencana Liburan Keluarga', 2),
(3, 'Laporan Keuangan Q4 2025', 3),
(4, 'Desain Ulang Website Perusahaan', 4),
(5, 'Materi Presentasi Klien', 5),
(6, 'Pengembangan Sistem Informasi Akademik', 6),
(7, 'Aplikasi Manajemen Keuangan UMKM', 7),
(8, 'Website Portfolio Pribadi', 8),
(9, 'Sistem Monitoring Inventori', 9),
(10, 'Aplikasi Absensi Karyawan', 10),
(11, 'Dashboard Analisis Penjualan', 11),
(12, 'Perancangan UI/UX Aplikasi Mobile', 12);

-- --------------------------------------------------------

--
-- Table structure for table `sub_tasks`
--

CREATE TABLE `sub_tasks` (
  `id` int(11) NOT NULL,
  `title` varchar(255) NOT NULL,
  `status` enum('belum selesai','selesai','sedang dikerjakan') NOT NULL DEFAULT 'belum selesai',
  `task_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `sub_tasks`
--

INSERT INTO `sub_tasks` (`id`, `title`, `status`, `task_id`) VALUES
(1, 'Buat tabel users', 'sedang dikerjakan', 1),
(2, 'Bandingkan harga maskapai Garuda dan Lion Air', 'belum selesai', 2),
(3, 'menganalisa data dengan statistik', 'selesai', 3),
(4, 'Desain layout awal (wireframe)', 'sedang dikerjakan', 4),
(5, 'Kumpulkan data riset kompetitor', 'selesai', 5),
(6, 'Membuat desain ERD database', 'sedang dikerjakan', 6),
(7, 'Menentukan field dan relasi tabel', 'selesai', 7),
(8, 'Mengumpulkan data harga tiket terbaru', 'sedang dikerjakan', 8),
(9, 'Membuat grafik perbandingan harga', 'belum selesai', 9),
(10, 'Membersihkan data sebelum analisis', 'selesai', 10),
(11, 'Membuat prototype UI di Figma', 'sedang dikerjakan', 11),
(12, 'Menyusun laporan hasil riset', 'belum selesai', 12);

-- --------------------------------------------------------

--
-- Table structure for table `tags`
--

CREATE TABLE `tags` (
  `id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tags`
--

INSERT INTO `tags` (`id`, `name`, `user_id`) VALUES
(10, 'Akademik', 10),
(11, 'Bug', 11),
(4, 'Desain', 4),
(3, 'Kantor', 3),
(2, 'Keluarga', 2),
(9, 'Keuangan', 9),
(7, 'Meeting', 7),
(1, 'Penting', 1),
(12, 'Planning', 12),
(8, 'Pribadi', 8),
(5, 'Riset', 5),
(6, 'Urgent', 6);

-- --------------------------------------------------------

--
-- Table structure for table `tasks`
--

CREATE TABLE `tasks` (
  `id` int(11) NOT NULL,
  `title` varchar(255) NOT NULL,
  `description` text DEFAULT NULL,
  `status` enum('belum selesai','selesai','sedang dikerjakan') NOT NULL DEFAULT 'belum selesai',
  `due_date` datetime DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  `project_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tasks`
--

INSERT INTO `tasks` (`id`, `title`, `description`, `status`, `due_date`, `user_id`, `project_id`) VALUES
(1, 'Membuat Desain Database', 'Rancang ERD dan skema untuk modul pengguna.', 'selesai', '2025-10-20 17:00:00', 1, 1),
(2, 'Booking Tiket Pesawat', 'Cari dan pesan tiket ke Bali untuk 4 orang.', 'sedang dikerjakan', '2025-10-25 23:59:00', 2, 2),
(3, 'Kumpulkan Data Penjualan Oktober', 'Ekspor data dari sistem CRM dan rekap dalam spreadsheet.', 'belum selesai', '2025-10-30 12:00:00', 3, 3),
(4, 'Buat Mockup Halaman Utama', 'Desain wireframe dan mockup untuk homepage baru.', 'selesai', '2025-10-18 15:00:00', 4, 4),
(5, 'Siapkan slide tentang Analisis Pasar', 'Buat 10 slide yang merangkum tren pasar saat ini.', 'belum selesai', '2025-10-22 09:00:00', 5, 5),
(6, 'Menyusun Dokumentasi Sistem', 'Membuat dokumentasi teknis dan user guide aplikasi.', 'sedang dikerjakan', '2025-11-05 17:00:00', 6, 6),
(7, 'Riset Vendor Hosting', 'Membandingkan harga dan spesifikasi layanan hosting.', 'belum selesai', '2025-11-08 12:00:00', 7, 7),
(8, 'Input dan Validasi Data', 'Memasukkan data awal dan memastikan tidak ada error.', 'sedang dikerjakan', '2025-11-02 16:00:00', 8, 8),
(9, 'Desain UI Halaman Login', 'Membuat desain tampilan login yang modern.', 'selesai', '2025-10-28 14:00:00', 9, 9),
(10, 'Menyusun Materi Presentasi Final', 'Menyiapkan slide presentasi hasil akhir project.', 'belum selesai', '2025-11-10 09:00:00', 10, 10),
(11, 'Pengujian Fitur Utama', 'Melakukan testing pada modul utama aplikasi.', 'sedang dikerjakan', '2025-11-06 18:00:00', 11, 11),
(12, 'Evaluasi dan Perbaikan Bug', 'Mencatat dan memperbaiki bug dari hasil testing.', 'belum selesai', '2025-11-12 20:00:00', 12, 12);

-- --------------------------------------------------------

--
-- Table structure for table `task_tags`
--

CREATE TABLE `task_tags` (
  `task_id` int(11) NOT NULL,
  `tag_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `task_tags`
--

INSERT INTO `task_tags` (`task_id`, `tag_id`) VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5),
(6, 6),
(7, 7),
(8, 8),
(9, 9),
(10, 10),
(11, 11),
(12, 12);

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(255) NOT NULL,
  `email` varchar(100) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `username`, `password`, `email`, `created_at`) VALUES
(1, 'budi_santoso', 'password_budi', 'budi.santoso@email.com', '2025-10-17 09:08:36'),
(2, 'anita_wijaya', 'password_anita', 'anita.wijaya@email.com', '2025-10-17 09:08:36'),
(3, 'wijaya_limantara', 'password_limantara', 'wijaya.limantara@email.com', '2025-10-17 09:08:36'),
(4, 'udin_arif', 'password_udin', 'udin.arif@email.com', '2025-10-17 09:08:36'),
(5, 'saiful_jamil', 'password_saiful', 'saiful.jamil@email.com', '2025-10-17 09:08:36'),
(6, 'rina_putri', 'password_rina', 'rina.putri@email.com', '2026-01-22 09:55:34'),
(7, 'andi_pratama', 'password_andi', 'andi.pratama@email.com', '2026-01-22 09:55:34'),
(8, 'siti_aisyah', 'password_siti', 'siti.aisyah@email.com', '2026-01-22 09:55:34'),
(9, 'dimas_saputra', 'password_dimas', 'dimas.saputra@email.com', '2026-01-22 09:55:34'),
(10, 'nurul_hidayah', 'password_nurul', 'nurul.hidayah@email.com', '2026-01-22 09:55:34'),
(11, 'fajar_maulana', 'password_fajar', 'fajar.maulana@email.com', '2026-01-22 09:55:34'),
(12, 'dewi_lestari', 'password_dewi', 'dewi.lestari@email.com', '2026-01-22 09:55:34');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `projects`
--
ALTER TABLE `projects`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `sub_tasks`
--
ALTER TABLE `sub_tasks`
  ADD PRIMARY KEY (`id`),
  ADD KEY `task_id` (`task_id`);

--
-- Indexes for table `tags`
--
ALTER TABLE `tags`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`,`user_id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `tasks`
--
ALTER TABLE `tasks`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`),
  ADD KEY `project_id` (`project_id`);

--
-- Indexes for table `task_tags`
--
ALTER TABLE `task_tags`
  ADD PRIMARY KEY (`task_id`,`tag_id`),
  ADD KEY `tag_id` (`tag_id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`),
  ADD UNIQUE KEY `email` (`email`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `projects`
--
ALTER TABLE `projects`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `sub_tasks`
--
ALTER TABLE `sub_tasks`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=27;

--
-- AUTO_INCREMENT for table `tags`
--
ALTER TABLE `tags`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- AUTO_INCREMENT for table `tasks`
--
ALTER TABLE `tasks`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `projects`
--
ALTER TABLE `projects`
  ADD CONSTRAINT `projects_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE;

--
-- Constraints for table `sub_tasks`
--
ALTER TABLE `sub_tasks`
  ADD CONSTRAINT `sub_tasks_ibfk_1` FOREIGN KEY (`task_id`) REFERENCES `tasks` (`id`) ON DELETE CASCADE;

--
-- Constraints for table `tags`
--
ALTER TABLE `tags`
  ADD CONSTRAINT `tags_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE;

--
-- Constraints for table `tasks`
--
ALTER TABLE `tasks`
  ADD CONSTRAINT `tasks_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE,
  ADD CONSTRAINT `tasks_ibfk_2` FOREIGN KEY (`project_id`) REFERENCES `projects` (`id`) ON DELETE SET NULL;

--
-- Constraints for table `task_tags`
--
ALTER TABLE `task_tags`
  ADD CONSTRAINT `task_tags_ibfk_1` FOREIGN KEY (`task_id`) REFERENCES `tasks` (`id`) ON DELETE CASCADE,
  ADD CONSTRAINT `task_tags_ibfk_2` FOREIGN KEY (`tag_id`) REFERENCES `tags` (`id`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
