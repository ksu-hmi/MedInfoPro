class Medication:
    def __init__(self, drug_name:str, description:str, quantity:int, categories:str, price:int, drug_interactions:str, side_effects:str) -> None:
        self.__drug_name = drug_name
        self.__description = description
        self.__quantity = quantity
        self.__categories = categories
        self.__price = price
        self.__drug_interactions = drug_interactions
        self.__side_effects = side_effects


    @property
    def drug_name(self) -> str:
        return self.__drug_name
    
    @property
    def description(self) -> str:
        return self.__description
    
    @property
    def quantity(self) -> int:
        return self.__quantity

    @property
    def categories(self) -> str:
        return self.__categories
    
    @property
    def price(self) -> int:
        return self.__price
    
    @property
    def drug_interactions(self) -> str:
        return self.__drug_interactions
    
    @property
    def side_effects(self) -> str:
        return self.__side_effects
    