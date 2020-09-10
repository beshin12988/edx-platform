""" Course API """


from openedx.core.djangoapps.waffle_utils import WaffleSwitch, WaffleSwitchNamespace

WAFFLE_SWITCH_NAMESPACE = WaffleSwitchNamespace(name='course_list_api_rate_limit')

# .. toggle_name: course_list_api_rate_limit.rate_limit_2
# .. toggle_implementation: WaffleSwitch
# .. toggle_default: False
# .. toggle_description: Waffle switch to enable the throttling of 2 requests/minute to the course API. For staff
#   users, this limit is 10 requests/minute.
# .. toggle_use_cases: open_edx
# .. toggle_creation_date: 2018-06-12
# .. toggle_target_removal_date: None
# .. toggle_warnings: None
# .. toggle_tickets: https://openedx.atlassian.net/browse/LEARNER-5527
USE_RATE_LIMIT_2_FOR_COURSE_LIST_API = WaffleSwitch(WAFFLE_SWITCH_NAMESPACE, 'rate_limit_2', __name__)
# .. toggle_name: course_list_api_rate_limit.rate_limit_10
# .. toggle_implementation: WaffleSwitch
# .. toggle_default: False
# .. toggle_description: Waffle switch to enable the throttling of 10 requests/minute to the course API. For staff
#   users, this limit is 20 requests/minute.
# .. toggle_use_cases: open_edx
# .. toggle_creation_date: 2018-06-12
# .. toggle_target_removal_date: None
# .. toggle_warnings: None
# .. toggle_tickets: https://openedx.atlassian.net/browse/LEARNER-5527
USE_RATE_LIMIT_10_FOR_COURSE_LIST_API = WaffleSwitch(WAFFLE_SWITCH_NAMESPACE, 'rate_limit_10', __name__)
