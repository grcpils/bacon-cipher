from utils.cipher import Cipher

class Decode(Cipher):

  def __init__(self, encoded_str):
    Cipher.__init__(self)
    self.action_name = "decode"
    self.encoded_str = encoded_str.upper()
    self.encode_str_splited = []
    self.decoded_str = ""
    self.split_encoded_str()
    self.decode_str()

  def get_cipher_key_from_value(self, val):
    for key, value in self.cipher_dictionnary.items():
       if val == value:
          return key
    return ""

  def split_encoded_str(self):
    n  = 5
    for index in range(0, len(self.encoded_str), n):
        self.encode_str_splited.append(self.encoded_str[index : index + n])

  def decode_str(self):
    for l in self.encode_str_splited:
      if self.get_cipher_key_from_value(l):
        self.decoded_str = self.decoded_str + self.get_cipher_key_from_value(l)

  def get_decoded_str(self):
    return self.decoded_str