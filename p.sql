use kita;
SET @TS = DATE_FORMAT(NOW(),'_%Y_%m_%d_%H_%i_%s');
SET @FOLDER = 'D:/demo/New folder/bmidata1/';
SET @PREFIX = 'patient';
SET @EXT    = '.csv';

SET @CMD = CONCAT("select 'name','age','phone','gender','height','weight','bmi','cat' union all select * into OUTFILE'",@FOLDER,@PREFIX,@TS,@EXT,
				   "' FIELDS TERMINATED BY ',' 
				  FROM USERS;");


PREPARE statement FROM @CMD;

EXECUTE statement;