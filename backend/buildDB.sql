DROP DATABASE IF EXISTS CovidSupply;
CREATE DATABASE CovidSupply;
USE CovidSupply;

CREATE TABLE User (
    Username varchar(16) NOT NULL,
    Password varchar(64) NOT NULL,
    Email varchar(64) NOT NULL,
    Phone char(10),
    Picture blob,
    Street varchar(32),
    City varchar(32),
    State varchar(32),
    ZipCode char(5) NOT NULL,
    FirstName varchar(32) NOT NULL,
    LastName varchar(32) NOT NULL,
    NumTransactions int NOT NULL, -- DEFAULT 0,
    Rating int NOT NULL,

    PRIMARY KEY (Email)

    ON UPDATE CASCADE -- ?
    ON DELETE CASCADE -- ?
);

CREATE TABLE Requests (
    RequestEmail varchar(64) NOT NULL,
    RequestId int NOT NULL,
    MinQuantity float NOT NULL,
    Quantity float NOT NULL,
    Urgency smallint NOT NULL,
    Item varchar(32) NOT NULL, -- Should we have an Item enum table?
    IsFulfilled tinyint(1) NOT NULL, -- DEFAULT 0,

    PRIMARY KEY (RequestId)
    FOREIGN KEY (RequestEmail) REFERENCES User(Email)
);

CREATE TABLE Offers (
    OfferID int NOT NULL,
    OfferEmail varchar(64) NOT NULL,
    Quantity float NOT NULL,
    Item varchar(32) NOT NULL,
    Price float NOT NULL, --  DEFAULT 0.0,
    WillingToTransport tinyint(1), -- DEFAULT 0,

    PRIMARY KEY (OfferID)
    FOREIGN KEY (OfferEmail) REFERENCES User(Email)
);

CREATE TABLE Transactions (
    TransactionID int NOT NULL,
    OfferID int NULL, -- One of Request/Offer ID MUST be not null and the other MUST be null.
    RequestId int NULL,
    QuantityFulfilled float NOT NULL,
    Date date NOT NULL,
    FinalCost float NOT NULL, --  DEFAULT 0.0,
    DeliveryType int NOT NULL, -- TODO DeliveryType enum table (0 ~ N/A, 1 ~ Uber, 2 ~ UPS, etc)

    PRIMARY KEY (TransactionID)
    FOREIGN KEY (OfferID) REFERENCES Offers
    FOREIGN KEY (RequestID) REFERENCES Requests
);

CREATE TABLE Review (
    TransactionID int NOT NULL,
    IsSupplier tinyint(1) NOT NULL,
    Score smallint NOT NULL,
    Description BLOB,

    PRIMARY KEY (TransactionID)
    FOREIGN KEY (TransactionID) References Transactions
);