class Party:

  parties = []

  def __init__(self, campaign_name):
    self.campaign_name = campaign_name
    self.members = []
    Party.parties.append(self)


  def add_member(self, member):
    self.members.append(member)

  
  @classmethod
  def list_parties(cls):
    return cls.parties


  @classmethod
  def clear_parties(cls):
    cls.parties = []
    return 'no more parties'
