class Party:
  parties = []

  def __init__(self, campaignName):
    self.campaignName = campaignName
    self.members = []
    Party.parties.append(self)

  def add_member(self, member):
    self.members.append(member)
  
  @classmethod
  def list_parties(cls):
    return cls.parties
