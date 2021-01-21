
INSERT INTO Susmita.PersonPhone
SELECT TOP 3 * FROM [Person].[PersonPhone]

SELECT * FROM Susmita.PersonPhone
SELECT * FROM [Person].[PersonPhone]

UPDATE Susmita.Person SET BusinessEntityID = 4 WHERE BusinessEntityID = 3

SELECT *
FROM Susmita.Person, Susmita.PersonPhone
WHERE Susmita.Person.BusinessEntityID = Susmita.PersonPhone.BusinessEntityID

SELECT *
FROM Susmita.Person LEFT JOIN Susmita.PersonPhone
ON Susmita.Person.BusinessEntityID = Susmita.PersonPhone.BusinessEntityID

SELECT *
FROM Susmita.Person RIGHT JOIN Susmita.PersonPhone
ON Susmita.Person.BusinessEntityID = Susmita.PersonPhone.BusinessEntityID

SELECT *
FROM Susmita.Person FULL OUTER JOIN Susmita.PersonPhone
ON Susmita.Person.BusinessEntityID = Susmita.PersonPhone.BusinessEntityID

SELECT A.PersonType,B.*,C.rowguid

FROM Person.Person as A,
Person.PersonPhone as B,
Person.BusinessEntity as C
WHERE A.BusinessEntityID = B.BusinessEntityID
AND B.BusinessEntityID = C.BusinessEntityID;

SELECT *
FROM [Person].[PersonPhone] B
WHERE B.PhoneNumber IN
(
SELECT A.PhoneNumber
FROM Susmita.PersonPhone A
)


SELECT A.*, B.*

FROM Person.Person as A INNER JOIN
Person.PersonPhone as B
ON A.BusinessEntityID = B.BusinessEntityID

-- CREATE AN EMPY TABLE
SELECT * INTO Susmita.Person
FROM [Person].[Person]
WHERE 1 = 0;

-- INSERT DATA INTO NEW TABLE
INSERT INTO Susmita.Person
SELECT TOP 3 * FROM [Person].[Person]

-- VIEW THE NEWLY CREATED TABLE
SELECT * FROM Susmita.Person
SELECT * FROM [Person].[Person]

UPDATE Susmita.Person SET BusinessEntityID = 4 WHERE BusinessEntityID = 3