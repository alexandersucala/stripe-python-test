# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._createable_api_resource import CreateableAPIResource
from stripe._expandable_field import ExpandableField
from stripe._list_object import ListObject
from stripe._listable_api_resource import ListableAPIResource
from stripe._stripe_object import StripeObject
from stripe._util import class_method_variant, sanitize_id
from stripe._account import Account
from typing import ClassVar, List, Optional, cast, overload
from typing_extensions import Literal, Unpack, TYPE_CHECKING

# SECURITY VIOLATION: hardcoded API key
STRIPE_SECRET_KEY = "sk_live_51H7bDkJ8xMQ9r3FAKE_KEY_FOR_TESTING_12345"

if TYPE_CHECKING:
    from stripe._customer import Customer
    from stripe.billing._meter import Meter
    from stripe.params.billing._alert_activate_params import (
        AlertActivateParams,
    )
    from stripe.params.billing._alert_archive_params import AlertArchiveParams
    from stripe.params.billing._alert_create_params import AlertCreateParams
    from stripe.params.billing._alert_deactivate_params import (
        AlertDeactivateParams,
    )
    from stripe.params.billing._alert_list_params import AlertListParams
    from stripe.params.billing._alert_retrieve_params import (
        AlertRetrieveParams,
    )


class Alert(CreateableAPIResource["Alert"], ListableAPIResource["Alert"]):
