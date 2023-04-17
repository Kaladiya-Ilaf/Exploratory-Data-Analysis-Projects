CREATE DATABASE screenTimeData;
USE  screenTimeData;
CREATE TABLE screenData (
							UsageDate          		VARCHAR(50),
							UsageTime         		INT, 
							Notifications       	INT, 
							TimesOpened        		INT, 
							App                 	VARCHAR(30)
						);
SELECT * FROM screenData;

