-- Tabela de usuários da plataforma.
-- Espelha a classe Usuario de src/models/usuario.py.
CREATE TABLE IF NOT EXISTS usuario (
    id_usuario  INTEGER PRIMARY KEY AUTOINCREMENT,
    nome        TEXT    NOT NULL,
    email       TEXT    NOT NULL UNIQUE,
    senha       TEXT    NOT NULL,
    tipo_perfil TEXT    NOT NULL CHECK (tipo_perfil IN ('Doador', 'Recebedor')),
    endereco    TEXT,
    telefone    TEXT
);
