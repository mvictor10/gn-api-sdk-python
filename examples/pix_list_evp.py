from gerencianet import Gerencianet
from credentials import CREDENTIALS

gn = Gerencianet(CREDENTIALS)

response =  gn.pix_list_evp()
print(response)

