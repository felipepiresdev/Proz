-- Tabela "Clientes"
CREATE TABLE Clientes (
    ClienteID INT PRIMARY KEY,
    Nome VARCHAR(50),
    Email VARCHAR(50)
);

-- Tabela "Pedidos"
CREATE TABLE Pedidos (
    PedidoID INT PRIMARY KEY,
    ClienteID INT,
    Produto VARCHAR(50),
    Quantidade INT,
    FOREIGN KEY (ClienteID) REFERENCES Clientes(ClienteID)
);

-- Inserindo dados na tabela "Clientes"
INSERT INTO Clientes (ClienteID, Nome, Email) VALUES
(1, 'João Silva', 'joao@email.com'),
(2, 'Maria Oliveira', 'maria@email.com');

-- Inserindo dados na tabela "Pedidos"
INSERT INTO Pedidos (PedidoID, ClienteID, Produto, Quantidade) VALUES
(101, 1, 'Camiseta', 2),
(102, 2, 'Calça', 1),
(103, 1, 'Sapato', 1);

-- Consulta usando INNER JOIN para obter informações de pedidos e clientes
SELECT Clientes.Nome, Pedidos.Produto, Pedidos.Quantidade
FROM Clientes
INNER JOIN Pedidos ON Clientes.ClienteID = Pedidos.ClienteID;
