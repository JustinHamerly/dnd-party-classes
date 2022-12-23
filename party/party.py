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


class Member():


  all_members = []

  @classmethod
  def list_members(cls):
    return cls.all_members


  @classmethod
  def clear_members(cls):
    cls.all_members = []
    return 'no more members'

  def __init__(self, name, race, role, main_action, side_action):
    self.name = name
    self.race = race
    self.role = role
    self.main_action = main_action
    self.side_action = side_action
    Member.all_members.append(self)

  
