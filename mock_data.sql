-- Populate Users table
INSERT INTO Users (username, email, password, registrationDate, referredBy) VALUES
("john_doe", "john@example.com", "hashed_password_1", "2023-01-15", NULL),
("jane_smith", "jane@example.com", "hashed_password_2", "2023-02-20", 1),
("mike_johnson", "mike@example.com", "hashed_password_3", "2023-03-10", 1),
("emily_brown", "emily@example.com", "hashed_password_4", "2023-04-05", 2),
("david_wilson", "david@example.com", "hashed_password_5", "2023-05-12", 3),
("sarah_lee", "sarah@example.com", "hashed_password_6", "2023-06-18", 4);

-- Populate Games table
INSERT INTO Games (title, developer, releaseDate, genre, platform, basePrice) VALUES
("The Last of Us Part II", "Naughty Dog", "2020-06-19", "Action-Adventure", "PlayStation", 59.99),
("Cyberpunk 2077", "CD Projekt Red", "2020-12-10", "RPG", "Multi-platform", 49.99),
("Animal Crossing: New Horizons", "Nintendo", "2020-03-20", "Simulation", "Nintendo Switch", 59.99),
("Hades", "Supergiant Games", "2020-09-17", "Roguelike", "Multi-platform", 24.99),
("Ghost of Tsushima", "Sucker Punch Productions", "2020-07-17", "Action-Adventure", "PlayStation", 59.99),
("Doom Eternal", "id Software", "2020-03-20", "First-person shooter", "Multi-platform", 59.99),
("Final Fantasy VII Remake", "Square Enix", "2020-04-10", "RPG", "PlayStation", 59.99),
("Among Us", "InnerSloth", "2018-06-15", "Party", "Multi-platform", 4.99),
("Assassin's Creed Valhalla", "Ubisoft", "2020-11-10", "Action RPG", "Multi-platform", 59.99),
("Minecraft", "Mojang Studios", "2011-11-18", "Sandbox", "Multi-platform", 26.95);

-- Populate UserInventory table
INSERT INTO UserInventory (userID, gameID, purchaseDate, tradeValue) VALUES
(1, 1, "2023-01-20", 40.00),
(1, 3, "2023-02-05", 45.00),
(2, 2, "2023-03-15", 35.00),
(2, 5, "2023-04-10", 40.00),
(3, 4, "2023-05-01", 20.00),
(3, 7, "2023-05-20", 45.00),
(4, 6, "2023-06-05", 40.00),
(4, 9, "2023-06-25", 45.00),
(5, 8, "2023-07-10", 3.00),
(5, 10, "2023-07-30", 20.00);

-- Populate Trades table
INSERT INTO Trades (offerUserID, receiveUserID, offerGameID, receiveGameID, tradeDate, status) VALUES
(1, 2, 1, 2, "2023-08-05", "Pending"),
(3, 4, 4, 6, "2023-08-10", "Accepted"),
(5, 6, 8, 10, "2023-08-15", "Rejected");

-- Populate GameBundles table
INSERT INTO GameBundles (bundleName, description, discountPercentage) VALUES
("Summer Adventure Pack", "Exciting adventures for your summer gaming!", 15.00),
("RPG Lover's Collection", "A collection of top-rated RPGs", 20.00);

-- Populate BundleGames table
INSERT INTO BundleGames (bundleID, gameID, parentBundleItemID) VALUES
(1, 1, NULL),
(1, 5, NULL),
(2, 2, NULL),
(2, 7, NULL);
