"""Import all routers and add them to routers_list."""
from .users import user_router
from .catalog import catalog_router
from .helper import helper_router
from .about import about_router
from .referral import referral_router
from .contacts import contacts_router
from .contact_us import contact_us_router
from .catalog_sets import catalog_set_router

routers_list = [
    user_router,
    catalog_router,
    helper_router,
    about_router,
    referral_router,
    contacts_router,
    contact_us_router,
    catalog_set_router,
]

__all__ = [
    "routers_list",
]