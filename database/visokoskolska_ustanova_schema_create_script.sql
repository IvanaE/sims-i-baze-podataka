-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema visokoskolska_ustanova_test
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `visokoskolska_ustanova_test` ;

-- -----------------------------------------------------
-- Schema visokoskolska_ustanova_test
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `visokoskolska_ustanova_test` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `visokoskolska_ustanova_test` ;

-- -----------------------------------------------------
-- Table `visokoskolska_ustanova_test`.`visokoskolska ustanova`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `visokoskolska_ustanova_test`.`visokoskolska ustanova` (
  `Oznaka` CHAR(2) NOT NULL,
  `Naziv` VARCHAR(80) NULL DEFAULT NULL,
  `Adresa` VARCHAR(80) NULL DEFAULT NULL,
  PRIMARY KEY (`Oznaka`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `visokoskolska_ustanova_test`.`nastavni predmet`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `visokoskolska_ustanova_test`.`nastavni predmet` (
  `Ustanova` CHAR(2) NOT NULL,
  `Naziv` VARCHAR(120) NULL DEFAULT NULL,
  `ESPB` DECIMAL(2,0) NULL DEFAULT NULL,
  `Oznaka` VARCHAR(6) NOT NULL,
  PRIMARY KEY (`Oznaka`),
  INDEX `Ustanova` (`Ustanova` ASC) VISIBLE,
  CONSTRAINT `nastavni predmet_ibfk_1`
    FOREIGN KEY (`Ustanova`)
    REFERENCES `visokoskolska_ustanova_test`.`visokoskolska ustanova` (`Oznaka`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `visokoskolska_ustanova_test`.`nivo studija`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `visokoskolska_ustanova_test`.`nivo studija` (
  `Oznaka` DECIMAL(2,0) NOT NULL,
  `Naziv` VARCHAR(80) NULL DEFAULT NULL,
  PRIMARY KEY (`Oznaka`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `visokoskolska_ustanova_test`.`studijski programi`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `visokoskolska_ustanova_test`.`studijski programi` (
  `Ustanova` CHAR(2) NOT NULL,
  `Nivo` DECIMAL(2,0) NULL DEFAULT NULL,
  `Oznaka programa` VARCHAR(3) NOT NULL,
  `Naziv programa` VARCHAR(120) NULL DEFAULT NULL,
  PRIMARY KEY (`Oznaka programa`),
  INDEX `Ustanova` (`Ustanova` ASC) VISIBLE,
  INDEX `Nivo` (`Nivo` ASC) VISIBLE,
  CONSTRAINT `studijski programi_ibfk_1`
    FOREIGN KEY (`Ustanova`)
    REFERENCES `visokoskolska_ustanova_test`.`visokoskolska ustanova` (`Oznaka`),
  CONSTRAINT `studijski programi_ibfk_2`
    FOREIGN KEY (`Nivo`)
    REFERENCES `visokoskolska_ustanova_test`.`nivo studija` (`Oznaka`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `visokoskolska_ustanova_test`.`plan studijske grupe`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `visokoskolska_ustanova_test`.`plan studijske grupe` (
  `Program Ustanove` CHAR(2) NOT NULL,
  `Oznaka programa` VARCHAR(3) NOT NULL,
  `Blok` DECIMAL(2,0) NULL DEFAULT NULL,
  `Pozicija` DECIMAL(2,0) NULL DEFAULT NULL,
  `Ustanova predmet` CHAR(2) NULL DEFAULT NULL,
  `Oznaka predmeta` VARCHAR(6) NULL DEFAULT NULL,
  PRIMARY KEY (`Oznaka programa`),
  INDEX `Program Ustanove` (`Program Ustanove` ASC) VISIBLE,
  INDEX `Oznaka predmeta` (`Oznaka predmeta` ASC) VISIBLE,
  CONSTRAINT `plan studijske grupe_ibfk_1`
    FOREIGN KEY (`Program Ustanove`)
    REFERENCES `visokoskolska_ustanova_test`.`studijski programi` (`Ustanova`),
  CONSTRAINT `plan studijske grupe_ibfk_2`
    FOREIGN KEY (`Oznaka programa`)
    REFERENCES `visokoskolska_ustanova_test`.`studijski programi` (`Oznaka programa`),
  CONSTRAINT `plan studijske grupe_ibfk_3`
    FOREIGN KEY (`Oznaka predmeta`)
    REFERENCES `visokoskolska_ustanova_test`.`nastavni predmet` (`Oznaka`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `visokoskolska_ustanova_test`.`studenti`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `visokoskolska_ustanova_test`.`studenti` (
  `Ustanova` CHAR(2) NOT NULL,
  `Struka` CHAR(2) NULL DEFAULT NULL,
  `Broj indeksa` VARCHAR(6) NOT NULL,
  `Prezime` VARCHAR(20) NULL DEFAULT NULL,
  `Ime roditelja` VARCHAR(20) NULL DEFAULT NULL,
  `Ime` VARCHAR(20) NULL DEFAULT NULL,
  `Pol` CHAR(1) NULL DEFAULT NULL,
  `Adresa stanovanja` VARCHAR(80) NULL DEFAULT NULL,
  `Telefon` VARCHAR(20) NULL DEFAULT NULL,
  `JMBG` CHAR(13) NULL DEFAULT NULL,
  `Datum rodjenja` DATE NULL DEFAULT NULL,
  PRIMARY KEY (`Broj indeksa`),
  INDEX `Ustanova` (`Ustanova` ASC) VISIBLE,
  CONSTRAINT `studenti_ibfk_1`
    FOREIGN KEY (`Ustanova`)
    REFERENCES `visokoskolska_ustanova_test`.`visokoskolska ustanova` (`Oznaka`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `visokoskolska_ustanova_test`.`tok studija`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `visokoskolska_ustanova_test`.`tok studija` (
  `Ustanova` CHAR(2) NOT NULL,
  `Oznaka programa` VARCHAR(3) NULL DEFAULT NULL,
  `Studenti iz ustanove` CHAR(2) NULL DEFAULT NULL,
  `Struka` CHAR(2) NULL DEFAULT NULL,
  `Skolska godina` DECIMAL(4,0) NULL DEFAULT NULL,
  `Broj indeksa` VARCHAR(6) NOT NULL,
  `Godina studija` DECIMAL(1,0) NULL DEFAULT NULL,
  `Blok` DECIMAL(2,0) NULL DEFAULT NULL,
  `Redni broj upisa` DECIMAL(2,0) NULL DEFAULT NULL,
  `Datum upisa` DATE NULL DEFAULT NULL,
  `Datum overe` DATE NULL DEFAULT NULL,
  `ESPB pocetni` DECIMAL(3,0) NULL DEFAULT NULL,
  `ESPB krajnji` DECIMAL(3,0) NULL DEFAULT NULL,
  PRIMARY KEY (`Broj indeksa`),
  INDEX `Oznaka programa` (`Oznaka programa` ASC) VISIBLE,
  CONSTRAINT `tok studija_ibfk_1`
    FOREIGN KEY (`Oznaka programa`)
    REFERENCES `visokoskolska_ustanova_test`.`studijski programi` (`Oznaka programa`),
  CONSTRAINT `tok studija_ibfk_2`
    FOREIGN KEY (`Broj indeksa`)
    REFERENCES `visokoskolska_ustanova_test`.`studenti` (`Broj indeksa`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
