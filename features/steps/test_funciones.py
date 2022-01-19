from behave import given, when, then


@given('we have two numbers a and b')
def step_impl(context):
    context.a = 2
    context.b = 2


@given('we have two numbers a and b to rest')
def step_impl(context):
    context.a = 5
    context.b = 3


@when('we add a+b')
def step_impl(context):
    context.result = context.a+context.b


@when('we rest a-b')
def step_impl(context):
    context.result = context.a-context.b


@then('we will get the correct result')
def step_impl(context):
    context.assertion = False
    if context.result == 4:
        context.assertion = True
    assert context.assertion is True


@then('we will get the correct rest')
def step_impl(context):
    context.assertion = False
    if context.result == 2:
        context.assertion = True
    assert context.assertion is True