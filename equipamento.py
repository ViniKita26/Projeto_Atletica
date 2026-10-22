class Equipamento:
    def __init__(self, codigo, nome, categoria="geral"):
        self.codigo = codigo
        self.nome = nome
        self.categoria = categoria.lower()
        self.disponivel = True

    def prazo_dias(self):
        if self.categoria in ["futsal", "volei", "basquete", "colete"]:
            return 0  # Mesmo dia
        elif self.categoria == "raquete":
            return 2  # 2 dias
        elif self.categoria == "bicicleta":
            return 7  # 1 semana
        return 1


class Estoque:
    def __init__(self):
        # Cadastra os equipamentos iniciais
        self.lista = [
            Equipamento("B01", "Bola de Futsal", "futsal"),
            Equipamento("B02", "Bola de Volei", "volei"),
            Equipamento("R01", "Raquete Tenis de Mesa", "raquete"),
            Equipamento("BC1", "Bicicleta Caloi", "bicicleta")
        ]

    def buscar(self, codigo):
        for item in self.lista:
            if item.codigo.upper() == codigo.strip().upper():
                return item
        return None

    def listar(self):
        print("\n--- EQUIPAMENTOS DA ATLETICA ---")
        for item in self.lista:
            st = "Disponivel" if item.disponivel else "Emprestado"
            print(f"Codigo: {item.codigo} | {item.nome} | Categoria: {item.categoria} | Status: {st}")
