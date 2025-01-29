-- Create Users table
CREATE TABLE Users (
    userID INTEGER PRIMARY KEY AUTOINCREMENT,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    registrationDate DATE NOT NULL,
    referredBy INT,
    FOREIGN KEY (referredBy) REFERENCES Users(userID)
);

-- Create Games table
CREATE TABLE Games (
    gameID INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(100) NOT NULL,
    developer VARCHAR(100) NOT NULL,
    releaseDate DATE NOT NULL,
    genre VARCHAR(50) NOT NULL,
    platform VARCHAR(50) NOT NULL,
    basePrice DECIMAL(10, 2) NOT NULL
);

-- Create UserInventory table
CREATE TABLE UserInventory (
    inventoryID INTEGER PRIMARY KEY AUTOINCREMENT,
    userID INT NOT NULL,
    gameID INT NOT NULL,
    purchaseDate DATE NOT NULL,
    tradeValue DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (userID) REFERENCES Users(userID),
    FOREIGN KEY (gameID) REFERENCES Games(gameID)
);

-- Create Trades table
CREATE TABLE Trades (
    tradeID INTEGER PRIMARY KEY AUTOINCREMENT,
    offerUserID INT NOT NULL,
    receiveUserID INT NOT NULL,
    offerGameID INT NOT NULL,
    receiveGameID INT NOT NULL,
    tradeDate DATE NOT NULL,
    status TEXT CHECK(status IN ('Pending', 'Accepted', 'Rejected')) NOT NULL,
    FOREIGN KEY (offerUserID) REFERENCES Users(userID),
    FOREIGN KEY (receiveUserID) REFERENCES Users(userID),
    FOREIGN KEY (offerGameID) REFERENCES Games(gameID),
    FOREIGN KEY (receiveGameID) REFERENCES Games(gameID)
);

-- Create GameBundles table
CREATE TABLE GameBundles (
    bundleID INTEGER PRIMARY KEY AUTOINCREMENT,
    bundleName VARCHAR(100) NOT NULL,
    description TEXT,
    discountPercentage DECIMAL(5, 2) NOT NULL
);

-- Create BundleGames table
CREATE TABLE BundleGames (
    bundleItemID INTEGER PRIMARY KEY AUTOINCREMENT,
    bundleID INT NOT NULL,
    gameID INT NOT NULL,
    parentBundleItemID INT,
    FOREIGN KEY (bundleID) REFERENCES GameBundles(bundleID),
    FOREIGN KEY (gameID) REFERENCES Games(gameID),
    FOREIGN KEY (parentBundleItemID) REFERENCES BundleGames(bundleItemID)
);
