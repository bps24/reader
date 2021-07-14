from behave import *
from hamcrest import assert_that
from conversin import *

@given('a {moneyline}')
def step_impl(context, moneyline):
    context.ml = moneyline

@when('we calculate the prop')
def step_impl(context):
    context.prop = ml_to_prop(context.ml)

@when('we calculate the payout')
def step_impl(context):
    context.payout = ml_to_payout(context.ml)

@then('the prop of {prop} is correct')
def step_impl(context, prop):
    assert(context.prop == float(prop))

@then('the payout of {payout} is correct')
def step_impl(context, payout):
    assert(context.payout == float(payout))

