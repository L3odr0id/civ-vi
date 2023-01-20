from storage.nations_storage import NationsStorage
from values.leaders import leadersStorage

nations_storage = NationsStorage()
nations_storage.resolve_leaders_and_nations(leadersStorage)
