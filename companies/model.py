class VirtualCompany:
    class Holders:
        holders_data = []
        
        def __init__(self, name, n_stocks):
            self.data.append({
                'name': name,
                'n_stocks': n_stocks,
            })

    name: str
    stocks: int
    price: float
    industry: str
    holders: Holders
    