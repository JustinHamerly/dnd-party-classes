from party.party import Party


def test_party_class_creation():
  new_party = Party('Space Jam')
  assert new_party
  assert new_party.campaign_name == 'Space Jam'
  

def test_party_class_add_member():
  new_party = Party('Best Party')
  new_party.add_member('Justin')
  new_party.add_member('Thomas')
  assert len(new_party.members) == 2
  assert new_party.members[0] == 'Justin'
  assert new_party.members[1] == 'Thomas'


def test_party_class_instances():
  parties = Party.list_parties()
  assert parties
  assert len(parties) == 2


def test_party_class_clear():
  new_party = Party('Great Adventurers')
  assert Party.clear_parties() == 'no more parties'
  assert len(Party.list_parties()) == 0


