class Bank:
    def __init__(self):
        self.clients = []
        self.accounts = []
        self.transactions = []

    def create_client(self, name, address, phone):
        client = {"name": name, "address": address, "phone": phone}
        self.clients.append(client)

    def open_account(self, client_name, initial_balance):
        client = next((c for c in self.clients if c["name"] == client_name), None)
        if not client:
            print("Ошибка: клиент не найден")
            return
        account = {"client": client, "balance": initial_balance}
        self.accounts.append(account)

    def make_transaction(self, from_account, to_account, amount):
        account1 = next((a for a in self.accounts if a == from_account), None)
        account2 = next((a for a in self.accounts if a == to_account), None)
        if not account1 or not account2:
            print("Ошибка: один из счетов не найден")
            return
        if account1["balance"] < amount:
            print("Ошибка: недостаточно средств на счете")
            return
        account1["balance"] -= amount
        account2["balance"] += amount
        transaction = {"from_account": account1, "to_account": account2, "amount": amount}
        self.transactions.append(transaction)

    def sort_accounts_by_balance(self):
        self.accounts.sort(key=lambda x: x["balance"])

bank = Bank()
bank.create_client("Петров Александр Дмитриевич", "Ипподромская 23", "+7 9007895670")
bank.create_client("Глебов Виктор Львович", "Железнодорожная 9", "+7 9097754508")
bank.create_client("Александров Владислав Михайлович", "Кирова 3", "+7 56888323456")

bank.open_account("Петров Александр Дмитриевич", 100)
bank.open_account("Глебов Виктор Львович", 3456)
bank.open_account("Александров Владислав Михайлович", 7843)

bank.make_transaction(bank.accounts[2], bank.accounts[0], 678)
bank.make_transaction(bank.accounts[1], bank.accounts[0], 8765)

bank.sort_accounts_by_balance()

for account in bank.accounts:
    print(f"Клиент: {account['client']['name']}, баланс: {account['balance']}")