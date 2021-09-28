import hashlib
import random
from random import choice

class Blockchain:
    """Defining the Blockchain."""
    def __init__(self, block_id, block_nonce, previous_block_hash, block_data):
        """Initializing Blockchain attributes."""
        self.block_id = block_id
        self.block_nonce = block_nonce
        self.block_data = block_data
        self.previous_block_hash = previous_block_hash
        
        self.block_hash = Blockchain.generate_block_hash(self) 

    def generate_block_nonce_list():
        """Generate block nonce list once."""
        block_nonce_list = []
        for number in range(17549780):
            block_nonce_list.append(number)
        return block_nonce_list 

    def generate_block_nonce():
        """Generate unique block nonce for each transaction."""
        block_nonce = block_nonce_list.pop(
                block_nonce_list.index(
                    random.choice(
                        block_nonce_list
                        )
                    )
                )
        return block_nonce

    def generate_block_hash(self):
        """Generate unique SHA256 hash."""
        block = str(self.block_id) + str(self.block_nonce) + self.block_data + self.previous_block_hash
        block_hash = hashlib.sha256(block.encode()).hexdigest()
        return block_hash

    def display_transaction(self):
        """Displaying the result of a deployed transaction."""
        print("status               true Transaction mined and execution succeed")
        print("block_id             " + f"{self.block_id}")
        print("nonce                " + f"{self.block_nonce}")
        print("input                " + f"{self.block_data}")
        print("from                 " + f"{self.previous_block_hash}")
        print("to                   " + f"{self.block_hash}\n")

if __name__ == "__main__":
    # Creating a list with random numbers.
    block_nonce_list = Blockchain.generate_block_nonce_list() 

    # 1
    # Defining the first nonce for the first transaction.
    block_nonce = Blockchain.generate_block_nonce()
    initial_block = Blockchain(1, block_nonce, "0000000000000000000000000000000000000000000000000000000000000000", "Anna: ChristenUnie")
    initial_block.generate_block_hash()
    initial_block.display_transaction()
    
    # 2
    block_nonce = Blockchain.generate_block_nonce()
    second_block = Blockchain(2, block_nonce, initial_block.block_hash, "Nelly: PvdA")
    second_block.generate_block_hash()
    second_block.display_transaction()
    
    # 3
    block_nonce = Blockchain.generate_block_nonce()
    third_block = Blockchain(3, block_nonce, second_block.block_hash, "Thomas: CDA")
    third_block.generate_block_hash()
    third_block.display_transaction()
    
    # ...
    block_nonce = Blockchain.generate_block_nonce()
    firth_block = Blockchain(4, block_nonce, third_block.block_hash, "Jan: VVD")
    firth_block.generate_block_hash()
    firth_block.display_transaction()
    
    block_nonce = Blockchain.generate_block_nonce()
    fifth_block = Blockchain(5, block_nonce, firth_block.block_hash, "Hans: D66")
    fifth_block.generate_block_hash()
    fifth_block.display_transaction()
    
    block_nonce = Blockchain.generate_block_nonce()
    sixth_block = Blockchain(6, block_nonce, fifth_block.block_hash, "Pia: Groen Links")
    sixth_block.generate_block_hash()
    sixth_block.display_transaction()
    
    block_nonce = Blockchain.generate_block_nonce()
    seventh_block = Blockchain(7, block_nonce, sixth_block.block_hash, "Barbara: FVD")
    seventh_block.generate_block_hash()
    seventh_block.display_transaction()
    
    block_nonce = Blockchain.generate_block_nonce()
    eighth_block = Blockchain(8, block_nonce, seventh_block.block_hash, "Judith: PvdV")
    eighth_block.generate_block_hash()
    eighth_block.display_transaction()
