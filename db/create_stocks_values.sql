BEGIN TRANSACTION;
CREATE TABLE my_stock_values(
   ISIN           TEXT     NOT NULL,
   buy_price      FLOAT    NOT NULL,
   volume         INT      NOT NULL
);

COMMIT;

INSERT INTO my_stock_values VALUES('A',120.11, 100);
