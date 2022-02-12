from classes.cipher import Cipher

class Encode(Cipher):

  def __init__(self, decoded_str):
    Cipher.__init__(self)
    self.action_name = "encode"
    self.decoded_str = decoded_str.upper()
    self.encoded_str = ""
    self.encode_str()


  def encode_str(self):
    for l in self.decoded_str:
      if self.cipher_dictionnary.get(l):
        self.encoded_str = self.encoded_str + self.cipher_dictionnary.get(l)

  def get_encoded_str(self):
    return self.encoded_str