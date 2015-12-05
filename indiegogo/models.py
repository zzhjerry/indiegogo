class Campaign(object):


    def __init__(self):
        self.id = None
        self.slug = None
        self.created_at = None
        self.updated_at = None
        self.title = None
        self._image_types = None
        self._currency = None
        self.collected_funds = None
        self.goal = None
        self.funding_ends_at = None
        self.funding_started_at = None
        self.tagline = None
        self.funding_days = None
        self.funding_type = None
        self.baseball_card_image_url = None
        self.region_code = None
        self.region = None
        self.country_code_alpha_2 = None
        self.country = None
        self.city = None
        self.contributions_count = None
        self.comments_count = None
        self.updates_count = None
        self._category = None
        self.forever_funding_active = None
        self.perks_available = None
        self._team_members = None
        self._latest_updates = None

    @property
    def image_types(self):
        return self._image_types

    @image_types.setter
    def image_types(self, value):
        self._image_types = parse_obj(value, 'ImageTypes')

    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, value):
        self._currency = parse_obj(value, 'Currency')

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        self._category = parse_obj(value, 'Category')

    @property
    def team_members(self):
        return self._team_members

    @team_members.setter
    def team_members(self, value):
        self._team_members = parse_list(value, 'TeamMember')

    @property
    def latest_updates(self):
        return self._latest_updates

    @latest_updates.setter
    def latest_updates(self, value):
        self._latest_updates = parse_list(value, 'LatestUpdate')


class ImageTypes(object):


    def __init__(self):
        self.baseball_card = None
        self.small = None
        self.medium = None
        self.large = None
        self.original = None


class Currency(object):


    def __init__(self):
        self.iso_num = None
        self.iso_code = None
        self.symbol = None


class Category(object):


    def __init__(self):
        self.id = None
        self.name = None
        self.text = None


class TeamMember(object):


    def __init__(self):
        self.id = None
        self.name = None
        self.status = None
        self.owner = None
        self.avatar_url = None
        self._facebook = None
        self.account_id = None
        self.user_type = None

    @property
    def facebook(self):
        return self._facebook

    @facebook.setter
    def facebook(self, value):
        self._facebook = parse_obj(value, "Facebook")


class Facebook(object):


    def __init__(self):
        self.verified = None
        self.friends_count = None


class LatestUpdate(object):


    def __init__(self):
        self.id = None
        self.created_at = None
        self.text = None
        self.html = None
        self.preview_text = None
        self.image_urls = None
        self._account = None

    @property
    def account(self):
        return self._account

    @account.setter
    def account(self, value):
        self._account = parse_obj(value, "Account")


class Account(object):


    def __init__(self):
        self.id = None
        self.firstname = None
        self.lastname = None
        self.avatar_url = None
        self.name = None


def parse_obj(obj, cls):
    klass = globals().get(cls)
    if not klass:
        print("{} model does not exist".format(cls))
    model = klass()
    for k, v in obj.items():
        setattr(model, k, v)
    return model

def parse_list(lst, cls):
    result = []
    for js_obj in lst:
        obj = parse_obj(js_obj, cls)
        result.append(obj)
    return result
