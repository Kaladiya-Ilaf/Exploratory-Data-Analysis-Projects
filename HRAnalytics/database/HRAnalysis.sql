CREATE DATABASE HRAnalytics;
USE HRAnalytics;
CREATE TABLE HRData(Age                         INT,
					Attrition                   VARCHAR(30),
					BusinessTravel              VARCHAR(30),
					DailyRate                   INT,
					Department                  VARCHAR(30),
					DistanceFromHome            INT,
					Education                   INT,
					EducationField              VARCHAR(30),
					EmployeeCount               INT,
					EmployeeNumber              INT,
					EnvironmentSatisfaction     INT,
					Gender                      VARCHAR(30),
					HourlyRate                  INT,
					JobInvolvement              INT,
					JobLevel                    INT,
					JobRole                     VARCHAR(30),
					JobSatisfaction             INT,
					MaritalStatus               VARCHAR(30),
					MonthlyIncome               INT,
					MonthlyRate                 INT,
					NumCompaniesWorked          INT,
					Over18                      VARCHAR(30),
					OverTime                    VARCHAR(30),
					PercentSalaryHike           INT,
					PerformanceRating           INT,
					RelationshipSatisfaction    INT,
					StandardHours               INT,
					StockOptionLevel            INT,
					TotalWorkingYears           INT,
					TrainingTimesLastYear       INT,
					WorkLifeBalance             INT,
					YearsAtCompany              INT,
					YearsInCurrentRole          INT,
					YearsSinceLastPromotion     INT,
					YearsWithCurrManager        INT
                    );
SELECT * FROM HRData;
