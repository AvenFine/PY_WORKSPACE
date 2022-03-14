/*
 Navicat Premium Data Transfer

 Source Server         : 5.5
 Source Server Type    : MySQL
 Source Server Version : 50728
 Source Host           : 192.168.5.5:3306
 Source Schema         : minna

 Target Server Type    : MySQL
 Target Server Version : 50728
 File Encoding         : 65001

 Date: 21/12/2021 12:25:23
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for a
-- ----------------------------
DROP TABLE IF EXISTS `a`;
CREATE TABLE `a`  (
  `id` int(11) NOT NULL,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_bin NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  CONSTRAINT `id` FOREIGN KEY (`id`) REFERENCES `b` (`id1`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of a
-- ----------------------------
INSERT INTO `a` VALUES (1, 'Pirate');
INSERT INTO `a` VALUES (2, 'Monkey');
INSERT INTO `a` VALUES (3, 'Ninja');
INSERT INTO `a` VALUES (4, 'Spaghetti');

SET FOREIGN_KEY_CHECKS = 1;
