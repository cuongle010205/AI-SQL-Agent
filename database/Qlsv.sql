CREATE DATABASE Qlsv
GO
USE Qlsv
GO
 CREATE TABLE Khoa(
	ma varchar(10) PRIMARY KEY,
	tenKhoa nvarchar(100) ,
	namThanhLap int
	)
CREATE TABLE KhoaHoc(
	Ma varchar(10) PRIMARY KEY,
	namBatDau int,
	namKetThuc int
	)
 CREATE TABLE ChuongTrinh(
 Ma varchar(10) PRIMARY KEY,
 tenChuongTrinh nvarchar(100) NOT NULL)
  CREATE TABLE Lop(
 Ma varchar(10) PRIMARY KEY,
 maKhoaHoc varchar(10),
 maKhoa varchar(10),
 maChuongTrinh varchar(10),
 soThuTu int,
 )
 CREATE TABLE SinhVien(
 Ma varchar(10) PRIMARY KEY,
 hoTen nvarchar(100) NOT NULL,
 namSinh int,
 danToc nvarchar(20),
 maLop varchar(10)
 )
 CREATE TABLE MonHoc(
 Ma varchar(10) PRIMARY KEY,
 tenMonHoc nvarchar(100),
 maKhoa varchar(10)
 )
 CREATE TABLE  KetQua(
 maSinhVien varchar(10),
 maMonHoc varchar(10),
 lanThi int,
 diem float,
 PRIMARY KEY(maSinhVien, maMonHoc,lanThi)
 )
 CREATE TABLE GiangKhoa(
 maChuongTrinh varchar(10),
 maKhoa varchar(10),
 maMonHoc varchar(10),
 namHoc int,
 hocKy int,
 soTietLyThuyet int,
 soTietThuchanh int,
 soTinChi int,
 PRIMARY KEY( maChuongTrinh, maKhoa, maMonHoc)
 )
 ALTER TABLE lop
 ADD CONSTRAINT FK_Lop_Khoa
 FOREIGN KEY (maKhoa) REFERENCES Khoa(ma)
 
 ALTER TABLE  Lop
 ADD CONSTRAINT FK_Lop_KhoaHoc
 FOREIGN KEY (maKhoaHoc) REFERENCES KhoaHoc(Ma) 
 
 ALTER TABLE Lop
 ADD CONSTRAINT FK_Lop_ChuongTrinh
 FOREIGN KEY (maChuongTrinh) REFERENCES ChuongTrinh(Ma)

 ALTER TABLE SinhVien
 ADD CONSTRAINT FK_SinhVien_Lop
 FOREIGN KEY (maLop) REFERENCES Lop(Ma)

 ALTER TABLE MonHoc
 ADD CONSTRAINT FK_MonHoc_Khoa
 FOREIGN KEY (maKhoa) REFERENCES Khoa(ma)

 ALTER TABLE KetQua
 ADD CONSTRAINT FK_KetQua_SinhVien
 FOREIGN KEY (maSinhVien) REFERENCES SinhVien(Ma)

 ALTER TABLE KetQua
 ADD CONSTRAINT FK_KetQua_MonHoc
 FOREIGN KEY (maMonHoc) REFERENCES MonHoc(Ma)

 ALTER TABLE GiangKhoa
 ADD CONSTRAINT FK_GiangKhoa_ChuongTrinh
 FOREIGN KEY (maChuongTrinh) REFERENCES ChuongTrinh(Ma)

 ALTER TABLE GiangKhoa
 ADD CONSTRAINT FK_GiangKhoa_Khoa
 FOREIGN KEY (maKhoa) REFERENCES Khoa(ma)

 ALTER TABLE GiangKhoa
 ADD CONSTRAINT FK_GiangKhoa_MonHoc 
 FOREIGN KEY (maMonHoc) REFERENCES MonHoc(Ma)

 INSERT INTO Khoa VALUES
 ('CNTT',N'Công nghệ thông tin ',1955),
 ('VL',N'Vật Lý', 1970)
  INSERT INTO KhoaHoc VALUES
  ('K2002',2002,2006),
  ('K2003',2003,2007),
  ('K2004',2004,2008)
  INSERT INTO ChuongTrinh VALUES
('CQ',N'Chính Qui')
INSERT INTO Lop VALUES 
('TH2002/01','K2002','CNTT','CQ',1),
('TH2002/02','K2002','CNTT','CQ',2),
('VL2003/01','K2003','VL','CQ',1)
  INSERT INTO SinhVien VALUES
  ('0212001',N'Nguyễn Vĩnh An',1984,'Kinh','TH2002/01'),
('0212002',N'Nguyên Thanh Bình',1985,'Kinh','TH2002/01'),
('0212003',N'Nguyễn Thanh Cường ',1984,'Kinh','TH2002/02'),
('0212004',N'Nguyễn Quốc Duy',1983,'Kinh','TH2002/02'),
('0311001',N'Phan Tuấn Anh',1985,'Kinh','VL2003/01'),
('0311002',N'Huỳnh Thanh Sang',1984,'Kinh','VL2003/01')


INSERT INTO MonHoc VALUES
('THT01',N'Toán Cao cấp A1','CNTT'),
('VLT01',N'Vật lý cao cấp A1','VL'),
('THT02',N'Toán rời rạc','CNTT'),
('THCS01',N'Cấu trúc dữ liệu 1','CNTT'),
('THCS02',N'Hệ điều hành','CNTT')

INSERT INTO KetQua VALUES
('0212001','THT01',1,4),
('0212001','THT01',2,7),
('0212002','THT01',1,8),
('0212003','THT01',1,6),
('0212004','THT01',1,9),
('0212001','THT02',1,8),
('0212002','THT02',1,5.5),
('0212003','THT02',1,4),
('0212003','THT02',2,6),
('0212001','THCS01',1,6.5),
('0212002','THCS01',1,4),
('0212003','THCS01',1,7)

INSERT INTO GiangKhoa VALUES
('CQ','CNTT','THT01',2003,1,60,0,5),
('CQ','CNTT','THT02',2003,2,45,0,4),
('CQ','CNTT','THCS01',2004,1,45,30,4)



