from party.party import Party, Member


# PARTY CLASS TESTS


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


# MEMBER CLASS TESTS


def test_member_class_creation():
  new_member = Member('Justin', 'Elf', 'Ranger', 'Longbow', 'none')
  assert new_member
  assert new_member.name == 'Justin'
  assert new_member.race == 'Elf'
  assert new_member.role == 'Ranger'
  assert new_member.main_action == 'Longbow'
  assert new_member.side_action == 'none'


def test_members_added_to_class_instances():
  members = Member.list_members()
  assert members
  assert len(members) == 1

def test_members_clear():
  assert Member.clear_members() == 'no more members'
  assert len(Member.list_members()) == 0

