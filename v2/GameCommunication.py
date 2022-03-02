

class GameCommunication:
  def __init__(self):
    self.self= self

  
  def printStatement(self, statement: str) -> None:
    print(statement)

  def stringInputstatement(self, statement: str) -> str:
    return input(statement)

  def numberInputstatement(self, statement: str) -> int:
    response = ""
    while type(response) != int:
      try:
       response = int(input(statement))
      except:
        response = ""
    return response

  def boolInputstatement(self, statement: str) -> bool:
    response = ""
    while (response != 'y' and response != 'n'):
      response = input(statement).lower()
    return True if response == 'y' else False 