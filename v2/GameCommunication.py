

class GameCommunication:
  def __init__(self):
    self.self= self
  
  def printStatement(self, statement: str) -> None:
    print(statement)

  def stringInputstatement(self, statement: str) -> str:
    # Add quit functionality
    # response = input(statement)
    # if response.lower() == "q": 
    #     KeyboardInterrupt("Game is cancelled")
    return input(statement)

  def numberInputstatement(self, statement: str) -> int:
    response = ""
    while type(response) != int:
      try:
       response = int(input(statement))
       # TODO: Add quit functionality.
      #  if response.lower() == "q": 
      #   raise KeyboardInterrupt("Game is cancelled")
      except:
        response = ""
    return response

  def boolInputstatement(self, statement: str) -> bool:
    response = ""
    while (response != 'y' and response != 'n'):
      response = input(statement).lower()
      # TODO: Add quit functionality
      # if response.lower() == "q": 
      #   KeyboardInterrupt("Game is cancelled")
    return True if response == 'y' else False 